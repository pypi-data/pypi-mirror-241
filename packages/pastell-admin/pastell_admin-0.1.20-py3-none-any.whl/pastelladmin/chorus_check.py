#!/usr/bin/env python3
import csv, re
from datetime import datetime
import argparse
from .api.client import Session, Connector
from .shared.configuration import getConfiguration


def writeResults(output, csv_list):
  header = ['id_ce', 'utilisateur']

  with open(output, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(csv_list)

def check(env, id_ce, output):
    config = getConfiguration()
    server = config[env]['server']
    user = config[env]['login']
    pwd = config[env]['password']
    #global_connector = '6926'
    session = Session(server,  user, pwd)
    #Check if session is valid
    if not session.valid:
        exit()

    #Get infos from Pastell global connector
    request = Connector(session).action(id_e='0', id_ce=id_ce, action='verification_connectivite')
    if request.result:
      html = request.result
      #with open("chorus.txt", "w") as text_file:
        #text_file.write(html)
      #with open("chorus.txt", "r") as text_file:
        #html = text_file.read()
      id_ce_lst = re.findall('(?<=id_ce\=)([0-9]*)', html)
      pre_user_lst = re.findall('(?<=Utilisateur ).*', html)
      user_lst = [u.split("<br/>")[0].replace("<br />", "") for u in (pre_user_lst)]
      assert len(id_ce_lst) == len(user_lst)
      rows = [[id_ce_lst[i], user_lst[i]] for i in range(len(id_ce_lst))]
      writeResults(output,rows)







def script_wrapper():
  xstart = datetime.now()
  parser = argparse.ArgumentParser()
  parser.add_argument("-e", "--env", type=str, help="Selection de l'environnement", choices=['preprod','prod'], required=True)
  parser.add_argument("-i", "--id_ce", type=str, help="Selection du connecteur global", required=True)
  parser.add_argument("-o", "--output", type=str, help="Nom des fichiers exportes (csv + json)")
  args = parser.parse_args()
  check(env=args.env, id_ce=args.id_ce, output=args.output)
  xend = datetime.now()
  delta = xend - xstart
  msg = f"info : script execute en {delta.seconds // 60} minutes et {delta.seconds % 60} secondes"
  print(msg)

if __name__ == '__main__':
  script_wrapper()