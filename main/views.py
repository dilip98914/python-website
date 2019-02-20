from django.shortcuts import render
# from django.http import HttpResponse



def homepage(request):
	title='hello'
	return render(request,
					'main/home.html',
					{'title':title})


