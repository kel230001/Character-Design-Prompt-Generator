import random 
import csv
#can I import more than one of these...?



def character_type(artist):
    #add docstring
    print("Would you like to randomize or input type of character?")
    if (artist == "yes")
    #add case sensitive
        character_type = ["human","animal"]
            elif (artist == "animal")
            #add case sensitive
            character_type = [#animal file like artist prompt lab 6..?]
    if (artist == "input")
    #add case sensitive
        character_type = print("Input your type")
        #define character_type?



def character_gender(artist):
    """
    :return: gender
    :rtype: str
    """
    print("Would you like to randomize or input gender?")
    if (artist == "yes")
        gender = ["male","female"]
        idx = random.randrange(2)
        return gender[idx]
    if (artist == "input")
    #add case sensitive
        character_gender = print("Input your type")
        #define character_gender?




def add_item(filename, new_emotion, new_theme):
    """
    :param filename:
    :type filename: str
    :param new_emotion:
    :type new_emotion: str
    :param new_theme:
    :type new_theme: int
    """
    with open(filename, 'a', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=['emotion', 'theme'])
        csv_writer.writerow({'emotion': new_emotion, 'theme': new_theme})


def character_trait(traitsfile):
    """
    :param traitsfile:
    :type traitsfile: str
    """
    with open (traitsfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile, #IDK=['first thing', 'second thing'])
    #defaults 2 traits
    print("How many personality traits would you like your character to have? (1-4)")
    if (artist == 1)
        
    if (artist == 2)
    if (artist == 3)
    if (artist == 4)
    

    print("How many personality traits will your character have? Type answer.")

def character_trademark(artist)
    
print(character_type,)

if __name__ == "__main__":
    main()