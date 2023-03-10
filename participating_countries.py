import random


def finalists(): #A function for making finalists
    grand_final = []
    p = 0
    print('''Hello, and welcome to Eurovision Hero :)
    please write your participating countries of desire in order of who should have the highest odds of winning.
    Should you wish to delete the last country you wrote, write "delete" 
    When you are done, press "enter" on your keyboard
    ''') #Welcome message

    '''This loop asks the user to add their countries of choice to a list
    which will be used as the participants in the "grand final" of Eurovision Hero"'''

    while True: #A while loop that lets the user add countries and press 'enter', when they're finished
        print('\n')
        add_country = input() 
        if add_country == '': 
            break

        elif add_country == 'delete': 
            print(grand_final[-1], 'was deleted from the list!')
            grand_final.pop()
            print("\nYour list:")
            for x in range(len(grand_final)):
                print(x + 1, grand_final[x])
            p -= 1
            

        elif p >= 26: 
            print("Sorry, but you can't add any more countries!") 

        else:
            grand_final.append(add_country) 
            print("\nYour list:")
            for x in range(len(grand_final)):
                print(x + 1, grand_final[x])
            p += 1 
    return grand_final


def jury(participants): #A function for making the jury and the televote
    jury_loop = True
    the_jury = []
    the_televote = []
    print('Do you want to make your own jury?\n\nyes\nno\n')
    while jury_loop == True:
        same_as_grand_final = input()
        if same_as_grand_final == 'no':
            the_jury = participants.copy()
            print("")
            jury_loop = False
        elif same_as_grand_final == 'yes':
            print('''\nplease write your jury of desire.
Should you wish to delete the last jury you wrote, write "delete" 
When you are done, press "enter" on your keyboard and watch your grand final''')
            while True:
                print('\n')
                add_jury = input() 
                if add_jury == '':
                    jury_loop = False 
                    break
                elif add_jury == 'delete': 
                    print(the_jury[-1], 'was removed from the jury!')
                    the_jury.pop()
                    print("\nYour jury:")
                    for x in range(len(the_jury)):
                        print(the_jury[x])
                    
                else:
                    the_jury.append(add_jury) 
                    print("\nYour jury:")
                    for x in range(len(the_jury)):
                        print(the_jury[x])
        else:
            print('invalid input, try again')

    the_televote = list(the_jury)
    random.shuffle(the_jury)
    random.shuffle(the_televote)
    return the_jury, the_televote, participants