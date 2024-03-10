from django.shortcuts import render


def homePage(request):
    return render(request,"index.html")
def Login(request):
    return render(request,"Login.html")

def contactpage(request):
    return render(request,"contact.html")
def aboutus(request):
    return render(request,"about.html")
def registrationpage(request):
    return render(request,"register.html")