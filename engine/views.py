from django.http import JsonResponse
import models
import json


'''
request.user <- contrib.auth.User
request.auth <- token
'''


def unit_index(request):
    """json get request, with SID: sid"""
    if request.method == 'GET':
        try:
            body = json.load(request.body.decode('utf-8'))
            serial = body['serial']
            unit = models.Unit.objects.get(serial=serial)
            contacts = models.Contact.objects.find(unit=unit)
            unit_name = unit.name
            response = JsonResponse({'name': unit_name, 'contacts': contacts})
            return response
        except Exception:
            return error




