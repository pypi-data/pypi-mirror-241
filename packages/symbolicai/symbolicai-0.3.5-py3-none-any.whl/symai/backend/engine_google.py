from typing import List

from IPython.utils import io

from .base import Engine
from .settings import SYMAI_CONFIG

try:
    from serpapi import GoogleSearch
except:
    GoogleSearch = None



class GoogleEngine(Engine):
    def __init__(self):
        super().__init__()
        config = SYMAI_CONFIG
        self.api_key = config['SEARCH_ENGINE_API_KEY']
        self.engine = config['SEARCH_ENGINE_MODEL']

    def command(self, wrp_params):
        super().command(wrp_params)
        if 'SEARCH_ENGINE_API_KEY' in wrp_params:
            self.api_key = wrp_params['SEARCH_ENGINE_API_KEY']
        if 'SEARCH_ENGINE_API_KEY' in wrp_params:
            self.engine = wrp_params['SEARCH_ENGINE_MODEL']

    def forward(self, queries: List[str], *args, **kwargs) -> List[str]:
        queries_ = queries if isinstance(queries, list) else [queries]
        rsp      = []

        input_handler = kwargs['input_handler'] if 'input_handler' in kwargs else None
        if input_handler:
            input_handler((queries_,))

        for q in queries_:
            query = {
                "api_key": self.api_key,
                "engine": self.engine,
                "q": q,
                "google_domain": "google.com",
                "gl": "us",
                "hl": "en"
            }

            # send to Google
            with io.capture_output() as captured: # disables prints from GoogleSearch
                search = GoogleSearch(query)
                res = search.get_dict()

            if 'answer_box' in res.keys() and 'answer' in res['answer_box'].keys():
                toret = res['answer_box']['answer']
            elif 'answer_box' in res.keys() and 'snippet' in res['answer_box'].keys():
                toret = res['answer_box']['snippet']
            elif 'answer_box' in res.keys() and 'snippet_highlighted_words' in res['answer_box'].keys():
                toret = res['answer_box']["snippet_highlighted_words"][0]
            elif 'organic_results' in res and 'snippet' in res["organic_results"][0].keys():
                toret= res["organic_results"][0]['snippet']
            else:
                toret = res

            rsp.append(toret)

        output_handler = kwargs['output_handler'] if 'output_handler' in kwargs else None
        if output_handler:
            output_handler(rsp)

        metadata = {}
        if 'metadata' in kwargs and kwargs['metadata']:
            metadata['kwargs'] = kwargs
            metadata['input']  = queries_
            metadata['output'] = rsp

        output = rsp if isinstance(queries, list) else rsp[0]
        return output, metadata

    def prepare(self, args, kwargs, wrp_params):
        wrp_params['queries'] = [str(wrp_params['query'])]
