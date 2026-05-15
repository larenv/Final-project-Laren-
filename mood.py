

if __name__ == '__main__':
    print('welcome to LaRen\'s mood tracking application!')

    # this is a list of all moods (happy / sad / frustrated)
    moods = [0, 0, 0]

    # moods[0] is happy
    # moods[1] is sad
    # moods[2] is frustrated

    # TODO use a loop to ask for each day of the week
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day in week:

        response = input(f'enter your mood on {day}! (happy/sad/frustrated) ')
        if response.lower() == 'happy':
            print(f'we were happy on {day} ... great!')
            moods[0] += 1
        if response.lower() == 'sad':
            print(f'oh you were sad on {day} ... hope you feel better.')
            moods[1] += 1
        if response.lower() == 'frustrated':
            print(f'you were frustrated on {day} ... it\'s ok to not be ok!')
            moods[2] += 1

    if moods[0] >= moods[1] and moods[0] >= moods[2]:
        print('you were mostly happy this week -- fantastic!')
    if moods[1] >= moods[0] and moods[1] >= moods[2]:
        print('you were mostly sad this week -- hope you feel better!')
    if moods[2] >= moods[0] and moods[2] >= moods[1]:
        print('you were mostly fustrated this week -- take a deep breath ...')
    
    