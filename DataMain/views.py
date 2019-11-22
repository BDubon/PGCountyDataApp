from django.shortcuts import render
from django.http import HttpResponse
from sodapy import Socrata
from .credentials import APPTOKEN, USERNAME, PASSWORD

LIMIT = 1    # Total number of records to request from the API


# Create your views here.
def index(request):
    """ Homepage view """
    context = {
        'title': 'Homepage',
        'section_one': 'Homepage Subtitle',
        'text': 'Sample text for the homepage',
        }

    return render(request, 'index.html', context)


def data(request):
    """ Secondary view can be found at /blog """
    client = Socrata('data.princegeorgescountymd.gov', APPTOKEN, USERNAME, PASSWORD)
    received_data = client.get("364y-gm2b", limit=LIMIT)  # 2017 Data

    context = {
        'title': 'Blog',
        'data': received_data,
        }

    return render(request, 'data.html', context)
