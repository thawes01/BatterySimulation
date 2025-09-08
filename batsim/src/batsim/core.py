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
                timepoint=Timepoint(), market_id=market1.id, power=0, timespan_mins=30
            ),
            market1.id: Dispatch(
                timepoint=Timepoint(), market_id=market1.id, power=0, timespan_mins=60
            ),
        }


def run_simulation():
    market1 = Market("market1", price_interval=30)
    market2 = Market("market2", price_interval=60)

    battery = Battery()

    operator = Operator()

    n_timesteps = 10
    # simulation_interval = 30  # mins
    timepoints = [Timepoint() for _ in range(n_timesteps)]
    dispatches = []
    for timepoint in timepoints:
        market_dispatches = operator.dispatch(timepoint, battery, market1, market2)
        battery.update(market_dispatches)
        dispatches.append(market_dispatches)

    return dispatches
