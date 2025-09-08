class Timepoint:
    pass


class Market:
    def __init__(self, id: str, price_interval: int):
        self.id = id
        self.price_interval = price_interval


class Dispatch:
    def __init__(
        self, timepoint: Timepoint, market_id: str, power: float, timespan_mins: int
    ):
        self.timepoint = timepoint
        self.market_id = market_id
        self.power = power
        self.timespan_mins = timespan_mins


class Battery:
    def update(self, dispatches: dict[str, Dispatch]):
        pass


class Operator:
    def dispatch(
        self, timepoint: Timepoint, battery: Battery, market1: Market, market2: Market
    ) -> dict[str, Dispatch]:
        return {
            market1.id: Dispatch(
                timepoint=timepoint, market_id=market1.id, power=0, timespan_mins=30
            ),
            market2.id: Dispatch(
                timepoint=timepoint, market_id=market2.id, power=0, timespan_mins=60
            ),
        }
