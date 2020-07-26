from django.http import JsonResponse
from issuer.models import (Issuer, BadgeClass, BadgeInstance)

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

def badgeinstances_for_issuer_count(request, issuer_slug):
    data = {
        'count': BadgeInstance.objects.filter().count()
    }
    return JsonResponse(data)

def badgeinstances_for_badgeclass_count(request, badgeclass_slug):
    badgeclass = BadgeClass.objects.get(entity_id=badgeclass_slug)
    data = {
        'count': BadgeInstance.objects.filter(badgeclass_id=badgeclass.id).count()
    }
    return JsonResponse(data)