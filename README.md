# BatterySimulation

Simulate battery dispatch within simplified electricity markets.

## Approach taken

My approach was to try and create a package that could be used to model
different market commitment strategies. Initially I sketched out an example
of how I would want to use the package in a script to run a simulation, to get
the main classes I thought I'd need. I felt like an object-oriented approach
was a natural way to do this, especially given there is state that needs to
evolve as the simulation runs (e.g. battery charge, whether there is an existing
commitment to the hourly market that needs to be respected). The logic for
determining an optimal battery charge/discharge commitment to the market(s)
is encapsulated in the `Operator` class (see the `determine_commitment` method).
I wanted to have a single place where this is encapsulated so that it would be
easy to try different strategies (I envisage that `Operator` would become an 
abstract base class in the long run, with different concrete derivative classes
for different market commitment strategies). I did a bit of TDD to
start fleshing out the logic for the main `determine_commitment` method of
`Operator`.

### Known limitations

* The solution is very incomplete and doesn't implement all the rules set by the
  task.
* There is know code included to read in the battery and market data from the
  Excel files. Although I have some rough code to read this in using Pandas
  (see first cell in `example/Exploration.ipynb` if you're interested),
  I didn't get to incorporating it with the package. My approach was to design
  the main package API first, then worry about how to get the data into it
  later.
* The csv file output by the `example/simulate.py` script just holds stub values.
* I am aware that there are awkward aspects to the market timeseries data that
  would need to be addressed: specifically, how to deal with clock changes and
  the fact that some data doesn't fall exactly on the hour / half-hour, but is
  a few nanoseconds out.
* There are no docstrings -- apologies. But I have tried to use descriptive
  names.

