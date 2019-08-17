from django.urls import path
from app_main import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404

urlpatterns = [
	path('',views.index, name = "index"),
	path('pyblog/', views.pyblog, name = "pyblog"),
	path('pybasic/', views.pybasic, name = "pybasic"),

	# path('sendmessage/',views.sendmessage),
	# path('msaleh/', views.mysaleh)


	
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
