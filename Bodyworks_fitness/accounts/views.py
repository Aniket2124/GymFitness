from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout, login
from .models import Contact,Membership_Plan,Trainer,Enrollment, Gallery, Attendance
# Create your views here.
def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('phone_number')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(username)>10 or len(username)<10:
            messages.info(request, "User Phone Number Must be 10 Digits")
            return redirect('/signup/')
        
        if password1 != password2:
            messages.info(request, "Password is Not Matching")
            return redirect('/signup/')
        

        try:
            if User.objects.get(username=username):
                messages.warning(request, "Phone Number Already Exits")
                return redirect('/signup/')
        except Exception as identifire:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email Already Exits")
                return redirect('/signup/')
        except Exception as identifire:
            pass

        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, "User is Created Please Login")
        return redirect('/login/')

    return render(request, 'signup.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('phone_number')
        password = request.POST.get('password1')
        myuser = authenticate(username=username, password=password )
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "You have Login Successfully")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login/')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You have Logout Successfully")
    return redirect('/login/')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phonenumber')
        description = request.POST.get('desc')

        mycontact = Contact(name=name, email=email, phonenumber=phone, description=description)
        mycontact.save()

        messages.info(request, "Thanks For Contacting us we will get back to you soon")
        return redirect('/contact/')
  
    return render(request, 'contact.html')


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to Enroll")
        return redirect('/login/')
    
    membership = Membership_Plan.objects.all()
    trainer = Trainer.objects.all()

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phonenumber = request.POST.get('phonenumber')
        dob = request.POST.get('dob')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        referance = request.POST.get('referance')
        address = request.POST.get('address')

        enroll_data = Enrollment(fullname=fullname, email=email, gender=gender, phonenumber=phonenumber, 
                                 dob=dob, select_membership_plan=member, select_trainer=trainer, referance=referance, address=address )
        enroll_data.save()
        messages.success(request, "Thanks for Enrollment")
        return redirect('/enroll/')


    return render(request, 'enroll.html', {'membership':membership, 'trainer':trainer})


def user_profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to Enroll")
        return redirect('/login/')
    user_phone = request.user
    user_detail = Enrollment.objects.filter(phonenumber=user_phone)
    user_attendance = Attendance.objects.filter(phonenumber=user_phone)
    return render(request, 'profile.html',{'user_detail':user_detail, 'user_attendance':user_attendance})


def gallery(request):
    post = Gallery.objects.all()
    return render(request, 'gallery.html',{'post':post})


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login to Enroll")
        return redirect('/login/')
    trainer = Trainer.objects.all()

    if request.method == 'POST':
        phonenumber = request.POST.get('phonenumber')
        select_workout = request.POST.get('workout')
        login = request.POST.get('login')
        logout = request.POST.get('logout')
        trained_by = request.POST.get('trainer')

        attendance = Attendance(phonenumber=phonenumber, select_workout=select_workout, login=login, logout=logout, trained_by=trained_by)
        attendance.save()
        messages.success(request, "Attendance Applied Successful")
        return redirect('/attendance/')
    return render(request, 'attendance.html', {'trainer':trainer})


 