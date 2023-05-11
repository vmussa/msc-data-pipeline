import requests
import time
import datetime as dt
import json
from tracer.config import cfg


def extract_comments(params: dict):
    """
    Yield each 1000 comments to a file.
    """

    n_comments = 0
    chunk = 0
    while params['before'] > params['after']:

        print(f"Fetching comments for chunk of number {chunk}")
        response = requests.get(cfg.pushshift_api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            new_comments = data['data']
            print(f'{new_comments=}')
            
            if not new_comments:
                break
            
            n_comments += len(new_comments)
            print(f'Fetched {len(new_comments)} comments, total: {n_comments}')

            last_comment_utc = new_comments[-1]['created_utc']
            params['before'] = last_comment_utc
            print(f'Last comment UTC: {last_comment_utc} ({dt.datetime.fromtimestamp(last_comment_utc)})')
        else:
            print(f'Request failed with status code {response.status_code}')
            print(f'{response.content=}')
            break
        
        with open(f'data/{cfg.subreddit_name}_comments_{chunk}.ndjson', 'w', encoding='utf-8') as f:
            for comment in new_comments:
                comment['body'] = comment['body'].replace(',', '&#44;').replace('\n', ' ').replace('\r', '')
                f.write(json.dumps(comment) + '\n')

        chunk += 1
        time.sleep(1) # avoid rate limiting issues

    print(f'Successfully saved {n_comments} comments to local disk.')
