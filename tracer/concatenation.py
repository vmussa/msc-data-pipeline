import os
import pandas as pd
import json

def read_ndjson(file_path):
    data = []
    with open(file_path) as f:
        for line in f:
            data.append(json.loads(line))
    return pd.DataFrame(data)


if __name__ == '__main__':
    dir_path = 'data/'
    df = pd.concat([read_ndjson(os.path.join(dir_path, filename)) for filename in os.listdir(dir_path) if filename.endswith('.ndjson')], ignore_index=True)
    df.to_csv('data/corpus.csv', index=False)
