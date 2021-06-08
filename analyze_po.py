import pandas as pd
import numpy as np
import json
from PIL import Image
import os

DIR = os.environ['RESULTS_FOLDER']
log_lines = open(os.path.join(DIR, 'details.log')).readlines()
df = pd.DataFrame.from_records(list(map(json.loads, log_lines)))

# From class index to class name (for readability)
class_map = json.load(open(os.path.join(DIR, 'class_maps.json')))
df['prediction'] = df['prediction'].apply(lambda x: class_map[x[0]])

# We'll be a little lenient here to get a more interesting heatmap
df['is_correct'] = df['prediction'].isin(['cup', 'coffee mug'])

uv_num_correct = np.zeros((256, 256))
uv_num_visible = np.zeros((256, 256))
for imid in df["id"].unique().tolist():
    is_correct = float(df.set_index('id').loc[imid]['is_correct'])
    vis_coords_im = Image.open(os.path.join(DIR, f'images/{imid}_uv.png'))
    vis_coords = np.array(vis_coords_im).reshape(-1, 3)
    # R and G channels encode texture coordinates (x, y), 
    # B channel is 255 for object and 0 for background
    # So we will filter by B then only look at R and G.
    vis_coords = vis_coords[vis_coords[:,2] > 0][:,:2]

    uv_num_visible[vis_coords[:,0], vis_coords[:,1]] += 1.
    uv_num_correct[vis_coords[:,0], vis_coords[:,1]] += is_correct

# Accuracy = # correct / # visible
uv_accuracy = uv_num_correct / (uv_num_visible + 1e-4)

# Saves a black-and-white heatmap
Image.fromarray((255 * uv_accuracy).astype('uint8'))
