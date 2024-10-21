from typing import List, Tuple
from collections import Counter
import json
import time
import os

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path, 'r') as f:
        data = [json.loads(line)['mentionedUsers'] for line in f.readlines()]
    usernames = [user['username'] for item in data if item is not None for user in item]

    return Counter(usernames).most_common(10)

if __name__ == '__main__':
    initial_time = time.time()
    current_dir = os.path.dirname(os.path.abspath('')) 
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    return_list = q3_memory(file_path)
    
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')
