# -*- coding: UTF-8 -*-
from django.http import JsonResponse, Http404
from django.forms.models import model_to_dict
from .models import Exposed

# Create your views here.


def getExposed(request, category):
    exposed = Exposed.objects.filter(category__name=category)
    if exposed:
        latest = exposed.latest('created_at')
        dic = model_to_dict(latest, fields=['label', 'title', 'url'])
        dic.update({'status': 'OK'})
        return JsonResponse(dic)
    else:    
        raise Http404('There\'s no exposed news')
