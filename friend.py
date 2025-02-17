import pyttsx3
friend=pyttsx3.init()
# already given one
friend.say("hello everyone. Rahita here!")

#taking the input from the user
speech=input("enter the input: ")
friend.say(speech)

#change the speed of the speech
rate=friend.getProperty('rate')
print(f"the rate is {rate}")#by default it is 200
friend.setProperty('rate',130)
friend.say("hello! the speed is 150")
friend.runAndWait()
