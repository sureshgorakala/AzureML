from azureml.core import Run,Dataset
import pandas as pd
import argparse as arg

parser = arg.ArgumentParser()
parser.add_argument('--ds',type=str,dest='dataset_name')#receiving registered dataset name as parameter
parser.add_argument('--dsobj',type=str,dest='dataset_name2')#receiving registered dataset obj as parameter
args = parser.parse_args()
print('************************************')
print(args.dataset_name2)
print('************************************')
run = Run.get_context()
ws = run.experiment.workspace
dataset = Dataset.get_by_name(ws,name=args.dataset_name)#read data from 1st arg
dataset2 = Dataset.get_by_id(ws,id=args.dataset_name2) #read data from 2nd arg

print(dataset.take(3).to_pandas_dataframe())
print('******************************')
print(dataset2.take(3).to_pandas_dataframe())
