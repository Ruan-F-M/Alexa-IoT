print("testando")

import speech_recognition as sr

import os


#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #Usando o microfone
    with sr.Microphone() as source:

        #Chama um algoritmo de redução de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #Frase para o usuário dizer algo
        print("Diga alguma coisa:")

        #Armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:

        #Passa a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio,language='pt-BR')

        if "code" in frase:
            os.system("start idea64.exe")

        if "discord" in frase:
            os.system("start https://discord.com/channels/@me")

        if "Destiny" in frase:
            os.system("start steam://rungameid/1085660")

        elif "Warframe" in frase:
            os.system("start steam://rungameid/230410")


        #Retorna a frase pronunciada
        print("Você disse: " + frase)

    #Se não reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return frase

ouvir_microfone()
