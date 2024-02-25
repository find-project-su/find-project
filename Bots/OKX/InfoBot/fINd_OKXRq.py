# Класс с запросами к OKX
import requests
import time
import base64
import hmac
import hashlib
import okx.MarketData as MarketData
import okx.Account as Account


class pubOKXRq:
    # Максимальное Количество повторений запросов
    maxReqCount = 100
    # Реальный счет => 0
    flag = '0'

    # Получаем тикер last price
    def getTicker(self, instId: str, debug: bool):
        j = 0
        # По умолчанию ответ не получен
        result = "Service OKX is unavailable. Please visit https://www.okx.com/ for details"
        while j < self.maxReqCount:
            try:
                marketDataAPI = MarketData.MarketAPI(flag=self.flag, debug=debug)
            except Exception:
                j += 1
                # Пауза перед следующей попыткой запроса
                time.sleep(0.2)
            else:
                tickData = marketDataAPI.get_ticker(instId=instId)
                result = tickData['data'][0]['last']
                # Выход из цикла while
                j = self.maxReqCount
        return result


class privateOKXRq:
    # Максимальное Количество повторений запросов
    maxReqCount = 100
    rqTimeOut = 15
    flag = '0'

    def __init__(self, api_key, secret_key, passphrase, debug):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        self.debug = debug

    # Получаем баланс аккаунта
    def getAccountBalance(self):
        accountAPI = Account.AccountAPI(self.api_key,
                                        self.secret_key,
                                        self.passphrase,
                                        False,
                                        flag=self.flag,
                                        debug=self.debug)
        j = 0
        # По умолчанию ответ не получен
        result = ["Service OKX is unavailable. Please visit https://OKX.com/ for details"]
        while j < self.maxReqCount:
            try:
                accountDataAPI = accountAPI.get_account_balance()
            except Exception:
                j += 1
                # Пауза перед следующей попыткой запроса
                time.sleep(0.2)
            else:
                result = ["{:.1f}".format(float(accountDataAPI['data'][0]['totalEq'])),
                          "{:.1f}".format(float(accountDataAPI['data'][0]['totalEq']))]
                # Выход из цикла while
                j = self.maxReqCount
        return result

    # Получаем список открытых позиций
    def getFuturesPositions(self):
        # Ссылка для запроса
        # url = 'https://futures-api.OKX.com/api/v1/positions'
        # now = int(time.time() * 1000)
        # # Формируем и шифруем строку запроса
        # str_to_sign = str(now) + 'GET' + '/api/v1/positions'
        # signature = base64.b64encode(
        #     hmac.new(self.secret_key.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        # headers = {
        #     'User-Agent': 'My User Agent 1.0',
        #     "PF-API-SIGN": signature,
        #     "PF-API-TIMESTAMP": str(now),
        #     "PF-API-KEY": self.api_key,
        #     "PF-API-PASSPHRASE": self.passphrase
        # }
        # j = 0
        # # По умолчанию ответ не получен
        # result = ["Service OKX is unavailable. Please visit https://OKX.com/ for details"]
        # while j < self.maxReqCount:
        #     try:
        #         response = requests.request('get', url, headers=headers, timeout=self.rqTimeOut)
        #     except Exception:
        #         j += 1
        #         # Пауза перед следующей попыткой запроса
        #         time.sleep(0.2)
        #     else:
        #         if len(response.json()['data']) > 0:
        #             result = response.json()['data']
        #         else:
        #             result = []
        #             # Выход из цикла while
        #         j = self.maxReqCount
        result = []
        return result

    # Получаем список открытых ордеров
    def getFuturesOrders(self):
        # Ссылка для запроса
        # url = 'https://futures-api.OKX.com/api/v1/orders?status=active'
        # now = int(time.time() * 1000)
        # # Формируем и шифруем строку запроса
        # str_to_sign = str(now) + 'GET' + '/api/v1/orders?status=active'
        # signature = base64.b64encode(
        #     hmac.new(self.secret_key.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        # headers = {
        #     'User-Agent': 'My User Agent 1.0',
        #     "PF-API-SIGN": signature,
        #     "PF-API-TIMESTAMP": str(now),
        #     "PF-API-KEY": self.api_key,
        #     "PF-API-PASSPHRASE": self.passphrase
        # }
        # j = 0
        # # По умолчанию ответ не получен
        # result = ["Service OKX is unavailable. Please visit https://OKX.com/ for details"]
        # while j < self.maxReqCount:
        #     try:
        #         response = requests.request('get', url, headers=headers, timeout=self.rqTimeOut)
        #     except Exception:
        #         j += 1
        #         # Пауза перед следующей попыткой запроса
        #         time.sleep(0.2)
        #     else:
        #         if len(response.json()['data']['items']) > 0:
        #             # Сортируем открытые заявки по цене по убыванию
        #             result = sorted(response.json()['data']['items'], key=lambda order: order['price'], reverse=True)
        #         else:
        #             result = []
        #             # Выход из цикла while
        #         j = self.maxReqCount
        result = []
        return result

    # Получаем список закрытых позиций (за последние 24 часа)
    def getFuturesFills(self):
        # Ссылка для запроса
        url = 'https://futures-api.OKX.com/api/v1/fills'
        now = int(time.time() * 1000)
        # Формируем и шифруем строку запроса
        str_to_sign = str(now) + 'GET' + '/api/v1/fills'
        signature = base64.b64encode(
            hmac.new(self.secret_key.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
        headers = {
            'User-Agent': 'My User Agent 1.0',
            "PF-API-SIGN": signature,
            "PF-API-TIMESTAMP": str(now),
            "PF-API-KEY": self.api_key,
            "PF-API-PASSPHRASE": self.passphrase
        }
        j = 0
        # По умолчанию ответ не получен
        result = ["Service OKX is unavailable. Please visit https://OKX.com/ for details"]
        while j < self.maxReqCount:
            try:
                response = requests.request('get', url, headers=headers, timeout=self.rqTimeOut)
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
