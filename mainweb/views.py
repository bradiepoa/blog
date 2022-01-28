from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category
from django.db.models import F

# Create your views here.

def homeview(request):
	object_list = Post.published.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(object_list,24)

	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)

	context = {'posts':users, 'object_list':object_list}
	return render(request, 'mainweb/index.html',context)


def sportview(request):
	object_list = Post.objects.filter(category=25)

	context = {'object_list':object_list}
	return render(request, 'mainweb/category.html',context)

def politicsview(request):
	object_list = Post.objects.filter(category=26)

	context = {'object_list':object_list}
	return render(request, 'mainweb/category.html',context)

def educationview(request):
	object_list = Post.objects.filter(category=27)

	context = {'object_list':object_list}
	return render(request, 'mainweb/category.html',context)

def businessview(request):
	object_list = Post.objects.filter(category=28)

	context = {'object_list':object_list}
	return render(request, 'mainweb/category.html',context)

def scienceview(request):
	object_list = Post.objects.filter(category=29)

	context = {'object_list':object_list}
	return render(request, 'mainweb/category.html',context)

def healthview(request):
	object_list = Post.objects.filter(category=30)

	context = {'object_list':object_list}
	return render(request, 'mainweb/category.html',context)

#Product.objects.update(price=F('price') * 1.2)



def post_detail(request,pk_details):

	object_list = Post.published.get(id=pk_details)
#	object_list.viewers = F('viewers') + 1
#	object_list.save()
	context = {'object_list':object_list}
	return render(request, 'mainweb/details.html',context)

def React(request):
	return render(request, 'mainweb/reactions.html')

def BussinessView(request):

	return render(request, 'mainweb/biz.html')
