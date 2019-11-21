from django.shortcuts import render
from django.http import HttpResponse
from sodapy import Socrata
from .credentials import APPTOKEN, USERNAME, PASSWORD

LIMIT = 50       # Total number of records to request from the API
# Create your views here.
def index(request):
    client = Socrata('data.princegeorgescountymd.gov',
                      APPTOKEN,
                      USERNAME,
                      PASSWORD)
    results = client.get("364y-gm2b", limit=LIMIT)  # 2017 Data

    return render(request, 'index.html', {'data': results})


def blog(request):
    return HttpResponse("Cool blog brah,")
