# Класс с запросами к Poloniex
import requests
# import json
import time
import base64
import hmac
import hashlib


class pubPoloRq:
    # Получаем тикер BTCUSDTPERP - усредненная цена Bid-Ask
    @classmethod
    def getFuturesTickerBTCUSDT(cls):
        # Ссылка на получение тикера
        url = 'https://futures-api.poloniex.com/api/v2/ticker?symbol=BTCUSDTPERP'
        headers = {
            'User-Agent': 'My User Agent 1.0',
        }
        # Максимальное Количество повторений запросов
        maxReqCount = 100
        j = 0
        # По умолчанию ответ не получен
        result = "Service Poloniex is unavailable. Please visit https://poloniex.com/ for details"
        while j < maxReqCount:
            try:
                response = requests.request('get', url, headers=headers)
            except Exception:
                j += 1
                # Пауза перед следующей попыткой запроса
                time.sleep(0.2)
            else:
                avgBidAsk = (float(response.json()['data']['bestBidPrice']) +
                             float(response.json()['data']['bestAskPrice'])) * 0.5
                result = "{:.1f}".format(avgBidAsk)
                # Выход из цикла while
                j = maxReqCount
        return result


class privatePoloRq:
    # Максимальное Количество повторений запросов
    maxReqCount = 100

    def __init__(self, api_key, api_secret, api_passphrase):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase

    # Получаем баланс аккаунта
    def getFuturesAccountBalance(self):
        # Ссылка для запроса
        url = 'https://futures-api.poloniex.com/api/v1/account-overview'
        now = int(time.time() * 1000)
        # Формируем и шифруем строку запроса
        str_to_sign = str(now) + 'GET' + '/api/v1/account-overview'
        signature = base64.b64encode(
            hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        headers = {
            'User-Agent': 'My User Agent 1.0',
            "PF-API-SIGN": signature,
            "PF-API-TIMESTAMP": str(now),
            "PF-API-KEY": self.api_key,
            "PF-API-PASSPHRASE": self.api_passphrase
        }
        j = 0
        # По умолчанию ответ не получен
        result = ["Service Poloniex is unavailable. Please visit https://poloniex.com/ for details"]
        while j < self.maxReqCount:
            try:
                response = requests.request('get', url, headers=headers)
            except Exception:
                j += 1
                # Пауза перед следующей попыткой запроса
                time.sleep(0.2)
            else:
                result = ["{:.1f}".format(float(response.json()['data']['accountEquity'])),
                          "{:.1f}".format(float(response.json()['data']['availableBalance']))]
                # Выход из цикла while
                j = self.maxReqCount
        return result

    # Получаем список открытых позиций
    def getFuturesPositions(self):
        # Ссылка для запроса
        url = 'https://futures-api.poloniex.com/api/v1/positions'
        now = int(time.time() * 1000)
        # Формируем и шифруем строку запроса
        str_to_sign = str(now) + 'GET' + '/api/v1/positions'
        signature = base64.b64encode(
            hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        headers = {
            'User-Agent': 'My User Agent 1.0',
            "PF-API-SIGN": signature,
            "PF-API-TIMESTAMP": str(now),
            "PF-API-KEY": self.api_key,
            "PF-API-PASSPHRASE": self.api_passphrase
        }
        j = 0
        # По умолчанию ответ не получен
        result = ["Service Poloniex is unavailable. Please visit https://poloniex.com/ for details"]
        while j < self.maxReqCount:
            try:
                response = requests.request('get', url, headers=headers)
            except Exception:
                j += 1
                # Пауза перед следующей попыткой запроса
                time.sleep(0.2)
            else:
                if len(response.json()['data']) > 0:
                    result = response.json()['data']
                else:
                    result = []
                    # Выход из цикла while
                j = self.maxReqCount
        return result

    # Получаем список открытых ордеров
    def getFuturesOrders(self):
        # Ссылка для запроса
        url = 'https://futures-api.poloniex.com/api/v1/orders?status=active'
        now = int(time.time() * 1000)
        # Формируем и шифруем строку запроса
        str_to_sign = str(now) + 'GET' + '/api/v1/orders?status=active'
        signature = base64.b64encode(
            hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        headers = {
            'User-Agent': 'My User Agent 1.0',
            "PF-API-SIGN": signature,
            "PF-API-TIMESTAMP": str(now),
            "PF-API-KEY": self.api_key,
            "PF-API-PASSPHRASE": self.api_passphrase
        }
        j = 0
        # По умолчанию ответ не получен
        result = ["Service Poloniex is unavailable. Please visit https://poloniex.com/ for details"]
        while j < self.maxReqCount:
            try:
                response = requests.request('get', url, headers=headers)
            except Exception:
                j += 1
                # Пауза перед следующей попыткой запроса
                time.sleep(0.2)
            else:
                if len(response.json()['data']['items']) > 0:
                    # Сортируем открытые заявки по цене по убыванию
                    result = sorted(response.json()['data']['items'], key=lambda order: order['price'], reverse=True)
                else:
                    result = []
                    # Выход из цикла while
                j = self.maxReqCount
        return result

    # Получаем список закрытых позиций (за последние 24 часа)
    def getFuturesFills(self):
        # Ссылка для запроса
        url = 'https://futures-api.poloniex.com/api/v1/fills'
        now = int(time.time() * 1000)
        # Формируем и шифруем строку запроса
        str_to_sign = str(now) + 'GET' + '/api/v1/fills'
        signature = base64.b64encode(
            hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        headers = {
            'User-Agent': 'My User Agent 1.0',
            "PF-API-SIGN": signature,
            "PF-API-TIMESTAMP": str(now),
            "PF-API-KEY": self.api_key,
            "PF-API-PASSPHRASE": self.api_passphrase
        }
        j = 0
        # По умолчанию ответ не получен
        result = ["Service Poloniex is unavailable. Please visit https://poloniex.com/ for details"]
        while j < self.maxReqCount:
            try:
                response = requests.request('get', url, headers=headers)
            except Exception:
                j += 1
                # Пауза перед следующей попыткой запроса
                time.sleep(0.2)
            else:
                if len(response.json()['data']['items']) > 0:
                    result = response.json()['data']['items']
                else:
                    result = []
                    # Выход из цикла while
                j = self.maxReqCount
        return result
