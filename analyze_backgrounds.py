import pandas as pd
import numpy as np
import json

log_lines = open('results/details.log').readlines()
class_map = json.load(open('results/class_maps.json'))
df = pd.DataFrame.from_records(list(map(json.loads, log_lines)))
df['prediction'] = df['prediction'].apply(lambda x: class_map[x[0]])
df['is_correct'] = (df['is_correct'] == 'True')

res = df.groupby('environment').agg(accuracy=('is_correct', 'mean'),
        most_frequent_prediction=('prediction', lambda x: x.mode()))
print(res)

