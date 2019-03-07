from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'index.html')

def about(request):
	my_dict = {'insert_content' : "hello i am from app1 facebook views throw context dict"}
	return render(request,'about.html', context=my_dict)
