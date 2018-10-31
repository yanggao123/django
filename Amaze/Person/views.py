from django.shortcuts import render,reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect
from django.utils import timezone
from Person.models import Person,Teacher,Course

#认证装饰器 未登录时，跳转登入页面
def log_in(func):
    def wrapper(request,*args,**kwargs):
        if not request.session.get("useremail"):
            return HttpResponseRedirect(reverse('login'))
        return func(request,*args, **kwargs)
    return wrapper

# Create your views here.
def Login(request):
    if request.method.upper()=='GET':
        return render(request, 'Person/Login.html')
    elif request.method.upper()=='POST':
        email=request.POST['email']
        password=request.POST['password']
        persons=Person.objects.filter(email=email)
        if len(persons)!=0:
            if persons[0].password==password:
                request.session['useremail'] = email
                print(request.session['useremail'])
                return render(request, 'Person/Index.html')
            else:
                return render(request, 'Person/Login.html',{'message':'用户名或者密码错误'})
        else:
            return render(request, 'Person/Login.html',{'message':'用户名或者密码错误'})

def Logout(request):
    if request.session.get("useremail"):
        del request.session['useremail']
    return HttpResponseRedirect(reverse('login'))

@log_in
def Index(request):
    return render(request,'Person/Index.html')

def UserInfo(request):
    useremail=request.session['useremail']
    print(useremail)
    return render(request, 'Person/UserInfo.html',{'useremail':useremail})

def PersonList(request,page):
    #修改时间倒序
    persons=Person.objects.all().order_by("-modifydate")
    #分页实例化
    paginator1= Paginator(persons, 1)
    try:
        students=paginator1.page(page)
    except PageNotAnInteger:
        students =paginator1.page(1)
    except EmptyPage:
        students =paginator1.page (paginator1 .num_pages)

    return render(request, 'Person/PersonList.html',{'students':students})

def PersonDetail(request,id):
    if request.method.upper()=="GET":
        person=Person.objects.get(id=id)
        return render(request, 'Person/PersonDetail.html',{'person':person})
    else:
        person = Person.objects.get(id=id)
        person.username=request.POST['username']
        person.age=request.POST['age']
        person.mobilephone=request.POST['mobilephone']
        person.email = request.POST['email']
        person.modifydate=timezone.now()
        person.save()
        return HttpResponseRedirect(reverse('personlist',kwargs={'page':1}))

def PersonDelete(request,id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect(reverse('personlist', kwargs={'page': 1}))

def PersonAdd(request):
    if request.method.upper()=="GET":
        return render(request, 'Person/PersonAdd.html')
    else:
        person=Person()
        person.username=request.POST['username']
        person.age=request.POST['age']
        person.mobilephone=request.POST['mobilephone']
        person.email = request.POST['email']
        person.createdate=timezone.now()
        person.modifydate=timezone.now()
        person.save()
        return HttpResponseRedirect(reverse('personlist',kwargs={'page':1}))

def TeacherList(request,page):
    persons=Teacher.objects.all()
    paginator=Paginator(persons,1)
    try:
        teachers=paginator.page(page)
    except PageNotAnInteger:
        teachers=paginator.page(1)
    except EmptyPage:
        teachers=paginator.page(paginator.num_pages)

    return render(request, 'Person/TeacherList.html',{'teachers':teachers})

def TeacherDetail(request,id):
    if request.method.upper()=='GET':
        person=Teacher.objects.get(id=id)
        return render(request,'Person/TeacherDetail.html',{'person':person})
    else:
        person = Teacher.objects.get(id=id)
        person.username = request.POST['username']
        person.age = request.POST['age']
        person.mobilephone = request.POST['mobilephone']
        person.email = request.POST['email']
        person.modifydate = timezone.now()
        person.save()
        return HttpResponseRedirect(reverse('teacherlist', kwargs={'page': 1}))

def TeacherAdd(request):
    if request.method.upper()=="GET":
        return render(request,'Person/TeacherAdd.html')
    else:
        person = Teacher()
        person.username = request.POST['username']
        person.age = request.POST['age']
        person.mobilephone = request.POST['mobilephone']
        person.email = request.POST['email']
        person.modifydate = timezone.now()
        person.save()
        return HttpResponseRedirect(reverse('teacherlist', kwargs={'page': 1}))

def TeacherDelete(request,id):
    Teacher.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('teacherlist', kwargs={'page': 1}))

def CourseList(request,page):
    courselist=Course.objects.all();
    paginator=Paginator(courselist,1)
    try:
        courses=paginator.page(page)
    except PageNotAnInteger:
        courses=paginator.page(1)
    except EmptyPage:
        courses=paginator.page(paginator.num_pages)
    return render(request,'Person/CourseList.html',{'courses':courses})

def CourseDetail(request,id):
    if request.method.upper()=='GET':
        course=Course.objects.get(id=id)
        print(course.teachers.all())
        teachers = Teacher.objects.all()
        return render(request,'Person/CourseDetail.html',{'course':course,'teachers':teachers})
    else:
        course = Course.objects.get(id=id)
        course.name=request.POST['name']
        course.descrption=request.POST['descrption']
        course.teachers.set(request.POST.getlist('teachers_id'))
        course.modifydate=timezone.now()
        course.save()
        return HttpResponseRedirect(reverse('courselist',kwargs={'page':1}))

def CourseAdd(request):
    if request.method.upper()=="GET":
        teachers=Teacher.objects.all()
        return render(request,'Person/CourseAdd.html',{'teachers':teachers})
    else:
        course= Course()
        course.name = request.POST['name']
        course.descrption = request.POST['descrption']
        course.modifydate = timezone.now()
        course.save()
        course.teachers.set(request.POST.getlist('teachers_id'))
        return HttpResponseRedirect(reverse('courselist', kwargs={'page': 1}))

def CourseDelete(request,id):
    Course.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('courselist', kwargs={'page': 1}))
