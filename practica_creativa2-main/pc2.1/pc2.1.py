import os
import time
import sys
path=os.getcwd()
#borramos la practica_creativa2 si existiera
os.system("rm -rf ./practica_creativa2/")
#instalar PIP3
os.system('sudo apt-get install python3-pip')

#VARIABLE GLOBAR 
os.environ['GROUP_NUMBER']="Grupo50"

#clonar programa de github
os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git ")

#movernos al repo-productpage
os.chdir("./practica_creativa2/bookinfo/src/productpage")


#modificar libreria urllib3
fr=open("requirements.txt",'r')
fw=open("copia.txt",'w')
for line in fr:
    if("urllib3=" in line):
        fw.write("urllib3==1.24\n")
    else:
        fw.write(line)
fr.close()
fw.close()
os.system("rm -r requirements.txt")
os.system("mv copia.txt requirements.txt")

#instalamos requirements
os.system('sudo pip install -r requirements.txt')

#movernos a la carpeta templates
os.chdir("templates")
fr=open("productpage.html","r")
fw=open("copia.html",'w')
for line in fr:
    if('{% block title %}Simple Bookstore App{% endblock %}' in line):
        fw.write('{% block title %}'+os.environ['GROUP_NUMBER']+'{% endblock %}\n')
    else:
        fw.write(line)
os.system("mv copia.html productpage.html")
fr.close()
fw.close()

#movernos de vuelta a productpage
print(path)
os.chdir(str(path)+"/practica_creativa2/bookinfo/src/productpage")
os.system("python3 productpage_monolith.py 9080")

