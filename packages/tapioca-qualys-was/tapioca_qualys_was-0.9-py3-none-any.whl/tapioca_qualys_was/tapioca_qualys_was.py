# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from requests.auth import HTTPBasicAuth
import xmltodict

from .resource_mapping import RESOURCE_MAPPING


class Qualys_wasClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://qualysapi.qg3.apps.qualys.com'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        # stores kwargs prefixed with 'xmltodict_unparse__' for use by xmltodict.unparse
        self._xmltodict_unparse_kwargs = {k[len('xmltodict_unparse__'):]: kwargs.pop(k)
                                          for k in kwargs.copy().keys()
                                          if k.startswith('xmltodict_unparse__')}
        # stores kwargs prefixed with 'xmltodict_parse__' for use by xmltodict.parse
        self._xmltodict_parse_kwargs = {k[len('xmltodict_parse__'):]: kwargs.pop(k)
                                        for k in kwargs.copy().keys()
                                        if k.startswith('xmltodict_parse__')}

        params = super(Qualys_wasClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = HTTPBasicAuth(
            api_params.get('user'), api_params.get('password'))

        if 'headers' not in params:
            params['headers'] = {}

        params['headers'].update({
            'Content-Type': 'application/json'})

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass

    def response_to_native(self, response):
        if response.content.strip():
            if 'xml' in response.headers['content-type']:
                return xmltodict.parse(response.content, **self._xmltodict_parse_kwargs)
            elif 'json' in response.headers['content-type']:
                return response.json()
        return {'text': response.text}


Qualys_was = generate_wrapper_from_adapter(Qualys_wasClientAdapter)
