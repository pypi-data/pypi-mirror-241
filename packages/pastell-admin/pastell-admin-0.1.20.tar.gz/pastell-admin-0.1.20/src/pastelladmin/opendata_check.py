#!/usr/bin/env python3
import json, csv, re
from datetime import datetime, timedelta
import argparse
import requests
from .api.client import Session, Stat, Document, Entity
from .shared.configuration import getConfiguration

def getStats(session, org=None):
  stats = False
  #Get stats from Pastell API. If ORG is None get all stats
  request = Stat(session).get(id_e=org)
  if request.success:
    stats = request.result
  return stats

def writeResults(output, csv_list):
  header = ['siren', 'id_e', 'id_d', 'date_action', 'acte_nature', 'analyse', 'publication_opendata','titre', 'lien_pastell', 'unvalid_date']

  with open(output, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(csv_list)

def check(env, output, compare_key, days, org=None, rejeu=False):
    config = getConfiguration()
    csv_list = []
    docs_error = []
    server = config[env]['server']
    user = config[env]['login']
    pwd = config[env]['password']
    dossier = 'ged-megalis-opendata'
    session = Session(server,  user, pwd)
    date = (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")
    #Check if session is valid
    if not session.valid:
        exit()
    if not org:
        entities = Entity(session).getAll().result
        #Sort entities by id_e ASC
        entities = sorted(entities, key=lambda x:int(x['id_e']))
    else:
        entities = [{"id_e": org }]
    #Get stats from Pastell API
    stats_entites_json = getStats(session, org)
    for entity in entities:
        id_e = entity["id_e"]
        if id_e in stats_entites_json and stats_entites_json[id_e]['flux'][dossier]:
            siren = stats_entites_json[id_e]['info']['siren']
            #print (f"{siren} - {id_e}")
            docs = Document(session).getByFilter(id_e, dossier,status="termine", start=date).result
            if len(docs) > 0:
                if env == 'preprod':
                    check_url = f'https://data-api-preprod.megalis.bretagne.bzh/private_api/v1/publication/search/light?pageIndex=0&pageSize=1000'
                    pastell_url = 'https://pastell-preprod.megalis.bretagne.bzh'
                    rejeu_url = 'https://data-api-preprod.megalis.bretagne.bzh/private_api/v1/pastell/rejeu_doc'
                    API_TOKEN = '15KVVNHu2ixEtK8F7gKA'
                elif env == 'prod':
                    check_url = f'https://data-api.megalis.bretagne.bzh/private_api/v1/publication/search/light?pageIndex=0&pageSize=1000'
                    pastell_url = 'https://pastell.megalis.bretagne.bzh'
                    rejeu_url = 'https://data-api.megalis.bretagne.bzh/private_api/v1/pastell/rejeu_doc'
                    API_TOKEN = 'QgyKkjsWLVHG8iKd7xcQrJEVEYEpUKJEPk6NZTtN'
                pub_request = requests.post(check_url,data={"siren": siren})
                registre1 = []
                registre2 = []
                if pub_request.status_code == 200:
                    publications = json.loads(pub_request.text)
                    if len(publications["publications"]) > 0:
                        for publication in publications["publications"]:
                            # store key in array
                            if compare_key == 'id_d':
                                registre1.append(publication['pastell_id_d'])
                            elif compare_key == 'numero_de_lacte':
                                registre1.append(publication[compare_key])
                            elif compare_key == 'objet':
                                registre1.append(publication[compare_key])
                                registre2.append(publication['numero_de_lacte'])

                if len(publications["publications"]) > 0 and len(docs) > 0:
                    for doc in docs:
                        id_d = doc["id_d"]
                        titre = doc["titre"]
                        date_action = doc["last_action_date"]
                        acte_nature = "?"
                        if compare_key == 'numero_de_lacte':
                            detail = Document(session).detail(id_e, doc["id_d"]).result
                            key = detail["data"]["numero_de_lacte"]
                        elif compare_key == 'id_d':
                            key = id_d
                        else:
                            key = titre
                        analyse = compare_key
                        publication_opendata = key in registre1
                        #Check with numero_de_lacte if false
                        if not publication_opendata and (compare_key == 'objet' or compare_key == 'id_d'):
                            detail = Document(session).detail(id_e, doc["id_d"]).result
                            key = detail["data"]["numero_de_lacte"]
                            acte_nature = detail["data"]["acte_nature"]
                            date_acte = detail["data"]["date_de_lacte"]
                            #check date format
                            valid_date = re.search('^\d{4}-?\d{2}-?\d{2}$', date_acte)
                            publication_opendata = key in registre2
                            analyse += "/numero_de_lacte"
                        doc_link = None
                        unvalid_date = False
                        if not publication_opendata:
                            unvalid_date = (valid_date == None)
                            docs_error.append({'id_d': id_d, 'unvalid_date': unvalid_date })
                            doc_link = f"{pastell_url}/Document/detail?id_d={id_d}&id_e={id_e}"
                            print (f"warning: document {id_d} non publie : {titre} - (entite  {id_e}) - bug date : {unvalid_date}")
                        raw = [siren, id_e, id_d, date_action, acte_nature, analyse, publication_opendata, titre, doc_link, unvalid_date]
                        csv_list.append(raw)
                    writeResults(output,csv_list)
    if rejeu:
        for doc in docs_error:
            if doc['unvalid_date'] == False:
                idd = doc['id_d']
                rejeu_request = requests.post(f"{rejeu_url}?id_d={idd}", headers={'x-access-tokens': API_TOKEN})
                print(f"info: retour rejeu de {idd} :  {rejeu_request.text}")





def script_wrapper():
  xstart = datetime.now()
  parser = argparse.ArgumentParser()
  parser.add_argument("-e", "--env", type=str, help="Selection de l'environnement", choices=['preprod','prod'], required=True)
  parser.add_argument("-o", "--output", type=str, help="Nom des fichiers exportes (csv + json)")
  parser.add_argument("-g", "--org", type=str, help="Selection de l'entite")
  parser.add_argument("-d", "--days", type=int, help="Anteriorite des documents en jours")
  parser.add_argument("-k", "--key", type=str, help="Selection de la cle de comparaison", choices=['objet', 'numero_de_lacte', 'id_d'])
  parser.add_argument("-r", "--rejeu", help="Flag Rejeu de la publication en cas d erreur", action='store_true')
  args = parser.parse_args()
  check(env=args.env, org=args.org, output=args.output, compare_key=args.key, days=args.days, rejeu=args.rejeu)
  xend = datetime.now()
  delta = xend - xstart
  msg = f"info : script execute en {delta.seconds // 60} minutes et {delta.seconds % 60} secondes"
  print(msg)

if __name__ == '__main__':
  script_wrapper()