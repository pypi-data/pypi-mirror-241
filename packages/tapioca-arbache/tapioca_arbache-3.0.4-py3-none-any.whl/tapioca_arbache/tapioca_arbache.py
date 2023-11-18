import json

from tapioca import (
    JSONAdapterMixin, TapiocaAdapter, generate_wrapper_from_adapter
)
from requests_oauthlib import OAuth2
from tapioca.exceptions import ClientError

from tapioca_arbache.resource_mapping import (
    CRM_EQUIPES_ENDPOINT, CRM_MIDIAS_ENDPOINT, CRM_PERFIL_ENDPOINT, CRM_OAUTH,
    CRM_LICENCA_ENDPOINT, INTERFACE, JOGO_SELF, PLAY_MIDIAS_ENDPOINT,
    RELATORIOS, CRM_JOGO_ENDPOINT, PLAY_RESULTADOS_JOGOS_ENDPOINT,
    PLAY_SUBDOMINIO_ENDPOINT, PLAY_JOGO_SUBDOMINIO_ENDPOINT
)
from tapioca_arbache.exceptions import ConflictException


class ArbacheAdapter(JSONAdapterMixin, TapiocaAdapter):
    prod_url = 'https://crm.arbache.com.br'
    homolog_url = 'https://crm-homolog.arbache.dev.br'
    dev_url = 'http://127.0.0.1:8000'

    def get_api_root(self, api_params, **kwargs):
        if url := api_params.get('url', ''):
            return url
        elif api_params.get('ambiente', '').lower() == 'dev':
            return self.dev_url
        elif api_params.get('ambiente', '').lower() == 'homolog':
            return self.homolog_url
        else:
            return self.prod_url

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(ArbacheAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )

        assert 'perfil' in api_params, ('Obrigatorio passar o perfil requisitante')

        params['auth'] = OAuth2(
            api_params.get('client_id'),
            token={
                'access_token': api_params.get('access_token'),
                'token_type': 'Bearer'
            }
        )

        if not params.get('params', False):
            params['params'] = {}

        params['params']['perfil'] = api_params['perfil']

        return params

    def get_iterator_list(self, response_data):
        return response_data['registros']

    def get_iterator_next_request_kwargs(
        self, iterator_request_kwargs, response_data, response
    ):
        pagina_atual = iterator_request_kwargs['params'].get('pagina', None)
        if pagina_atual is None:
            iterator_request_kwargs['params']['pagina'] = 2
        else:
            iterator_request_kwargs['params']['pagina'] = pagina_atual + 1

        return iterator_request_kwargs

    def process_response(self, response):
        if response.status_code == 409:
            raise ConflictException()

        elif 400 <= response.status_code < 500:
            if response.content and response.request.body:
                response_body = json.loads(response.content)
                request_body = json.loads(response.request.body)

                message = {
                    'status_code': response.status_code,
                    'response_body': response_body,
                    'request_body': request_body
                }

                erro = ClientError(message=message)
                erro.status_code = response.status_code
                raise erro

        return super().process_response(response)


class PerfilAdapter(ArbacheAdapter):
    resource_mapping = CRM_PERFIL_ENDPOINT


class OauthAdapter(ArbacheAdapter):
    resource_mapping = CRM_OAUTH

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(ArbacheAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )
        required = ['client_id', 'grant_type', 'username', 'password']

        assert params['data'], ('Os dados necessários não foram informados')

        for param in required:
            assert param in params['data'], (f'{param} não informado')

        return params


class LicencaAdapter(ArbacheAdapter):
    resource_mapping = CRM_LICENCA_ENDPOINT


class JogoSelfAdapter(ArbacheAdapter):
    prod_url = 'https://play-api.arbache.dev.br'
    homolog_url = 'https://play-api-homolog.arbache.dev.br'
    dev_url = 'http://127.0.0.1:8003'
    resource_mapping = JOGO_SELF


class RelatoriosAdapter(ArbacheAdapter):
    prod_url = 'https://gestao.arbache.dev.br'
    homolog_url = 'https://gestao-homolog.arbache.dev.br/'
    dev_url = 'http://127.0.0.1:8002'
    resource_mapping = RELATORIOS


class JogoAdapter(ArbacheAdapter):
    resource_mapping = CRM_JOGO_ENDPOINT


class EquipeAdapter(ArbacheAdapter):
    resource_mapping = CRM_EQUIPES_ENDPOINT


class PlayMidiaAdapter(ArbacheAdapter):
    resource_mapping = PLAY_MIDIAS_ENDPOINT


class InterfaceAdapter(ArbacheAdapter):
    resource_mapping = INTERFACE


class CrmMidiaAdapter(ArbacheAdapter):
    resource_mapping = CRM_MIDIAS_ENDPOINT


class PlayResultadoJogoAdapter(ArbacheAdapter):
    prod_url = 'https://play-api.arbache.dev.br'
    homolog_url = 'https://play-api-homolog.arbache.dev.br'
    dev_url = 'http://127.0.0.1:8003'
    resource_mapping = PLAY_RESULTADOS_JOGOS_ENDPOINT


class PlaySubdominioAdapter(ArbacheAdapter):
    prod_url = 'https://play-api.arbache.dev.br'
    homolog_url = 'https://play-api-homolog.arbache.dev.br'
    dev_url = 'http://127.0.0.1:8003'
    resource_mapping = PLAY_SUBDOMINIO_ENDPOINT


class PlayJogosSubdominioAdapter(ArbacheAdapter):
    prod_url = 'https://play-api.arbache.dev.br'
    homolog_url = 'https://play-api-homolog.arbache.dev.br'
    dev_url = 'http://127.0.0.1:8003'
    resource_mapping = PLAY_JOGO_SUBDOMINIO_ENDPOINT


PerfilClient = generate_wrapper_from_adapter(PerfilAdapter)
OauthClient = generate_wrapper_from_adapter(OauthAdapter)
LicencaClient = generate_wrapper_from_adapter(LicencaAdapter)
JogoSelfClient = generate_wrapper_from_adapter(JogoSelfAdapter)
RelatorioClient = generate_wrapper_from_adapter(RelatoriosAdapter)
JogoClient = generate_wrapper_from_adapter(JogoAdapter)
EquipeClient = generate_wrapper_from_adapter(EquipeAdapter)
PlayMidiaClient = generate_wrapper_from_adapter(PlayMidiaAdapter)
InterfaceClient = generate_wrapper_from_adapter(InterfaceAdapter)
CrmMidiaClient = generate_wrapper_from_adapter(CrmMidiaAdapter)
ResultadoJogoClient = generate_wrapper_from_adapter(PlayResultadoJogoAdapter)
PlaySubdominioClient = generate_wrapper_from_adapter(PlaySubdominioAdapter)
PlayJogosSubdominioClient = generate_wrapper_from_adapter(PlayJogosSubdominioAdapter)
