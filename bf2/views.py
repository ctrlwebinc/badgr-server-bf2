from django.http import JsonResponse
from issuer.models import (Issuer, BadgeClass)

def issuers_count(request):
    data = {
        'count': Issuer.objects.count()
    }
    return JsonResponse(data)

def badgeclasses_count(request):
    data = {
        'count': BadgeClass.objects.count()
    }
    return JsonResponse(data)