from typing import List, Tuple
from datetime import datetime
import json
import time
import os

def load_tweets(file_path: str) -> dict:
    """Carga los tweets desde el archivo y cuenta los tweets por fecha y usuario."""
    dates_dict = {}

    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tweet_date = tweet['date'].split('T')[0]
            username = tweet['user']['username']

            # Inicializar el diccionario para la fecha si no existe
            if tweet_date not in dates_dict:
                dates_dict[tweet_date] = {}
            
            # Contar el tweet por usuario
            dates_dict[tweet_date][username] = dates_dict[tweet_date].get(username, 0) + 1

    return dates_dict

def get_top_dates(dates_dict: dict) -> List[str]:
    """Obtiene las 10 fechas con el mayor número de tweets."""
    return sorted(dates_dict.keys(), key=lambda date: sum(dates_dict[date].values()), reverse=True)[:10]

def get_top_users(dates_dict: dict, top_dates: List[str]) -> List[str]:
    """Obtiene el usuario con la mayor cantidad de tweets para cada fecha."""
    return [max(dates_dict[date], key=dates_dict[date].get) for date in top_dates]

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """Función principal para analizar los tweets y devolver las fechas y usuarios top."""
    dates_dict = load_tweets(file_path)
    top_dates = get_top_dates(dates_dict)
    top_users = get_top_users(dates_dict, top_dates)

    # Convertir las fechas a formato datetime.date
    top_dates = [datetime.strptime(date_str, "%Y-%m-%d").date() for date_str in top_dates]

    return list(zip(top_dates, top_users))


if __name__ == '__main__':
    initial_time = time.time()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    return_list = q1_memory(file_path)
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')
