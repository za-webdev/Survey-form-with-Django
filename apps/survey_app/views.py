# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages


def index(request):
	if not in session:
		request.session['count']=0

	return render(request,'survey_app/survey.html')

def process(request):

	request.session['count']+=1
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']


	return render(request,'survey_app/result.html')