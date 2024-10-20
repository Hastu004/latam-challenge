from typing import List, Tuple
from datetime import datetime
import pandas as pd
import time
import os

def load_data(file_path: str) -> pd.DataFrame:
    columns = ['date', 'user']
    return pd.read_json(file_path, lines=True)[columns]

def preprocess_dates(df: pd.DataFrame) -> pd.DataFrame:
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df

def get_top_dates(df: pd.DataFrame, top_n: int = 10) -> List[datetime.date]:
    top_dates = df['date'].value_counts(ascending=False).index.to_list()
    return top_dates[:top_n] if len(top_dates) > top_n else top_dates

def extract_usernames(df: pd.DataFrame) -> pd.DataFrame:
    df['username'] = df['user'].apply(lambda x: x['username'])
    #df['username'] = df['user'].str['username']

    return df

def get_top_users_per_date(df: pd.DataFrame, top_dates: List[datetime.date]) -> List[str]:
    top_users = []
    for date in top_dates:
        # Obtener la lista de usuarios para la fecha específica y contar las veces que aparece
        top_user = df.loc[df['date'] == date, 'username'].value_counts(ascending=False).index.to_list()
        top_users.append(top_user[0] if top_user else None)
    return top_users

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    df = load_data(file_path)
    df = preprocess_dates(df)
    df = extract_usernames(df)
    
    top_dates = get_top_dates(df)
    top_users = get_top_users_per_date(df, top_dates)
    
    # Return a list of tuples containing dates and their corresponding top users
    return [(top_dates[i], top_users[i]) for i in range(len(top_dates))]



if __name__ == '__main__':
    initial_time = time.time()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'farmers-protest-tweets-2021-2-4.json')
    return_list = q1_time(file_path)
    
    print(return_list)
    print(f'EXECUTION TIME: {time.time() - initial_time}')