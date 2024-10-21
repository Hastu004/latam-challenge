from typing import List, Tuple
import json
from emoji import emoji_list
from collections import Counter
import os
import time
import emoji

from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    with open(file_path, 'r') as f:
        for tweet in f:
            content = json.loads(tweet)['content']
            emoji_counter.update(char for char in content if emoji.is_emoji(char))

    return emoji_counter.most_common(10)




if __name__ == '__main__':
    initial_time = time.time()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    
    return_list = q2_time(file_path)
    
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')
