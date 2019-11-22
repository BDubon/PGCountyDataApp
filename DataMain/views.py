from django.shortcuts import render
from django.http import HttpResponse
from sodapy import Socrata
from .credentials import APPTOKEN, USERNAME, PASSWORD

LIMIT = 5000     # Total number of records to request from the API


# Create your views here.
def index(request):
    """ Homepage view """
    client = Socrata('data.princegeorgescountymd.gov', APPTOKEN, USERNAME, PASSWORD)
    results = client.get("364y-gm2b", limit=LIMIT)  # 2017 Data
    context = {
        'data': results,
        'title': 'Homepage',
        'section_one': 'Homepage Subtitle',
        }

    return render(request, 'index.html', context)


def blog(request):
    """ Secondary view can be found at /blog """
    form = 123
    context = {
        'title': 'Blog',
        'form': form,
        'section_one': 'Blog Subtitle',
        }

    return render(request, 'blog.html', context)
