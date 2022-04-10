import os,time
import base as assistante
import pyautogui
import threading
def lancement():
    with open("lancer","w") as f: f.write("False")
    file = open("information.txt","r") #Ouvre un fichier txt
    info =file.read() #Lire le fichier ouvert
    
    #Transformer le contenu du fichier en tableau
    #info.split() --> chaque saisir séparer d'un espace equivaut à une colonne du tableau
    info_list = info.split(';')
    
    #on appel la fonction principale avec les informations de l'utilisateur
    assistante.main(info_list)


#on verifie si c'esst la premiere fois qu'on lance le programme sur l'ordi
#en verifiant si le fichier information.txt existe
if (not os.path.exists("information.txt")) :
    intro = """Bienvenu ! Je suis Kyry votre assistante personnel . Je me lance pour la première fois sur votre ordinateur .
            je vais vous poser quelques questions avant de commencer !"""

    assistante.voice(intro)
   
    threading.Thread(target=lambda :assistante.voice("quel est votre nom s'il vous plait ?")).start()
    
    nom=pyautogui.prompt(text='votre nom ?', title='information' , default='')
    while(not nom) : nom=pyautogui.prompt(text='votre nom ?', title='information' , default='')
    #time.sleep(2)

    assistante.voice("vous êtes un homme, ou une femme ?")
    genre = pyautogui.confirm(text='vous êtes un homme ou une femme ?', title='Information', buttons=['Homme', 'Femme'])
    while(not genre) : genre = pyautogui.confirm(text='vous êtes un homme ou une femme ?', title='Information', buttons=['Homme', 'Femme'])
    #time.sleep(2)
    """
    #Tant que le genre est différent de H ou F Réécrire le genre
    while(genre != "H") or (genre != "F"):
        genre=input("H ou F :")
        
        #genre.upper() permet de convertir la saisie en majuscule / genre.lower() permet de convertir la saisie en miniscule
        #Si le genre est H ou F: Arreter la boucle
        
        if genre.upper() == "H":
            break
        elif genre.upper() == "F":
            break
        else:print("ATTENTION !! Vous vous êtes trompé de caractère.")
    """
       
 
    assistante.voice("quel est votre email ?")
    email=pyautogui.prompt(text='votre email ?', title='information' , default='')
    while(not email and "@" not in email or "." not in email) : email=pyautogui.prompt(text='votre mail ?', title='information' , default='')
   
    #time.sleep(2)
    #Rééssayer jusqu'a inscrit un entier, si c'est un entier bon est vrai
    assistante.voice("Donnez moi votre numero de telephone !")
    num = pyautogui.prompt(text='votre numero ?', title='information' , default='')
    while(not num or not num.isdigit()) : num=pyautogui.prompt(text='entrer un bon numero ?', title='information' , default='')
    time.sleep(2)
    """bon = False
    while(not bon):
        try:
            num= int(input("Entrez votre numero de telephone > "))
            bon = True
        except :
            bon = False
    """

    threading.Thread(target=lambda :assistante.voice("à présent,   parmis les programmes afficher,  selectionnez ceux que vous voulez voir lancer  au démarrage de l'ordinateur . 3 choix possible .!")).start()
    choix = 0
    liste_des_programmes_a_choisir = ["Google Chrome","Edge","Bloc-Note","Explorateur de fichier","IDLE","Visual Studio Code","invite de commande"]
    liste_des_programmes_au_demarrage =[]

    while(choix<3):
        prg = pyautogui.confirm(text='programme à lancer au demarrage\nvotre choix ( 3 posible) ?', title='Information', buttons=liste_des_programmes_a_choisir)
        choix+=1
        liste_des_programmes_au_demarrage.append(prg)
        liste_des_programmes_a_choisir.remove(prg)
        
    #Ouvre le fichier txt et écrit les informations ("w" qui signifie write) 
    with open("information.txt","w") as file : file.write(nom + ";" + genre + ";" + email + ";" + str(num)+";"+str(liste_des_programmes_au_demarrage))
    time.sleep(2)
   
    assistante.voice("merci "+nom+" pour les info !")
    lancement()
    
else:
    
    lancement()




    

