playernumbers = []
lotterynumbers = []
class variables:
    matches = 0
    attempts = 0
    millenium = 0
    centuries = 0
    decades = 0
    years = 0
    months = 0
    days = 0
import random

def convertdays():
    while variables.days > 30.5:
        variables.days -= 30.5
        variables.months += 1
    while variables.months > 12:
    	variables.months -= 12
    	variables.years += 1
    while variables.years > 10:
        variables.years -= 10
        variables.decades += 1
    while variables.decades > 10:
        variables.decades -= 10
        variables.centuries += 1
    while variables.centuries > 10:
        variables.centuries -= 10
        variables.millenium += 1
        
def comparenumbers():
    while True:
        variables.attempts += 1
        variables.days += 1
        lotterynumberscompare = getnumbersfromlottery()
        lotterynumberscompare.sort()
        playernumbers.sort()
        if lotterynumberscompare == playernumbers:
            variables.matches += 1
            convertdays()
            print('Match {} found on attempt {}. The lottery numbers were {} and your numbers were {}. It has been {} millenia, {} centuries, {} decades, {} years, {} months, and {} days.'.format(variables.matches, variables.attempts, lotterynumberscompare, playernumbers, variables.millenium, variables.centuries, variables.decades, variables.years, variables.months, variables.days))
        if variables.matches == 100:
            break

def getnumbersfromlottery():
    lotterynumbers= []
    for i in range(3):
        lotterynumbers.append(random.randrange(0, 100))
    return lotterynumbers

def getnumbersfromplayers():
    for i in range(3):
        while True:
                try:
                    rawinput = int(input('Please input number {}:'.format(i+1)))
                    if 0 <= rawinput <= 100:
                        playernumbers.append(rawinput)
                        break
                    else:
                        print('Your number was not 1-100. Please try again!')
                        continue
                except:
                    print('There was an error. Please try again.')
                    continue
    return

def main():
    getnumbersfromplayers()
    comparenumbers()
    convertdays()
    print('Congratulations! It took you {} millenia, {} centuries, {} decades, {} years, {} months, and {} days to win the lottery 100 times!'.format(variables.millenium, variables.centuries, variables.decades, variables.years, variables.months, variables.days))
    
main()
    