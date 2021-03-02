# Sam Pitonyak
# CS021: Intro To Python
# Final Project
# This program has all the March Madness upsets from each year back
# to 2010 and has them stored in dictionaries
# The user is prompted to enter a team, year, one must be filled out
# What is returned is the upset, with the seedings, and score


# Define the main() function
def main():
# ADD ERROR EXCEPTION HANDLING, EDDY WILL TRY TO BREAK CODE
    try:
# Make a while loop so that the user can enter more information
# if they would like the program to keep running
# ALL of the if statements will be inside of the while loop
# allowing for the user to see more data
        yes = 'y'
        while yes == 'y':
# Prompt the user to enter the name of a school and the year
# that they played in or one of the options
            print('Enter a school name, just the name of the school.')
            print("For example: University of North Carolina would be entered as 'North Carolina'.")
            school = input('Please enter a school name: ')
            # Replace spaces with 'xzq' so that it can pass the test to make sure there are
            # no numbers/punctuation in the name of the school
            university = school.replace(' ', 'xzq')
            while university.isalpha() == False:
                university = input('Please enter a school name with only alphabetic letters: ')
                university = university.replace(' ', 'xzq')
            # Replace 'xzq' with spaces so the program can search through the dictionaries
            # to find the corresponding keys
            education = university.replace('xzq', ' ')
            college = education.lower()

# Send the name of the school to each function of the year to
# see if the school entered upset any teams
            twenty10(college)
            twenty11(college)
            twenty12(college)
            twenty13(college)
            twenty14(college)
            twenty15(college)
            twenty16(college)
            twenty17(college)
            twenty18(college)
            twenty19(college)

            # Add a histogram for what seeds won the upset for that year
            # Ask the user if they would like to view a histogram from a specific year
            print('')
            print('Would you like to view a histogram of the amount of wins each', end = ' ')
            histo = input('seeding had? (y/n): ')
            lower = histo.lower()
            # Make an if statement for if the user says yes
            if lower == 'y':
                time = int(input("What year's histogram would you like to view (2010-2019)? "))
                # Make an if statement for which year the user enters and define the function
                # that makes the histogram for that year
                print('')
                print('Number of upsets by each seed.')
                print('Seeding', end = ' ')
                if time == 2010:
                    print('for 2010')
                    print('----------------')
                    seed10 = ten10()
                    for key in seed10:
                        print(format(key, '7') + '*' * seed10[key])
                elif time == 2011:
                    print('for 2011')
                    print('----------------')
                    seed11 = ten11()
                    for key in seed11:
                        print(format(key, '7') + '*' * seed11[key])
                elif time == 2012:
                    print('for 2012')
                    print('----------------')
                    seed12 = ten12()
                    for key in seed12:
                        print(format(key, '7') + '*' * seed12[key])
                elif time == 2013:
                    print('for 2013')
                    print('----------------')
                    seed13 = ten13()
                    for key in seed13:
                        print(format(key, '7') + '*' * seed13[key])
                elif time == 2014:
                    print('for 2014')
                    print('----------------')
                    seed14 = ten14()
                    for key in seed14:
                        print(format(key, '7') + '*' * seed14[key])
                elif time == 2015:
                    print('for 2015')
                    print('----------------')
                    seed15 = ten15()
                    for key in seed15:
                        print(format(key, '7') + '*' * seed15[key])
                elif time == 2016:
                    print('for 2016')
                    print('----------------')
                    seed16 = ten16()
                    for key in seed16:
                        print(format(key, '7') + '*' * seed16[key])
                elif time == 2017:
                    print('for 2017')
                    print('----------------')
                    seed17 = ten17()
                    for key in seed17:
                        print(format(key, '7') + '*' * seed17[key])
                elif time == 2018:
                    print('for 2018')
                    print('----------------')
                    seed18 = ten18()
                    for key in seed18:
                        print(format(key, '7') + '*' * seed18[key])
                elif time == 2019:
                    print('for 2019')
                    print('----------------')
                    seed19 = ten19()
                    for key in seed19:
                        print(format(key, '7') + '*' * seed19[key])

