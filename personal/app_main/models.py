import os
from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings

class Message(models.Model):
	Name= models.CharField(max_length = 40, default = "No Name")
	Email= models.EmailField(max_length = 50 , blank = True, default = "example@mail.com")
	Subject= models.CharField(max_length = 40 , blank = True, default = "No Subject")
	Message= models.TextField(blank = True)
	def __str__(self):
		return self.Name


class Post(models.Model):
	publish = models.BooleanField(default=True)
	Name = models.CharField(max_length=40, null = True)
	Title = models.CharField(max_length=80 , null = True)
	Description = models.TextField(blank = True )
	Image = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT)
	Video = models.FileField(blank = True , null = True , upload_to = settings.MEDIA_ROOT)
	DateCreate = models.DateTimeField(auto_now_add=True)
	# def image_tag(self):
	#   	  return mark_safe("<img src='%s' style='max-width:250px ; height = auto'/>" % self.Image)
	def url(self):
		return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.Image)))
	def image_tag(self):
		return mark_safe('<img src="{}" width="150" height="150"/>'.format(self.url()) )
	image_tag.short_description = 'Image'

	def __str__(self):
		return self.Name


class PythonBasicCourse(models.Model):
	publish = models.BooleanField(default=True)
	Session = models.IntegerField(default = "0")
	Description = models.TextField(blank = True)
	Image = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT)
	Teacher = models.CharField(max_length=80 , null = True , default = "Erfan Esmaeeli")
	DateCreate = models.DateTimeField(auto_now_add=True)
	
	def url(self):
		return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.Image)))
	def image_tag(self):
		return mark_safe('<img src="{}" width="150" height="150"/>'.format(self.url()) )
	image_tag.short_description = 'Image'

	def __str__(self):
		return str(self.Session)       