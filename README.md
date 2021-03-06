# Project 2 (Working Title)

## Overview

The distribution of scarce resources is a common problem. Specifically, test
kits for the recent COVID-19 pandemic are in very short supply. It is still
crucial to understand how many people are infected at which county. This project
abstracts the problem as a classical [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) AI problem. The goal
is to determine if an intelligent agent (utilizing an epsilon-greedy algorithm)
can outperform a naive approach when distributing test kits to counties as
infections grow.

For this simulation there will be a fixed number of "arms" (i.e., counties). The simulation is run in T episodes, each lasting a simulated day.

Each day the number of infected patients at a county increase at a fixed rate.

Each day a fixed number of test kits are manufactured and ready to distribute.

The mathematical formula for this will be adjusted for the sake of the
simulation, but should form an exponential increase to remain accurate. The
rate may also be extrapolated from real-world data if possible.

A stretch-goal could be to contribute an agent implementation that may improve
upon the epsilon-greedy approach.

## Running the Project

Configuration is done inside `simulation.py`. Specify the counties you want to simulate, along with their populations, as the `counties` variable.
Adjust `start_date` and `end_date` as desired.

option | type | description
--- | --- | ---
`counties` | `List[County]`, | The list of counties to simulate. Each county must have its population specified in its constructor
`start_date` | `datetime` | The date from which to start the simulation (e.g., `datetime(2020, 1, 1)`)
`end_date` | `datetime` | The date at which to end the simulation (e.g., `datetime(2020, 3, 23)`)
`num_test_kits_per_day` | `int` | The number of test kits available for distribution per-day
`agent` | `Agent` | The type of agent to use in the simulation. Use `NaiveAgent` or `EpsilonGreedyAgent`.
`test_kit_evaluator` | `TestKitEvaluator` | The implementation of the class used to evaluate the test kits. Use `RandomTestKitEvaluator` or `PandasTestKitEvaluator`
 
Requirements are expressed using standard python `setuptools`. To install the dependencies run:

```bash
python3 setup.py install --user
```

To run the simulation, run:

```bash
python3 simulation.py
```

Daily reported infections will be printed to STDOUT. At the end of the simulation a graph will be generated with the current timestamp in a PNG form.
The agents are evaluated based on minimizing the difference between the sum of the positive results measured for every county and the sum of the total actual results from every county.

## Requirements

This project is built with Python 3.8 but has been tested with Python 3.6.

## Task Environment (PEAS)

* Performance Measure - The reward function is 1 point for a negative test and 10 points for a positive test. The agent's reward is the sum of the test results from each hospital.
* Environment - The environment will be:
    - partially observable - we can only measure the infection rate of counties that tests are distributed to
    - stochastic - the next state of the environment is determined by the previous state, the current action, and a random element of increase in infections
    - episodic - each round of the simulation represents a day
    - sequential - the agent is aware of the previous "arm" reward, which feeds into exploration vs. exploitation trade-off
    - dynamic - each county may increase the number of infections regardless of the chosen "arm"
    - discrete - fixed number of test kits to distribute among a fixed number of counties in the sim
    - single-agent - we only simulate the distribution of test kits, which is controlled by our single agent
* Actuators - The agent interacts with the environment by distributing test kits
* Sensors - The results of the distributed test kits from the previous round are reported back to the agent.

## Data

Data is pulled from https://www.nytimes.com/article/coronavirus-county-data-us.html, which includes county-by-county historical infection data.

## Tasks (no order)

- [X] Create classes to run the environment
- ~[X] Read initial information from a config file (YAML?)~ configuration done in `simulation.py`
- [X] Implement reading infection data using PANDAS and the NYT test data
- [X] Discover useful data set from NYT test data (South Florida)
- [X] Implement even distribution of test kits strategy
- [X] Implement epsilon-greedy strategy
- [X] Run the experiment with both strategies, adjusting the data as needed
- [X] Plot the data in a line chart for each county
- [X] Summarize experiment in report
- [X] Build tools to package project
- [X] Document running the project
- [ ] Earn another A

# Resources

* https://en.wikipedia.org/wiki/Multi-armed_bandit
* https://jamesmccaffrey.wordpress.com/2017/11/30/the-epsilon-greedy-algorithm/
* https://www.nytimes.com/article/coronavirus-county-data-us.html
