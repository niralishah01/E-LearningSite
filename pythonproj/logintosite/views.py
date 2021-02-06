import re

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf

from registration.models import UserDetails


# Create your views here.
def adminlogin(request):
    if(request.session.get('admin')):
        return render(request,'adminhomepg.html',{'msg':'You are already logged in,admin!!'})
    else:
        a={}
        a.update(csrf(request))
        return render(request,'adminlogin.html',a)

def authenticateadmin(request):
    user=request.POST['user']
    password=request.POST['password']
    if user=='nirali110' and password=='nirshah123':
        request.session['admin']=user
        request.session.set_expiry(0)
        return render(request,'adminhomepg.html')
    else:
        return render(request,'adminlogin.html',{'msg':'First login here..'})
        
def login(request):
    l={}
    l.update(csrf(request))
    return render(request,'login.html',l)

def authentication(request):
    uname=request.POST['email']
    password=request.POST['password']
    users=UserDetails.objects.all()
    for user in users:
        if user.emailID==uname:
            if user.password==password:
                count=1
                break
            else:
                count=0
                break
        else:
            count=-1
    if count==-1:
        return render(request,'login.html',{'msg':'user does not exist'})
    elif count==0:
        return render(request,'login.html',{'msg':'invalid password'})
    else:
        request.session['user']=user.name
        request.session.set_expiry(0)
        lg={}
        lg.update(csrf(request))
        #print(request.session.get(user.name))
        #return render(request,'userhomepg.html',{'user':user,'lg':lg})
        return HttpResponseRedirect('/userhome/gotouserhome/')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def sendmail(request):
    email=request.POST['email']
    users=UserDetails.objects.all()
    c=0
    for user in users:
        if user.emailID==email:
            c=1
            break
    if c!=0:
        r={}
        r.update(csrf(request))
        return render(request,'send_mail.html',{'user':user,'r':r})
    else:
        return render(request,'forgotpassword.html',{'msg':'This is not valid registered email.Please enter your valid registered emailID once gain.'})

def passwordresetform(request):
    email=request.POST['user']
    user=UserDetails.objects.get(emailID=email)
    r={}
    r.update(csrf(request))
    return render(request,'resetpassword.html',{'user':user,'r':r})

def resetpassword(request):
    new=request.POST.get('npwd','')
    rpwd=request.POST.get('rpwd','')
    email=request.POST['user']
    user=UserDetails.objects.get(emailID=email)
    passwordregex='[a-zA-Z0-9]{6,12}'
    if len(new)>=6 and len(new)<=15:
        if re.search(passwordregex,new):
            if new==rpwd:
                user.password=new
                user.save()
                return render(request,'resetpassworddone.html',{'user':user})
            else:
                return render(request,'resetpassword.html',{'user':user,'msg':'both passwords must be matched'})
        else:
            return render(request,'resetpassword.html',{'user':user,'msg':'password credentials are not matched'})
    else:
        return render(request,'resetpassword.html',{'user':user,'msg':'password must be between 6 to 12 characters'})
        
def logout(request):
    #print(request.session.get(user))
    del request.session['user']
    return HttpResponseRedirect('/home/gotohome/')

def logoutadmin(request):
    del request.session['admin']
    return HttpResponseRedirect('/home/gotohome/')
