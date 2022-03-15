# Import libraries
import os
import argparse
import pandas as pd
from azureml.core import Run,Dataset,Workspace
from sklearn.preprocessing import MinMaxScaler

# Get parameters
parser = argparse.ArgumentParser()
parser.add_argument("--input-data", type=str, dest='raw_dataset_id', help='raw dataset')
parser.add_argument('--prepped-data', type=str, dest='prepped_data', default='prepped_data', help='Folder for results')
args = parser.parse_args()

save_folder = args.prepped_data

# Get the experiment run context
run = Run.get_context()
ws = run.experiment.workspace

# load the data (passed as an input dataset)

print("Loading Data...")


diabetes =Dataset.get_by_id(ws, id=args.raw_dataset_id).to_pandas_dataframe()

print("Loading Data complete...")
print('**********')
# Log raw row count
row_count = (len(diabetes))
run.log('raw_rows', row_count)
print('**********')
# remove nulls
diabetes = diabetes.dropna()

# Normalize the numeric columns
#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
scaler = MinMaxScaler()
num_cols = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
diabetes[num_cols] = scaler.fit_transform(diabetes[num_cols])

# Log processed rows
row_count = (len(diabetes))
run.log('processed_rows', row_count)

# Save the prepped data
print("Saving Data...")
os.makedirs(save_folder, exist_ok=True)
save_path = os.path.join(save_folder,'data.csv')
diabetes.to_csv(save_path, index=False, header=True)

# End the run
run.complete()