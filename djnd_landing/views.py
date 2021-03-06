# -*- coding: UTF-8 -*-
from django.http import JsonResponse, Http404
from django.forms.models import model_to_dict
from .models import Exposed

# Create your views here.


def getExposed(request, category, num_of_news='1'):
    exposed = Exposed.objects.filter(category__name=category).order_by('-created_at')
    if exposed:
        if num_of_news == '1':
            news = exposed[0]
            data = {'label': news.label,
                    'title': news.title,
                    'url': news.url,
                    'date': news.date.isoformat(),
                    'image': news.image.url if news.image else ''}
        else:
            data = {}
            data['data'] = [{'label': news.label,
                             'title': news.title,
                             'url': news.url,
                             'date': news.date.isoformat(),
                             'image': news.image.url if news.image else ''} for news in list(exposed)[:int(num_of_news)]]
            print(data['data'])
        data.update({'status': 'OK'})
        return JsonResponse(data, safe=False)
    else:    
        raise Http404('There\'s no exposed news')
