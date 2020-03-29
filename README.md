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

## Methods (classes)

### Variables

Simulation:

* Date range to simulate
* The counties being simulated
* Production count of test kits per-day
* Table of actual infection numbers. Look up based on county and day.
* Which agent implementation to use

Environment:

* Current date
* County list
* Distribution agent

County:

* Population count
* Number of test kits (N)
* The result of using those test kits (measured positive + measured negative)
* Method to test population

All agents:

* Table of counties and their test results
* Method to distribute test kits

Epsilon-Greedy Agent:

* Average "payout" for each county. This is based on the utility function where a positive test result is 10 points and a negative test result is 1 point.
* Epsilon value (e.g., 0.10)
* Assuming 1000 test kits for 5 counties, epsilon = 0.10:
    * (1 - epsilon) + (epsilon / k) * 100 = 920 test kits to the county with the highest score 
    * 20 test kits to the remaining 4 counties respectively
    * Note we may need to adjust the scoring algorithm and epsilon to find a useful combination. Keep them constant for the sake of simplicity in this experiment.
    
Test Evaluator:

* Actual data evaluator
* Random evaluator
* Simulated evaluator
    
### Simulation

Read in simulation config to have `start_date`, `end_date`, `counties`, `agent_type`, and `test_kit_production_capacity`.

* Each day:
  * Each county c:
    * get test results
    * print/export results, along with actual numbers
    * feed results to agent
  * Instruct the agent to distribute `test_kit_production_capacity` test kits to all `counties`
* At the end of the simulation, print the accumulated utility of the agent implementation

We will test the following strategies:

* naive - `test_kit_production_capacity` / `counties.length()` test kits to each county
* epsilon-greedy
 
### Test Method

Each county will call `perform_test` for each test kit they have. Since this is a simulation its success percentage will be:

    alpha * num_infected(day) / population
    
where `alpha` is a constant that represents the fact that someone who is asymptomatic will not be tested (suggested: start with 2, indicating that we rule 50% of the population out appear to have not been exposed).

The test will return `True` or `False` based on whether or not a random number between 1 and 100 are within the test success percentage.

## Requirements

This project is built with Python 3.8

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

- [ ] Create classes to run the environment
- [ ] Read initial information from a config file (YAML?)
- [ ] Implement reading infection data using PANDAS and the NYT test data
- [ ] Discover useful data set from NYT test data
- [X] Implement even distribution of test kits strategy
- [ ] Implement epsilon-greedy strategy
- [ ] Run the experiment with both strategies, adjusting the data as needed
- [ ] Plot the data in a bar chart for each county
- [ ] Summarize experiment in report
- [X] Build tools to package project
- [ ] Document running the project
- [ ] Earn another A

# Resources

* https://en.wikipedia.org/wiki/Multi-armed_bandit
* https://jamesmccaffrey.wordpress.com/2017/11/30/the-epsilon-greedy-algorithm/
* https://www.nytimes.com/article/coronavirus-county-data-us.html
