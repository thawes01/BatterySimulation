from batsim.core import Battery, Market, Operator, Timepoint
from batsim.io import write_commitments

# Set up battery and markets.
# In full solution, markets and battery would be initialised with data from the
# Excel files.
battery = Battery(capacity=12)
market1 = Market("market1")
market2 = Market("market2")
markets = [market1, market2]

# Initialise the battery operator
# Contains the logic for determining optimal market power commitments.
operator = Operator()

# Set up parameters for the simulation -- here using 10 (half-hourly)
# timesteps. The timepoints represent timestamps for the simulation.
n_timesteps = 10
timepoints = [Timepoint() for _ in range(n_timesteps)]

# Iterate through the timepoints and determine market commitments step-wise.
# The operator determines the commitment to each market for the current timepoint
# and then the battery's state is updated according to the committed charge/discharge.
commitments = []
for timepoint in timepoints:
    commitment = operator.determine_commitment(timepoint, battery, markets)
    battery.update(commitment)
    commitments.append(commitment)

# The commitments form the output of the simulation; write to file
write_commitments(commitments, "simulation.csv")
