# Createur < Doc.Shaka >
# -*- coding: utf-8 -*-

# Importation librairy

import faker
import random
from faker import Faker
from faker_wifi_essid import WifiESSID
from faker_web import WebProvider
from colorama import Back, Fore, Style, deinit, init
import webbrowser
from art import *
from termcolor import colored
from tqdm import tqdm

# Ascii Art

print (colored(text2art ("\t______________________\n"),'yellow')) 
print (colored(text2art ("\t_______S.M.D.P.H________"),'red'))
print (colored(text2art ("\t______________________"),'yellow')) 

# Code Pure

print ()
print(Fore.GREEN + Style.NORMAL + "S.M.D.P.H:> Entrez votre pseudo pour vous identifié sur le system ")

def main():

    # Variables et source

    fake = Faker(locale="fr_FR")
    fake1 = Faker(['it_IT', 'en_US', "fr_FR"])
    typecb = ["MasteCard World Elite","Visa Infinite","Visa Premier","Gold MasterCard","Black MasterCard","Visa Classique","Mastercard Classique","CB Prépayée","Carte de Crédit","Carte de Paiement","Carte de Retrait","Visa Electron"]
    typecc = random.choice(typecb)
    fake.add_provider(WifiESSID)
    fake.add_provider(WebProvider)

    # Code 
    print ()
    name = input("S.M.D.P.H:> ")
    print ()
    print ("S.M.D.P.H:> Bonjour et bienvenue ", name, ",vous êtes bien authentifié sur le Stockage Modiale de Donnée Personnelle Hacké")
    print ()
    print (name, ",Voulez vous faire une recherche aléatoire ou sortir du sytem S.M.D.P.H ? [o/n]")
    print ()
    choice = input("S.M.D.P.H:> ")
    if choice == "o":
        print ()
        print ("S.M.D.P.H:> ", name, ",Je recherche une correspondance dans nos bases de données")
        print ()
        for i in tqdm(range(100000000)): # Range = durée de chargement
            pass     
        print ()
        print ("S.M.D.P.H:> ", name, ",Nous vous affichons les données correspondantes collectés")
        print ()
        print ("S.M.D.P.H:> Nom & prénom : " ,"[", fake1.name(), "]")
        print ("S.M.D.P.H:> date de naissance : ","[", fake1.date(), "]")
        print ("S.M.D.P.H:> Job : " ,"[", fake1.job(), "]")
        print ("S.M.D.P.H:> société : ","[", fake1.company(), "]" )
        print ("S.M.D.P.H:> Adresse : " ,"[", fake1.address(), "]")
        print ("S.M.D.P.H:> numéro de telephone : " ,"[", fake.phone_number(), "]")
        print ("S.M.D.P.H:> Pseudo mail : ","[", fake1.user_name(), "]" ," et l'@: ", "[", fake1.email(), "]", " ainsi que le password du @: ", "[", fake1.password(), "]",)
        print ("S.M.D.P.H:> Numéro de sécurité social : " ,"[" ,fake.ssn(), "]",)
        print ("S.M.D.P.H:> Information compléte de la CB : " ,"[" ,fake.credit_card_number(), "]", "[", fake.credit_card_expire(), "]", "[", fake.credit_card_security_code(), "]", "[", typecc, "]")
        print ("S.M.D.P.H:> path du persistant vidéo: " ,"[" ,fake.file_path(depth=3, category='video'), "]")
        print ("S.M.D.P.H:> Date de post du persistant actif : " ,"[" ,fake.date_time(), "]")
        print ("S.M.D.P.H:> I.P.V 4 de la machine :" ,"[" ,fake.ipv4_private(), "]")
        print ("S.M.D.P.H:> Nom du wifi : ","[" ,fake.user_name(), "]", "& le password wifi : ", "[", fake.wifi_essid(), "]")
        print ("S.M.D.P.H:> Website personelle : ", "[", fake.url(), "]")
        print ("S.M.D.P.H:> Host Name : ", "[", fake.hostname(), "]")
        print ("S.M.D.P.H:> Path website : ", "[", fake.uri_path(), "]")
        print ("S.M.D.P.H:> Request méthode website : ", "[", fake.http_method(), "]")
        print ("S.M.D.P.H:> Exploreur web & OS : " , "[", fake.user_agent(), "]")
        print () 
        print (name, ",Voulez vous que le system S.M.D.P.H pénêtre la cible grâce aux données collecté pour vous  ? [o/n]")
        print ()
        choice1 = input("S.M.D.P.H:> ")
        print ()
        if choice1 == 'o':         
            webbrowser.open('https://www.youtube.com/watch?v=SjHUb7NSrNk&ab_channel=Grayhyaena') 
            print ()       
        elif choice1 == 'n':           
            print ()
            print ("S.M.D.P.H:> ", name, ",Nous vous déconnectons du system S.M.D.P.H")
            print ()
            for i in tqdm(range(100000000)): # Range = durée de chargement
                pass
            print ()                    
            print("S.M.D.P.H:> ", name, ",dsl mais vous êtes rester conecté trop longtemps . Nous avons detecté une unité de cybercriminalité qui vient a votre domicile")
            print ()
            print("S.M.D.P.H:> ", name, ",nous vous deconnectons de S.M.D.P.H et effacons vos trace dans nos base de données de connexion ; bonne chance")
            webbrowser.open('https://www.youtube.com/watch?v=yZPm7Oxn2x4&ab_channel=AnalyseActu')
            print ()  
    elif choice == 'n':           
        print ()
        print ("S.M.D.P.H:> ", name, ",Nous vous déconnectons du system S.M.D.P.H")
        print ()
        for i in tqdm(range(100000000)): # Range = durée de chargement
                pass
        print ()                    
        print("S.M.D.P.H:> ", name, ",dsl mais vous êtes rester conecté trop longtemps . Nous avons detecté une unité de cybercriminalité qui vient a votre domicile")
        print ()
        print("S.M.D.P.H:> ", name, ",nous vous deconnectons de S.M.D.P.H et effacons vos trace dans nos base de données de connexion ; bonne chance")
        webbrowser.open('https://www.youtube.com/watch?v=qz-O8XmpuoI&ab_channel=Markyun')
        print ()
main()
