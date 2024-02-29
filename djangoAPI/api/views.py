from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import contacts
# Create your views here.







def allData(request):

    getContacts = contacts.objects.filter(fName='mehran')
    jsonContacts = {}

    for item in getContacts:
        jsonContacts[item.id] = {
            'id': item.id,
            'fName': item.fName,
            'lName': item.lName,
            'age': item.age,
            'city': item.city,
            'country': item.country,
            'job': item.job,
            'phoneNumber': item.phoneNumber,
            'email': item.email,
            'DWY': item.DWY,
            'DWM': item.DWM,
            'favorites': item.favorites

        }




    return JsonResponse(jsonContacts)