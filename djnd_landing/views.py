from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Exposed

# Create your views here.


def getExposed(request, category):
    exposed = Exposed.objects.filter(category__name=category)
    if exposed:
        latest = exposed.latest('created_at')
        dic = model_to_dict(latest, fields=[field.name
                                            for field
                                            in speech._meta.fields])
        dic.update({'status': 'OK'})
        return JsonResponse(dic)
    return raise Http404('There\'s no exposed news')
