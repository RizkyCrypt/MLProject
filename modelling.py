import argparse
import pandas as pd
import mlflow
from sklearn.ensemble import RandomForestClassifier

parser = argparse.ArgumentParser()
parser.add_argument("--n_estimators", type=int, default=505)
parser.add_argument("--max_depth", type=int, default=35)
parser.add_argument("--dataset", type=str, default="train_pca.csv")
args = parser.parse_args()

file_path = args.dataset

data = pd.read_csv(file_path)
