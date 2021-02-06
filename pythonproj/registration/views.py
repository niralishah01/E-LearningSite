from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.template.context_processors import csrf
from registration.models import UserDetails,enrollDetails,courses
import re

def getregsdetails(request):
    r = {}
    r.update(csrf(request))
    return render(request,'regestration.html', r)

def addregsdetails(request):
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    password=request.POST.get('passwd','')
    repassword=request.POST.get('repasswd','')
    passwordregex='[a-zA-Z0-9]{6,12}'
    #emailregex='+@+\.^[0-9]{2,}'
    #emailregex='[a-z][!@A-Z]+@[a-z]+.[a-z]+'
    count=0
    users=UserDetails.objects.all()
    if users is not None:
        for user in users:
            if user.emailID==email:
                count=1
                break
    if count!=1:
        if len(password)>=6 and len(password)<=15:
            if re.search(passwordregex,password):
                #if re.search(emailregex,email):
                if password==repassword:
                    u = UserDetails(name=name,emailID=email,password=password)
                    u.save()
                    #request.session['uname']=name
                    i={}
                    i.update(csrf(request))
                    #cat=categories.objects.all()
                    #return render(request,'homepg.html',{'user':u,'i':i})
                    return HttpResponseRedirect('/home/gotohome/')
                else:
                    return render(request,'regestration.html',{'msg2':'both password must be matched.'}) 
                    #else:
                        #return render(request,'regestration.html',{'msg3':'email credentials are not matched'})
            else:
                return render(request,'regestration.html',{'msg4':'password credentials are not matched'})
        else:
            return render(request,'regestration.html',{'msg1':'password must be between 6 to 15 characters'})
    else:
        return render(request,'regestration.html',{'msg5':'this user is already registered'})

def delete(request):
    uname=request.POST['name']
    cusers=enrollDetails.objects.filter()
    for u in cusers:
        if u.name==uname:
            u.delete()
    user=UserDetails.objects.get(name=uname)
    user.delete()
    del request.session['user']
    return HttpResponseRedirect('/home/gotohome/')

