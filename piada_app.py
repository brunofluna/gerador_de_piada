# importando bibliotecas
import pyjokes
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='auto', target='pt')

while True:
    piada = pyjokes.get_joke()
    piada_traduzida = tradutor.translate(piada, target='pt')
    print(piada_traduzida)

    repetir = input('Gerar outra piada (S/N)? ').lower()

    if repetir == 's':
        continue
    else: 
        break