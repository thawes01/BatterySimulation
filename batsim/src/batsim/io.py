import csv
from typing import Iterable

from batsim.core import Commitment


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
