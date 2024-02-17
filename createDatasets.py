import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
import time

#Spotify Web API
client_id = ''
client_secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Take playlist and create dataframe
def getTrackIDs(playlist_id):
    """Return track ids from playlist"""
    ids = []
    results = sp.playlist(playlist_id= playlist_id)
    for item in results['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

#Accessing public playlists

print("Getting Track IDs")
##########
#Rap
##########
rapIDs = getTrackIDs("spotify:playlist:4wNaifk1uOfpnKQrIpkHl9")
rapIDs2 = getTrackIDs("spotify:playlist:2e0d7otcM1oyecfi3zZPWk")

##########
#Spanish
##########
SpanIds = getTrackIDs("spotify:playlist:32zAUaYOXlXaTnRCF6YZro")
Span2Ids = getTrackIDs("spotify:playlist:2tbpZ1Cj6K7SoUgh8KgeWg")

##########
#Hindi
##########
HindiIds = getTrackIDs("spotify:playlist:6dPIDyUPTzA2dGmbo5I32l")
Hindi2Ids = getTrackIDs("spotify:playlist:7txATsRO9GWnExLEBLQfCh")

##########
#Hip-Hop
##########
HipHopIds = getTrackIDs("spotify:playlist:0OtdLZ5JVyqB4Zp8aylECe")
HipHopIds2 = getTrackIDs("spotify:playlist:003RTZc7voFjhdAwzZ5SC9")
HipHopIds3 = getTrackIDs("spotify:playlist:6Myw1PqQ874lA3ZUd6snjE")

##########
#Jazz
##########
JazzIds = getTrackIDs("spotify:playlist:05Hd48jdQIz3s8WRrvGnzf")

##########
#Workout
##########
WorkoutIds = getTrackIDs("spotify:album:4weGX8IhVS58obcLfTKE9Z")
WorkoutIds2 = getTrackIDs("spotify:album:47lKL6TX4rmyHEzHqbG7Tg")
WorkoutIds3 = getTrackIDs("spotify:playlist:2fHWrFrakadfGmnI5smgSL")

##########
#Sad/Slow
##########
SadIds = getTrackIDs("spotify:playlist:0N2pTjZX98Piir6i1VUTzZ")
SadIds2 = getTrackIDs("spotify:playlist:0RVjFnEY7zzHWtQzOG4wKB")
SadIds3 = getTrackIDs("spotify:playlist:0964aStNDTMmCPbaWwoHDc")

##########
#Romantic
##########
RomanticIds = getTrackIDs("spotify:playlist:5G9DUTgJYuQGNUDnKSrRw4")
RomanticIds2 = getTrackIDs("spotify:playlist:1oSlx4XxBp12uknXcuhaDg") #Hindi

def getTrackFeatures(id):
    """Extracting Spotify audio features from track"""
    meta = sp.track(id)
    features = sp.audio_features(id)

    #meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    #features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    #returning tracks
    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

def createSongList(ids):
    """Create List of Songs with Audio Features for pandas dataframe"""
    tracks = []
    for i in range(len(ids)):
        time.sleep(.5)
        track = getTrackFeatures(ids[i])
        tracks.append(track)
    return tracks

#Creating list of tracks

print("Creating list of tracks")
############
#Rap
############
tracksRap1 = createSongList(rapIDs)
tracksRap2 = createSongList(rapIDs2)

############
#Spanish
############
tracksSpan1 = createSongList(SpanIds)
tracksSpan2 = createSongList(Span2Ids)

##########
#Hindi
##########
tracksHindi1 = createSongList(HindiIds)
tracksHindi2 = createSongList(Hindi2Ids)

##########
#Hip-Hop
##########
tracksHipHop1 = createSongList(HipHopIds)
tracksHipHop2 = createSongList(HipHopIds2)
tracksHipHop3 = createSongList(HipHopIds3)

##########
#Jazz
##########
tracksJazz = createSongList(JazzIds)

##########
#Workout
##########
tracksWorkout1 = createSongList(WorkoutIds)
tracksWorkout2 = createSongList(WorkoutIds2)
tracksWorkout3 = createSongList(WorkoutIds3)

##########
#Sad/Slow
##########
tracksSad1 = createSongList(SadIds)
tracksSad2 = createSongList(SadIds2)
tracksSad3 = createSongList(SadIds3)

##########
#Romantic
##########
tracksRomantic1 = createSongList(RomanticIds)
tracksRomantic2 = createSongList(RomanticIds2)


#Creating dataframes of different playlists

print("Creating dataframes of data")
############
#Rap
############
rapDF1 = pd.DataFrame(tracksRap1, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
rapDF2 = pd.DataFrame(tracksRap2, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])

############
#Spanish
############
spanDF1 = pd.DataFrame(tracksSpan1, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
spanDF2 = pd.DataFrame(tracksSpan2, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])

##########
#Hindi
##########
hindiDF1 = pd.DataFrame(tracksHindi1, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
hindiDF2 = pd.DataFrame(tracksHindi2, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])

##########
#Hip-Hop
##########
hiphopDF1 = pd.DataFrame(tracksHipHop1, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
hiphopDF2 = pd.DataFrame(tracksHipHop2, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
hiphopDF3 = pd.DataFrame(tracksHipHop3, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])

##########
#Jazz
##########
jazzDF = pd.DataFrame(tracksJazz, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])

##########
#Workout
##########
workoutDF1 = pd.DataFrame(tracksWorkout1, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
workoutDF2 = pd.DataFrame(tracksWorkout2, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
workoutDF3 = pd.DataFrame(tracksWorkout3, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])

##########
#Sad/Slow
##########
sadDF1 = pd.DataFrame(tracksSad1, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
sadDF2 = pd.DataFrame(tracksSad2, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
sadDF3 = pd.DataFrame(tracksSad3, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])

##########
#Romantic
##########
romanticDF1 = pd.DataFrame(tracksRomantic1, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
romanticDF2 = pd.DataFrame(tracksRomantic2, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])


print("Adding genres")

def addGenre(df, genre):
    """Creating a separate column for genre/mood"""
    df["Genre/Mood"] = genre
    return df

#Adding genre column

############
#Rap
############
rapDF1 = addGenre(rapDF1, "Rap")
rapDF2 = addGenre(rapDF2, "Rap")

############
#Spanish
############
spanDF1 = addGenre(spanDF1, "Hip-Hop")
spanDF2 = addGenre(spanDF2, "Hip-Hop")

##########
#Hindi
##########
hindiDF1 = addGenre(hindiDF1, "Hip-Hop")
hindiDF2 = addGenre(hindiDF2, "Throwback")

##########
#Hip-Hop
##########
hiphopDF1 = addGenre(hiphopDF1, "Hip-Hop")
hiphopDF2 = addGenre(hiphopDF2, "Hip-Hop")
hiphopDF3 = addGenre(hiphopDF3, "Hip-Hop")

##########
#Jazz
##########
jazzDF = addGenre(jazzDF, "jazz")

##########
#Workout
##########
workoutDF1 = addGenre(workoutDF1, "workout")
workoutDF2 = addGenre(workoutDF2, "workout")
workoutDF3 = addGenre(workoutDF3, "workout")

##########
#Sad/Slow
##########
sadDF1 = addGenre(sadDF1, "sad")
sadDF2 = addGenre(sadDF2, "sad")
sadDF3 = addGenre(sadDF3, "sad")

##########
#Romantic
##########
romanticDF1 = addGenre(romanticDF1, "romantic")
romanticDF2 = addGenre(romanticDF2, "romantic")


print("Adding language")

def addLanguage(df, language):
    """Creating a separate column for language"""
    df["Language"] = language
    return df

#Adding language column

############
#Rap
############
rapDF1 = addLanguage(rapDF1, "English")
rapDF2 = addLanguage(rapDF2, "English")

############
#Spanish
############
spanDF1 = addLanguage(spanDF1, "Spanish")
spanDF2 = addLanguage(spanDF2, "Spanish")

##########
#Hindi
##########
hindiDF1 = addLanguage(hindiDF1, "Hindi")
hindiDF2 = addLanguage(hindiDF2, "Hindi")

##########
#Hip-Hop
##########
hiphopDF1 = addLanguage(hiphopDF1, "English")
hiphopDF2 = addLanguage(hiphopDF2, "English")
hiphopDF3 = addLanguage(hiphopDF3, "English")

##########
#Jazz
##########
jazzDF = addLanguage(jazzDF, "English")

##########
#Workout
##########
workoutDF1 = addLanguage(workoutDF1, "English")
workoutDF2 = addLanguage(workoutDF2, "English")
workoutDF3 = addLanguage(workoutDF3, "English")

##########
#Sad/Slow
##########
sadDF1 = addLanguage(sadDF1, "English")
sadDF2 = addLanguage(sadDF2, "English")
sadDF3 = addLanguage(sadDF3, "English")

##########
#Romantic
##########
romanticDF1 = addLanguage(romanticDF1, "English")
romanticDF2 = addLanguage(romanticDF2, "Hindi")

print("Adding year")

def addYear(df):
    """Creating a year column for release year"""
    df['release_date'] = pd.to_datetime(df['release_date']) #converting to datetime column
    df['release_year'] = df['release_date'].dt.year #creating release year column
    return df

#Adding year released column

############
#Rap
############
rapDF1 = addYear(rapDF1)
rapDF2 = addYear(rapDF2)

############
#Spanish
############
spanDF1 = addYear(spanDF1)
spanDF2 = addYear(spanDF2)

##########
#Hindi
##########
hindiDF1 = addYear(hindiDF1)
hindiDF2 = addYear(hindiDF2)

##########
#Hip-Hop
##########
hiphopDF1 = addYear(hiphopDF1)
hiphopDF2 = addYear(hiphopDF2)
hiphopDF3 = addYear(hiphopDF3)

##########
#Jazz
##########
jazzDF = addYear(jazzDF)

##########
#Workout
##########
workoutDF1 = addYear(workoutDF1)
workoutDF2 = addYear(workoutDF2)
workoutDF3 = addYear(workoutDF3)

##########
#Sad/Slow
##########
sadDF1 = addYear(sadDF1)
sadDF2 = addYear(sadDF2)
sadDF3 = addYear(sadDF3)

##########
#Romantic
##########
romanticDF1 = addYear(romanticDF1)
romanticDF2 = addYear(romanticDF2)

print("Concatenating dfs together")

#Concatenating dataframes together
rapDF = pd.concat([rapDF1,rapDF2])
spanDF = pd.concat([spanDF1,spanDF2])
hindiDF = pd.concat([hindiDF1,hindiDF2])
hiphopDF = pd.concat([hiphopDF1,hiphopDF2,hiphopDF3])
#jazzDF
workoutDF = pd.concat([workoutDF1,workoutDF2,workoutDF3])
sadDF = pd.concat([sadDF1, sadDF2, sadDF3])
romanticDF = pd.concat([romanticDF1, romanticDF2])
spotifyDataDF = pd.concat([rapDF, spanDF, hindiDF, hiphopDF, jazzDF, workoutDF, sadDF, romanticDF])

print("Creating data file")
#Creating csv files for data
spotifyDataDF.to_csv("spotify.csv", sep=',')

############
#Rap
############
#rapDF.to_csv("rap.csv", sep = ',')
#spanDF.to_csv("span.csv", sep = ',')
#hindiDF.to_csv("hindi.csv", sep =',')
