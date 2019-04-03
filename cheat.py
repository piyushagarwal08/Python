import text_to_speech as say
import sys
def safe(Girl,Boy):
    if(Girl == "harshita sharma" and Boy != "piyush agarwal"):
        print("best friends always together")
        say.speak("best friends always together")
        sys.exit()
        
