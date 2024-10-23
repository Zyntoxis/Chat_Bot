import sys

name = input("Hello! What is your name?")                                           #Namensabfrage
print(f"Nice to meet you, {name}!")

age_input = input("How old are you?")                                               #Altersabfrage
age = int(age_input)                        
bot_age = 3
age_difference = age - bot_age 
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")

color = input("What's your favorite color?")                                        #Lieblingsfarbe
print(f"Oh, {color} is a beautiful color!")

weather = input("How's the weather today?")                                         #Wetterabfrage
print(f"Oh {weather} sounds interesting!")



sports = ["football", "tennis", "basketball", "swimming", "ride horses", "soccer", "go-cart", "hiking", "extreme sports", "cycling", "motor sports", "winter sports"]
hobby = ["reading", "cooking", "painting", "dancing", "listening to or playing music", "photography", "gardening", "writing" ]
hobbies = input("Do you have a favorite Sport or Hobby?")

if hobbies.lower() in sports:
    print(f"Oh wow, what an coincidence. {hobbies.capitalize()} is also my favorite Sport!")
elif hobbies.lower() in hobby:
    print(f"This is unbelivable. {hobbies.capitalize()} is my favorite  Hobby too!") 
else:
    print(f"I'm not familiar with {hobbies}, bit it sounds fun!")
    
    
print("So nice, to hear so much about you.")

sys.exit()