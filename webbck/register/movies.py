from requests.auth import HTTPBasicAuth
from django.http import HttpResponse
import requests

def func(request):

    x = requests.get('https://demo.credy.in/api/v1/maya/movies/', auth=HTTPBasicAuth('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0',
    'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'))
    #print(x.text)
   
    #print(lis)
    return HttpResponse(x.json()['results'][2])
    
