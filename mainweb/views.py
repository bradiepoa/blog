from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.

def homeview(request):
	object_list = Post.published.all()


	paginator = Paginator(object_list,3)
	page = request.GET.get('page')

	try:

		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'object_list':object_list, 'page':page, 'posts':posts}
	return render(request, 'mainweb/index.html',context)

def sportview(request):
	object_list = Post.objects.filter(category=1)


	paginator = Paginator(object_list,3)
	page = request.GET.get('page')

	try:

		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'object_list':object_list, 'page':page, 'posts':posts}
	return render(request, 'mainweb/index.html',context)


def post_detail(request,pk_details):

	object_list = Post.published.get(id=pk_details)

	context = {'object_list':object_list}
	return render(request, 'mainweb/details.html',context)

def React(request):
	return render(request, 'mainweb/reactions.html')

def BussinessView(request):

	return render(request, 'mainweb/biz.html')

def sportview(request):
	object_list = Post.published.filter(category=1)


	paginator = Paginator(object_list,3)
	page = request.GET.get('page')

	try:

		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'object_list':object_list, 'page':page, 'posts':posts}
	return render(request, 'mainweb/index.html',context)
