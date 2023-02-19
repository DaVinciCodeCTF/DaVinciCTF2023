FROM tomcat:9.0

RUN apt update && apt install -y unzip

WORKDIR /tmp
RUN wget https://download.eclipse.org/birt/downloads/drops/R-R1-4.12.0-202211301856/birt-runtime-4.12.0-20221128.zip
RUN unzip -p birt-runtime-4.12.0-20221128.zip birt.war > /usr/local/tomcat/webapps/birt.war

EXPOSE 8080
