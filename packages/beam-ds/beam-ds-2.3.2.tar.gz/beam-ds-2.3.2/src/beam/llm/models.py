import json
from typing import Optional, Any
import openai
import requests
import pandas as pd
import numpy as np
from transformers.pipelines import Conversation

from ..logger import beam_logger as logger
from .llm import BeamLLM
from pydantic import BaseModel, Field, PrivateAttr
from ..path import beam_key, normalize_host


class OpenAIBase(BeamLLM):

    api_key: Optional[str] = Field(None)
    api_base: Optional[str] = Field(None)
    organization: Optional[str] = Field(None)

    def __init__(self, api_key=None, api_base=None, organization=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.api_key = api_key
        self.api_base = api_base
        self.organization = organization

    def update_usage(self, response):

        if 'usage' in response:
            response = response['usage']

            self.usage["prompt_tokens"] += response["prompt_tokens"]
            self.usage["completion_tokens"] += response["completion_tokens"]
            self.usage["total_tokens"] += response["prompt_tokens"] + response["completion_tokens"]

    def sync_openai(self):
        openai.api_key = self.api_key
        openai.api_base = self.api_base
        openai.organization = self.organization

    def _chat_completion(self, **kwargs):
        self.sync_openai()
        return openai.ChatCompletion.create(model=self.model, **kwargs)

    def _completion(self, **kwargs):
        self.sync_openai()
        return openai.Completion.create(engine=self.model, **kwargs)

    def verify_response(self, res):
        res = res.response
        finish_reason = res.choices[0].finish_reason
        if finish_reason != 'stop':
            logger.warning(f"finish_reason is {finish_reason}")
        return True

    def extract_text(self, res):

        stream = res.stream
        res = res.response

        if not self.is_chat:
            res = res.choices[0].text
        else:
            if not stream:
                res = res.choices[0].message.content
            else:
                res = res.choices[0].delta.content
        return res

    def openai_format(self, res):

        res = res.response
        return res


class OpenAI(OpenAIBase):

    _models: Any = PrivateAttr()

    def __init__(self, model='gpt-3.5-turbo', api_key=None, organization=None, *args, **kwargs):

        api_key = beam_key('OPENAI_API_KEY', api_key)

        kwargs['scheme'] = 'openai'
        super().__init__(api_key=api_key, api_base='https://api.openai.com/v1',
                         organization=organization, *args, **kwargs)

        self.model = model
        self._models = None

    @property
    def is_chat(self):
        chat_models = ['gpt-4', 'gpt-4-0314', 'gpt-4-32k', 'gpt-4-32k-0314', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0301']
        if any([m in self.model for m in chat_models]):
            return True
        return False

    def file_list(self):
        return openai.File.list()

    def build_dataset(self, data=None, question=None, answer=None, path=None) -> object:
        """
        Build a dataset for training a model
        :param data: dataframe with prompt and completion columns
        :param question: list of questions
        :param answer: list of answers
        :param path: path to save the dataset
        :return: path to the dataset
        """
        if data is None:
            data = pd.DataFrame(data={'prompt': question, 'completion': answer})

        records = data.to_dict(orient='records')

        if path is None:
            print('No path provided, using default path: dataset.jsonl')
            path = 'dataset.jsonl'

        # Open a file for writing
        with open(path, 'w') as outfile:
            # Write each data item to the file as a separate line
            for item in records:
                json.dump(item, outfile)
                outfile.write('\n')

        return path

    def retrieve(self, model=None):
        if model is None:
            model = self.model
        return openai.Engine.retrieve(id=model)

    @property
    def models(self):
        if self._models is None:
            models = openai.Model.list()
            models = {m.id: m for m in models.data}
            self._models = models
        return self._models

    def embedding(self, text, model=None):
        if model is None:
            model = self.model
        response = openai.Engine(model).embedding(input=text, model=model)
        embedding = np.array(response.data[1]['embedding'])
        return embedding


class FCConversationLLM(BeamLLM):

    _ma: Any = PrivateAttr()
    _conv: Any = PrivateAttr()

    def __init__(self, *args, model=None, model_adapter=None, **kwargs):

        super().__init__(*args, model=model, **kwargs)

        if model_adapter is not None:
            model = model_adapter

        from fastchat.model.model_adapter import get_model_adapter
        self._ma = get_model_adapter(model)
        self._conv = self._ma.get_default_conv_template('       ')

    @property
    def stop_sequence(self):
        return self._conv.stop_str

    def get_prompt(self, messages):

        conv = self._ma.get_default_conv_template('       ')

        for m in messages:

            if m['role'] == 'system':

                role = m['system_name'] if 'system_name' in m else 'system'
                content = m['content']

            else:

                if m['role'] == 'user':
                    role = conv.roles[0]
                else:
                    role = conv.roles[1]

                content = m['content']

            conv.append_message(role, content)

        conv.append_message(self._conv.roles[1], None)

        return conv.get_prompt()

    @property
    def is_chat(self):
        return True

    @property
    def is_completions(self):
        return True


class TGILLM(FCConversationLLM):

    _info: Any = PrivateAttr()
    _client: Any = PrivateAttr()

    def __init__(self, hostname=None, port=None, *args, **kwargs):

        api_base = f"http://{normalize_host(hostname, port)}"

        from text_generation import Client
        self._client = Client(api_base)

        req = requests.get(f"{api_base}/info")
        self._info = json.loads(req.text)

        kwargs['model'] = self._info['model_id']
        kwargs['scheme'] = 'tgi'
        super().__init__(*args, **kwargs)

    def update_usage(self, response):

        self.usage["prompt_tokens"] += 0
        self.usage["completion_tokens"] += response.details.generated_tokens
        self.usage["total_tokens"] += 0 + response.details.generated_tokens

    def openai_format(self, res):
        return super().openai_format(res, tokens=res.response.details.tokens,
                                     completion_tokens=res.response.details.generated_tokens,
                                     total_tokens=res.response.details.generated_tokens)

    @property
    def is_chat(self):
        return False

    @property
    def is_completions(self):
        return True

    def process_kwargs(self, prompt, **kwargs):

        processed_kwargs = {}

        max_tokens = kwargs.pop('max_tokens', None)
        max_new_tokens = None

        if max_tokens is not None:
            max_new_tokens = max_tokens - self.len_function(prompt)

        max_new_tokens = kwargs.pop('max_new_tokens', max_new_tokens)
        if max_new_tokens is not None:
            processed_kwargs['max_new_tokens'] = max_new_tokens

        temperature = kwargs.pop('temperature', None)
        if temperature is not None:
            processed_kwargs['temperature'] = temperature

        top_p = kwargs.pop('top_p', None)
        if top_p is not None and 0 < top_p < 1:
            processed_kwargs['top_p'] = top_p

        best_of = kwargs.pop('n', None)
        if best_of is not None and best_of > 1:
            processed_kwargs['best_of'] = best_of

        stop_sequences = kwargs.pop('stop', None)
        if stop_sequences is None:
            stop_sequences = []
        elif type(stop_sequences) is str:
            stop_sequences = [stop_sequences]

        if self.stop_sequence is not None:
            stop_sequences.append(self.stop_sequence)

        if len(stop_sequences) > 0:
            processed_kwargs['stop_sequences'] = stop_sequences

        if 'top_k' in kwargs:
            processed_kwargs['top_k'] = kwargs.pop('top_k')

        if 'truncate' in kwargs:
            processed_kwargs['truncate'] = kwargs.pop('truncate')

        if 'typical_p' in kwargs:
            processed_kwargs['typical_p'] = kwargs.pop('typical_p')

        if 'watermark' in kwargs:
            processed_kwargs['watermark'] = kwargs.pop('watermark')

        if 'repetition_penalty' in kwargs:
            processed_kwargs['repetition_penalty'] = kwargs.pop('repetition_penalty')

        decoder_input_details = kwargs.pop('logprobs', None)
        if decoder_input_details is not None:
            processed_kwargs['decoder_input_details'] = decoder_input_details

        if 'seed' in kwargs:
            processed_kwargs['seed'] = kwargs.pop('seed')

        do_sample = None
        if temperature is not None and temperature > 0:
            do_sample = True
        do_sample = kwargs.pop('do_sample', do_sample)

        if do_sample is not None:
            processed_kwargs['do_sample'] = do_sample

        return processed_kwargs

    def _completion(self, prompt=None, **kwargs):

        prompt = self.get_prompt([{'role': 'user', 'content': prompt}])
        generate_kwargs = self.process_kwargs(prompt, **kwargs)
        return self._client.generate(prompt, **generate_kwargs)

    def _chat_completion(self, messages=None, **kwargs):

        prompt = self.get_prompt(messages)
        generate_kwargs = self.process_kwargs(prompt, **kwargs)

        return self._client.generate(prompt, **generate_kwargs)

    def extract_text(self, res):

        res = res.response
        text = res.generated_text
        text = text.rstrip(self.stop_sequence)
        return text


class FastChatLLM(OpenAIBase):

    def __init__(self, model=None, hostname=None, port=None, *args, **kwargs):

        api_base = f"http://{normalize_host(hostname, port)}/v1"
        api_key = "EMPTY"  # Not support yet
        organization = "EMPTY"  # Not support yet

        kwargs['scheme'] = 'fastchat'
        super().__init__(*args, api_key=api_key, api_base=api_base, organization=organization, model=model, **kwargs)

        self.model = model

    @property
    def is_chat(self):
        return True


class FastAPILLM(FCConversationLLM):

    model: Optional[str] = Field(None)
    hostname: Optional[str] = Field(None)
    headers: Optional[dict] = Field(None)
    consumer: Optional[str] = Field(None)
    protocol: Optional[str] = Field(None)
    _models: Any = PrivateAttr()

    def __init__(self, *args, model=None, hostname=None, port=None, username=None, protocol='https', **kwargs):

        kwargs['scheme'] = 'fastapi'
        super().__init__(*args, model=model, **kwargs)

        self.consumer = username
        self.hostname = normalize_host(hostname, port)
        self._models = None
        self.headers = {'Content-Type': 'application/json'}
        self.protocol = protocol

        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        # Suppress only the single InsecureRequestWarning from urllib3
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    @property
    def models(self):
        if self._models is None:
            res = requests.get(f"{self.protocol}://{self.hostname}/models", headers=self.headers, verify=False)
            self._models = res.json()
        return self._models

    @property
    def is_chat(self):
        return True

    @property
    def is_completions(self):
        return True

    def process_kwargs(self, prompt, **kwargs):

        kwargs_processed = {}

        max_tokens = kwargs.pop('max_tokens', None)
        max_new_tokens = None

        if max_tokens is not None:
            max_new_tokens = max_tokens - self.len_function(prompt)

        max_new_tokens = kwargs.pop('max_new_tokens', max_new_tokens)
        if max_new_tokens is not None:
            kwargs_processed['max_new_tokens'] = max_new_tokens

        temperature = kwargs.pop('temperature', None)
        if temperature is not None:
            kwargs_processed['temp'] = temperature

        return kwargs_processed

    def _chat_completion(self, messages=None, **kwargs):

        d = {}
        d['model_name'] = self.model
        d['consumer'] = self.consumer
        d['input'] = self.get_prompt(messages)
        d['hyper_params'] = self.process_kwargs(d['input'], **kwargs)

        res = requests.post(f"{self.protocol}://{self.hostname}/predict/once", headers=self.headers, json=d,
                            verify=False)
        return res.json()

    def _completion(self, prompt=None, **kwargs):

        d = {}
        d['model_name'] = self.model
        d['consumer'] = self.consumer
        d['input'] = self.get_prompt([{'role': 'user', 'content': prompt}])
        d['hyper_params'] = self.process_kwargs(d['input'], **kwargs)

        res = requests.post(f"{self.protocol}://{self.hostname}/predict/once", headers=self.headers, json=d,
                            verify=False)
        return res.json()

    def verify_response(self, res):
        try:

            if not res.response['is_done']:
                logger.warning(f"Model {self.model} is_done=False.")

            assert 'res' in res.response, f"Response does not contain 'res' key"

        except Exception as e:
            logger.error(f"Error in response: {res.response}")
            raise e
        return True

    def extract_text(self, res):
        return res.response['res']


class HuggingFaceLLM(BeamLLM):
    config: Any
    tokenizer: Any
    net: Any
    pipline_kwargs: Any
    input_device: Optional[str] = Field(None)
    eos_pattern: Optional[str] = Field(None)
    _text_generation_pipeline: Any = PrivateAttr()
    _conversational_pipeline: Any = PrivateAttr()

    def __init__(self, model, tokenizer=None, dtype=None, chat=False, input_device=None, compile=True, *args,
                 model_kwargs=None,
                 config_kwargs=None, pipline_kwargs=None, text_generation_kwargs=None, conversational_kwargs=None,
                 eos_pattern=None, **kwargs):

        kwargs['scheme'] = 'huggingface'
        kwargs['model'] = model
        super().__init__(*args, **kwargs)

        from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig
        import transformers

        transformers.logging.set_verbosity_error()

        if model_kwargs is None:
            model_kwargs = {}

        if config_kwargs is None:
            config_kwargs = {}

        if pipline_kwargs is None:
            pipline_kwargs = {}

        if text_generation_kwargs is None:
            text_generation_kwargs = {}

        if conversational_kwargs is None:
            conversational_kwargs = {}

        self.pipline_kwargs = pipline_kwargs

        self.input_device = input_device
        self.eos_pattern = eos_pattern

        self.config = AutoConfig.from_pretrained(model, trust_remote_code=True, **config_kwargs)
        tokenizer_name = tokenizer or model
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, trust_remote_code=True)

        self.net = AutoModelForCausalLM.from_pretrained(model, trust_remote_code=True,
                                                        config=self.config, **model_kwargs)

        if compile:
            import torch
            self.net = torch.compile(self.net)

        self._text_generation_pipeline = transformers.pipeline('text-generation', model=self.net,
                                                               tokenizer=self.tokenizer, device=self.input_device,
                                                               return_full_text=False, **text_generation_kwargs)

        self._conversational_pipeline = transformers.pipeline('conversational', model=self.net,
                                                              tokenizer=self.tokenizer, device=self.input_device,
                                                              **conversational_kwargs)

    def extract_text(self, res):

        res = res.response
        if type(res) is list:
            res = res[0]

        if type(res) is Conversation:
            res = res.generated_responses[-1]
        else:
            res = res['generated_text']

        if self.eos_pattern:
            res = res.split(self.eos_pattern)[0]

        return res

    @property
    def is_chat(self):
        return True

    @property
    def is_completions(self):
        return True

    def _completion(self, prompt=None, **kwargs):

        # pipeline = transformers.pipeline('text-generation', model=self.model,
        #                                  tokenizer=self.tokenizer, device=self.input_device, return_full_text=False)

        res = self._text_generation_pipeline(prompt, pad_token_id=self._text_generation_pipeline.tokenizer.eos_token_id,
                                             **self.pipline_kwargs)

        return res

    def _chat_completion(self, **kwargs):

        # pipeline = transformers.pipeline('conversational', model=self.model,
        #                                  tokenizer=self.tokenizer, device=self.input_device)

        return self._conversational_pipeline(self.conversation,
                                             pad_token_id=self._conversational_pipeline.tokenizer.eos_token_id,
                                             **self.pipline_kwargs)
