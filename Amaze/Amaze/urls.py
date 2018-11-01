"""Amaze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Person import views as person_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', person_views.Login,name='login'),
    path('logout/', person_views.Logout, name='logout'),
    path('index/', person_views.Index,name='index'),
    path('userinfo/', person_views.UserInfo,name='userinfo'),
    path('personlist/<int:page>/', person_views.PersonList,name='personlist'),
    path('persondetail/<int:id>/', person_views.PersonDetail,name='persondetail'),
    path('persondelete/<int:id>/', person_views.PersonDelete, name='persondelete'),
    path('personadd/', person_views.PersonAdd, name='personadd'),
    path('personenrolllist/<int:id>/', person_views.PersonEnrollList, name='personenrolllist'),
    path('teacherlist/<int:page>/', person_views.TeacherList,name='teacherlist'),
    path('teacherdetail/<int:id>/', person_views.TeacherDetail, name='teacherdetail'),
    path('teacherdelete/<int:id>/', person_views.TeacherDelete, name='teacherdelete'),
    path('teacheradd/', person_views.TeacherAdd, name='teacheradd'),
    path('courselist/<int:page>/', person_views.CourseList,name='courselist'),
    path('coursedetail/<int:id>/', person_views.CourseDetail, name='coursedetail'),
    path('coursedelete/<int:id>/', person_views.CourseDelete, name='coursedelete'),
    path('courseadd/', person_views.CourseAdd, name='courseadd'),
    path('coursefilelist/<int:id>/<int:page>/', person_views.CourseFileList, name='coursefilelist'),
    path('coursefileupload/<int:courseid>/', person_views.CourseFileUpload, name='coursefileupload'),
    path('coursefiledelete/<int:id>/<int:courseid>/', person_views.CourseFileDelete, name='coursefiledelete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = person_views.page_not_found
handler500 = person_views.page_error


