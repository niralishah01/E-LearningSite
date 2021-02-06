from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,FileResponse
from django.template.context_processors import csrf
from django.db.models import Q
from registration.models import categories,UserDetails,courses,coursecontent,coursevideocontent

def gotohome(request):
    cat=categories.objects.all()
    return render(request,'homepg.html',{'cats':cat})

def adminhome(request):
    return render(request,'adminhomepg.html')

# def viewcourses(request):
#     category=request.POST['category']
#     course=courses.objects.filter(categoryname=category)
#     return render(request,'viewcourse.html',{'course':course})

def getcoursedetails(request):
    if(request.session.get('admin')):
        c={}
        c.update(csrf(request))
        cats=categories.objects.all()
        return render(request,'addcourse.html',{'cats':cats,'c':c})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def addcoursedetails(request):
    if(request.session.get('admin')):
        cname=request.POST.get('name','')
        category=request.POST.get('category','')
        cat=categories.objects.get(categoryname=category)
        cat.course_count=cat.course_count+1
        cat.save()
        if(request.FILES.get('img','')):
            img_file=request.FILES['img']
        else:
            return render(request,'adminhomepg.html')
        count=0
        c=courses(cname=cname,categoryname=cat,img_file=img_file,user_count=count)
        c.save()
        return HttpResponseRedirect('/home/adminhome/')
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def showcourses(request):
    if(request.session.get('admin')):
        cr=courses.objects.all()
        return render(request,'showcourses.html',{'courses':cr})
    else:
        return render(request,'login.html',{'msg':'First login here..'})
    
def deletecourse(request):
    if(request.session.get('admin')):
        cname=request.POST['cname']
        course=courses.objects.get(cname=cname)
        course.delete()
        return HttpResponseRedirect('/home/adminhome/')

def getcoursecontent(request):
    if(request.session.get('admin')):
        cc={}
        cc.update(csrf(request))
        course=courses.objects.all()
        return render(request,'addcoursecontent.html',{'course':course,'cc':cc})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def addcoursecontent(request):
    if(request.session.get('admin')):
        cname=request.POST.get('course','')
        if(request.FILES.get('txt','')):
            text_file=request.FILES['txt']
        course=courses.objects.get(cname=cname)
        cc=coursecontent(cname=course,text_file=text_file)
        cc.save()
        return HttpResponseRedirect('/home/adminhome/')
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def getvideocoursecontent(request):
    if(request.session.get('admin')):
        cc={}
        cc.update(csrf(request))
        course=courses.objects.all()
        return render(request,'addvideocontent.html',{'course':course,'cc':cc})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def addvideocoursecontent(request):
    if(request.session.get('admin')):
        cname=request.POST.get('course','')
        if(request.FILES.get('video','')):
            video_file=request.FILES['video']
        course=courses.objects.get(cname=cname)
        cc=coursevideocontent(cname=course,video_file=video_file)
        cc.save()
        return HttpResponseRedirect('/home/adminhome/')
    else:
        return render(request,'login.html',{'msg':'First login here..'})


def delete(request):
    if(request.session.get('admin')):
        c={}
        c.update(csrf(request))
        cc=coursecontent.objects.all()
        return render(request,'deletecoursecontent.html',{'course':cc,'c':c})
    else:
        return render(request,'login.html',{'msg':'First login here..'})

def deletecoursecontent(request):
    if(request.session.get('admin')):
        cname=request.POST['course']
        id=request.POST['coursecontentid']
        cr=coursecontent.objects.get(id=id,cname=cname)
        cr.delete()
        return HttpResponseRedirect('/home/adminhome/')
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
            context={'results': results,
                     'submitbutton': submitbutton,
                     'cats':cat}
            return render(request,'homepg.html',context)
        else:
            return HttpResponseRedirect('/home/gotohome/')
    else:
        return HttpResponseRedirect('/home/gotohome/')


