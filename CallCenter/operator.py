from call_center import CallCenter
from call_class import Call

# We create the call instances
call1 = Call('Vitalie', 2063355088, 1900, "request for sevice upgrade")
call2 = Call('Diana', 2533299958, 1930, "cancel service")
call3 = Call('Galina', 2536668888, 1945, "initiate service")
call4 = Call('Nicolae', 2064441111, 2000, "customer complaint")
# ~~~~~~~+++++++~~~~~~~~=======~~~~~~~~+++++++~~~~~~~~~

center1 = CallCenter()
center1.add(call2).add(call3).add(call1).add(call4).info()
print  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
center1.sort()
center1.info()
# center1.remove()
# center1.info()
print  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
center1.ninja_remove(253666888)