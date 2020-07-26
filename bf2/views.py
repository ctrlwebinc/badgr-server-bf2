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
    try:
        badgeclass = BadgeClass.objects.get(entity_id=badgeclass_slug)
    except BadgeClass.DoesNotExist:
        badgeclass = None
    if badgeclass is None:
        data = {
        'count': 0
        }
    else:
        data = {
            'count': BadgeInstance.objects.filter(badgeclass_id=badgeclass.id).count()
        }
    return JsonResponse(data)