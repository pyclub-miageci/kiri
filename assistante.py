from boule_ui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random,time, pyautogui
import threading,sys,wikipedia
#import wikipedia
import webbrowser,pyautogui as p
import locale,pyttsx3
import speech_recognition as sr
import os, pyautogui as p
#from deep_translator import GoogleTranslator
locale.setlocale(locale.LC_TIME,'FR')
r = sr.Recognizer()
engine = pyttsx3.init()
sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**27)  # new thread will get stack of such size

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        MainWindow.setGeometry(self,15, 25, 94, 81)
        MainWindow.setWindowFlags(self,
                             QtCore.Qt.WindowStaysOnTopHint
                             | QtCore.Qt.FramelessWindowHint
                             | QtCore.Qt.Tool)
        MainWindow.setAttribute(self,QtCore.Qt.WA_TranslucentBackground)
        self.time = 160
        self.ui.attente = self.time 
        
        self.stop = False
        self.thread1=threading.Thread(target=lambda : self.main())
        self.thread1.start()
        
        self.thread2=threading.Thread(target=lambda : self.time_stop())
        self.thread2.start()
        self.init()
        username = os.getlogin()    # Fetch username
        self.base_folder = f'C:\\Users\\{username}\\'
              
        #self.ui.label.installEventFilter(self)
    def init(self):
        with open("lancer","w") as f: f.write("True")
        self.ui.label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border : 0px solid #fff;\n"
