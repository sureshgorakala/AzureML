from azureml.core import Run,Dataset
import pandas as pd
import argparse as arg

parser = arg.ArgumentParser()
parser.add_argument('--ds',type=str,dest='dataset_name')
args = parser.parse_args()


run = Run.get_context()
ws = run.experiment.workspace
dataset = Dataset.get_by_name(ws,name=args.dataset_name)

print(dataset.take(3).to_pandas_dataframe())
