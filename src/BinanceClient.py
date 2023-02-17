import asyncio
import time

import aiohttp


class BinanceApi:
    """
    https://www.binance.com/ru/binance-api simple
    asyncio client for small task
    """
    def __init__(self):
        self.base_url = "https://api.binance.com"

    async def get_kliness(
            self,
            symbol: str = None,
            interval: str = "1m",
            limit: int = 100,
            start_time: int = int(time.time() - 3600) * 1000):
        """
        Kline/candlestick bars for the index price of a pair.
        :param symbol: required
        :type symbol: str
        :param interval: required
        :type interval: str
        :param limit: optional
        :type limit: int
        :param start_time: time in unixstamp in ms optional (but required)
        :type start_time: int
        :return:
        [
              [
                1591256400000,          // Open time
                "9653.69440000",        // Open
                "9653.69640000",        // High
                "9651.38600000",        // Low
                "9651.55200000",        // Close (or latest price)
                "0  ",                  // Ignore
                1591256459999,          // Close time
                "0",                    // Ignore
                60,                     // Ignore
                "0",                    // Ignore
                "0",                    // Ignore
                "0"                     // Ignore
              ]
        ]
        :rtype: dict
        """

        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
            "startTime": start_time,
        }

        path = "/api/v3/klines"

        async with aiohttp.ClientSession() as session:
            req = await session.get(self.base_url + path, params=params)

            req_json = await req.json()

            return req_json