"border-radius : 25%;")
        #while (self.thread2.is_alive()): print("g")
        
    def talk(self,text):
        engine.setProperty("rate",150)
        engine.say(text)
        engine.runAndWait()
        if engine._inLoop:engine.endLoop()   # add this line
        engine.stop()
        """print(text)"""

    def time_stop(self):
        #print(self.ui.attente)
        while self.ui.attente>0 and not self.stop:
             time.sleep(1)
             self.ui.attente-=1
             print(self.ui.attente)
        #self.thread1.join()
        self.stop = True
        with open("lancer","w") as f: f.write("False")
        self.close()
    """def mousePressEvent(self, event):
        print(event)
        self.close()"""
    def eventFilter(self, object, event):
        print(event.type())
        if event.type() == QEvent.MouseButtonPress :
            try:
                self.close()
                print("pfff")
            except Exception as e : print(e)
        if event.type() == QEvent.Enter:
            print("Mouse is over the label")
            self.stop = True
            print('program stop is', self.stop)
            return True
        elif event.type() == QEvent.Leave:
            print("Mouse is not over the label")
            self.stop = False
            print('program stop is', self.stop)
        return False

        
    def close(self):
        
        ui.hide()
        
        #while (self.thread1.is_alive()): pass
        ui.close()
    def closeEvent(self,event):
        
        self.stop = True
        print(event)
        event.accept()
        return 1
    def main(self):
        while True and not self.stop:
            print("lo")
            with sr.Microphone() as source:
                if self.stop == True : break
                try:
                        print("j'ecoute")
                        self.ui.label.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                        "border : 0px solid #fff;\n"
                        "border-radius : 25%;")
                        r.adjust_for_ambient_noise(source, duration=0.5)
                        audio = r.listen(source)                                                                #Permet de comprendre la source
                        self.ui.label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                "border : 0px solid #fff;\n"
                                "border-radius : 25%;")
                        command = r.recognize_google(audio,language="fr-FR")                                    #Recherche dans le dictionnaire nos dits
                        command = command.lower()                                                               #Réécrire en miniscule nos dits pour la comprehension (Youtube != youtube)
                        print("WW > "+command)
                        self.execute(command)
                        
                except Exception as e:
                            print(e)
        print("main kill")
    def jeu(self):
        #Nombre gagnant
        nbre_win = random.randrange(1,250)
        #Nbre d'essai
        nbre_essai = 0
        essai_max = 6
        while nbre_essai!=essai_max:
            jeu=p.prompt(text="Le jeu consiste à trouver le nombre gagnant entre 1 et 250.\nVous aviez droit à 6 chances",title="Game",default="")
            print(jeu)
            jeu=int(jeu)
            nbre_essai=nbre_essai+1
            if jeu==nbre_win:
                win=p.alert(text="FELICITATION!!! Vous avez gagné",title='Game')
            else:
                if nbre_essai == essai_max:
                    egal=p.alert(text="OUPSSS!!! Vous avez perdu",title="Game")
                    break
                elif nbre_essai == 3:
                    egal=p.alert(text="ATTENTION!!! Il vous reste trois chances .....",title="Game")
                if jeu < nbre_win:
                    inf=p.alert(text=("ATTENTION!!!!!", jeu, "< au nombre gagnant, Chercher plus haut...."),title="Game")
                else:
                    sup=p.alert(text=("ATTENTION!!!!!", jeu, "> au nombre gagnant, Chercher plus bas...."),title="Game")

        vict=p.alert(text=("Le nombre gagnant est:",nbre_win),title="Game")



    def execute(self,command):
        self.ui.attente = self.time
        
        if "ça va" in command or "comment tu va" in command:
            self.talk("je vais bien, j'espère que vous allez bien de même ")                                                             #Si "ca va" est dans tes dits, repondre "oui et toi"
        elif "capture d'écran" in command:
            screen = pyautogui.screenshot()                                                 #Bouton qui permet de faire les captures d'écran
            screen.save(self.base_folder+"Desktop\\capture.jpg")                                                          #Enreigistrer avec ce nom
            self.talk("La capture d'écran a été faite, et est situé sur ton bureau")
        elif 'wikipedia' in command or 'Wikipédia' in command or 'wikipédia' in command:
            self.talk('recherche Wikipedia en cour...')
            statement = command
            statement =statement.lower().replace("recherche sur wikipédia", "")
            statement =statement.lower().replace("recherche wikipédia", "")
            statement =statement.lower().replace("wikipédia", "")
            statement =statement.lower().replace("wikipedia", "")
            wikipedia.set_lang("fr")
            results = wikipedia.summary(statement, sentences=3)
            self.talk("d'après wikipedia : ")
            print(results)
            self.talk(results)

        elif 'cherche sur youtube'  in command or 'recherche youtube'  in command or 'recherche sur youtube'  in command:
                statement = command
                statement = statement.command("recherche youtube", "")
                statement = statement.replace("cherche sur youtube", "")
                statement = statement.replace("recherche sur youtube", "")
                webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+statement)
        elif 'cherche'  in command or 'recherche'  in command:
                statement = command
                statement = statement.replace("recherche sur google", "")
                statement = statement.replace("recherche google", "")
                statement = statement.replace("recherche", "")
                webbrowser.open_new_tab("https://www.google.com/search?q="+statement)
                #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                #webbrowser.get(chrome_path).open(statement)
                #webbrowser.get(using='windows-default').open(statement,new=2)
                time.sleep(1)
                self.talk("recherche effectuée")
        elif 'open' in command or 'ouvre' in command or 'ouvre l\'application' in command:
            
            command =command.lower().replace("ouvre l'aplication ", "")
            command =command.lower().replace("ouvre aplication ", "")
            command =command.lower().replace("ouvre ", "")
            print(command)
            if command =="google" or command =="youtube" or command =="gmail" :
                webbrowser.open_new_tab("https://www."+command+".com")
                time.sleep(2)
            else :
                self.prog(command)
            self.talk(command+" est ouvert")
            
        elif 'qui es-tu' in command or 'qui es tu' in command or 'que fais tu' in command or 'parle moi de toi' in command or 'parle-moi de toi' in command:
                self.talk("""Je suis Kyry votre assistante personnel. Je suis programmé pour des tâches mineures comme
                        ouvrir une application ou un site web , faire des rechercher sur wikipedia , google et youtube , vous pouvez également me poser diverses questions !""")


        elif "date" in command or "heure" in command: 
            date = time.strftime("%A, %d %B %Y")                                                #Récupère la date [%A:le jour de la semaine; %d:le jour; #%Y:L'année]
            print(date)
            self.talk("Nous sommes le:" + date)
            heure = time.strftime("%H:%M")                                                      #Récupère l'heure [%H:L'heure; %M:Les minutes]
            print(heure)
            self.talk("Et Il est actuellement: " + heure)
        elif "bonjour" in command :
            self.talk("j'espère que vous allez bien ... .que puis-je faire pour vous")
        elif "merci" in command :
            self.talk("je vous en prie ... .que puis-je faire")
            """elif "qui est" in command:
            person = command.replace("qui est", "")                                             #Recupère le nom
            wikipedia.set_lang("fr")                                                            #langue=FRANCAIS
            info = wikipedia.summary(person, 1)                                                 #Recherche la personne sur Wikipédia
            print(info)
            self.talk(info)"""
        elif "désactive toi" in command:
            self.talk("daccord je me desactive")
            self.stop=True
            with open("lancer","w") as f: f.write("False")
            
            ui.close()
            sys.exit()                                                                          #Permet de fermer le programme
            """elif "youtube" in command:
            self.talk("je recherche")
            key = command.replace("recherche sur youtube","")                                   #Recupère le nom à chercher
            webbrowser.open_new_tab("https://youtube.com/results?search_query="+key)            #Ouvre un nouvel onglet; l'addresse est le debut de la page de youtube et ajoute le nom recherché
        elif "google" in command:
            self.talk("je recherche")
            word = command.replace("recherche sur google","")
            webbrowser.open_new_tab("https://www.google.com/search?q="+word)"""
        elif ("traduction" or "traduit") in command:
            trad=p.prompt(text="Veuillez saisir le texte à traduire...",title="Translate")
            lang=p.confirm(text="Veuillez choisir la langue",title="Translate",buttons=["Français","Anglais","Espagnol","Allemand"])
            def language(lan):
                if lang=="Francais":
                    return "fr"
                elif lang=="Anglais":
                    return "en"
                elif lang=="Espagnol":
                    return "es"
                elif lang=="Allemand":
                    return "de"
            translate=GoogleTranslator(source="auto", target=language(lang)).translate(trad)
            self.talk("Veuillez patientez s'il vous plait")
            p.alert(text=('La traduction donne',translate),title="Translate")
        elif 'nouvelle' in command or 'actualité' in command or 'actualités' in command or 'nouvelles' in command:
                news = webbrowser.open_new_tab("https://www.lemonde.fr/cote-d-ivoire/")
                time.sleep(1)
                speak('Ici vous aurez les dernières nouvelles du pays')
                
        elif "jeu" in command:
            self.jeu()
            replay=p.confirm(text="Voulez vous rejouer?", title="Game", buttons=["Oui","Non"])
            while replay =="Oui":
                jeu()
                replay=p.confirm(text="Voulez vous rejouer?", title="Game", buttons=["Oui","Non"])
                if replay=="Non":
                    sys.exit()
                else:
                    self.talk("Désolé pourrais tu repété? je n'ai pas bien compris.")
        elif "test" in command :
                self.talk("je fonctionne, en quoi puis-je vous aider .")
        elif "je veux coder" in command:
                os.system("code")
        else:
            self.talk("Désolé pourrais tu repété? je n'ai pas bien compris.")
        

    def mousePressEvent(self, event):
        
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def prog(self,z):
        #pyautogui.click(150, 767)
        #pyautogui.click()
        p.hotkey("win")
        time.sleep(1.5)
        p.write(str(z), interval=0.15)
        p.press('enter')
        time.sleep(2)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
