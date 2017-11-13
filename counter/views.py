# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Vote, MailAddress
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("")

def plusOne(request, type_):
	Vote(type_of=type_).save()
	return HttpResponse("Added")


def getCoutner(request, type_):
	count = Vote.objects.filter(type_of=type_).count()
	return HttpResponse(count)


@csrf_exempt
def sender(request):
	if request.method == 'POST':
		content = request.POST["content"]
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


def addSigniture(request):
	name = request.GET.get('name', '')
	email = request.GET.get('email', '')
	peticija = request.GET.get('peticija', '')
	MailAddress(e_mail=email, type_of=peticija, name=name).save()
	return HttpResponse("Saved")

def getAllSignitures(request):
	peticija = request.GET.get('peticija', '')
	names = MailAddress.objects.filter(type_of=peticija).values_list('name', flat=True)
	out = ', '.join(list(names))
	return HttpResponse(out)

def getNumberOfSignatures(request):
	peticija = request.GET.get('peticija', '')
	mail_count = MailAddress.objects.filter(type_of=peticija).count()
	return HttpResponse(str(mail_count))
