import win32com.client

def change_voice(new_voice_name):
    engine = win32com.client.Dispatch("SAPI.SpVoice")
    voices = engine.GetVoices()
    
    # Find the desired voice by name
    desired_voice = None
    for voice in voices:
        if voice.GetDescription().lower() == new_voice_name.lower():
            desired_voice = voice
            break
    
    if desired_voice is not None:
        # Set the desired voice
        engine.Voice = desired_voice
        print(f"Changed voice to: {new_voice_name}")
    else:
        print(f"Voice '{new_voice_name}' not found.")

# Example usage
new_voice_name = "Microsoft David Desktop - English (United States)"
change_voice(new_voice_name)
