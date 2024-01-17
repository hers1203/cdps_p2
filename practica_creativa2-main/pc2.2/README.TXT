1.) CONSTRUIMOS LA IMAGEN A PARTIR DEL DOCKERFILE
docker build -t grupo5/productpage .
2.) EJECUTAMOS EL CONTENEDOR A PARTIR DE LA IMAGEN 
docker run -p 9080:9080 -e "GROUP_NUMBER=grupo5" --name grupo5-productpage grupo5/productpage
