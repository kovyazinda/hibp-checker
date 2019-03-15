import requests
import json
import csv
import sys
import time

url = 'https://haveibeenpwned.com/api/v2/breachedaccount/'

headers = requests.utils.default_headers()
headers.update({
        'User-Agent': 'HIBP-checker-python-v.0.1',
    })

#print(data_json)

inputfile = sys.argv[1]
outputfile = sys.argv[2]

if sys.argv[1] and sys.argv[2]:
 infile=open(inputfile,"r")
 outfile=open(outputfile,"w+")
 csvrecord = csv.writer(outfile, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
 headerarray=["Email","Title","BreachDate","Description","IsSensitive"]
 csvrecord.writerow(headerarray)

 for string in infile:

  target=url+string.rstrip()
  try:
   response = requests.get(target,headers=headers)
   print (target)
   print (response)
   print (response.text)

   data_json = json.loads(response.text)
   i=0
   for result in data_json:
    print (i)
    resulttitle=data_json[i]['Title']
    resultbreachdate=data_json[i]['BreachDate']
    resultdescription=data_json[i]['Description']
    resultsensitivity=data_json[i]['IsSensitive']
    valuearr=[string,resulttitle,resultbreachdate,resultdescription.encode('ascii', 'ignore'),resultsensitivity]
    csvrecord.writerow(valuearr)
    time.sleep(5)
    i += 1


  except:
   print ("Query Error")

