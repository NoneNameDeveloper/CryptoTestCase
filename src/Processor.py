import asyncio

from src import BinanceApi

import numpy as np

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s::%(message)s')


class Processor:
    """
    executable class
    """

    def __init__(self):
        pass

    @staticmethod
    def get_correlation(rates_1: list[float], rates_2: list[float]) -> float:
        """
        return lineal correlation of 2 lists
        :param rates_1:
        :type rates_1:
        :param rates_2:
        :type rates_2:
        :return:
        :rtype:
        """
        # getting correlation
        correlation = np.corrcoef(rates_1, rates_2)

        return correlation

    @staticmethod
    async def main():
        """
        main
        :return:
        :rtype:
        """

        while True:
            client = BinanceApi()

            eth_klineses = await client.get_kliness(
                symbol="ETHUSDT"
            )
            btc_klineses = await client.get_kliness(
                symbol="BTCUSDT"
            )

            eth_tickers = [float(u[4]) for u in eth_klineses]
            btc_tickers = [float(u[4]) for u in btc_klineses]

            # different length of the arrays - correlation unavailable
            if len(eth_tickers) == len(btc_tickers):
                correlation = Processor.get_correlation(eth_tickers, btc_tickers)
            else:
                continue

            # getting data of corellation and
            # comparing it with my theory
            correlation_row = correlation[0][1]

            if isinstance(correlation_row, float):
                if correlation_row > 0.9:
                    continue

                # getting diff percentage of
                # now and 1h ago ticks
                eth_delta = abs(eth_tickers[-1] / eth_tickers[0] * 100 - 100)

                if eth_delta >= 1:
                    logging.info(f"Percent: {eth_delta}%!")

            await asyncio.sleep(1)
