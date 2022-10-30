import requests
import json 
import re

port = 80
dest = 'localhost'

txt1 = 'http:/{endpoint}:{p}'.format(endpoint = dest, p = port)
request = requests.get(txt1)
print(request)


dic = requests.headers
dic = str(dic)
print(dic)


server = re.findall("'Server:' '([a-zA-Z0-9)\/\.{1,}]' ", dic)
print(server)


