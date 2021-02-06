from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,FileResponse
from registration.models import UserDetails,courses,coursecontent,enrollDetails,categories,coursevideocontent
from django.template.context_processors import csrf
from django.db.models import Q

# Create your views here.
def gotouserhome(request):
    if(request.session.get('user')):
        name=request.session['user']
        cat=categories.objects.all()
        return render(request,'userhomepg.html',{'user':name,'cats':cat})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def categorizedcourses(request):
    if(request.session.get('user')):
        user=request.session['user']
        catname=request.POST['category']
        course=courses.objects.filter(categoryname=catname)
        return render(request,'categorizedcourse.html',{'user':user,'course':course})
    else:
        return render(request,'login.html',{'msg':'First login here..'})


def enroll(request):
    if(request.session.get('user')):
        cname=request.POST.get('cname','')
        print(cname)
        c=courses.objects.get(cname=cname)
        c.user_count=c.user_count+1
        c.save()
        uname=request.session.get('user')
        u=UserDetails.objects.get(name=uname)
        e=enrollDetails(name=u,cname=c)
        e.save()
        return HttpResponseRedirect("/userhome/gotouserhome/")
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def viewprofile(request):
    if(request.session.get('user')):
        uname=request.session['user']
        user=UserDetails.objects.get(name=uname)
        u={}
        u.update(csrf(request))
        return render(request,'profile.html',{'user':user,'u':u})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def showtext(request):
    if(request.session.get('user')):
        uname=request.session['user']
        cname=request.POST['cname']
        content=coursecontent.objects.filter(cname=cname)
        return render(request,'showtext.html',{'content':content,'cname':cname,'user':uname})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

             
def showvideo(request):
    if(request.session.get('user')):
        uname=request.session['user']
        cname=request.POST['cname']
        content=coursevideocontent.objects.filter(cname=cname)
        # count=0
        # for c in content:
        #     if c.cname==cname:
        #         count+=1
        # if count > 0:
        return render(request,'showvideo.html',{'content':content,'cname':cname,'user':uname})
        # else:
        #     return render(request,'viewcoursecontent.html',{'cname':cname,'msg1':'video is not available','user':uname})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def mycourses(request):
    if(request.session.get('user')):
        uname=request.session['user']
        cu=enrollDetails.objects.filter(name=uname)   
        return render(request,'mycourses.html',{'course':cu,'user':uname})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def viewcourse(request):
    if(request.session.get('user')):
        uname=request.session['user']
        cname=request.POST['cname']
        return render(request,'viewcoursecontent.html',{'cname':cname,'user':uname})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def viewstatus(request):
    if(request.session.get('user')):
        uname=request.session.get('user')
        cname=request.POST['cname']
        if(request.POST.get('text','')):
            return render(request,'viewcoursecontent.html',{'cname':cname,'msg2':'completed','user':uname})
        elif(request.POST.get('video','')):
            return render(request,'viewcoursecontent.html',{'cname':cname,'msg1':'completed','user':uname})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def updatestatus(request):
    if(request.session.get('user')):
        uname=request.session['user']
        cname=request.POST['cname']   
        cu=enrollDetails.objects.get(cname=cname,name=uname)
        cu.status='completed'
        cu.save()
        return HttpResponseRedirect('/userhome/mycourses/')
    else:
        return render(request,'login.html',{'msg':'First login here..'})
    
def searchcourses(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(cname__icontains=query)
            results= courses.objects.filter(lookups).distinct()
            cat=categories.objects.all()
            uname=request.session.get('user')
            context={'results': results,
                     'submitbutton': submitbutton,
                     'cats':cat,
                     'user':uname}
            return render(request,'userhomepg.html',context)
        else:
            return HttpResponseRedirect('/userhome/gotouserhome/')
    else:
        return HttpResponseRedirect('/userhome/gotouserhome/')


