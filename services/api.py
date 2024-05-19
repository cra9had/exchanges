import asyncio
import logging
import xml.etree.ElementTree as ET
from typing import Literal

import aiohttp

from services.const import CB_GET_EXCHANGE_RATE_URL

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
    async def convert
    url = 'https://api.coincap.io/v2/assets/monero'
