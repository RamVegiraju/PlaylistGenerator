#functions for model building and EDA
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import pickle
import joblib

data = pd.read_csv('Data/SpotifyData.csv')

def processData(df):
    """Preprocesses and encodes the data
        #Genre:
        #sad: 5
        #romantic: 4
        #jazz: 3
        #Throwback: 2
        #Rap: 1
        #Hip-Hop: 0

        #Language:
        #Spanish: 2
        #Hindi: 1
        #English: 0
    """
    df = df.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1)
    enc = OrdinalEncoder()
    encodedVariables = df[['Genre/Mood','Language']]
    enc.fit(encodedVariables[["Genre/Mood","Language"]])
    encodedVariables[["Genre/Mood","Language"]] = enc.transform(encodedVariables[["Genre/Mood","Language"]])
    df['encodedLanguage'] = encodedVariables['Language']
    df['encodedGenre'] = encodedVariables['Genre/Mood']
    return df

df = processData(data)

def model(df):
    """Model creation"""
    data = df[['encodedGenre','encodedLanguage']]
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=150, n_jobs=-1).fit(data)
    distances, indices = model_knn.kneighbors(data)
    return model_knn

model_knn = model(df)

def serializeModel(model, name="recommenderModel"):
    """Making model accessible on the backend Flask app"""
    with open(name, 'wb') as f:
        pickle.dump(model, f)

serializeModel(model_knn)

def processGenre(genre):
    """Process Genre from front-end and encode for model to understand"""
    if genre == 'Hip-Hop':
        genre = 0
    elif genre == 'Rap':
        genre = 1
    elif genre == 'Throwback':
        genre = 2
    elif genre == 'Jazz':
        genre = 3
    elif genre == 'Romantic':
        genre = 4
    elif genre == 'Sad':
        genre = 5
    return genre

def processLanguage(language):
    """Process language from front-end and encode for model to understand"""
    if language == 'English':
        language = 0
    elif language == 'Hindi':
        language = 1
    elif language == 'Spanish':
        language = 2
    return language

def getPredictions(genre, language, favorite_artists, playlistSize):
    """Inference function"""
    genre = processGenre(genre)
    language = processLanguage(language)
    results = model_knn.kneighbors([[genre, language]])
    results = results[1]
    resultList = results.tolist()
    resultList = resultList[0]
    playlist = df.loc[resultList]
    playlist = playlist[['name','artist','popularity','release_year']]
    playlist['ContainsArtist'] = playlist['artist'].apply(lambda x: any([k in x for k in favorite_artists])) #searches for favorite artists
    playlist = playlist.sort_values(["ContainsArtist","popularity"],ascending = (False, False)) #sorts favorite artists by popularity of song
    notPopular = playlist[playlist['popularity'] < 40].index #drops songs with less than 40 popularity
    playlist.drop(notPopular, inplace=True)
    playlist = playlist.drop(['ContainsArtist','popularity','release_year'], axis=1)
    playlist.columns = ['Song','Artist']
    playlist = playlist.iloc[0:playlistSize]
    #playlist = playlist.head(playlistSize)
    #playlist = playlist.to_dict()
    return playlist

print(getPredictions("Rap","English",['Eminem','Meek Mill'],10))