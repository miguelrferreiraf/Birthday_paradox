"""This algorithm demonstrates a funny fact: the birthday paradox. Although there are 365 days in a year, 
if you're a house with other 20 people, there is a 50% chance one of them having the same birthday of you!""" 

import datetime, random

def getBirthdays(totalBirthdays):
    birthdays = []
    for i in range(totalBirthdays):
        startYear = datetime.date(1950, 1, 1)
        randomDay = datetime.timedelta(random.randint(0,364))
        birthday = startYear + randomDay
        birthdays.append(birthday)
    return birthdays

def Match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, Birthday_a in enumerate(birthdays):
        for b, Birthday_b in enumerate(birthdays[a + 1 :]):
            if Birthday_a == Birthday_b:
                return Birthday_a

""" Now it comes somewhat like a frontend display"""
print('''\n\nDid you know the if you sharing some environment with 70 people, there's a 99.9% probability 
some of them share the same birthday?? It's called the birthday paradox (it isn't a real paradox, just a funny
fact about Monte Carlo probability distribution). Let's take a look:''')

Month = ('Jan','Feb','Mar','Apr','May','Jun','Jul',
        'Aug','Set','Oct','Nov','Dec')
while True:
    print('''How many birthdays shall we generate? (max: 100)''')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <=100):
        numBDays = int(response)
        break
print()

#Generate and display the birthdays

print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(',', end='')
        monthName = Month[birthday.month - 1]
        dateText = '{} {}'.format(monthName,birthday.day)
        print (dateText, end='')
print()
print()

#Now, we determine if there are two similar birthdays
match = Match(birthdays)

print('Here we have ', end='')
if match != None:
    monthName = Month[match.month - 1]
    dateText = '{} {}' .format(monthName,match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('no matching birthdays')
print()

# Running 50.000 simulations

print('Generating', numBDays,'random birthdays 50.000 times.......')
input('Press enter to yeehaaaa!')

print('\nLets run 50.000 simulations...')

simulationMatch = 0
for i in range (50_000):
    if i% 1500 == 0:
        print('\nRunning simulation....')
    birthdays = getBirthdays(numBDays)
    if Match(birthdays) != None:
        simulationMatch = simulationMatch + 1
print('50 000 SIMULATIONS RUN!')

print('\n\n Lets see the results:')
probability = round(simulationMatch / 50_000 * 100, 2)

print('\nOut of 50.000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simulationMatch, 'times. So')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching day in this group')

print('\n\n You werent expecting that numbers, werent you?')
