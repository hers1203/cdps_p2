
FROM ubuntu:20.04
RUN apt-get update
RUN apt-get -y install python3-pip 
RUN apt-get -y install python3 

RUN apt-get -y install git 
ENV GROUP_NUMBER Grupo50

WORKDIR /
RUN git clone  https://github.com/CDPS-ETSIT/practica_creativa2.git
#RUN SED PARA MODIFICAR LOS FICHEROS
WORKDIR /practica_creativa2/bookinfo/src/productpage
RUN sed -i 's/urllib3==1.26.5/urllib3==1.24/g' requirements.txt 
RUN cat requirements.txt 
WORKDIR /practica_creativa2/bookinfo/src/productpage/templates
RUN sed -i "s/Simple Bookstore App/$GROUP_NUMBER/g" productpage.html
RUN cat productpage.html
WORKDIR /practica_creativa2/bookinfo/src/productpage
RUN pip3 install -r requirements.txt 
EXPOSE 9080
CMD ["python3","/practica_creativa2/bookinfo/src/productpage/productpage_monolith.py","9080"]

