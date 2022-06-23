from django.http import HttpResponse
import requests
import json
import pytz
from datetime import datetime

# URLs to refer for the endpoint
# 1. https://documenter.getpostman.com/view/9564387/TzRPip7u#4766cca6-e5f7-4276-97e5-55e9117ec195
# 2. https://apisetu.gov.in/api/cowin#/Appointment%20Availability%20APIs/findByPin

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, pincode):
    # sets up the timezone
    timezone = pytz.timezone('Asia/Kolkata')
    # gets current date for the given timezone
    today = datetime.now(timezone).date()
    # creates date in DD-MM-YYYY format
    date_time_str = today.strftime("%d-%m-%Y")
    headers = {"Content-Type": "application/json"}
    # creates query params in request
    params = {'pincode': pincode, 'date': date_time_str}
    # API to fetch slots available by pincode
    api_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin'
    response = requests.get(api_url, params=params, headers=headers, verify=False)
    # returns response
    return HttpResponse(json.dumps(response.json()), content_type="application/json")
