# Risk-Management-Simulation-Tool
This project uses a Monte Carlo simulation to model project step durations, factoring in risk scenarios to generate probabilistic estimates for project completion times.

## Data Import and Preparation:
The code reads project data from an Excel sheet containing duration and risk data for each project step.
The data is structured into a list of dictionaries, where each entry represents a project step with its minimum, mid, and maximum estimated durations and associated risks.

## Monte Carlo Simulation Function:
The monte_carlo_simulation function takes a single row of data and the number of simulations to run.

## For each simulation:
It samples a duration for each step using a triangular distribution based on the minimum, mid, and maximum durations.
For each risk scenario, if a random number falls within the risk’s probability, it adjusts the duration by the risk’s severity.
The function accumulates these durations for each simulation, storing the total duration in total_costs.

## Running the Simulation:
The script performs the Monte Carlo simulation for each project step, running a specified number of simulations (10,000 in this example).
It calculates the 10th, 50th, and 90th percentiles (P10, P50, and P90) from the simulation results, providing estimates for low, median, and high completion times for each step.

## Output:
The resulting percentiles are added to the original DataFrame, which is printed to display each step’s estimated durations at different confidence levels.
This project allows for risk-adjusted duration estimates, aiding project managers in understanding possible timelines under various risk scenarios.
