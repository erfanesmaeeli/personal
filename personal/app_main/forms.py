from django import forms

class SendMessage(forms.Form):
	name= forms.CharField(max_length=40)
	email= forms.EmailField(max_length=50)
	subject= forms.CharField(max_length=40)
	message= forms.Textarea()