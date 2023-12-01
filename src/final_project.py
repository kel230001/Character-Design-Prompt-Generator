import random
#import os
#import openai
#import nextcord
#from nextcord.ext import commands
from craiyon import Craiyon
from PIL import Image
from io import BytesIO
import time
#from config import TOKEN

#pip install openai
#To update, run: python.exe -m pip install --upgrade pip
#pip install -U craiyon.py
 
print("Welcome to character generator! Would you like to start your character?")
 
artist = input()
#def start(artist):
if (artist == "yes"):
        """
        :param artist
        :type artist: str
        :returns: print function
        :rtype: TYPE IDK
         """
        ##two lines below make case sensitive?
        #artist=input(answer_yes)
        #answer_yes = answer_yes.casefold()
    #return
        print("Great! Let's get Started!")
   
 
print("Would you like to randomize your type of character?")
 
 
def character_type(artist):
    """
    :param artist
    :type artist: str
    :return: type
    :rtype: str
    """
artist = input()
if (artist == "yes"):
        ##two lines below make case sensitive?
        #artist=input(answer_yes)
        #answer_yes = answer_yes.casefold()
        #return character_type
    character_type = ["Human", "Animal"]
    idx = random.randrange(2)
    print("Your character is a" , character_type[idx])
#character_type[idx]=type
if (character_type[idx] == "Animal"):
#elif(idx == "Animal"):
    file_path = "animal.txt"
    #try:
    with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines)
                animal_type = random_line.strip()
                print("a(an)",animal_type)
    #def get_prompts_from_file(animal):
        #animals = get_prompts_from_file("animal.txt")
    #def pick_random_prompt(prompts):    
        #animal = pick_random_prompt(prompts)
        #f = open(animal , 'r')
        #prompt_list = f.read().split('\n')
        #f.close()
        #return prompt_list
        #return animal
#artist = input()  
#if (artist == "no"):
        ##two lines below make case sensitive?
        #artist = input(answer_input)
        #answer_input = answer_input.casefold()
#print("Input your type")
   
#print("Would you like to choose the gender?")   
print("Would you like to know the gender?")
artist = input()
if (artist == "yes"):
    gender = ["Male","Female"]
    random_gender = random.choice(gender)
    print("Your character is",random_gender) 
#if (artist == "yes"):
    #print("Type your gender choice")
    #artist = input()
    #type_gender = f" {artist}"

    
 
       
#def character_gender(artist):
    #fix docstring
    #"""
    #:param artist
    #:type artist: str
    #:return: gender
    #:rtype: str
    #"""
    #print("Would you like to randomize or input gender?")
    #gender = ["male","female"]
    #idx = random.randrange(2)
    #if (artist == "yes"):
        ####two lines below make case sensitive?
        #artist=input(answer_yes)
        #answer_yes = answer_yes.casefold()
        #return gender[idx]
    #if (artist == "input"):
    ####two lines below make case sensitive?
        #artist = input(answer_input)
        #answer_input = answer_input.casefold()
        #return(print("Input your type"))
 
#def main():
    ##doctstring?
    #gender = character_gender()
#print(character_gender)
 
print("Would you like to know the vibe of your character?")


artist = input()
file_path = "emotion.txt"
with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines:
            random_line = random.choice(lines)
            emotion = random_line.strip()
            

file_path = "theme.txt"
with open(file_path,'r') as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines)
                theme = random_line.strip()

            print("Your character is a(an)" , emotion , theme)
 
#def character_theme():
    ##add docstring
    #themes = get_prompts_from_file("theme.txt")
    #theme = pick_random_prompt(themes)
 
#def character_emotion():
    #emotions = get_prompts_from_file("emotion.txt")
    #emotion = pick_random_prompt(emotions)
 
#def main():
    #emotion= character_emotion
    #theme = character_theme
 
    #print(f"{emotion} {theme}")
    #print(character_theme + character_emotion)
   

   

 
#'''
if (character_type[idx] == "Animal"):
    print("In sum, your character is a(an)",character_type[idx],animal_type,random_gender,"who is a(an)",emotion,theme,"!")
if (character_type[idx]) == "Human":
    print("In sum, your character is a(an)",character_type[idx],random_gender,"who is a(an)",emotion,theme,"!")


print("Would you like to see an example of your new generated character?")
artist = input()
if (artist == "yes"):
    print("give me a minute to generate your image")

    
#open.api_key = os.getenv("OPENAI_API_KEY")
if (character_type[idx] == "Animal"):
    user_prompt = (character_type[idx],animal_type,random_gender,emotion,theme)
if (character_type[idx]) == "Human":
    user_prompt = (character_type[idx],animal_type,random_gender,emotion,theme)
#response = openai.Image.create(
    prompt = user_prompt
#    n=1,
#    size = "1024x1024"
#)

#bot = command.Bot(command_prefix="!", intents = nextcord.Intents.all())
#@bot.event
#@bot.command()
#async def generate(ctx: commands.Context, *, prompt: str))
#    ETA = itt(time.time() = 60)
#   msg = await ctx.send(f"generating... ETA: ,t:{ETA}:R>")
#    generator= Craiyon()
#    result = generator.generate(prompt)
#    images=result.images
#    for i in imgages:
#        image = BytesIO(base64.decodebytes(i.encode("utf-8")))
#        return await msg.edit(content= "Content Generated by **craiyon.com**", f=nextcord.File(image,"generatedImage.png"))
    
#bot.run(TOKEN)

#openai.api_key = os.getenv("OPENAI_API_KEY")
 
#user_prompt = input("write your prompt for DLL-E 2: ")
 
#response = openai.Image.create(
#    prompt=user_prompt,
#    n=1,
#    #n is the number of images...if code isnt long enough, add a prompt to let the user pick n
#   size = "1024x1024"
#   #make sure resolution is adequete according to digital rain
#)
 
#image_url = response['data'][0]['url']
#print(image_url)
#minute 4.57 in video
 
#open in code     openai.api_key = <API-KEY>
#  OPENAI_API_KEY=<API-KEY>)
 
 
#if __name__ == "__main__":
#    main()
 
 
#'''