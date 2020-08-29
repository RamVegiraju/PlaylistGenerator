def processGenre(genre):
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

print(processGenre("Sad"))