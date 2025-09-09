# BatterySimulation

Simulate battery dispatch within simplified electricity markets.

## Contents

- [Installing and running an example simulation](#installing-and-running-an-example-simulation)
- [Approach taken](#approach-taken)
  - [Known limitations](#known-limitations)

## Installing and running an example simulation

The code in this repo requires Python 3.13. After cloning this repo, change
into the `example` directory within your local clone and then follow the
instructions for one of the options below:

### Option 1: using `uv`

Simply sync to create a new virtual environmet and then run the `simulate.py`
script within via `uv run`:

```
uv sync
uv run python simulate.py
```

This will create an output file, `simulation.csv`, in the same folder.

### Option 2: using `venv` and `pip`

First create a new virtual environment with your Python 3.13, then 
`pip install` the requirements from the `requirements.txt` file into the
virtual environment. Finally, run the `simulate.py` script, which will
create an output file, `simulation.csv`, in the same folder.

Commands for your OS are below:

#### Unix

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python simulate.csv
```

#### Windows
  
```
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py simulate.csv
```


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
* The market commitments logic is only a stub implementation and does not
  define a valid market commitment (let alone an optimal one).
* The csv file output by the `example/simulate.py` script just holds stub values.
* I am aware that there are awkward aspects to the market timeseries data that
  would need to be addressed: specifically, how to deal with clock changes and
  the fact that some data doesn't fall exactly on the hour / half-hour, but is
  a few nanoseconds out.
* There are no docstrings -- apologies. But I have tried to use descriptive
  names.

