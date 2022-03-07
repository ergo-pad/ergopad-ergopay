# ergopad-ergopay
1. Build fat.jar: `docker compose -f docker-compose-sbt.yml up -d`
<pre>
/app> ./build-fat-jar.sh
/app> copy file target/scala-*.jar to /app/jars/fat.jar
</pre>
2. Start the ergopay docker: `docker compose up -d`
3. Test the build with: `python`
<pre>
import jpype
import jpype.imports
from jpype.types import *
from jpype import JImplements, JOverride

jpype.startJVM()
jpype.addClassPath('jars/*')

import java.lang
from org.ergoplatform.appkit import Address
from java.math import BigInteger
</pre>
