git clone https://github.com/ergoplatform/ergo-appkit.git 
cd ergo-appkit 

sbt publishLocal 

sbt clean assembly 

cp -R target/scala-*.jar jars
