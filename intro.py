import sys

userInput = sys.argv[1].lower()

if userInput == '/name':
    print('My name is Isabella Peters and I am a senior majoring in Computer Science.')
elif userInput == '/why':
    print('I enjoy puzzles and learning langauges, and computer science was just a logical application of that.')
elif userInput == '/what':
    print('I have worked as a Backend Engineer intern for the past 2 years and I plan to continue in that field.')
elif userInput == '/fact':
    print('I have hiked over 100 miles this year already!')
else:
    print('That is not a valid input, please try again.')