from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login,logout,authenticate
from .models import Tutorial


def homepage(request):
	title='hello'
	return render(request,
					'main/home.html',
					{'title':title})


def register(request):
	if request.method=='POST':
		# crate form object
		form=UserCreationForm(request.POST)
		# check for validation
		if form.is_valid():
			# essentially saving or creating user
			user=form.save()
			username=form.cleaned_data.get('username')
			# login with request and user just created
			login(request,user)
			return redirect('/')
		else:
			print('validation error')
			return render(request,
						'main/register.html',
						{'form':form})

	form=UserCreationForm()
	return render(request,
					'main/register.html',
						{'form':form})