from django.shortcuts import render, HttpResponseRedirect
from app_main.forms import SendMessage
from app_main.models import Message , Post , PythonBasicCourse
import smtplib, ssl
from django.core.mail import send_mail
from django.contrib import messages
import time



def index(request):
	mypost = Post.objects.all().order_by('-id')
	error = False
	if request.method == 'POST':
		name = request.POST.get("name")
		dsc = request.POST.get("message")
		if name != "":
			NewMessage = Message(Name=name , Message=dsc)
			NewMessage.save()
			error = True


		else:	
			NewMessage = Message(Message = dsc)
			NewMessage.save()	
			error = True

		# time.sleep(2) # delays for 10 seconds
		context = {
        		'error':error,
        	}
		return HttpResponseRedirect("/..", context)
	
	return render(request, "index.html", { 'mypost' : mypost })


# def sendmessage(request):
# 		test = True
# 		if request.method == 'POST':
# 			name = request.POST.get("name")
# 			dsc = request.POST.get("message")
# 			if name != "":
# 				NewMessage = Message(Name=name , Message=dsc)
# 				NewMessage.save()

# 			else:	
# 				NewMessage = Message(Message = dsc)
# 				NewMessage.save()	

# 			# 	name,
# 			# 	dsc,
# 			# 	'pythonerfan@gmail.com',
# 			# 	['erfan.es00749@gmail.com'],
# 			# )
# 			time.sleep(2) # delays for 10 seconds
# 		context = {
#         		'test':test,
#         	}
		# return HttpResponseRedirect("/", context)


def mysaleh(request):
	return render(request, "mysaleh.html")


def pyblog(request):
	PythonBasic = PythonBasicCourse.objects.all().order_by('-id')
	PythonBasic.reverse()

	return render(request, "pyblog.html", {'PythonBasic' : PythonBasic})

def error_404(request, Exception):
        data = {}
        return render(request,'404.html', data)


def pybasic(request):
	return render(request, "pybasic.html")

