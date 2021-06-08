import pandas as pd
import numpy as np
import json
import os

log_lines = open(os.path.join(os.environ['RESULTS_FOLDER'], 'details.log')).readlines()
class_map = json.load(open(os.path.join(os.environ['RESULTS_FOLDER'], 'class_maps.json')))
df = pd.DataFrame.from_records(list(map(json.loads, log_lines)))
df = df.drop('render_args', axis=1).join(pd.DataFrame(df.render_args.values.tolist()))
df['prediction'] = df['prediction'].apply(lambda x: class_map[x[0]])
df['is_correct'] = (df['is_correct'] == 'True')

res = df.groupby('MaterialControl.replacement_material').agg(acc=('is_correct', 'mean'),
      most_frequent_prediction=('prediction', lambda x: x.mode()))
print(res)