# Ask the user if they would like to look at other years/teams (y/n)
            repeat = input('Would you like to look at another team or year? (y/n): ')
            yes = repeat.lower()

    except ValueError:
        print('Please enter alphabetical letters for the school name')

# Define the twenty10()
# Search through for whatever was sent
def twenty10(name):
    # Make a dictionary with the name of the team that won as the key and the teams that lost as the value
    year_10 = {'northern iowa':'No. 8 UNLV (69)-(66) and beat No. 1 Kansas (69)-(67)', 'ohio':'No, 3 Georgetown (97)-(83)',
               'georgia tech':'No. 7 Oklahoma State (64)-(59)', 'murray state':'No. 4 Vanderbilt (66)-(65)',
               'wake forest':'No. 8 Texas (81)-(80)', 'cornell':'No. 5 Temple (78)-(65) and beat No. 4 Wisconsin (87)-(69)',
               'washington':'No. 6 Marquette (80)-(78) and beat No. 3 New Mexico (82)-(64)',
               'missouri':'No. 7 Clemson (86)-(78)', 'old dominion':'No. 6 Notre Dame (51)-(50)',
               "st. mary's":'No. 7 Richmond (80)-(71) and beat No. 2 Villanova (75)-(68)',
               'michigan state':'No. 4 Maryland (85)-(83)',
               'xavier':'No. 3 Pittsburgh (71)-(68)', 'tennessee':'No. 2 Ohio State (76)-(73)',
               'butler':'No. 1 Syracuse (63)-(59) and beat No. 2 Kansas State (63)-(56)',
               'west virginia':'No. 1 Kentucky (73)-(66)'}
    # Make a dictionary for the seedings that the teams that won were
    seeding_10 = {'northern iowa':'NO. 9', 'ohio':'NO. 14', 'georgia tech':'NO. 10', 'murray state':'NO. 13',
                  'wake forest':'NO. 9', 'cornell':'NO. 12', 'washington':'NO. 11', 'missouri':'NO. 10',
                  'old dominion':'NO. 11', "st. mary's":'NO. 10', 'michigan state':'NO. 5', 'xavier':'NO. 6',
                  'tennessee':'NO. 6', 'butler':'NO. 5', 'west virginia':'NO. 2'}
    # Create a for loop to search through year_10 and if the name is found, retrieve the value and print the information
    for i in year_10:
        if i == name:
            value = year_10.get(name)
            for seed in seeding_10:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == name:
                    rank = seeding_10.get(seed)
                    print('')
                    print(rank, end = ' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2010 TOURNAMENT.')

            # Add the number of upsets for the total year
            num_upsets10 = 20
            print('THERE WERE', num_upsets10, 'UPSETS IN THE 2010 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if name not in year_10:
        print('')
        absent = name.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2010.')
        print('')
# Define the twenty11()
# Search through for whatever was sent
def twenty11(school):
    # Make a dictionary with the name of the team that won as the key and the teams that lost as the value
    year_11 = {'marquette':'No. 6 Xavier (66)-(55) and beat No. 3 Syracuse (66)-(62)',
               'kentucky':'No. 1 Ohio State (62)-(60) and beat No. 2 North Carolina (76)-(69)',
               'arizona':'No. 4 Texas (70)-(69) and beat No. 1 Duke (93)-(77)',
               'connecticut':'No. 2 San Diego State (74)-(67)', 'illinois':'No. 8 UNLV (73)-(62)',
               'richmond':'No. 5 Vanderbilt (69)-(66)', 'morehead state':'No. 4 Louisville (62)-(61)',
               'vcu':'No. 6 Georgetown (74)-(56), beat No. 3 Purdue (94)-(76), beat No. 10 Florida State (72)-(71) and beat No. 1 Kansas (71)-(61)',
               'florida state':'No. 7 Texas A&M (57)-(50) and beat No. 2 Notre Dame (71)-(57)',
               'gonzaga':'No. 6 St. Johns (86)-(71)', 'butler':'No. 1 Pittsburgh (71)-(70), beat No. 4 Wisconsin (61)-(54) and beat No. 2 Florida (74)-(71)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_11 = {'marquette':'NO. 11', 'kentucky':'NO. 4', 'arizona':'NO. 5', 'connecticut':'NO. 3', 'illinois':'NO. 9',
                  'richmond':'NO. 12', 'morehead state':'NO. 13', 'vcu':'NO. 11', 'florida state':'NO. 10',
                  'gonzaga':'NO. 11', 'butler':'NO. 8'}
    # Create a for loop to search through year_11 and if the name is found, retrieve the value and print the information
    for i in year_11:
        if i == school:
            value = year_11.get(school)
            for seed in seeding_11:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == school:
                    rank = seeding_11.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2011 TOURNAMENT.')

            # Add the number of upsets for the total year
            num_upsets11 = 20
            print('THERE WERE', num_upsets11, 'UPSETS IN THE 2011 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if school not in year_11:
        print('')
        absent = school.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2011.')
        print('')
# Define the twenty12()
# Search through for whatever was sent
def twenty12(label):
    # Make a dictionary with the name of the team that won as the key and the teams that lost as the value
    year_12 = {'vcu':'No. 5 Wichita St. (62)-(59)', 'colorado':'No. 6 UNLV (68)-(64)', 'xavier':'No. 7 Notre Dame (67)-(63)',
               'lehigh':'No. 2 Duke (75)-(70)', 'saint louis':'No. 8 Memphis (61)-(54)', 'norfolk state':'No. 2 Missouri (86)-(84)',
               'south florida':'No. 5 Temple (58)-(44)', 'ohio':'No. 4 Michigan (65)-(60) and No. 12 South Florida (62)-(56)',
               'n.c. state':'No. 6 San Diego State (79)-(65) and No. 3 Georgetown (66)-(63)',
               'purdue':"No. 7 Saint Mary's (Calif.) (72)-(69)", 'cincinnati':'No. 3 Florida State (62)-(56)',
               'louisville':'No. 1 Michigan State (57)-(44)', 'florida':'No. 3 Marquette (68)-(58)', 'ohio state':'No. 1 Syracuse (77)-(70)',
               'kansas':'No. 1 North Carolina (80)-(67)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_12 = {'vcu':'NO. 12', 'colorado':'NO. 11', 'xavier':'NO. 10', 'lehigh':'NO. 15', 'saint louis':'NO. 9',
                  'norfolk state':'NO. 15', 'south florida':'NO. 12', 'ohio':'NO. 13', 'n.c. state':'NO. 11',
                  'purdue':'NO. 10', 'cincinnati':'NO. 6', 'louisville':'NO. 4', 'florida':'NO. 7',
                  'ohio state':'NO. 2', 'kansas':'NO. 2'}
    # Create a for loop to search through year_12 and if the name is found, retrieve the value and print the information
    for i in year_12:
        if i == label:
            value = year_12.get(label)
            for seed in seeding_12:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == label:
                    rank = seeding_12.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2012 TOURNAMENT.')

            # Add the number of upsets for the total year
            num_upsets12 = 17
            print('THERE WERE', num_upsets12, 'UPSETS IN THE 2012 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if label not in year_12:
        print('')
        absent = label.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2012.')
        print('')
# Define the twenty13()
# Search through for whatever was sent
def twenty13(alias):
    # Make a dictionary with the name of the team that won as the key and the teams that lost as the value
    year_13 = {'oregon':'No. 5 Oklahoma St. (68)-(55) and beat No. 4 Saint Louis (74)-(57)',
               'wichita state':'No. 8 Pittsburgh (73)-(55), No. 1 Gonzaga (76)-(70), and beat No. 2 Ohio State (70)-(66)',
               'mississippi':'No. 5 Wisconsin (57)-(46)', 'la salle':'No. 4 Kansas State (63)-(61) and No. 12 Mississippi (76)-(74)',
               'harvard':'No. 3 New Mexico (68)-(62)', 'iowa state':'No. 7 Notre Dame (76)-(58)', 'minnesota':'No. 6 UCLA (83)-(63)',
               'florida gulf coast':'No. 2 Georgetown (78)-(68) and No. 7 San Diego State (81)-(71)',
               'michigan':'No. 1 Kansas (87)-(85) and No. 3 Florida (79)-(59)', 'temple':'No. 8 NC State (76)-(72)',
               'california':'No. 5 UNLV (64)-(61)', 'syracuse':'No. 1 Indiana (61)-(50) and beat No. 3 Marquette (55)-(39)',
               'marquette':'No. 2 Miami (FL) (71)-(61)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_13 = {'oregon':'NO. 12', 'wichita state':'NO. 9', 'mississippi':'NO. 12', 'la salle':'NO. 13',
                  'harvard':'NO. 14', 'iowa state':'NO. 10', 'minnesota':'NO. 11', 'florida gulf coast':'NO. 15',
                  'michigan':'NO. 4', 'temple':'NO. 9', 'california':'NO. 12', 'syracuse':'NO. 4', 'marquette':'NO. 3'}
    # Create a for loop to search through year_13 and if the name is found, retrieve the value and print the information
    for i in year_13:
        if i == alias:
            value = year_13.get(alias)
            for seed in seeding_13:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == alias:
                    rank = seeding_13.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2013 TOURNAMENT.')

            # Add the number of upsets for the total year
            num_upsets13 = 20
            print('THERE WERE', num_upsets13, 'UPSETS IN THE 2013 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if alias not in year_13:
        print('')
        absent = alias.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2013.')
        print('')
# Define the twenty14()
# Search through for whatever was sent
def twenty14(sign):
    year_14 = {'pittsburgh':'No. 8 Colorado (77)-(48)', 'stephen f. austin':'No. 5 VCU (77)-(75)',
               'dayton':'No. 6 Ohio State (60)-(59), No. 3 Syracuse (55)-(53), and beat No. 10 Stanford (82)-(72)',
               'stanford':'No. 7 New Mexico (58)-(53) and beat No. 2 Kansas (60)-(57)',
               'harvard':'No. 5 Cincinnati (61)-(51)', 'michigan state':'No. 1 Virginia (61)-(59)',
               'connecticut':'No. 2 Villanova (77)-(65), No. 3 Iowa State (81)-(76), No. 4 Michigan State (60)-(54), and beat No. 1 Florida (63)-(53)',
               'north dakota state':'No. 5 Oklahoma (80)-(75)', 'baylor':'No. 3 Creighton (85)-(55)',
               'wisconsin':'No. 1 Arizona (64)-(63)', 'tennessee':'No. 6 Massachusetts (86)-(67)', 'mercer':'No. 3 Duke (78)-(71)',
               'kentucky':'No. 1 Wichita State (78)-(76), No. 4 Louisville (74)-(69), No. 2 Michigan (75)-(72), and beat No. 2 Wisconsin (74)-(73)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_14 = {'pittsburgh':'NO. 9', 'stephen f. austin':'NO. 12', 'dayton':'NO. 11', 'stanford':'NO. 10',
                  'harvard':'NO. 12', 'michigan state':'NO. 4', 'connecticut':'NO. 7', 'north dakota state':'NO. 12',
                  'baylor':'NO. 6', 'wisconsin':'NO. 2', 'tennessee':'NO. 11', 'mercer':'NO. 14', 'kentucky':'NO. 8'}
    # Create a for loop to search through year_14 and if the name is found, retrieve the value and print the information
    for i in year_14:
        if i == sign:
            value = year_14.get(sign)
            for seed in seeding_14:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == sign:
                    rank = seeding_14.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2014 TOURNAMENT.')

            # Add the number of upsets for the total year
            num_upsets14 = 22
            print('THERE WERE', num_upsets14, 'UPSETS IN THE 2014 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if sign not in year_14:
        print('')
        absent = sign.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2014.')
        print('')
# Define the twenty15()
# Search through for whatever was sent
def twenty15(nickname):
    year_15 = {'wichita state':'No. 2 Kansas (78)-(65)', 'west virginia':'No. 4 Maryland (69)-(59)',
               'georgia state':'No. 3 Baylor (57)-(56)', 'ohio state':'No. 7 VCU (75)-(72)',
               'dayton':'No. 6 Providence (66)-(53)', 'michigan state':'No. 2 Virginia (60)-(54), No. 3 Oklahoma (62)-(58), and beat No. 4 Louisville (76)-(70)',
               'nc state':'No. 1 Villanova (71)-(68)', 'ucla':'No. 6 Southern Methodist (60)-(59)',
               'uab':'No. 3 Iowa State (60)-(59)', 'utah':'No. 4 Georgetown (75)-(64)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_15 = {'wichita state':'NO. 7', 'west virginia':'NO. 5', 'georgia state':'NO. 14',
                  'ohio state':'NO. 10', 'dayton':'NO. 11', 'michigan state':'NO. 7',
                  'nc state':'NO. 8', 'ucla':'NO. 11', 'uab':'NO. 14', 'utah':'NO. 5'}
    # Create a for loop to search through year_15 and if the name is found, retrieve the value and print the information
    for i in year_15:
        if i == nickname:
            value = year_15.get(nickname)
            for seed in seeding_15:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == nickname:
                    rank = seeding_15.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2015 TOURNAMENT.')

            num_upsets15 = 12
            print('THERE WERE', num_upsets15, 'UPSETS IN THE 2015 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if nickname not in year_15:
        print('')
        absent = nickname.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2015.')
        print('')

# Define the twenty16()
# Search through for whatever was sent
def twenty16(brand):
    year_16 = {'connecticut':'No. 8 Colorado (74)-(67)', 'hawaii':'No. 4 California (77)-(66)',
               'wichita state':'No. 6 Arizona (65)-(55)', 'villanova':'No. 1 Kansas (64)-(59) and beat No. 1 North Carolina (77)-(74)',
               'northern iowa':'No. 6 Texas (75)-(72)', 'vcu':'No. 7 Oregon State (75)-(67)', 'oklahoma':'No. 1 Oregon (80)-(68)',
               'providence':'No. 8 USC (70)-(69)', 'stephen f. austin':'No. 3 West Virginia (70)-(56)',
               'wisconsin':'No. 2 Xavier (66)-(63)', 'indiana':'No. 4 Kentucky (73)-(67)', 'butler':'No. 8 Texas Tech (71)-(61)',
               'little rock':'No. 5 Purdue (85)-(83)', 'gonzaga':'No. 6 Seton Hall (68)-(52) and beat No. 3 Utah (82)-(59)',
               'syracuse':'No. 7 Dayton (70)-(51) and beat No. 1 Virginia (68)-(62)', 'middle tennessee':'No. 2 Michigan State (90)-(81)',
               'yale':'No. 5 Baylor (79)-(75)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_16 = {'connecticut':'NO. 9', 'hawaii':'NO. 13', 'wichita state':'NO. 11', 'villanova':'NO. 2', 'yale':'NO. 12',
                  'northern iowa':'NO. 11', 'vcu':'NO. 10', 'oklahoma':'NO. 2', 'providence':'NO. 9', 'stephen f. austin':'NO. 14',
                  'wisconsin':'NO. 7', 'indiana':'NO. 5', 'butler':'NO. 9', 'little rock':'NO. 12', 'gonzaga':'NO. 11',
                  'syracuse':'NO. 10', 'middle tennessee':'NO. 15'}
    # Create a for loop to search through year_16 and if the name is found, retrieve the value and print the information
    for i in year_16:
        if i == brand:
            value = year_16.get(brand)
            for seed in seeding_16:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == brand:
                    rank = seeding_16.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2016 TOURNAMENT.')

            num_upsets16 = 20
            print('THERE WERE', num_upsets16, 'UPSETS IN THE 2016 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if brand not in year_16:
        print('')
        absent = brand.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2016.')
        print('')
# Define the twenty17()
# Search through for whatever was sent
def twenty17(flag):
    year_17 = {'usc':'No. 6 Southern Methodist (66)-(65)', 'south carolina':'No. 2 Duke (88)-(81), No. 3 Baylor (70)-(50), and beat No. 4 Florida (77)-(70)',
               'wisconsin':'No. 1 Villanova (65)-(62)', 'xavier':'No. 6 Maryland (76)-(65), No. 3 Florida State (91)-(66), and beat No. 2 Arizona (73)-(71)',
               'michigan state':'No. 8 Miami (FL) (78)-(58)', 'rhode island':'No. 6 Creighton (84)-(72)',
               'michigan':'No. 2 Louisville (73)-(69)', 'oregon':'No. 1 Kansas (74)-(60)', 'middle tennessee':'No. 5 Minnesota (81)-(72)',
               'wichita state':'No. 7 Dayton (64)-(58)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_17 = {'usc':'NO. 11', 'south carolina':'NO. 7', 'wisconsin':'NO. 8', 'xavier':'NO. 11', 'michigan state':'NO. 9',
                  'rhode island':'NO. 11', 'michigan':'NO. 7', 'oregon':'NO. 3', 'middle tennessee':'NO. 12', 'wichita state':'NO. 10'}
    # Create a for loop to search through year_17 and if the name is found, retrieve the value and print the information
    for i in year_17:
        if i == flag:
            value = year_17.get(flag)
            for seed in seeding_17:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == flag:
                    rank = seeding_17.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2017 TOURNAMENT.')

            num_upsets17 = 14
            print('THERE WERE', num_upsets17, 'UPSETS IN THE 2017 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if flag not in year_17:
        print('')
        absent = flag.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2017.')
        print('')

# Define the twenty18()
# Search through for whatever was sent
def twenty18(signature):
    year_18 = {'umbc':'No. 1 Virginia (74)-(54)', 'kansas state':'No. 8 Creighton (69)-(59) and beat No. 5 Kentucky (61)-(58)', 'buffalo':'No. 4 Arizona (89)-(68)',
               'loyola-chicago':'No. 6 Miami (FL) (64)-(62), No. 3 Tennessee (63)-(62), No. 7 Nevada (69)-(68), and beat No. 9 Kansas State (78)-(62)',
               'nevada':'No. 2 Cincinnati (75)-(73)', 'florida state':'No. 8 Missouri (67)-(54), No. 1 Xavier (75)-(70), and beat No. 4 Gonzaga (75)-(60)',
               'texas a&m':'No. 2 North Carolina (86)-(65)', 'alabama':'No. 8 Virginia Tech (86)-(83)', 'marshall':'No. 4 Wichita State (81)-(75)',
               'butler':'No. 7 Arkansas (79)-(62)', 'texas tech':'No. 2 Purdue (78)-(65)', 'syracuse':'No. 6 TCU (57)-(52) and beat No. 3 Michigan State (55)-(53)',
               'clemson':'No. 4 Auburn (84)-(53)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_18 = {'umbc':'NO. 16', 'kansas state':'NO. 9', 'buffalo':'NO. 13', 'loyola-chicago':'NO. 11',
                  'nevada':'NO. 7', 'florida state':'NO. 9', 'texas a&m':'NO. 7', 'alabama':'NO. 9',
                  'marshall':'NO. 13', 'butler':'NO. 10', 'texas tech':'NO. 3', 'syracuse':'NO. 11', 'clemson':'NO. 5'}
    # Create a for loop to search through year_18 and if the name is found, retrieve the value and print the information
    for i in year_18:
        if i == signature:
            value = year_18.get(signature)
            for seed in seeding_18:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == signature:
                    rank = seeding_18.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2018 TOURNAMENT.')

            num_upsets18 = 20
            print('THERE WERE', num_upsets18, 'UPSETS IN THE 2018 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if signature not in year_18:
        print('')
        absent = signature.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2018.')
        print('')

# Define the twenty19()
# Search through for whatever was sent
def twenty19(style):
    year_19 = {'ucf':'No. 8 VCU (73)-(58)', 'liberty':'No. 5 Mississippi State (80)-(76)', 'minnesota':'No. 7 Louisville (86)-(76)',
               'michigan state':'No. 1 Duke (68)-(67)', 'baylor':'No. 8 Syracuse (78)-(69)', 'florida':'No. 7 Nevada (70)-(61)',
               'texas tech':'No. 2 Michigan (63)-(44), No. 1 Gonzaga (75)-(69), and beat No. 2 Michigan State (61)-(51)', 'oklahoma':'No. 8 Ole Miss (95)-(72)',
               'oregon':'No. 5 Wisconsin (72)-(54)', 'uc irvine':'No. 4 Kansas State (70)-(64)', 'iowa':'No. 7 Cincinnati (79)-(72)',
               'washington':'No. 8 Utah State (78)-(61)', 'ohio state':'No. 6 Iowa State (62)-(59)',
               'auburn':'No. 4 Kansas (89)-(75), No. 1 North Carolina (97)-(80), and beat No. 2 Kentucky (77)-(71)'}
    # Make a dictionary for the seeding of the teams that won
    seeding_19 = {'ucf':'NO. 9', 'liberty':'NO. 12', 'minnesota':'NO. 10', 'michigan state':'NO. 2', 'baylor':'NO. 9',
                  'florida':'NO. 10', 'texas tech':'NO. 3', 'oklahoma':'NO. 9', 'oregon':'NO. 12', 'uc irvine':'NO. 13',
                  'iowa':'NO. 10', 'washington':'NO. 9', 'ohio state':'NO. 11', 'auburn':'NO. 5'}
    # Create a for loop to search through year_19 and if the name is found, retrieve the value and print the information
    for i in year_19:
        if i == style:
            value = year_19.get(style)
            for seed in seeding_19:
                # Search through the seedings, if the name is equal to the key, get the value and print it
                if seed == style:
                    rank = seeding_19.get(seed)
                    print('')
                    print(rank, end=' ')
            # Make all of the information uppercase
            upseter = i.upper()
            upsety = value.upper()
            print(upseter, 'UPSET', upsety, 'IN THE 2019 TOURNAMENT.')

            num_upsets19 = 18
            print('THERE WERE', num_upsets19, 'UPSETS IN THE 2019 TOURNAMENT')
    # Make an if statement for if the team did not upset anyone for the year
    if style not in year_19:
        print('')
        absent = style.upper()
        print(absent, 'DID NOT UPSET ANY TEAM IN 2019.')
        print('')

# Define ten10() and make the histogram for the year then return it
def ten10():
    # Assign each seeding a total
    seed_tally10 = {'No. 1:':0, 'No. 2:':1, 'No. 3:':0, 'No. 4:':0, 'No. 5:':3, 'No. 6:':2, 'No. 7:':0, 'No. 8:':0,
                    'No. 9:':3, 'No. 10:':4, 'No. 11:':3, 'No. 12:':2, 'No. 13:':1, 'No. 14:':1, 'No. 15:':0, 'No. 16:':0}
    return seed_tally10

# Define ten11() and make the dictionary containing the histogram values
def ten11():
    # Assign each seeding a total
    seed_tally11 = {'No. 1:':0, 'No. 2:':0, 'No. 3:':1, 'No. 4:':2, 'No. 5:':2, 'No. 6:':0, 'No. 7:':0, 'No. 8:':3,
                    'No. 9:':1, 'No. 10:':2, 'No. 11:':7, 'No. 12:':1, 'No. 13:':1, 'No. 14:':0, 'No. 15:':0, 'No. 16:':0}
    return seed_tally11

# Define ten12() and make the dictionary containing the histogram values
def ten12():
    # Assign each seeding a total
    seed_tally12 = {'No. 1:':0, 'No. 2:':2, 'No. 3:':0, 'No. 4:':1, 'No. 5:':0, 'No. 6:':1, 'No. 7:':1, 'No. 8:':0,
                    'No. 9:':1, 'No. 10:':2, 'No. 11:':3, 'No. 12:':2, 'No. 13:':2, 'No. 14:':0, 'No. 15:':2, 'No. 16:':0}
    return seed_tally12
# Define ten13() and make the dictionary containing the histogram values
def ten13():
    # Assign each seeding a total
    seed_tally13 = {'No. 1:': 0, 'No. 2:': 0, 'No. 3:': 1, 'No. 4:': 4, 'No. 5:': 0, 'No. 6:': 0, 'No. 7:': 0, 'No. 8:': 0,
                    'No. 9:': 4, 'No. 10:': 1, 'No. 11:': 1, 'No. 12:': 4, 'No. 13:': 2, 'No. 14:': 1, 'No. 15:': 2,'No. 16:': 0}
    return seed_tally13
# Define ten14() and make the dictionary containing the histogram values
def ten14():
    # Assign each seeding a total
    seed_tally14 = {'No. 1:': 0, 'No. 2:': 1, 'No. 3:': 0, 'No. 4:': 1, 'No. 5:': 0, 'No. 6:': 1, 'No. 7:': 4, 'No. 8:': 4,
                    'No. 9:': 1, 'No. 10:': 2, 'No. 11:': 4, 'No. 12:': 3, 'No. 13:': 0, 'No. 14:': 1, 'No. 15:': 0, 'No. 16:': 0}
    return seed_tally14

# Define ten15() and make the dictionary containing the histogram values
def ten15():
    # Assign each seeding a total
    seed_tally15 = {'No. 1:': 0, 'No. 2:': 0, 'No. 3:': 0, 'No. 4:': 0, 'No. 5:': 2, 'No. 6:': 0, 'No. 7:': 4, 'No. 8:': 1,
                    'No. 9:': 0, 'No. 10:': 1, 'No. 11:': 2, 'No. 12:': 0, 'No. 13:': 0, 'No. 14:': 2, 'No. 15:': 0, 'No. 16:': 0}
    return seed_tally15
# Define ten16() and make the dictionary containing the histogram values
def ten16():
    # Assign each seeding a total
    seed_tally16 = {'No. 1:': 0, 'No. 2:': 3, 'No. 3:': 0, 'No. 4:': 0, 'No. 5:': 1, 'No. 6:': 0, 'No. 7:': 1, 'No. 8:': 0,
                    'No. 9:': 3, 'No. 10:': 3, 'No. 11:': 4, 'No. 12:': 2, 'No. 13:': 1, 'No. 14:': 1, 'No. 15:': 1, 'No. 16:': 0}
    return seed_tally16
# Define ten17() and make the dictionary containing the histogram values
def ten17():
    # Assign each seeding a total
    seed_tally17 = {'No. 1:': 0, 'No. 2:': 0, 'No. 3:': 1, 'No. 4:': 0, 'No. 5:': 0, 'No. 6:': 0, 'No. 7:': 4, 'No. 8:': 1,
                    'No. 9:': 1, 'No. 10:': 1, 'No. 11:': 5, 'No. 12:': 1, 'No. 13:': 0, 'No. 14:': 0, 'No. 15:': 0, 'No. 16:': 0}
    return seed_tally17
# Define ten18() and make the dictionary containing the histogram values
def ten18():
    # Assign each seeding a total
    seed_tally18 = {'No. 1:': 0, 'No. 2:': 0, 'No. 3:': 1, 'No. 4:': 0, 'No. 5:': 1, 'No. 6:': 0, 'No. 7:': 2, 'No. 8:': 0,
                    'No. 9:': 6, 'No. 10:': 1, 'No. 11:': 6, 'No. 12:': 0, 'No. 13:': 2, 'No. 14:': 0, 'No. 15:': 0, 'No. 16:': 1}
    return seed_tally18
# Define ten19() and make the dictionary containing the histogram values
def ten19():
    # Assign each seeding a total
    seed_tally19 = {'No. 1:': 0, 'No. 2:': 1, 'No. 3:': 3, 'No. 4:': 0, 'No. 5:': 3, 'No. 6:': 0, 'No. 7:': 0, 'No. 8:': 0,
                    'No. 9:': 4, 'No. 10:': 3, 'No. 11:': 1, 'No. 12:': 2, 'No. 13:': 1, 'No. 14:': 0, 'No. 15:': 0, 'No. 16:': 0}
    return seed_tally19

main()
