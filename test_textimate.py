from textimate import extract_text_from_image, recognize_speech_from_audio, translate_text

# Provide the correct path to the image
image_text = extract_text_from_image(r"D:\Projects\text recgonizaiton.png")
print("Extracted text:", image_text)

# Provide the correct path to the audio file
speech_text = recognize_speech_from_audio(r"D:\Projects\harvard.wav")
print("Recognized speech:", speech_text)

# Translate text from French to English
translated_text = translate_text("Bonjour", 'en')
print("Translated text:", translated_text)
