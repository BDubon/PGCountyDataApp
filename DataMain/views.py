from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from sodapy import Socrata
from .credentials import APPTOKEN, USERNAME, PASSWORD

# Class Based Views reference guide http://ccbv.co.uk/


LIMIT = 3000  # Total number of records to request from the API


def index(request):
    """ Homepage view / """
    template = 'index.html'

    context = {
        'page_title': 'Home',
        'title': 'VISIT OUR DATA DASHBOARD!!',
        'title_text': 'The Best Place to View Data.',
        'subtitle': 'About',
        'subtitle_text': 'Some Clever Line.',
        'alerts': [
            {
                'tags': 'primary',
                'message': 'Try Version 1.0!',
            },
            {
                'tags': 'warning',
                'message': 'Site is still under development, please be patient.',
            },
        ]
    }

    return render(request, template, context)


def data(request):
    """ Secondary view can be found at /data """
    client = Socrata('data.princegeorgescountymd.gov', APPTOKEN, USERNAME, PASSWORD)
    received_data = client.get("2qma-7ez9", limit=LIMIT)  # 2018 Data
    template = 'data.html'

    context = {
        'page_title': 'Data',
        'title': 'Blog',
        'data': received_data,
        'alerts': [
            {
                'tags': 'warning',
                'message': 'Site is still under development, please be patient.',
            },
            {
                'tags': 'danger',
                'message': 'No chart found!',
            },
        ]
    }

    # messages.add_message(request, messages.SUCCESS, 'Yeehaw!')
    # messages.add_message(request, messages.WARNING, 'You Suck defwge rver gvercgvf ergvfdv rv f gf vdfvd  v fced!')

    return render(request, template, context)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        client = Socrata('data.princegeorgescountymd.gov', APPTOKEN, USERNAME, PASSWORD)
        received_data = client.get("2qma-7ez9", limit=LIMIT)  # 2018 Data

        return Response(received_data)


