class Timepoint:
    def __init__(self):
        self._timestamp = "2025-01-01 06:30"

    def __str__(self):
        return self._timestamp


class Market:
    def __init__(self, id: str):
        self.id = id


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
    def __init__(self, capacity: float):
        self._capacity = capacity
        self._charge = capacity

    @property
    def capacity(self) -> float:
        return self._capacity

    @property
    def charge(self) -> float:
        return self._charge

    def execute(self, commitment: Commitment):
        pass


class Operator:
    def determine_commitment(
        self, timepoint: Timepoint, battery: Battery, markets: list[Market]
    ) -> Commitment:
        market_commitments = [
            MarketCommitment(market.id, battery.charge, 0.0) for market in markets
        ]
        return Commitment(timepoint, market_commitments)
