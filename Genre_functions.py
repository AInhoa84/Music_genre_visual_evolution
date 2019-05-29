#!/usr/bin/env python
# coding: utf-8


def assign_genre(df):
    """ Assigns the Main genre for each row in the dataframe"""
    df.reset_index(drop=True, inplace=True)
    for i in tqdm.tqdm(range(len(df))):
        if df['genre_counts'][i] == 2 and 'Electronic' in df['genres'][i]:
            df['Main_genre'][i] = 'Electronic'
        elif df['genre_counts'][i] == 2 and 'Punk' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Punk'
        elif df['genre_counts'][i] == 2 and 'Pop' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Pop'
        elif df['genre_counts'][i] == 2 and 'Rock' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Rock'
        elif df['genre_counts'][i] == 2 and 'Hip_Hop' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Hip Hop'
        elif df['genre_counts'][i] == 2 and 'Jazz' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Jazz'
        elif df['genre_counts'][i] == 2 and 'Folk' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Folk'
        elif df['genre_counts'][i] == 2 and 'Blues' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Blues'
        elif df['genre_counts'][i] == 2 and 'Latin' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Latin'
        elif df['genre_counts'][i] == 2 and 'Classical' in df['genres'][i] and pd.isnull(df['Main_genre'][i]):
            df['Main_genre'][i] = 'Classical'
        else:
            pass