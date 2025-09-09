from batsim.core import Battery, Market, Operator, Timepoint


class TestOperator:
    def test_discharges_full_capacity_if_full_charge_and_no_commitment_single_market(
        self,
    ):
        """Given a battery and a single market, if the operator has no prior commitments
        and the battery has full charge, then when the operator determines its next
        commitment this is to discharge its whole charge to the market.
        """
        battery = Battery(capacity=12)
        market = Market("1")
        operator = Operator()

        commitment = operator.determine_commitment(Timepoint(), battery, [market])

        assert commitment.discharge(market.id) == battery.capacity

    def test_discharges_current_capacity_if_no_commitment_single_market(self, mocker):
        """Given a battery and a single market, if the operator has no prior commitments
        and the battery has positive charge, then when the operator determines its next
        commitment this is to discharge its remaining charge to the market.
        """
        battery = Battery(capacity=12)
        market = Market("1")
        operator = Operator()
        mocker.patch("batsim.core.Battery.charge").return_value = 6

        commitment = operator.determine_commitment(Timepoint(), battery, [market])

        assert commitment.discharge(market.id) == battery.charge
