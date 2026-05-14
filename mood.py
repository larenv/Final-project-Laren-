

if __name__ == '__main__':
    print('welcome to LaRen\'s mood tracking application!')

    # this is a list of all moods (happy / sad / frustrated)
    moods = [0, 0, 0]

    response = input('enter your mood today! (happy/sad/frustrated) ')
    if response.lower() == 'happy':
        print('we\'re happy today ... great!')
        moods[0] += 1
    if response.lower() == 'sad':
        print('oh we\'re sad today ... hope you feel better.')
        moods[1] += 1
    if response.lower() == 'frustrated':
        print('frustrated today ... it\'s ok to not be ok!')
        moods[2] += 1