from typing import List, Tuple
import json
from collections import Counter
import time
import os


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    count_users = Counter()
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            mentioned_users = json.loads(line)['mentionedUsers']
            if mentioned_users is None:
                continue
            # Al obtener los usernames se actualiza el contador
            usernames = [user['username'] for user in mentioned_users]
            count_users.update(usernames)
            
    return count_users.most_common(10)

if __name__ == '__main__':
    initial_time = time.time()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    return_list = q3_time(file_path)
    
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')