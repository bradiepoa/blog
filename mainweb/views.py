from django.shortcuts import render, redirect, get_object_or_404
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


def post_detail(request,year,month,day,post):
	post = get_object_or_404(Post, slug=post,status='Published')
	return render(request, 'mainweb/detail.html',{'post':post}) 

def React(request):
	return render(request, 'mainweb/reactions.html')

def BussinessView(request):

	return render(request, 'mainweb/biz.html')

