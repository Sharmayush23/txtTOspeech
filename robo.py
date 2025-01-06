import pyttsx3

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties, if needed (optional)
    engine.setProperty('rate', 15)  # Speed of speech

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
 
if __name__ == "__main__":
    # Get input from the user
   
   while True:
    text_input = input("Enter the word or phrase you want the robo speaker to say: ")
    if (text_input=='q'):
     break
        
    text_to_speech(text_input)
    # Call the function to convert text to speech
    
