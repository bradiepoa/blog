from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# creating new manager
class PublishedManager(models.Manager):
	def get_querryset(self):
		return super(PublishedManager,self).get_querryset().filter(status='published')


class Category(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	img = models.ImageField(upload_to='images/blog', blank=True, null=True)
	created = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

# Create your models here.
class Post(models.Model):
	STATUS_CHIOCES = (
		('draft','Draft'),
		('published','Published'),
		)

	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True,blank=True )
	img = models.ImageField(upload_to='images/blog', blank=True, null=True)
	body =models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHIOCES, default='published ')
	viewers = models.IntegerField(default=0, null=True)
	objects =models.Manager()
	published = PublishedManager()

	def get_absolute_url(self):
		return reverse('blog:post_detail',
					args=[self.publish.year,
					self.publish.month,
					self.publish.day,
					self.slug])

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	@property
	def imgURL(self):
		try:
			url = self.img.url
		except:
			url =''
		return url



class Comment(models.Model):
	STATUS = (
		('pending','Pending'),
		('approve','Approve'),
		)


	name = models.CharField(max_length=250 ,blank=True, null=True)
	email = models.EmailField(max_length=254, blank=True, null=True)
	message = models.TextField(blank=True, null=True)
	status = models.CharField(max_length=254,choices=STATUS, default='Pending')
	created = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name