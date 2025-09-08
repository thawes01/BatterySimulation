import csv
from typing import Iterable


class Timepoint:
    def __init__(self):
        self._timestamp = "2025-01-01 06:30"

    def __str__(self):
        return self._timestamp


class Market:
    def __init__(self, id: str, price_interval: int):
        self.id = id
        self.price_interval = price_interval


class MarketDispatch:
    def __init__(self, market_id: str, discharge_power: float, price: float):
        self.market_id = market_id
        self.discharge_power = discharge_power
        self.price = price


class Dispatch:
    def __init__(self, timepoint: Timepoint, market_dispatches: list[MarketDispatch]):
        self._timepoint = timepoint
        self._market_dispatches = {m.market_id: m for m in market_dispatches}

    @property
    def timepoint(self) -> Timepoint:
        return self._timepoint

    def discharge(self, market_id: str) -> float:
        return self._market_dispatches[market_id].discharge_power

    def price(self, market_id: str) -> float:
        return self._market_dispatches[market_id].price

    @property
    def revenue(self) -> float:
        return 0.0


class Battery:
    def update(self, dispatch: Dispatch):
        pass


class Operator:
    def dispatch(
        self, timepoint: Timepoint, battery: Battery, market1: Market, market2: Market
    ) -> Dispatch:
        market_dispatches = [
            MarketDispatch(market1.id, 0.0, 0.0),
            MarketDispatch(market2.id, 0.0, 0.0),
        ]
        return Dispatch(timepoint, market_dispatches)


def write_dispatches(dispatches: Iterable[Dispatch], path: str):
    with open(path, newline="", mode="w") as csvfile:
        fieldnames = [
            "period_start",
            "market1_price",
            "market1_discharge",
            "market2_price",
            "market2_discharge",
            "revenue",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dispatch in dispatches:
            writer.writerow(
                {
                    fieldnames[0]: dispatch.timepoint,
                    fieldnames[1]: dispatch.price("market1"),
                    fieldnames[2]: dispatch.discharge("market1"),
                    fieldnames[3]: dispatch.price("market2"),
                    fieldnames[4]: dispatch.discharge("market2"),
                    fieldnames[5]: dispatch.revenue,
                }
            )
