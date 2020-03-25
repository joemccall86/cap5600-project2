# Project 2 (Working Title)

## Overview

The distribution of scarce resources is a common problem. Specifically, test
kits for the recent COVID-19 pandemic are in very short supply. It is still
crucial to understand how many people are infected at which town. This project
abstracts the problem as a classical [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) AI problem. The goal
is to determine if an intelligent agent (utilizing an epsilon-greedy algorithm)
can outperform a naive approach when distributing test kits to hospitals as
infections grow.

For this simulation there will be a fixed number of "arms" (i.e., towns). The simulation is run in T episodes, each lasting a simulated day.

Each day the number of infected patients at a town increase at a fixed rate.

Each day a fixed number of test kits are manufactured and ready to distribute.

The mathematical formula for this will be adjusted for the sake of the
simulation, but should form an exponential increase to remain accurate. The
rate may also be extrapolated from real-world data if possible.

A stretch-goal could be to contribute an agent implementation that may improve
upon the epsilon-greedy approach.

## Requirements

This project is built with Python 3.8

## Task Environment (PEAS)

* Performance Measure - The reward function is 1 point for a negative test and 10 points for a positive test. The agent's reward is the sum of the test results from each hospital.
* Environment - The environment will be:
    - partially observable - we can only measure the infection rate of towns that tests are distributed to
    - stochastic - the next state of the environment is determined by the previous state, the current action, and a random element of increase in infections
    - episodic - each round of the simulation represents a day
    - sequential - the agent is aware of the previous "arm" reward, which feeds into exploration vs. exploitation trade-off
    - dynamic - each town may increase the number of infections regardless of the chosen "arm"
    - discrete - fixed number of test kits to distribute among a fixed number of towns in the sim
    - single-agent - we only simulate the distribution of test kits, which is controlled by our single agent
* Actuators - The agent interacts with the environment by distributing test kits
* Sensors - The results of the distributed test kits from the previous round are reported back to the agent.


