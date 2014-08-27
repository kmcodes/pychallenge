import urllib
import re

value=8022
match,n = 1,0
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
while match==1:
     toopen = url+str(value)
     print toopen
     webpage = urllib.urlopen(toopen)
     chaine = webpage.read()
     print chaine
     regexp = r"and the next nothing is [0-9]{1,}"
     regexp1 = r"[0-9]{1,}"
     result = re.search(regexp,chaine)
     result = re.search(regexp1,result.group(0))
     print result.group(0)
     value = result.group(0)
     if result:
          match = 1
     else:
          match = 0