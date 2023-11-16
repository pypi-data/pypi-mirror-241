#!/usr/bin/env python3
import csv
from datetime import datetime
import argparse
from .api.client import Session, Connector
from .shared.configuration import getConfiguration


def writeResults(output, csv_list):
  header = ['id_ce', 'wsdl', 'id_e']

  with open(output, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(csv_list)

def check(env, output):
    config = getConfiguration()
    server = config[env]['server']
    user = config[env]['login']
    pwd = config[env]['password']
    session = Session(server,  user, pwd)
    #Check if session is valid
    if not session.valid:
        exit()

    #Get All iParapheur instances connectors
    request = Connector(session).getAll(scope='all', id_connecteur='iParapheur')
    if request.success:
      instances = request.result
      rows = []
      for instance in instances:
        id_ce = instance['id_ce']
        id_e = instance['id_e']
        request2 = Connector(session).detail(id_e=id_e, id_ce=id_ce)
        if request2.success:
          detail = request2.result
          if "iparapheur_wsdl" in detail["data"]:
            wsdl = detail["data"]["iparapheur_wsdl"]
            rows.append([id_ce, wsdl, id_e])

      writeResults(output,rows)







def script_wrapper():
  xstart = datetime.now()
  parser = argparse.ArgumentParser()
  parser.add_argument("-e", "--env", type=str, help="Selection de l'environnement", choices=['preprod','prod'], required=True)
  parser.add_argument("-o", "--output", type=str, help="Nom des fichiers exportes (csv + json)")
  args = parser.parse_args()
  check(env=args.env, output=args.output)
  xend = datetime.now()
  delta = xend - xstart
  msg = f"info : script execute en {delta.seconds // 60} minutes et {delta.seconds % 60} secondes"
  print(msg)

if __name__ == '__main__':
  script_wrapper()