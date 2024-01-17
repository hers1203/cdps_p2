import os
import sys
import time
#creacion del archivo de variables de entorno
r=os.getcwd()
#mkdir variables
os.chdir(r)
os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")
#mkdir variables
os.system("mkdir variables")
#cd variables 
os.chdir(r+"/variables/")
if os.path.isfile(r+'/variables/version1.env'):
    print('//----Los archivos de variables de entorno ya existen');
else:
    print('//----Los archivos de variables de entorno no existen');
    os.system('echo "SERVICE_VERSION=v1" >> version1.env')
    os.system('echo "ENABLE_RATINGS=false" >> version1.env')
    # os.system('echo STAR_COLOR=red >> version1.env')

    os.system('echo "SERVICE_VERSION=v2" >> version2.env')
    os.system('echo "ENABLE_RATINGS=true" >> version2.env')
    os.system('echo "STAR_COLOR=black" >> version2.env')

    os.system('echo "SERVICE_VERSION=v3" >> version3.env')
    os.system('echo "ENABLE_RATINGS=true" >> version3.env')
    os.system('echo "STAR_COLOR=red" >> version3.env')   


os.chdir(r)

os.chdir(r+"/practica_creativa2/bookinfo/src/reviews/")
os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
# time.sleep(11)
os.chdir(r)
os.system('sudo docker-compose build')
# time.sleep(4)
os.system('sudo docker-compose --env-file variables/'+str(sys.argv[1])+'.env up --remove-orphans ')





