from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "place holder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "place holder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    redirect('/')
def show(request, number):
    response = "Place holder for blog : " +str(number)
    return HttpResponse(response)
def edit(request, number):
    response = "Place holder to edit blog : " +str(number)
    return HttpResponse(response)
def destroy(request,number):
    redirect('/')

