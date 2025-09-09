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


class MarketCommitment:
    def __init__(self, market_id: str, discharge_power: float, price: float):
        self.market_id = market_id
        self.discharge_power = discharge_power
        self.price = price


class Commitment:
    def __init__(
        self, timepoint: Timepoint, market_commitments: list[MarketCommitment]
    ):
        self._timepoint = timepoint
        self._market_commitments = {m.market_id: m for m in market_commitments}

    @property
    def timepoint(self) -> Timepoint:
        return self._timepoint

    def discharge(self, market_id: str) -> float:
        return self._market_commitments[market_id].discharge_power

    def price(self, market_id: str) -> float:
        return self._market_commitments[market_id].price

    @property
    def revenue(self) -> float:
        return 0.0


class Battery:
    def execute(self, commitment: Commitment):
        pass


class Operator:
    def determine_commitment(
        self, timepoint: Timepoint, battery: Battery, market1: Market, market2: Market
    ) -> Commitment:
        market_commitments = [
            MarketCommitment(market1.id, 0.0, 0.0),
            MarketCommitment(market2.id, 0.0, 0.0),
        ]
        return Commitment(timepoint, market_commitments)


def write_commitments(commitments: Iterable[Commitment], path: str):
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
        for commitment in commitments:
            writer.writerow(
                {
                    fieldnames[0]: commitment.timepoint,
                    fieldnames[1]: commitment.price("market1"),
                    fieldnames[2]: commitment.discharge("market1"),
                    fieldnames[3]: commitment.price("market2"),
                    fieldnames[4]: commitment.discharge("market2"),
                    fieldnames[5]: commitment.revenue,
                }
            )
