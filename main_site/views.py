from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

def index(request):
    return render(request, 'main_site/home.html')

def case_study(request):
    return render(request, 'main_site/case_study.html')

def contact(request):
    return render(request, 'main_site/contact.html')

def charts(request):
    return render(request, 'main_site/charts.html')

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		data = {
			"sales": 100,
			"customers": 10,
			"users": User.objects.all().count(),
		}
		return JsonResponse(data)

def get_data(request, *args, **kwargs):
	data = {
		"sales": 100,
		"customers": 10,
	}
	return JsonResponse(data)
