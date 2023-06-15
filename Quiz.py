print('\n---Welcome to Quiz---\n')
print('This game is categorized into 5 rounds:\n1 --> Science\n2 --> Maths\n3 --> General Knowledge\n4 --> Sports\n5 --> History\n')
print('Each round consists of 5 questions and each question has weightage of 2 points each.')
rounds = ['science', 'maths', 'general knowledge', 'sports', 'history']
name = ['Science', 'Maths', 'General Knowledge', 'Sports', 'History']

rounds[0] = [
    ['Which of the following is used in pencils?', 'Graphite', 'Silicon', 'Charcoal', 'Phosphorous', 1],
    ['Chemical Formula of water is?', 'NaAlO2', 'H20', 'Al203', 'CaSiO3', 2],
    ['Which of the gas is not known as green house gas?', 'Methane', 'Nitrous Oxide', 'Carbon dioxide', 'Hydrogen', 4],
    ['Bromine is a?', 'Black Solid', 'Red liquid', 'Colorless gas', 'Highly inflammable gas', 2],
    ['The hardest substance on earth is?', 'Gold', 'Iron', 'Diamond', 'Platinum', 3]
]

rounds[1] = [
    ['50 times of 8 equal to?', '80', '400', '8000', '4000', 2],
    ['Factorial of 0 is?', '0', 'Undefined', '1', '-1', 3],
    ['All natural numbers and 0 are called the _____ numbers.', 'whole', 'prime', 'integer', 'rational', 1],
    ['How many seconds are there in one day?', '60 seconds', '86400 seconds', '100000 seconds', '360 seconds', 2],
    ['What is the value of pi?', '3.14', '22', '7', '11', 1]
]

rounds[2] = [
    ['Which is the smallest ocean in the World?', 'Indian', 'Pacific', 'Atlantic', 'Arctic', 4],
    ['Which country gifted the \'Statue of Liberty\' to USA in 1886?', 'France', 'Canada', 'Brazil', 'England', 1],
    ['Which is largest unit of storage among the following?', 'Terabyte', 'Byte', 'Gigabyte', 'Megabyte', 1],
    ['World Environmental Day is celebrated on ____.', 'August 5', 'June 5', 'July 5', 'November 5', 2],
    ['The burning of fossil fuels produces?', 'Soil pollution', 'Water pollution', 'Air pollution', 'All of the above', 4]
]

rounds[3] = [
    ['After how many years FIFA World Cup is held?', '2 Years', '4 Years', '3 Years', 'Every Year', 2],
    ['Which Country won the first World Cup?', 'Argentina', 'Brazil', 'Italy', 'Uruguay', 4],
    ['Who is known as the Flying Sikh?', 'Michael Jackson', 'Usain Bolt', 'Milkha Singh', 'Carl Lewis', 3],
    ['What does Magnus Carlsen play?', 'Chess', 'Football', 'Tennis', 'Golf', 1],
    ['What is the national Sports of China?', 'Baseball', 'Cricket', 'Swimming', 'Table Tennis', 4]
]

rounds[4] = [
    ['Which treaty was signed at the end of World War I?', 'Treaty of Paris', 'Treaty of Maastricht', 'Treaty of Versailles', 'Treaty of London', 3],
    ['Battle of Waterloo was fought in which country?', 'France', 'Iran', 'Belgium', 'India', 3],
    ['Which of the following metals was not known during the Indus Valley Civilization?', 'Iron', 'Gold', 'Copper', 'Silver', 1],
    ['In which year, America joined the World War II', '1939', '1940', '1941', '1942', 3],
    ['When was ancient Rome founded?', '776 BC', '753 BC', '752 BC', '742 BC', 2]
]

def questions():
    global point
    point = 0

    for index in range(len(rounds)):

        round = rounds[index]
        round_name = name[index]

        print(f'\n---Round {[index + 1]} : {round_name}---')

        for question in round:
            print(f'\nQ. {question[0]}\n')
            print(f'1. {question[1]}\n2. {question[2]}\n3. {question[3]}\n4. {question[4]}')

            answer = int(input('Enter your answer :'))

            if answer == question[5]:
                point = point + 2
                print(f'Your answer is Correct.\nYour score is {point}')

            else:
                print(f'Your answer is incorrect.\nThe correct answer is {question[question[5]]}.\nYour score is {point}')

for index in range(len(rounds)):
    questions()

    break

print(f'\nThe Quiz is Complete.\nYour Total score is {point}')