from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,redirect
from .models import Admin
from .models import Admin, Register,Packages
from django.contrib import messages
from .forms import ContactForm

def homepage(request):
    return render(request,"index.html")
def loginpage(request):
    return render(request,"login.html")
def ttmhome(request):
    return render(request,"ttmhome.html")
def register(request):
    return render(request,"register.html")
#def loginfail(request):
 #   return render(request,"loginfail.html")
def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwdd = request.POST["pwd"]
        flag = Register.objects.filter(username=name,password=pwdd).values()
        if flag:    #flag is not empty
            if name== "admin":        #Ramakrishna is admin
                messages.info(request,"This is Admin  Page")
                return render(request, "adminhome.html")
        if flag:
            messages.info(request, "This is User's  Page")
            return render(request, "afterlogin.html")
        else:
            messages.info(request, "Your Credentials are not correct")
            return render(request, "afterlogin.html")
            #return HttpResponse("Login Failed")

def about(request):
    return render(request,"about.html")

def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "Username taken...")
                return render(request, "register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "Email taken...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name, address=addr, email=email, phno=phno, username=uname, password=pwd)
                user.save()
                messages.info(request, "User created successfully...")
                return render(request, "Login.html")
        else:
            messages.info(request, "Passwords do not match...")
            return render(request, "register.html")
    else:
        # Render the register.html template for non-POST requests
        return redirect('register') 




def checkpackages(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]   #request.method is used to get the data from HTML
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack = Packages.objects.create(tourcode=tcode, tourname=tname, tourpackage=tpack, desc=tdesc)
        pack.save()
        messages.info(request, "Data Inserted Successfully")
        return render(request, "package.html")
    else:
            return render(request, "package.html")

def viewplaces(request):
    data=Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})

def checkchangepassword(request):
    if request.method == "POST":
        uname= request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag=Register.objects.filter(username=uname,password=opwd).values()
        #filter-> It is use to compare the HTML data with table Row
        if flag:
            Register.objects.filter(username=uname,password=opwd).update(password=npwd)
            messages.info(request, "Password Updated")
            return render(request,"index.html")
        else:
            return render(request,"index.html")
    else:
        return render(request, "changepassword.html")



def logout(request):
    messages.info(request, "Logout")
    return render(request,"index.html")

def buy(request):
    return render(request,"buy.html")

def houses(request):
    return render(request,"houses.html")

def lands(request):
    return render(request,"lands.html")

def apartments(request):
    return render(request,"apartments.html")

def villas(request):
    return render(request,"villas.html")

def house1(request):
    return render(request,"house1.html")

def house2(request):
    return render(request,"house2.html")

def house3(request):
    return render(request,"house3.html")

def house4(request):
    return render(request,"house4.html") 

def apartment1(request):
    return render(request,"apartment1.html")   

def apartment2(request):
    return render(request,"apartment2.html") 

def apartment3(request):
    return render(request,"apartment3.html") 

def apartment4(request):
    return render(request,"apartment4.html") 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # You can render a success page or redirect to another URL
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def agents(request):
    return render(request,"agents.html")

def terms(request):
    return render(request,"terms.html")