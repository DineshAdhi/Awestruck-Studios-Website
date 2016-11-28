from django.shortcuts import render, HttpResponse
import graphAPI

access_token="EAAYI9ZC7sTLABAE81X8ATJtSEpei5y2n6Sn0K3T8aqJotxWOPpTIHKHNaLcj9KzhUdRZCA3ePyTjZChGs2LHyQdZAOD0IBPuDDIx6heiidiEdsYbLju4NdJfN0eIySUGc8in109sH5eZBtZBJNiNx5g2E1vgvLjlUZD";

def index(request):
    return render(request, 'templates/index.html',{'nbar':'aboutus'})

def ourworks(request):
    return render(request, 'templates/ourworks.html',{'nbar':'ourworks','urls':getURL()});


def getURL():
    urls=[];
    graph = graphAPI.api('awestruckcrew/posts', access_token)
    urls=graph.request('full_picture')
    print urls;
    return urls;
