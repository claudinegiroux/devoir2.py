# coding: utf-8

import csv, json, requests

fichier = "lobbyistes.csv"

url= "http://jhroy.ca/uqam/lobby.json"

entetes = {
    "User-Agent":"Claudine - Requête envoyée dans le cadre du cours de journalisme de données",
    "From":"claudine.giroux14@gmail.com"
    }

req = requests.get(url, headers=entetes)

print(req)

# n=0
# a=list(range(0,72000))

#j'ai essayé de faire un range pour être capable de jouer dans tout le fichier, sans succès


if req.status_code != 200:
    print("Ça ne fonctionne pas!")

else:
    # for n in range(0,72000):
    lobby= req.json()
    #     # print(registre)
    #     print(lobby["registre"][0][0]["comlog_id"])
    #     print(lobby["registre"][0][0]["fr_client_org_corp_nm"])
    #     print(lobby["registre"][0][0]["en_client_org_corp_nm"])
    #     print(lobby["registre"][0][0]["date_comm"])
    #     print(lobby["registre"][0][1][1]["objet"])
    #     print(lobby["registre"][0][1][1]["objet_autre"])
    #     print(lobby["registre"][0][2][0]["institution"])
    #J'ai essayé d'aller chercher individuellement chaque donnée de chaque ligne, mais avec cette méthode, je n'arrivais pas à aller dans tout le registre.
    #lobbies =0
    for chacun in lobby["registre"]:
        info=[]
        nomfr=chacun[0]["fr_client_org_corp_nm"]
        nomang= chacun[0]["en_client_org_corp_nm"]
        comlog =chacun [0]["comlog_id"]
        date = chacun[0]["date_comm"]
        objet1=chacun[1][0]["objet"] ### COMME PLUSIEURS AUTRES, TU NE RECUEILLES ICI QUE LE PREMIER DE PLUSIEURS SUJETS POSSIBLES DANS UNE MÊME COMMUNICATION DE LOBBYING. ET SI LE CLIMAT EST MENTIONNÉ AU 3E OU 4E SUJET? TU L'"ÉCHAPPES"
        objet2 =chacun[1][0]["objet_autre"]
        institution=chacun[2][0]["institution"]

        info.append(nomfr)
        info.append(nomang)
        info.append(comlog)
        info.append(date)
        info.append(objet1)
        info.append(objet2)
        info.append(institution)

        # print(info)
        n=0
        if "limat" in objet1 or "limat" in objet2:
            n+=1
            print(info)

            dead=open(fichier,"a")
            obies= csv.writer(dead)
            obies.writerow(info)
