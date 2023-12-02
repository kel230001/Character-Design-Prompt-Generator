import random
#import os
#import openai
#import nextcord
#from nextcord.ext import commands
from craiyon import Craiyon
from PIL import Image
#pip install pillow
#from io import BytesIO
#import base64
import sys
#import time
#import keras_cv
#from tensorflow import keras
#import matplotlib.pylot as plt
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
if (artist == "no"):
    print ("well you just suck!")
    sys.exit()
    
 
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
    with open(file_path, 'r', encoding="utf-8-sig") as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines)
                animal_type = random_line.strip()
                print("a(an)", animal_type)
   
   
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

    
 
print("Would you like to know the vibe of your character?")


artist = input()
file_path = "emotion.txt"
with open(file_path, 'r', encoding="utf-8-sig") as file:
        lines = file.readlines()
        if lines:
            random_line = random.choice(lines)
            emotion = random_line.strip()
            

file_path = "theme.txt"
with open(file_path,'r', encoding="utf-8-sig") as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines)
                theme = random_line.strip()

            print("Your character is a(an)",emotion, theme)
 

 
#'''
if (character_type[idx] == "Animal"):
    print("In sum, your character is a(an)",character_type[idx],animal_type,random_gender,"who is a(an)",emotion,theme,"!")
if (character_type[idx]) == "Human":
    print("In sum, your character is a(an)",character_type[idx],random_gender,"who is a(an)",emotion,theme,"!")


print("Would you like to see an example of your new generated character?")
artist = input()
if (artist == "yes"):
    print("give me a minute to generate your image...")

    
#open.api_key = os.getenv("OPENAI_API_KEY")
if (character_type[idx] == "Animal"):
    user_prompt = (character_type[idx],animal_type,random_gender,emotion,theme)
if (character_type[idx]) == "Human":
    user_prompt = (character_type[idx],random_gender,emotion,theme)
#response = openai.Image.create(
#user_prompt = prompt
#    n=1,
#    size = "1024x1024"
#)

#model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

#images = model.txt_to_image(user_prompt, batch_size=3)

#def plot_images(images):
    #plt.figure(figsize(20,20))
    #for i in range(len(images)):
        #ax = plt.subplot(1, len(images), i +1)
        #plt.imshow(images[i])
        #plt.axis("off")

#plot_images(images)
print(user_prompt)
user_prompt_string = "." .join(user_prompt)


generator = Craiyon() 
result = generator.generate(user_prompt)
print(result.images)
for url in result.images:
    print(url)
print(result.description)
images = craiyon_utils.encode_base64(result.images)
for i in images:
    image = Image.open(BytesIO(base64(result.images)))



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
 
