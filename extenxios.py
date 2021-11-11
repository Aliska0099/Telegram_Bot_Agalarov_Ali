import json
import requests

from config import exchanger

class ConverterExeption(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(sym, base, amount):
        try:
            sym_key = exchanger[sym.lower()]
        except KeyError:
            raise ConverterExeption(f"Валюта {sym} не найдена!")

        try:
            base_key = exchanger[base.lower()]
        except KeyError:
            raise ConverterExeption(f"Валюта {base} не найдена!")

        if sym_key == base_key:
            raise ConverterExeption(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConverterExeption(f'Не удалось обработать количество {amount}!')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={sym_key}&tsyms={base_key}")
        resp = json.loads(r.content)
        new_price = resp[base_key] * amount
        new_price = round(new_price, 3)
        message = f"Цена {amount} {sym} в {base} : {new_price}"
        return message







