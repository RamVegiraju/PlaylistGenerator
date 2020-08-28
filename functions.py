#functions for model building and EDA
from sklearn.preprocessing import OrdinalEncoder

#Encoding the categorical variables
def encodeData(df):
    enc = OrdinalEncoder()
    encodedVariables = df[['Genre/Mood','Language']]
    enc.fit(encodedVariables[["Genre/Mood","Language"]])
    encodedVariables[["Genre/Mood","Language"]] = enc.transform(encodedVariables[["Genre/Mood","Language"]])
    df['encodedLanguage'] = encodedVariables['Language']
    df['encodedGenre'] = encodedVariables['Genre/Mood']
    return df

#Model Creation
def model(df):
    data = df[['encodedGenre','encodedLanguage']]
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=150, n_jobs=-1).fit(data)
    distances, indices = model_knn.kneighbors(data)
    return model_knn

def getPredictions(genre, language, favorite_artists, playlistSize):
    """
    Factors in genre, language, list of favorite artists, and the size of the playlist you want
    """
    results = model_knn.kneighbors([[genre, language]])
    results = results[1]
    resultList = results.tolist()
    resultList = resultList[0]
    playlist = df.loc[resultList]
    playlist = playlist[['name','artist','popularity','release_year']]
    playlist['ContainsArtist'] = playlist['artist'].apply(lambda x: any([k in x for k in favorite_artists])) #checks for favorite artist
    playlist = playlist.sort_values(["ContainsArtist","popularity"],ascending = (False, False))
    notPopular = playlist[playlist['popularity'] < 40].index
    playlist.drop(notPopular, inplace=True)
    return playlist.head(playlistSize)


#print("All is good right now")