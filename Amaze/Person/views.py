from django.shortcuts import render,reverse,render_to_response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect,HttpResponse,StreamingHttpResponse
from django.utils import timezone
import xlwt
import xlrd
from pyecharts import Bar
from Person.models import Person,Teacher,Course,Course_File,Person_UploadFile


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
        password=request.COOKIES.get('password','')
        return render(request, 'Person/Login.html',{'password':password})
    elif request.method.upper()=='POST':
        email=request.POST['email']
        password=request.POST['password']
        persons=Person.objects.filter(email=email)
        if len(persons)!=0:
            if persons[0].password==password:
                request.session['useremail'] = email
                print(request.session['useremail'])
                response = render_to_response('Person/Index.html', {})
                if 'rememberpwd' in request.POST.keys():
                    response.set_cookie('password', password)
                return response
            else:
                return render(request, 'Person/Login.html',{'message':'用户名或者密码错误'})
        else:
            return render(request, 'Person/Login.html',{'message':'用户名或者密码错误'})

def Logout(request):
    if request.session.get("useremail"):
        del request.session['useremail']
    return HttpResponseRedirect(reverse('login'))

def ForgetPassword(request):
    if request.method.upper()=="GET":
        return render(request,'Person/ForgetPassword.html')
    else:
        return HttpResponseRedirect(reverse('login'))

@log_in
def Index(request):
    return render(request,'Person/Index.html')
@log_in
def UserInfo(request):
    useremail=request.session['useremail']
    print(useremail)
    return render(request, 'Person/UserInfo.html',{'useremail':useremail})

@log_in
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

@log_in
def PersonDownload(request):
    persons = Person.objects.all().order_by("-modifydate")
    excel = xlwt.Workbook()
    sheet = excel.add_sheet('Sheet1', cell_overwrite_ok=True)
    #Excel表头
    sheet.write(0, 0, '姓名')
    sheet.write(0, 1, '电子邮箱')
    sheet.write(0, 2, '年龄')

    index=1
    for person in persons:
        sheet.write(index, 0, person.username)
        sheet.write(index, 1, person.email)
        sheet.write(index, 2, person.age)
        index+=1

    excel.save('media/upload/student.xls')
    response = StreamingHttpResponse(open('media/upload/student.xls','rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="student.xls"'
    return response

def PersonUpload(request):
    if request.method.upper()=="GET":
        return render(request,'Person/PersonUpload.html')
    else:
        uploadFile=Person_UploadFile()
        uploadFile.filename=request.FILES.get('file')
        uploadFile.save()

        excel=xlrd.open_workbook('media/'+uploadFile.filename.name)
        sheet=excel.sheet_by_index(0)
        rowcount=sheet.nrows
        for index in range(1,rowcount):
            row=sheet.row_values(index)
            person=Person()
            person.username=row[0]
            person.email=row[1]
            person.age=row[2]
            person.createdate=timezone.now()
            person.modifydate=timezone.now()
            person.save()
        return HttpResponseRedirect(reverse('personlist', kwargs={'page': 1}))

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
        person.headimg = request.FILES.get('img')
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
        person.headimg = request.FILES.get('img')
        person.save()
        return HttpResponseRedirect(reverse('personlist',kwargs={'page':1}))

def PersonEnrollList(request,id):
    if request.method.upper()=="GET":
        courses=Course.objects.all()
        person=Person.objects.get(id=id)
        return render(request,'Person/PersonEnrollList.html',{'courses':courses,'person':person})
    else:
        person = Person.objects.get(id=id)
        person.courses.set(request.POST.getlist('courses_id'))
        person.save()
        return  HttpResponseRedirect(reverse('personlist',kwargs={'page':1}))

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

def CourseFileList(request,id,page):
    coursefilelist=Course_File.objects.filter(courseid=id)
    paginator=Paginator(coursefilelist,1)
    try:
        coursefiles=paginator.page(page)
    except PageNotAnInteger:
        coursefiles=paginator.page(1)
    except EmptyPage:
        coursefiles=paginator.page(paginator.num_pages)
    return render(request,'Person/CourseFileList.html',{'coursefiles':coursefiles,'courseid':id})

def CourseFileUpload(request,courseid):
    if request.method.upper()=="GET":
        return render(request,'Person/CourseFileUpload.html',{'courseid':courseid})
    else:
        coursefile=Course_File()
        coursefile.courseid=Course.objects.get(id=courseid)
        coursefile.createdate=timezone.now()
        coursefile.filename=request.FILES.get('file')
        coursefile.save()
        return HttpResponseRedirect(reverse('coursefilelist',kwargs={'page':1,'id':courseid}))

def CourseFileDelete(request,id,courseid):
    Course_File.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('coursefilelist', kwargs={'page': 1,'id':courseid}))


def BarDemo(request):
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("各商家产品销售情况",'子标题')
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    url='media/upload/Bar.html'
    bar.render(url)
    return  render(request,'Person/BarDemo.html',{'url':url})

def page_not_found(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

def page_error(request):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response



