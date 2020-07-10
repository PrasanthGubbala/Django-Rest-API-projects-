from django.shortcuts import render
from project2.settings import COVID_19_FILE
from app2.middleware import covid_19
import json

def covid19_indian_data(request):
    str_data = open(COVID_19_FILE,'r').read()
    dict_data = json.loads(str_data)
    list_data = [x for x in dict_data]
    list_data.pop(0)
    return render(request,'covid19_indian_data.html',{'data':list_data})


def districts_data(request):
    state = request.GET.get('districts_data')
    str_data = open(COVID_19_FILE, 'r').read()
    dict_data = json.loads(str_data) 
    state_data = dict_data[state]
    return render(request,'covid19_states_data.html',{'state_name':state,'state':state_data})


def refresh(request):
    covid_19()
    sname = request.GET.get("state_name")
    dict_data = json.loads(open(COVID_19_FILE).read())
    return render(request, "covid19_states_data.html", {"state_name": sname, "state": dict_data[sname]})
