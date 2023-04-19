from django.shortcuts import render
from django.http import  HttpResponse

def main_page(request):
	return HttpResponse("Hello World")
def about_page(requst):
	return HttpResponse("HELLO HUMAN =3")