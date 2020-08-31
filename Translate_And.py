from gtts import gTTS

my_text = "Are you ready to kickstands your  Advanced NLP course? Are you ready to " \
          "deploy your machine learning models in production at AWS? You will learn " \
          "each and every steps on how to " \
          "build and deploy your ML model on a robust and secure server at AWS."
language = 'en'
output = gTTS(text=my_text, lang=language, slow=False)
output.save('english.mp3')
