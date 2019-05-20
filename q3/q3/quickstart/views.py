import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ServerTime(APIView):

    def get(self, request, format=None):
        now = datetime.datetime.now()
        timezone = now.astimezone().tzinfo
        return Response(now.strftime("%c ") + str(timezone))
