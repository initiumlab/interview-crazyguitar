from django.shortcuts import render
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class DatabaseTime(APIView):
    def get(self, request, format=None):
        with connection.cursor() as cursor:
            cursor.execute('SELECT NOW()')
            row = cursor.fetchone()
            print(row)
            return Response(row)
