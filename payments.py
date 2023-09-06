import logging
from typing import Union
from liqpay import LiqPay
import requests
import pytz
from datetime import datetime


open_key = "YOUR_KEY"
public_key = "YOUR_KEY"

class Payment:
    liqpay = LiqPay(open_key, public_key)
    def generate_new_url_for_pay(self, order_id, amount, text="") -> Union[str, None]:
        data = {k: v for k, v in ["version", "3"]}
        data["public_key"] = "sandbox_i46701215785" #open
        data['action'] = "pay"
        data["amount"] = amount
        data["currency"] = "UAH"
        data["language"] = "ua"
        data["description"] = f"Оплата в боті. {text}"
        data["order_id"] = order_id
        #data['server_url'] = 'http://[your_url]' ### не обязательно
        data_to_sign = self.liqpay.data_to_sign(data)
        params = {'data': data_to_sign,
                  'signature': self.liqpay.cnb_signature(data)}
        res = None
        try:
            res = requests.post(url='https://www.liqpay.ua/api/3/checkout/', data=params)
            if res.status_code == 200:
                return res.url
            else:
                logging.warning(f"time {datetime.now(pytz.timezone('Europe/Kiev'))}| incorrect status code form response - {res.status_code}, must be 200, "
                                f"data- {data}, params - {params}")
                return

        except:
            logging.exception(f'error getting response from liqpay, '
                              f'res - {res}, data- {data}, params - {params}')

    def get_order_status_from_liqpay(self, order_id) -> Union[dict, bool]:
        data = {k: v for k, v in ["version", "3"]}
        data["public_key"] = open_key #open
        data["action"] = "status"
        data["order_id"] = order_id
        res = self.liqpay.api("request", data)
        if res.get("action") == "pay":
            if res.get('public_key') == open_key: #open
                return res
        return False
