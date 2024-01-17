1)
git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
1*)
docker-compose rm -f -v 
 docker-compose  up --build --force-recreate --remove-orphans
2)
cd ./practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg/
3)**review service
docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
4)
docker-compose rm -f -v3
docker-compose --env-file variables/version1.env up --force-recreate --build
