# Runs a linear regression on the hospital charge dataset

import linear_regression as lr

path_to_data = './hospital_charge_sample.csv'

df = lr.load_hospital_data(path_to_data)
data = lr.prepare_data(df)
results = lr.run_hospital_regression(path_to_data)
print(results)

### END ###