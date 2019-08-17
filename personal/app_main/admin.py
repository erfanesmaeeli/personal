from django.contrib import admin
from app_main.models import Message, Post , PythonBasicCourse




class PostAdmin(admin.ModelAdmin):
	list_display = ('Name' , 'Title' , 'DateCreate' ,'image_tag','publish')
	list_filter = ('Name', 'Title','publish')
	search_fields = ('Name', 'Title', 'DateCreate','publish')

class PythonBasicCourseAdmin(admin.ModelAdmin):
	list_display = ('Session'  , 'DateCreate' ,'image_tag','publish')
	list_filter = ('Session', 'DateCreate','publish')
	search_fields = ('Session', 'DateCreate','publish')

admin.site.register(Message)
admin.site.register(Post, PostAdmin)
admin.site.register(PythonBasicCourse, PythonBasicCourseAdmin)