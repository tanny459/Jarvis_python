# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors




def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("The query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query
    
# creating Speak() function to giving Speaking power
# to our voice assistant 




def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()


# Driver Code


if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        
        if "hello" in command:
            Speak("a very good morning sir, how can i assist you")
        if "check for systems" in command:
            Speak("all systems are a 100 percent go sir")

        if "enter combat mode" in command:
            Speak("Entering combat mode sir")
        if "deploy drones" in command:
            Speak("sorry sir drones are anavailable , I can deploy heavy guns insted sir")
        
        if "countermeasures ready" in command:
            Speak("Counter measures are ready to deploy")
        if "exit" in command:
            Speak("Okay sir , wish you a good day ahead")
            break
        


