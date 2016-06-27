from django.shortcuts import render
from .models import Vote
from django.http import HttpResponse

# Create your views here.
def plusOne(request, type_):
	Vote(type_of=type_).save()
	return HttpResponse("Added")

def getCoutner(request, type_):
	count = Vote.objects.filter(type_of=type_).count()
	return HttpResponse(count)