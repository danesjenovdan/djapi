# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Vote
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def plusOne(request, type_):
	Vote(type_of=type_).save()
	return HttpResponse("Added")

def getCoutner(request, type_):
	count = Vote.objects.filter(type_of=type_).count()
	return HttpResponse(count)

@csrf_exempt
def sender(request):
	print "sender"
	if request.method == 'POST':
		content = request.POST["content"]
		print content
		send_mail(
			'Sprejemanje študentske zakonodaje',
			content,
			settings.DEFAULT_FROM_EMAIL,
			['cofek0@gmail.com'],
			fail_silently=False,
		)
	else:
		return HttpResponse("Neki ni ql")
	return HttpResponse("Sent")
