from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

# # ******************************* Subject ********************************
#
#     path('insertsubject/', subjectaddnew),
#     path('deletesubject/<int:id>', subjectdestroy),
#     path('searchsubject/', subjectindex),
#     path('updatesubject/<int:id>', subjectupdate),
#
# # ******************************* Series ********************************
#
#     path('insertbookseries/',bookseriesaddnew),
#     path('deletebookseries/<int:id>',bookseriesdestroy),
#     path('searchbookseries/',bookseriesindex),
#     path('updatebookseries/<int:id>',bookseriesupdate),
#     # path('searchseriesid/<int:pk>',searchseriesbyidview),
#
# # ******************************* Class ********************************
#
#     path('insertclass/',classaddnew),
#     path('deleteclass/<int:id>',classdestroy),
#     path('searchclass/',classindex),
#     path('updateclass/<int:pk>',classupdate),
#     # path('searchclassid/<int:pk>',searchclassbyidview),
#
# # ******************************* Chapter ********************************
#
#     path('insertchapter/', chapteraddnew),
#     path('deletechapter/<int:pk>', chapterdestroy),
#     path('searchchapter/', chapterindex),
#     path('updatechapter/<int:id>', chapterupdate),

]
