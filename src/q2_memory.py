from typing import List, Tuple
import json
from collections import Counter
import emoji
import pandas as pd
import os
import time

def q2_memory(file_path: str, chunksize: int = 1000) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    for chunk in pd.read_json(file_path, lines=True, chunksize=chunksize):
        for content in chunk['content']:
            emoji_counter.update(char for char in content if emoji.is_emoji(char))

    return emoji_counter.most_common(10)

if __name__ == '__main__':
    initial_time = time.time()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    
    return_list = q2_memory(file_path)
    
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time:.6f} seconds')
