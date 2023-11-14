from googletrans import Translator

def traducir_ingles_espanol(texto):
    translator = Translator()
    return translator.translate(texto, src='en', dest='es').text