"""sms1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *
from master.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

# # *********** Subject ************

    path('insertsubject/', subjectaddnew),
    path('deletesubject/<int:id>', subjectdestroy),
    path('searchsubject/', subjectindex,name='searchsubject'),
    path('updatesubject/<int:id>', subjectupdate),
#
# # *********** Series ************
#
    path('insertbookseries/',bookseriesaddnew),
    path('deletebookseries/<int:id>',bookseriesdestroy),
    path('searchbookseries/',bookseriesindex,name='searchbookseries'),
    path('updatebookseries/<int:id>/<str:subject>/',bookseriesupdate),
    # path('searchseriesid/<int:pk>',searchseriesbyidview),
#
# # *********** Class ************
#
    path('insertclass/',classaddnew),
    path('deleteclass/<int:pk>',classdestroy),
    path('searchclass/',classindex,name='searchclass'),
    path('updateclass/<int:pk>',classupdate),
    # path('searchclassid/<int:pk>',searchclassbyidview),
#
# # *********** Chapter ************
#

    path('insertchapter/', chapteraddnew),
    path('deletechapter/<int:pk>', chapterdestroy),
    path('searchchapter/', chapterindex,name='searchchapter'),
    path('updatechapter/<int:id>/<str:subject>/<str:bookseries>/<str:classid>', chapterupdate),

    # path('insertchapter/', chapteraddnew),
    # path('deletechapter/<int:pk>', chapterdestroy),
    # path('searchchapter/', chapterindex,name='searchchapter'),
    # path('updatechapter/<int:id>', chapterupdate),
    #

# *********** View Book ************

    path('insertpdf/', pdfaddnew),
    path('deletepdf/<int:id>', pdfdestroy),
    path('searchpdf/', pdfindex,name='searchpdf'),
    path('updatepdf/<int:id>/<str:subject>/<str:bookseries>/<str:classid>', pdfupdate),

# *********** Solution ************

    path('insertsolution/', solutionaddnew),
    path('deletesolution/<int:id>', solutiondestroy),
    path('searchsolution/', solutionindex,name='searchsolution'),
    path('updatesolution/<int:id>/<str:subject>/<str:bookseries>/<str:classid>', solutionupdate),

# *********** Lesson ************

    path('insertlesson/', lessonaddnew),
    path('deletelesson/<int:id>', lessondestroy),
    path('searchlesson/', lessonindex,name='searchlesson'),
    path('updatelesson/<int:id>/<str:subject>/<str:bookseries>/<str:classid>', lessonupdate),

# *********** Worksheets ************

    path('insertworksheet/',worksheetaddnew),
    path('deleteworksheet/<int:pk>',worksheetdestroy),
    path('searchworksheet/',worksheetindex,name='searchworksheet'),
    path('updateworksheet/<int:id>/<str:subject>/<str:bookseries>/<str:classid>/<str:chapter>',worksheetupdate),

# *********************************
    path('load-courses/', load_courses, name='ajax_load_courses'),
    path('webindex/', webindex,name='webindex'),
    path('auth/',auth_view,name='auth'),
    path('loginsection/', loginsection, name='loginsection'),

    path('webdownload/', webdownload, name='webdownload'),
    # path('downloadsection/', downloadsection,name='downloadsection'),
    path('weblogout/',weblogout_view),
    path('login_failed/',login_failed),
    path('notapproved/',notapproved,name='notapproved'),

    # path('<int:id>', downloadsection, name='viewbook'),
    # path('<int:id>', downloadsection, name='solution'),
    # path('<int:id>', downloadsection, name='lesson'),

    path('addreview/', reviewaddnew, name='addreview'),
    path('addsuggestion/', suggestionaddnew, name='addsuggestion'),


    # path('login/',login),
    # path('auth/',auth_view),
    # path('logout/',logout_view),
    path('register/',register),
    path('registration/',registration),

    path('',index),
    path('about/', about),
    path('contact/', contact),
    # path('editprofileupdate/<int:id>', editprofileupdate),
    path('updateeditprofile/<int:id>', editprofileupdate),

    path('searcheditprofile/', editprofileindex),
    path('deleteeditprofile/<int:id>', editprofiledestroy),
    path('updateeditprofile/<int:id>', editprofileupdate),

    path('insertreview/', reviewaddnew),
    path('searchreview/', reviewindex),
    path('editprofile/', editprofile, name='editprofile'),
    path('changepass/', changepass, name='changepass'),

    # path('insertsuggestion/', suggestionaddnew),
    # path('dbbackup/', dbbackup),

]



if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)