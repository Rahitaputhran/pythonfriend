import pyttsx3
friend=pyttsx3.init()
# already given one
friend.say("hello everyone. Rahita here!")

#taking the input from the user
speech=input("enter the input: ")
friend.say(speech)
friend.runAndWait()