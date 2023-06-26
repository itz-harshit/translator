import googletrans
import streamlit as st

# Getting list of available languages
langList = list(googletrans.LANGUAGES.keys())

# Initialising translator
translator = googletrans.Translator()

# Asking user to enter text for translation
input_lang = st.text_input('Enter text to translate', '')

# Defining lang_code
lang_code = st.selectbox('Select output language', langList)

# Basic Translate
if input_lang:
    results = translator.translate(input_lang, dest=lang_code)

    # Output result
    st.write(results.text)
    print(results.text)
