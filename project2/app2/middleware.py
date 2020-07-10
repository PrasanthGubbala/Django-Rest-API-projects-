import requests
import json
from project2.settings import COVID_19_FILE
#import app2

class Covid19Middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        covid_19()

    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        return response

def covid_19():
        response = requests.get('https://api.covid19india.org/state_district_wise.json')
        # print(response.status_code)
        dict_data = json.loads(response.text)
        json.dump(dict_data, open(COVID_19_FILE, 'w'))