from django.contrib import admin
from app_main.models import Message, Post , PythonCourse




class PostAdmin(admin.ModelAdmin):
	list_display = ('Name' , 'Title' , 'DateCreate' ,'image_tag')
	list_filter = ('Name' , 'Title')
	search_fields = ('Name', 'Title', 'DateCreate')

class PythonCourseAdmin(admin.ModelAdmin):
	list_display = ('Session' , 'Title' , 'DateCreate' ,'image_tag')
	search_fields = ('Session', 'Title', 'DateCreate')

admin.site.register(Message)
admin.site.register(Post, PostAdmin)
admin.site.register(PythonCourse, PythonCourseAdmin)