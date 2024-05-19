import asyncio
import logging
import os
import xml.etree.ElementTree as ET
from typing import Literal

import aiohttp
from aiohttp import ClientTimeout
from dotenv import load_dotenv, find_dotenv

from services.const import CB_GET_EXCHANGE_RATE_URL, COINCAP_MAIN_URL, TIMEOUT_RETRIES

load_dotenv(find_dotenv())

COINCAP_HEADERS = {
    'Accept-Encoding': 'gzip',
    'Authorization': f'Bearer {os.getenv("API_KEY")}'
}

print(COINCAP_HEADERS)

logger = logging.getLogger(__file__)


class Exchanger:

    @staticmethod
    async def _get_bank_curr_exchange_rates(curr_char_code: Literal['EUR', 'USD']):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(CB_GET_EXCHANGE_RATE_URL) as r:
                    if r.status != 200:
                        logging.error(f"Request to CBR failed with status {r.status}")
                        return None

                    xml_content = await r.read()
            except aiohttp.ClientError as e:
                logging.error(f"aiohttp ClientError: {e}")
                return None
        try:
            root = ET.fromstring(xml_content.decode('windows-1251'))
            curr_elem = root.find(f".//Valute[CharCode='{curr_char_code}']")
            curr = float(curr_elem.find('Value').text.replace(',', '.'))

        except (ET.ParseError, AttributeError, ValueError) as e:
            logger.error(f"Can't get USD/EUR value from XML content: {e}")
            return None

        return curr

    @staticmethod
    async def get_usd_and_euro_exchange_rates():
        usd = await Exchanger.get_usd_exchange_rates()
        euro = await Exchanger.get_euro_exchange_rates()

        return {'usd': usd, 'euro': euro}

    @staticmethod
    async def get_usd_exchange_rates():
        return await Exchanger._get_bank_curr_exchange_rates(curr_char_code='USD')

    @staticmethod
    async def get_euro_exchange_rates():
        return await Exchanger._get_bank_curr_exchange_rates(curr_char_code='EUR')

    @staticmethod
    async def _get_currency(currency_code: Literal['bitcoin', 'ethereum', 'tether', 'usd-coin', 'tron'] | str):
        for i in range(TIMEOUT_RETRIES):
            try:
                async with aiohttp.ClientSession(timeout=ClientTimeout(1)) as session:
                    session.headers.update(COINCAP_HEADERS)
                    r = await session.get(COINCAP_MAIN_URL + '/' + currency_code)
                    if r.status != 200:
                        logging.error(f"Request to {currency_code} failed with status {r.status}")
                        return None
                return await r.json()
            except aiohttp.ClientError as e:
                logging.error(f"aiohttp ClientError: {e}")
                return None
            except asyncio.TimeoutError as e:
                continue

    @staticmethod
    async def get_curr_value_in_rub(rub_value, currency_code):
        currency = await Exchanger._get_currency(currency_code)
        if not currency:
            logger.error(f"Can't get currency from {currency_code}")
            return None

        dollar_to_rub = await Exchanger.get_usd_exchange_rates()
        print(rub_value, dollar_to_rub, currency['data']['priceUsd'])
        result_curr_value = rub_value / dollar_to_rub / float(currency.get('data').get('priceUsd'))

        return result_curr_value
