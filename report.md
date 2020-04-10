% Multi-Armed Test Distribution
% Joe McCall; Chris Zahuranec
% 03-23-2020

---
fontfamily: mathptmx 
geometry:
- margin=1in
header-includes:
  - \usepackage{mathtools}
abstract: |
    When an infectious disease such as COVID-19 infects an area, a common problem is a shortage of test kits. The resulting lack of adequate information on the spread of the disease makes
    it difficult to mitigate. Furthermore it is reasonable to conclude that the novel nature of such diseases imply a limited supply of testing capability at first. This experiment runs on
    data pulled from a public data source on actual infection rates, and explores whether or not the classical artificial intelligence problem of the multi-armed bandit yields useful 
    test distrubiton strategies. Specifically, the epsilon-greedy algorithm is tested against a uniform-distribution model to determine if, given a more limited test supply, it out-performs
    the naive approach.
bibliography: 
   - nyt_dataset.bib
csl: ieee.csl
header-includes:
  - \usepackage{mathtools}
...

<!--
The report is a PDF-converted document that must contain the following information:

* A description of the data structures used in the code.
* Data source
* Methods - Epsilon-Greedy
* Methods - Scoring

The descriptions should be concise. The report itself should be no longer than 2-3 pages.
--> 

# Introduction

During the COVID-19 pandemic, test kits were distributed among counties to help assess the spread of the disease, and determine whether or not treatment was necessary. Ideally there are 
adequate tests for every person in a geographical area, but given the novel nature of the disease the test kits were in short supply.

While test kits are manufactured every day, the distributor of those test kits is left with a dilemma: should one distribute more to areas that appear to be experiencing more infections? If so, how much of the limited test kits should be allocated to highly-infectuous areas and how much should be allocated to areas with low levels of infection?

By treating the number of positive cases as the "score," one could model this problem as a classical multi-armed bandit problem, which illustrates the dilemma between exploration and exploitation. Specifically, the exploration of areas with low infection rates should be reconciled with the exploitation of areas with high infection rates. Given the multi-armed bandit problem is established, one can apply several known solutions to this problem and evaluate its performance against real publicly-provided infection data [@NYTData]. Since the data is given by counties, the simulation will be run with counties.

The goal is to use an artificial intelligent agent to smartly distribute limited test kits where they are needed most. Such an agent would help mitigate the test kit shortage until enough test kits can be distributed for everyone.

# Methods

* Simulation run for T days.
* Each day N test kits are distributed among M counties
* Test kits evaluated based on percent of population infected for that day
* Score for each "arm" (county) computed based on number of positive results
* Results are fed into the agent to help determine the distribution of test kits
* The agent distributes the test kit

## Naive Agent

The test kits for day $i$ ($N_i$) is described in @fig:naiveAgent. It is simply the distribution of test cases evenly among the number of counties being simulated.

$$
N_i = \frac{N}{M}
$${#fig:naiveAgent}

## Epsilon-Greedy Agent

The epilon-greedy agent is described by a constant defined as $\epsilon$, which is used in the computation of test kits distributed to the highest counties per-day. This is illustrated in @fig:epsilonGreedyAgent. If the number of detected cases in the county the previous day (given by $f(N_i)$) is the greatest number (given by $max(f)$), then the number of cases is $(1 - \epsilon) \times M$. These are considered the "exploitation" test kits. The remaining "exploration" test kits are distributed evenly among the remaining counties.

$$
N_i =
\begin{dcases}
(1 - \epsilon) \times M, f(N_i) = max(f) \\
\frac{(\epsilon \times M)}{N - 1}, f(N_i) \ne max(f) 
\end{dcases}
$${#fig:epsilonGreedyAgent}

# Experiment

# Results

# Conclusion

# References
