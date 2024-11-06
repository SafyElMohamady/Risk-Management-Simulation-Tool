


import pandas as pd
import numpy as np


# In[17]:


def monte_carlo_simulation(data_row, num_simulations):
    total_costs = []

    for _ in range(num_simulations):
        total_duration = 0
        for step, data in data_row.items():
            # Sample duration from the range
            duration = np.random.triangular(data["duration_min"], data["duration_mid"], data["duration_max"])
            
            # Calculate risk-adjusted duration
            for _, risk_data in data["risk"].items():
                if np.random.rand() < risk_data["probability"]:
                    duration *= (1 + risk_data["severity"])
            
            # Accumulate total duration
            total_duration += duration
        
        total_costs.append(total_duration)

    return total_costs


# In[7]:


# Read input data from Excel file
project_data_df = pd.read_excel("C:\\Users\\NEXT\\Downloads\\mydata.xlsx", sheet_name="Sheet1")


# In[18]:


# Convert DataFrame to list of dictionaries
project_data_list = []
for index, row in project_data_df.iterrows():
    step = row['Project Steps']
    duration_min = row['duration min.']
    duration_mid = row['duration mid.']
    duration_max = row['duration max.']
    risk = {
        'R1': {'probability': row['R1low scenario'], 'severity': row['R1mid scenario']},
        'R2': {'probability': row['R2Low senario'], 'severity': row['R2Mid scenario']},
        'R3': {'probability': row['R3Low scenario'], 'severity': row['R3Mid scenario']},
        'R4': {'probability': row['R4Low scenario'], 'severity': row['R4Mid Scenario']}
    }
    project_data_list.append({step: {'duration_min': duration_min, 'duration_mid': duration_mid, 'duration_max': duration_max,'risk': risk}})


# In[24]:


# Run Monte Carlo simulation for each row in the dataset
num_simulations = 10000
for i, data_row in enumerate(project_data_list):
    simulation_results = monte_carlo_simulation(data_row, num_simulations)
    project_data_df.loc[i, 'Total Risk Based Duration'] = np.percentile(simulation_results, 50)  # Using P50 as an example


# In[25]:


# Print DataFrame with the new column filled
print(project_data_df)

