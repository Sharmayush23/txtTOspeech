import pyttsx3

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties, if needed (optional)
    engine.setProperty('rate', 10)  # Speed of speech

    # Convert the text to speech
    engine.say(text)

    # Save the speech to an audio file
    engine.save_to_file(text, 'output_audio.mp3')

    # Wait for the speech to finish
    engine.runAndWait()
 
if __name__ == "__main__":
    # Get input from the user
    
    while True:
        text_input = input("Enter the word or phrase you want the robo speaker to say: ")
        if text_input == 'q':
            break
        text_to_speech(text_input)
    
