weather = input("What's the weather like today? (sunny / rain / cold): ").lower()
energy = input("What's your energy level? (high /medium / low): ").lower()
time = input("How much free time do you have? (a lot / some / almost none): ").lower()

if weather == 'sunny':
    if energy == 'high':
        if time == 'a lot':
            print(' a day for a walk ')
        elif time == 'some':
            print('Go for a short walk ')
        else:
            print('Open a window')
    elif energy == 'medium':
        print('read the book  ')
    else:
        print('Take a break')
elif weather == 'cold':
    if energy == 'high':
        print('do something')
    elif energy == 'medium':
        print('Watch the movie')
    else:
        print('drink tea')

elif weather == 'cold':
    if energy == 'high' and time == 'almost none':
        print('stairs to the hall')
    elif energy == 'medium' and time == 'some':
        print('Watch the series')
    else:
        print('take a rest')


else:
    print('Take a break')