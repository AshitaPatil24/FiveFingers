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
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transaction.urls')),

# ******************************* Subject ********************************

    # path('insertsubject/', include('master.urls')),
    # path('searchsubject/', include('master.urls')),
    # path('deletesubject/', include('master.urls')),
    # path('updatesubject/', include('master.urls')),

# ******************************* Book Series ********************************

    # path('insertbookseries/', include('master.urls')),
    # path('searchbookseries/', include('master.urls')),
    # path('deletebookseries/', include('master.urls')),
    # path('updatebookseries/', include('master.urls')),

# ******************************* Class ********************************

    # path('insertclass/', include('master.urls')),
    # path('searchclass/', include('master.urls')),
    # path('deleteclass/', include('master.urls')),
    # path('updateclass/', include('master.urls')),

# ******************************* Chapter ********************************

    # path('insertchapter/', include('master.urls')),
    # path('deletechapter/',include('master.urls')),
    # path('searchchapter/', include('master.urls')),
    # path('updatechapter/', include('master.urls')),

# ******************************* Viewbook ********************************

    # path('insertpdf/', include('transaction.urls')),
    # path('deletepdf/', include('transaction.urls')),
    # path('searchpdf/', include('transaction.urls')),
    # path('updatepdf/', include('transaction.urls')),

# ******************************* Solution ********************************
#
#     path('insertsolution/', include('transaction.urls')),
#     path('deletesolution/', include('transaction.urls')),
#     path('searchsolution/', include('transaction.urls')),
#     path('updatesolution/', include('transaction.urls')),

# ******************************* Lesson ********************************
#
#     path('insertlesson/', include('transaction.urls')),
#     path('deletelesson/', include('transaction.urls')),
#     path('searchlesson/', include('transaction.urls')),
#     path('updatelesson/', include('transaction.urls')),

# ******************************* Worksheets ********************************

    # path('insertworksheet/',include('transaction.urls')),
    # path('deleteworksheet/',include('transaction.urls')),
    # path('searchworksheet/',include('transaction.urls')),
    # path('updateworksheet/',include('transaction.urls')),

# # ******************************* Section ********************************
#
#     path('insertsection/', include('testgenerator.urls')),
#     path('searchsection/', include('testgenerator.urls')),
#     path('deletesection/', include('testgenerator.urls')),
#     path('updatesection/', include('testgenerator.urls')),
#
# # ******************************* Teacher SignUp ********************************
#
#     path('insertteachersignup/', include('testgenerator.urls')),
#     path('searchteachersignup/', include('testgenerator.urls')),
#     path('deleteteachersignup/', include('testgenerator.urls')),
#     path('updateteachersignup/', include('testgenerator.urls')),
#
# # ******************************* Teacher Login ********************************
#
#     path('insertteacherlogin/', include('testgenerator.urls')),
#     path('searchteacherlogin/', include('testgenerator.urls')),
#     path('deleteteacherlogin/', include('testgenerator.urls')),
#     path('updateteacherlogin/', include('testgenerator.urls')),
#
# # ******************************* Student Login ********************************
#
#     path('insertstudentlogin/', include('testgenerator.urls')),
#     path('searchstudentlogin/', include('testgenerator.urls')),
#     path('deletestudentlogin/', include('testgenerator.urls')),
#     path('updatestudentlogin/', include('testgenerator.urls')),
#
# # ******************************* Chapter ********************************
#
#     path('insertchapter/', include('testgenerator.urls')),
#     path('searchchapter/', include('testgenerator.urls')),
#     path('deletechapter/', include('testgenerator.urls')),
#     path('updatechapter/', include('testgenerator.urls')),
#
# # ******************************* Question Bank ********************************
#
#     path('insertquebankobj/', include('testgenerator.urls')),
#     path('searchquebankobj/', include('testgenerator.urls')),
#     path('deletequebankobj/', include('testgenerator.urls')),
#     path('updatequebankobj/', include('testgenerator.urls')),

    # ******************************* Project ********************************



    # path('inserteditprofile/', include('transaction.urls')),
    # path('searcheditprofile/', include('transaction.urls')),
    # path('updateeditprofile/', include('transaction.urls')),
    # path('deleteeditprofile/', include('transaction.urls')),
    #
    # path('insertreview/', include('transaction.urls')),
    # path('searchreview/', include('transaction.urls')),
    #
    # path('insertsuggestion/', include('transaction.urls')),
    #
    # path('dbbackup/', include('transaction.urls')),



]