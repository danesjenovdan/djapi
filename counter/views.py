# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Vote, MailAddress
from django.http import HttpResponse, JsonResponse 
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

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


def addSignature(request):
	name = strip_tags(request.GET.get('name', ''))
	email = strip_tags(request.GET.get('email', ''))
	peticija = request.GET.get('peticija', '')
	MailAddress(e_mail=email, type_of=peticija, name=name).save()
	return HttpResponse("Saved")

def getAllSignatures(request):
	peticija = request.GET.get('peticija', '')
	names = MailAddress.objects.filter(type_of=peticija).values_list('name', flat=True)
	out = ', '.join(list(names))
	return HttpResponse(out)

def getNumberOfSignatures(request):
	peticija = request.GET.get('peticija', '')
	mail_count = MailAddress.objects.filter(type_of=peticija).count()
	return HttpResponse(str(mail_count))


def getKura(request):
	peticije = ['imasjajca.djndtrue.dzzztrue', 'imasjajca.djndtrue.dzzzfalse', 'imasjajca.djndfalse.dzzzfalse', 'imasjajca.djndfalse.dzzztrue']
	hide = 'imasjajcaHIDE'
	all_mails = MailAddress.objects.filter(type_of__in=peticije)

	visited = []
	duplicated = []
	mejlz = []
	for mail in all_mails:
		if mail.e_mail in visited:
			duplicated.append(mail.id)
			mejlz.append(mail.e_mail)
		else:
			visited.append(mail.e_mail)

	counter = all_mails.count()
	all_mails = all_mails.exclude(id__in=duplicated)

	exclude = MailAddress.objects.filter(type_of=hide)
	all_mails=all_mails.exclude(e_mail__in=exclude.values_list("e_mail", flat=True))
	names = all_mails.values_list('name', flat=True)
	out = ', '.join(list(names))
	return JsonResponse({'names': out, 'counter': counter})
