import random

print("Welcome to character generator! Would you like to start your character?")


def start(artist):
    if (artist == "yes"):
        """
        :param artist
        :type artist: str
        :returns: print function
        :rtype: TYPE IDK
         """
        ##two lines below make case sensitive?
        artist=input(answer_yes)
        answer_yes = answer_yes.casefold()
        return print("Great! Let's get Started!")
    



def get_prompts_from_file(filename):
    """
    :param filename
    :type filename: str
    :returns: a list of prompts
    :rtype: list
    """
    f = open(filename, 'r')
    prompt_list = f.read().split('\n')
    f.close()
    return prompt_list

def pick_random_prompt(prompts):
    """
    :param prompts
    :type filename: list
    :returns: the string prompt that was randomly chosen
    :rtype: str
    """
    prompt = random.choice(prompts)
    return prompt




def character_type(artist):
    """
    :param artist
    :type artist: str
    :return: type
    :rtype: str
    """
    print("Would you like to randomize or input type of character?")
    
    if (artist == "yes"):
        ##two lines below make case sensitive?
        artist=input(answer_yes)
        answer_yes = answer_yes.casefold()
        return character_type
    character_type = ["human","animal"]
    elif (artist == "animal"):
        #elif (artist == "animal"):      ---but unexpected indent?
    ##two lines below make case sensitive?...shouldnt they be indented? error when indented
    artist=input(answer_animal)
    answer_animal = answer_animal.casefold
    def main():
        animals = get_prompts_from_file("animal.txt")
        animal = pick_random_prompt(animals)
        return animal
    if (artist == "input"):
        ##two lines below make case sensitive?
        artist = input(answer_input)
        answer_input = answer_input.casefold()
        return(print("Input your type"))



        
def character_gender(artist):
    """
    :param artist
    :type artist: str
    :return: gender
    :rtype: str
    """
    print("Would you like to randomize or input gender?")
    gender = ["male","female"]
    idx = random.randrange(2)
    if (artist == "yes"):
        ####two lines below make case sensitive?
        artist=input(answer_yes)
        answer_yes = answer_yes.casefold()
        return gender[idx]
    if (artist == "input"):
    ####two lines below make case sensitive?
        artist = input(answer_input)
        answer_input = answer_input.casefold()
        return(print("Input your type"))

def main():
    ##doctstring?
    gender = character_gender()
print(character_gender)




def main():
    ##add docstring
    themes = get_prompts_from_file("theme.txt")
    theme = pick_random_prompt(themes)
    
    emotions = get_prompts_from_file("emotion.txt")
    emotion = pick_random_prompt(emotions)

    print(f"{emotion} {theme}")
    



print("Your character is a" + character_type + character_gender + " who is a " emotion + theme "!")

if __name__ == "__main__":
    main()