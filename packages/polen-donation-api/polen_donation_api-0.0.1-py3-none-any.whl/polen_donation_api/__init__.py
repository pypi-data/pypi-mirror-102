import requests
import json


class PolenCharityDonationAPI:
    base_url = 'https://api.polen.com.br/api/v2'

    def __init__(self, api_token: str):
        self.api_token = api_token

    # Cause

    def get_all_cause(self, params={}):
        """Método que retorna todas as causas cadastradas
            Parameter
            ----------
              params: dict
                Dicionário com as configurações adicionais
        """

        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/cause/all', params=params)

    def get_all_categories(self, params={}):
        """Método que retorna todas as categorias cadastradas
              Parameter
              ----------
                params: dict
                  Dicionário com as configurações adicionais
        """

        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/cause/categories', params=params)

    def get_own_cause(self, params: dict):
        """Método que retorna todas as causas de uma loja
            Parameter
            ----------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/cause', params=params)

    # Company

    def get_company_detail(self, params: dict):
        """Método que retorna os detalhes de uma empresa
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/company/detail', params=params)

    def get_company_list(self, params: dict):
        """Método que retorna uma lista com as empresas de uma conta
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/company/list', params=params)

    def get_company_stores(self, params: dict):
        """Método que retorna uma lista de lojas de uma empresa
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/company/stores', params=params)

    def update_company(self, body: dict, params: dict):
        """Método que atualiza uma empresa
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.put(f'{self.base_url}/company/update', params=params, data=json.dump(body))

    def create_company(self, body: dict, params={}):
        """Método que cria uma nova empresa

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/company/update', params=params, json=body)

    # Donation Direct

    def create_donation_direct(self, body: dict, params={}):
        """Método que cria uma doação direta

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/donation/direct', params=params, json=body)

    # Donation Notify

    def get_donation_notify_detail(self, params: dict):
        """Método que retorna de detalhes de uma doação especifica
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/donation/notify/detail', params=params)

    def get_donation_notify_list(self, params: dict):
        """Método que retorna uma lista de doações da loja
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/donation/notify/list', params=params)

    def update_donation_notify(self, body: dict, params={}):
        """Método que atualiza o status da doação

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.put(f'{self.base_url}/donation/notify/update', params=params, data=json.dump(body))

    def create_donation_notify(self, body: dict, params: dict):
        """Método que cria uma nova doação

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/donation/notify/create', params=params, json=body)

    # Finance

    def get_finance_billing_list(self, params: dict):
        """Método que retorna uma lista de faturas de doações

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/finance/billing/list', params=params)

    # Platform

    def get_platform_list(self, params={}):
        """Método que retorna uma lista de plataformas associadas

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/platform/list', params=params)

    # Store

    def get_store_detail(self, params: dict):
        """Método que retorna detalhes de uma loja

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/store/detail', params=params)

    def get_store_list(self, params={}):
        """Método que retorna uma lista de lojas cadastradas em uma conta

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/store/list', params=params)

    def update_store(self, body: dict, params: dict):
        """Método que atualiza uma loja

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.put(f'{self.base_url}/store/update', params=params, data=json.dump(body))

    def add_cause_store(self, body: dict, params: dict):
        """Método que adiciona uma causa a loja

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/store/cause/add', params=params, json=body)

    def create_store(self, body: dict, params: dict):
        """Método que cria uma nova loja

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/store/create', params=params, json=body)

    def remove_cause_store(self, body: dict, params: dict):
        """Método que remove uma causa de uma loja

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/store/cause/remove', params=params, json=body)

    # Transparency

    def get_transparency_impact_consolidated(self, params: dict):
        """Método que retorna consolidado doado por uma empresa

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/transparency/impact/consolidated', params=params)

    def get_transparency_content_detail(self, params: dict):
        """Método que retorna detalhes do conteúdo de impacto

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/transparency/content/detail', params=params)

    def get_transparency_receipts(self, params: dict):
        """Método que retorna detalhes do conteúdo de impacto

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/transparency/receipts', params=params)

    def get_transparency_content_list(self, params: dict):
        """Método que retorna lista de conteúdos de impacto

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/transparency/content/list', params=params)

    # User

    def get_user_detail(self, params: dict):
        """Método que retorna detalhes de um usuário

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/user/detail', params=params)

    def get_user_impact(self, params: dict):
        """Método que retorna detalhes do impacto social causado pelo usuário

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/user/impact', params=params)

    def get_user_list(self, params: dict):
        """Método que retorna uma lista de usuários cadastrados na loja

            Parameter
            _________
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/user/list', params=params)

    def update_user(self, body: dict, params: dict):
        """Método que atualiza as informações de um usuário

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.put(f'{self.base_url}/user/update', params=params, data=json.dump(body))

    def add_user(self, body: dict, params: dict):
        """Método que cria um novo usuário ligado a loja

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/user/create', params=params, json=body)

    def update_user_cause(self, body: dict, params: dict):
        """Método que adiciona ou remove causas ligadas a um usuário

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/user/causes', params=params, json=body)

    #Transaction

    def update_transaction_status(self, params: dict, body={}):
        """Método que ajuda o sistema entender o status da compra

                    Parameter
                    ---------
                      params: dict
                        Dicionário com as configurações adicionais
                      body: dict
                        Dicionário com o corpo da requisição
                """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/user/causes', params=params, json=body)
