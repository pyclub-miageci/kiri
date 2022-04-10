import psutil , time
import os , pyautogui as p
import pyttsx3,socket
import time
import base,sys, threading,os
from pynput.keyboard import Listener, Key
import webbrowser
import locale

filename = "key_log.txt"  # The file to write characters to
locale.setlocale(locale.LC_TIME,'FR')
engine = pyttsx3.init()
engine.setProperty("rate",150)


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def talk(text):
     threading.Thread(target=lambda :voice(text)).start()


def voice(text):
    if engine._inLoop:
        engine.endLoop()
    engine.say(text)
    
    engine.runAndWait()
    if engine._inLoop:
        engine.endLoop()   # add this line
    engine.stop()
    """print(text)"""

def lancer(programme_au_demarrage):
    
    #os.system("explorer.exe")
    
    for p in programme_au_demarrage :
        #time.sleep(2)
        prog(p)
    
def battery_info():
    battery = psutil.sensors_battery()
    return battery

def verif_pourcentage():
    
    battery = battery_info()
    if battery.percent <= 50:
        engine.say("Songer à brancher votre pc")
        engine.runAndWait()
    
       
def salutation():
    
    h = time.strftime("%H")
    if h < str(14):
        return "Bonjour"
    else:
        return "Bonsoir"

def prog(z):
    #pyautogui.click(150, 767)
    #pyautogui.click()
    p.hotkey("win")
    time.sleep(1.5)
    p.write(str(z), interval=0.15)
    p.press('enter')
    time.sleep(2)
def genre(genre):

    if genre.lower() == "homme" : return "Monsieur"
    elif genre.lower() == "femme" : return "Madame"
    else : return " "
def main(info):
    #salutation
    voice(salutation()+" "+genre(info[1])+" "+info[0]+" . Il est "+time.strftime("%H:%M")+" .")
    battery = battery_info() #on recupere les infos concernant la battery
    #lecture info battery
    voice("Le pourcentage de votre batterie est à : " + str(battery.percent) + " pourcent.")
    verif_pourcentage()
    voice("Je vous lance vos programmes de base, merci de patienter !")
    lancer(eval(info[4]))
    voice("En cas de besoin , touchez la touche magique")
    voice("Passez un bon moment sur votre ordinateur ! .")
    listen()


def lancer_assistante():
    
    if is_connected() :
        with open("lancer","r") as f : en_cours =eval(f.read())
        if(not en_cours):
            talk("Je me lance")
            threading.Thread(target=lambda :os.system("assistante.py")).start()
        else :
            print("deja en cours")
        """import sys
        app = QtWidgets.QApplication(sys.argv)
        ui = MainWindow()
        ui.show()
        sys.exit(app.exec_())"""
    else :
        voice("sans connexion je n'es pas d'energie, essayer de vous connecter avant ")
  
    print("gtrr")

with open(filename,"w") as f : f.write("")
def on_press(key):
    try:
        if hasattr(key, 'char'):  # Write the character pressed if available
            print(key.char)
            with open(filename,"a") as f : f.write(key.char)
            if key.char=="k":
               with open(filename,"r") as f :
                    ctn = f.read()
                    
                    if "altk" in  ctn:
                        print("lancelnn")
                        with open(filename,"w") as f : f.write("")
                        lancer_assistante()
                        
                    else :
                        with open(filename,"w") as f : f.write("")
      
        else:  # If anything else was pressed, write [<key_name>]
            print(key)
            if key== Key.alt_l :
                with open(filename,"a") as f :f.write('alt')
            #else :
            #with open(filename,"w") as f : f.write("")
            
    except Exception as e :
        print(e)
def listen():
    
    with Listener(on_press=on_press) as listener:  # Setup the listener
            listener.join()  # Join the thread to the main thread
    #time.sleep(0.01)




"""nom =input("nom")
main(nom)"""








