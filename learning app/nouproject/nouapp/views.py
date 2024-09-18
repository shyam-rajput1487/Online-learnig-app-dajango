from django.shortcuts import render
from .models import Enquiry,Student,Login
from django.contrib import messages
from datetime import date
# Create your views here.
def index(request):
    return render(request,"index.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        enquirytext=request.POST['enquirytext']
        regdate=date.today()
        #ORM (object relationship Mapping)
        enq=Enquiry(name=name,gender=gender,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,addess=address,regdate=regdate)
        enq.save()
        messages.success(request,'your enquiry is submitted')
    return render(request,"contactus.html")

def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
            obj=Login.objects.get(userid=userid,password=password)
            messages.success(request,'Valid User')
        except:
            messages.error(request,'Invalid User')
    return render(request,"login.html")

def registration(request):
    if request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        dob=request.POST['dob']
        address=request.POST['address']
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        regdate=date.today()
        usertype='student'
        status='false'
        stu=Student(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,dob=dob,address=address,program=program,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,regdate=regdate)
        log=Login(userid=rollno,password=password,usertype=usertype,status=status)
        stu.save()
        log.save()
        messages.success(request,'Student  is registered')
    return render(request,"registration.html")