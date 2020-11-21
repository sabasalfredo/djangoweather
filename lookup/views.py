# This is my views.py file
from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests
	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=ABDF5AE6-987F-450F-86F0-3D4C82335F1F")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})
