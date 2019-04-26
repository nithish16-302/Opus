from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

from .models import WorkerDetails,UserDetails,Bookings
# Create your views here.
def loginpage(request):
    return render(request,"workerapp/login.html",{})

def login_view(request):
    if request.method == 'POST':
        mail=request.POST.get('email')
        pw=request.POST.get('loginpassword')
        print(mail,pw)
        user = authenticate(username=mail, password=pw)
        #userdet = User.objects.get(username=user)
        if user is not None:
            login(request,user)
            print(user)
            return redirect(reverse("dashboard"))
def dashboard1(request):
    user1 =request.user
    return render(request, "workerapp/dashboard.html", {"user": user1})

def dashboard(request):
    user1 = request.user
    worker2 = WorkerDetails.objects.get(user=user1)
    print(worker2.user)
    bookings = Bookings.objects.get(worker=worker2)
    if bookings.booking_status== "pending":
        addr = bookings.client_user
        print(addr.user)
        #userdet = User.objects.get(username=user)
        #print(userdet.lastname)
        return render(request, "workerapp/dashboard.html", {"user": user1,"client":addr.user,"address":bookings.address})
    elif bookings.booking_status == "Accepted":
        addr = bookings.client_user
        print(addr.user)
        # userdet = User.objects.get(username=user)
        # print(userdet.lastname)
        return render(request, "workerapp/dashboard.html",{"user": user1, "client2": addr.user, "address2": bookings.address})
    else:
        pass

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
def user_logout_view(request):
    logout(request)
    return redirect(reverse('userloginview'))

def signupview(request):
    return render(request, "workerapp/workersignup.html", {})

def signup(request):
    if request.method == 'POST':
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        mail = request.POST.get('email')
        phno = request.POST.get('contact')
        prof = request.POST.get('prof')
        pincode = request.POST.get('pincode')
        pw = request.POST.get('password')
        print(fname,pw,pincode,prof)
        user = User.objects.create_user(username=mail, email=mail, password=pw, first_name=fname)
        user.save()
        obj=WorkerDetails(user=user,phone_no=phno,pin_code=pincode,profession=prof)
        obj.save()
        user = authenticate(username=mail, password=pw)
        if user is not None:
            login(request,user)
            print(user)
            return redirect(reverse("dashboard1"))
    #return render(request, "workerapp/login.html", {})

def userloginview(request):
    return render(request, "workerapp/userlogin.html", {})
def userdashboard(request):
    user = request.user
    #userdet = User.objects.get(username=user)
    # print(userdet.lastname)
    return render(request, "workerapp/userdashboard.html", {"user": user})
def usersignupview(request):
    return render(request, "workerapp/usersignup.html", {})

def usersignup(request):
    return render(request, "workerapp/usersignup.html", {})
def userlogin(request):
    if request.method == 'POST':
        mail=request.POST.get('email')
        pw=request.POST.get('loginpassword')
        print(mail,pw)
        user = authenticate(username=mail, password=pw)
        #userdet = User.objects.get(username=user)
        if user is not None:
            login(request,user)
            return redirect(reverse("userdashboard"))

def requestwork(request):
    if request.method == 'GET':
        prof = request.GET.get('prof')
        dt = request.GET.get('datetime')
        address = request.GET.get('address')
        pc = request.GET.get('pincode')
        workers=WorkerDetails.objects.filter(pin_code =pc)
        mainwork=workers[0]
        cliuser = UserDetails.objects.get(user=request.user)
        worker2 = WorkerDetails.objects.get(user=mainwork.user)
        bookings = Bookings(client_user=cliuser,worker=worker2,booking_date=dt,booking_status="pending")
        bookings.save()
        print(mainwork.user)
        return render(request, "workerapp/userdashboard.html", {"worker": mainwork})
        pass
def acceptbooking(request):
    user1=request.user
    cli = request.GET.get('client')
    print(cli)
    #client = UserDetails.objects.get(user=cli)
    worker1= WorkerDetails.objects.get(user=user1)
    book = Bookings.objects.filter(worker=worker1)
    for i in book:
        if cli == str(i.client_user.user):
            print("IN The Hood")
            cliuser =i.client_user.user
            cl=UserDetails.objects.get(user=cliuser)
            book1 = Bookings.objects.get(worker=worker1,client_user=cl)
            book1.booking_status = "Accepted"
            book1.save()
            #return HttpResponse(book1.booking_status)
        return redirect(reverse("dashboard"))
    pass
def usersignupview(request):
    if request.method == 'POST':
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        mail = request.POST.get('email')
        phno = request.POST.get('contact')
        pw = request.POST.get('password')
        user = User.objects.create_user(username=mail, email=mail, password=pw, first_name=fname)
        user.save()
        obj=UserDetails(user=user,phone_no=phno)
        obj.save()
        user = authenticate(username=mail, password=pw)
        if user is not None:
            login(request,user)
            print(user)
            return redirect(reverse("userdashboard"))
        else:
            return redirect(reverse("userloginview"))

def home(request):
    return render(request,"workerapp/home.html",{})