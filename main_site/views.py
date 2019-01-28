from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

import json
import os

User = get_user_model()
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def index(request):
    return render(request, 'main_site/home.html')

def case_study(request):
    return render(request, 'main_site/case_study.html')

def contact(request):
    return render(request, 'main_site/contact.html')

def data(request):
    return render(request, 'main_site/data.html')

def charts(request):
    return render(request, 'main_site/charts.html')

class highDeltaChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		json_filepath = os.path.join(BASE_DIR, 'static\main_site\data\high_delta_scatter.json') #os.path.abspath(os.path.dirname(__name__))
		json_data = open(json_filepath).read()
		data = json.loads(json_data)
		return JsonResponse(data, safe=False)

class lowDeltaChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		json_filepath = os.path.join(BASE_DIR, 'static\main_site\data\low_delta_scatter.json') #os.path.abspath(os.path.dirname(__name__))
		json_data = open(json_filepath).read()
		data = json.loads(json_data)
		return JsonResponse(data, safe=False)

def get_household_data(request, *args, **kwargs):
	json_filepath = '/static/main_site/data/household_features.json' #os.path.join(BASE_DIR, 'static\main_site\data\household_features.json') #os.path.abspath(os.path.dirname(__name__))
	json_data = open(json_filepath).read()
	data = json.loads(json_data)

	household_id = kwargs['household_id']

	try:
		data_out = data[household_id]
		print(data_out)
	except:
		data_out = {'status':'The household ID you gave is unavailable'}

	return JsonResponse(data_out, safe=False)
