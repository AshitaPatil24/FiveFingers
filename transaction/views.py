import os
from audioop import error
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import auth, messages
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse

from fivefingers import settings
from .forms import *
from .models import *

# # Create your views here.

#****************************************Login and Registration**************************************

def register(request):
    return render(request, 'webs-1.html')


def sendmailview1(request,email):
    # print("inside send mail view")
    subject = 'Welcome To Fivefingers'
    message = "You have successfully registered. Wait for approval. We will let you know./n This is system generated email.Please do not reply back."
    email_from = settings.EMAIL_HOST_USER
    # print(email)
    recipient_list = [email]
    sad = send_mail(subject, message, email_from, recipient_list)
    print(sad)
    return sad


def registration(request):
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']

    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = firstname
        user.lastname = lastname
        user.email = email
        sendmailview1(request,email)
    except:
        return render(request, 'registration_error.html')

    customer = tblwebregistration(user=user, mobile=mobile)
    customer.save()
    user.save()
    return render(request, 'registered.html')


def auth_view(request):
    subject = tblsubject.objects.all()
    classidall = tblclass.objects.all()
    d = {'subject': subject, 'classidall': classidall}
    if request.user is not None:
        if request.user.is_authenticated:
            return render(request, 'webs-2.html',d)
        else:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                if username and password:
                    user = authenticate(username=username, password=password)
                    print(user)
                    rawq = "select is_staff from auth_user where username = %s"
                    lgarr = []
                    lgarr.append(str(username))
                    lst = User.objects.raw(rawq, lgarr)
                    print(username+":-     "+password)
                    print(User.objects.filter(username=username, password=password))
                    print(request.user.is_staff)
                    print("$$$$$$$$$$$$$$$$")
                    print(request.user.is_superuser)
                    if user is not None:
                        if user.is_staff and user.is_superuser:
                            login(request, user)
                            print("#############################")
                            return render(request, 'webs-2.html', d)
                        elif  user.is_staff:
                            login(request, user)
                            print("#############################")
                            return render(request,'webs-user.html',d)
                        else:
                            print("**************************************")
                            return render(request, 'notapproved.html')
                    else:
                        return render(request,'login_failed.html')

            else:
                print("/??/////////////////////")
                return render(request, 'webs-1.html',d)


def editprofile(request):
    msg = None
    if request.method == 'POST':
        form = editprofileform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg = 'Data has been saved'
    form = editprofileform(instance=request.user)
    return render(request, 'editprofile.html', {'form': form, 'msg': msg})

def changepass(request):
    if request.user.is_authenticated:
        msg = None #"Password has been changed successfully! Login with New Password !"
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                msg = "Password has been changed successfully! Login with New Password !"
                update_session_auth_hash(request,form.user)
                return render(request, 'changepass.html', {'form': form, 'msg': msg})
            else:
                msg = "Wrong New Password"
                return render(request, 'changepass.html', {'form': form, 'msg': msg})
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html',{'form':form, 'msg': msg})
    else:
        return render(request,'webs-1.html')



def weblogout_view(request):
    auth.logout(request)
    return render(request, 'webs-1.html')


def loginsection(request):
    return render(request, 'webs-1.html')


def is_websupport(user):
    return user.groups.filter(name='WEBSUPPORTUSER').exists()


def login_failed(request):
    return render(request, 'login_failed.html')


def notapproved(request):
    return render(request, 'notapproved.html')


def index(request):

    if not request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def webindex(request):
    return render(request, 'webs-1.html')


def about(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'contact us.html')


def load_courses(request):
    subject_id = request.GET.get('subject')
    print("(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((")
    print(subject_id)
    series = tblbookseries.objects.filter(subject_id=subject_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'series': series})

#***************************************** VIEWBOOK *******************************************************


# @login_required(login_url=webindex)
# def pdfaddnew(request):
#     if request.method == "POST":
#         form = viewbookform(request.POST, request.FILES)
#         print(form.is_valid())
#         for i in form:
#             print(i,i.errors)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/searchpdf/")
#     else:
#         form = viewbookform()
#     return render(request,'pdfindex.html',{'form':form})

@login_required(login_url=webindex)
def pdfaddnew(request):
    if request.method == "POST":
        form = viewbookform(request.POST,request.FILES)
        # cnt = tblviewbook.objects.filter(viewbook=request.FILES["viewbook"],subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"]).count()
        cnt = tblviewbook.objects.filter(subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"]).count()
        if (cnt <= 0):

            if form.is_valid():
                form.save()
                # return HttpResponseRedirect("/searchpdf/")
                return render(request, 'pdfindex.html', {'form': form, 'success': " Data Inserted Successfully!"})
            else:
                return render(request, 'pdfindex.html', {'form': form, 'error': "Insert Correct Chapter Name!"})
        else:
                return render(request, 'pdfindex.html', {'form': form, 'error': "Data already Exists!"})

    else:
        form = viewbookform()
        return render(request,'pdfindex.html',{'form':form,'error': " "})



@login_required(login_url=webindex)
def pdfindex(request):
    employees = tblviewbook.objects.all()
    return render(request,"pdfview.html",{'employees':employees})


@login_required(login_url=webindex)
def pdfupdate(request, id,subject,bookseries,classid):
    employee = tblviewbook.objects.get(id=id)
    path="media_cdn/viewbook"
    print(employee.viewbook.path)
    if request.method == "POST":
        print(employee.viewbook.path)
        if len(request.FILES) != 0:

            if len(employee.viewbook) > 0:
                print(employee.viewbook.path)

                os.remove(employee.viewbook.path)
            employee.viewbook = request.FILES['viewbook']
        sub = tblsubject.objects.get(name=subject)
        book = tblbookseries.objects.get(name=bookseries)
        cls = tblclass.objects.get(name=classid)
        tblviewbook.objects.filter(id=id).update(subject=sub, bookseries=book, classid=cls)
        employee.save()
        messages.success(request, "Product Updated Successfully")
        return HttpResponse("Updated Successfully")

    context = {'employee': employee, 'subject': subject, 'bookseries': bookseries, 'classid': classid}
    return render(request, 'pdfupdate.html', context)


@login_required(login_url=webindex)
def pdfdestroy(request, id):
    employee = tblviewbook.objects.get(id=id)
    employee.delete()
    return HttpResponse("Deleted")

# ******************************************** Solution *******************************************************


# @login_required(login_url=webindex)
# def solutionaddnew(request):
#     if request.method == "POST":
#         form = solutionform(request.POST, request.FILES)
#         print(form.is_valid())
#         for i in form:
#             print(i,i.errors)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/searchsolution/")
#     else:
#         form = solutionform()
#     return render(request,'solutionindex.html',{'form':form})

@login_required(login_url=webindex)
def solutionaddnew(request):
    if request.method == "POST":
        form = solutionform(request.POST,request.FILES)
        # cnt = tblviewbook.objects.filter(viewbook=request.FILES["viewbook"],subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"]).count()
        cnt = tblsolution.objects.filter(subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"]).count()
        if (cnt <= 0):

            if form.is_valid():
                form.save()
                # return HttpResponseRedirect("/searchsolution/")
                return render(request, 'solutionindex.html', {'form': form, 'success': " Data Inserted Successfully!"})
            else:
                return render(request, 'solutionindex.html', {'form': form, 'error': "Insert Correct Chapter Name!"})
        else:
                return render(request, 'solutionindex.html', {'form': form, 'error': "Data already Exists!"})

    else:
        form = solutionform()
        return render(request,'solutionindex.html',{'form':form,'error': " "})
    print("ashita")



@login_required(login_url=webindex)
def solutionindex(request):
    employees = tblsolution.objects.all()
    return render(request,"solutionview.html",{'employees':employees})


@login_required(login_url=webindex)
def solutionupdate(request, id,subject,bookseries,classid):
    employee = tblsolution.objects.get(id=id)
    path="media_cdn/viewbook"
    print(employee.solution.path)
    if request.method == "POST":
        print(employee.solution.path)
        if len(request.FILES) != 0:

            if len(employee.solution) > 0:
                print(employee.solution.path)

                os.remove(employee.solution.path)
            employee.solution = request.FILES['solution']
        sub = tblsubject.objects.get(name=subject)
        book = tblbookseries.objects.get(name=bookseries)
        cls = tblclass.objects.get(name=classid)
        tblviewbook.objects.filter(id=id).update(subject=sub, bookseries=book, classid=cls)
        employee.save()
        messages.success(request, "Updated Successfully")
        return HttpResponse("Updated Successfully")

    context = {'employee': employee, 'subject': subject, 'bookseries': bookseries, 'classid': classid}
    return render(request, 'solutionupdate.html', context)


@login_required(login_url=webindex)
def solutiondestroy(request, id):
    employee = tblsolution.objects.get(id=id)
    employee.delete()
    return HttpResponse("Deleted")



# ******************************************** lesson *******************************************************


# @login_required(login_url=webindex)
# def lessonaddnew(request):
#     if request.method == "POST":
#         form = lessonform(request.POST, request.FILES)
#         print(form.is_valid())
#         for i in form:
#             print(i,i.errors)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/searchlesson/")
#     else:
#         form = lessonform()
#     return render(request,'lessonindex.html',{'form':form})


@login_required(login_url=webindex)
def lessonaddnew(request):
    if request.method == "POST":
        form = lessonform(request.POST,request.FILES)
        # cnt = tblviewbook.objects.filter(viewbook=request.FILES["viewbook"],subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"]).count()
        cnt = tbllesson.objects.filter(subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"]).count()
        if (cnt <= 0):

            if form.is_valid():
                form.save()
                # return HttpResponseRedirect("/searchlesson/")
                return render(request, 'lessonindex.html', {'form': form, 'success': " Data Inserted Successfully!"})
            else:
                return render(request, 'lessonindex.html', {'form': form, 'error': "Insert Correct Chapter Name!"})
        else:
                return render(request, 'lessonindex.html', {'form': form, 'error': "Data already Exists!"})

    else:
        form = solutionform()
        return render(request,'lessonindex.html',{'form':form,'error': " "})




@login_required(login_url=webindex)
def lessonindex(request):
    employees = tbllesson.objects.all()
    return render(request,"lessonview.html",{'employees':employees})


@login_required(login_url=webindex)
def lessonupdate(request, id,subject,bookseries,classid):
    employee = tbllesson.objects.get(id=id)
    path="media_cdn/lesson"
    print(employee.lesson.path)
    if request.method == "POST":
        print(employee.lesson.path)
        if len(request.FILES) != 0:

            if len(employee.lesson) > 0:
                print(employee.lesson.path)

                os.remove(employee.lesson.path)
            employee.lesson = request.FILES['lesson']
        sub = tblsubject.objects.get(name=subject)
        book = tblbookseries.objects.get(name=bookseries)
        cls = tblclass.objects.get(name=classid)
        tbllesson.objects.filter(id=id).update(subject=sub, bookseries=book, classid=cls)
        employee.save()
        messages.success(request, "Updated Successfully")
        return HttpResponse("Updated Successfully")

    context = {'employee': employee, 'subject': subject, 'bookseries': bookseries, 'classid': classid}
    return render(request, 'lessonupdate.html', context)


@login_required(login_url=webindex)
def lessondestroy(request, id):
    employee = tbllesson.objects.get(id=id)
    employee.delete()
    return HttpResponse("Deleted")


# ****************************************** Worksheet ****************************************************

# @login_required(login_url=webindex)
# def worksheetaddnew(request):
#     if request.method == "POST":
#         form = worksheetform(request.POST,request.FILES)
#         employees = tblworksheet.objects.all()
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/searchworksheet/")
#
#         else:
#             messages.error(request,'invalidform submission.')
#             messages.error(request,form.errors)
#
#     else:
#         form = worksheetform
#     return render(request,'worksheetindex.html',{'form':form})


@login_required(login_url=webindex)
def worksheetaddnew(request):
    # subject = tblsubject.objects.all()
    # classidall = tblclass.objects.all()
    # d = {'subject': subject, 'classidall': classidall}
    if request.method == "POST":
        form = worksheetform(request.POST,request.FILES)
        # cnt = tblviewbook.objects.filter(viewbook=request.FILES["viewbook"],subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"]).count()
        cnt = tblworksheet.objects.filter(subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"],chapter=request.POST["chapter"]).count()
        if (cnt <= 0):

            if form.is_valid():
                form.save()
                # return HttpResponseRedirect("/searchworksheet/")
                return render(request, 'worksheetindex.html', {'form': form, 'success': " Data Inserted Successfully!"})
            else:
                return render(request, 'worksheetindex.html', {'form': form, 'error': "Insert Correct Chapter Name!"})
        else:
                return render(request, 'worksheetindex.html', {'form': form, 'error': "Data already Exists!"})

    else:
        form = worksheetform()
        return render(request,'worksheetindex.html',{'form':form,'error': " "})



@login_required(login_url=webindex)
def worksheetindex(request):
    employees = tblworksheet.objects.all()
    return render(request,"worksheetview.html",{'employees':employees})

@login_required(login_url=webindex)
def worksheetupdate(request, id,subject,bookseries,classid,chapter):
    employee = tblworksheet.objects.get(id=id)
    path="media_cdn/worksheet1"
    path="media_cdn/worksheet2"
    print(employee.worksheet1.path)
    print(employee.worksheet2.path)
    if request.method == "POST":
        print(employee.worksheet1.path)
        print(employee.worksheet2.path)
        if len(request.FILES) != 0:

            if len(employee.worksheet1) and len(employee.worksheet2) > 0:
                print(employee.worksheet1.path)
                print(employee.worksheet2.path)

                os.remove(employee.worksheet1.path)
            employee.worksheet1 = request.FILES['worksheet1']
            employee.worksheet2 = request.FILES['worksheet2']
        sub = tblsubject.objects.get(name=subject)
        book = tblbookseries.objects.get(name=bookseries)
        cls = tblclass.objects.get(name=classid)
        chapter = tblchapter.objects.get(name=chapter)
        tblworksheet.objects.filter(id=id).update(subject=sub, bookseries=book, classid=cls,chapter=chapter)
        employee.save()
        messages.success(request, "Updated Successfully")
        return HttpResponse("Updated Successfully")

    context = {'employee': employee, 'subject': subject, 'bookseries': bookseries, 'classid': classid,'chapter': chapter}
    return render(request, 'worksheetupdate.html', context)


@login_required(login_url=webindex)
def worksheetdestroy(request, pk):
    employee = tblworksheet.objects.get(pk=pk)
    employee.delete()
    return HttpResponse("Deleted")
# ****************************************Edit Profile******************************

@login_required(login_url=webindex)
def editprofileindex(request):
    employees = tblwebregistration.objects.all()
    return render(request,"editprofileview.html",{'employees':employees})


@login_required(login_url=webindex)
def editprofileupdate(request, id):
    employee = tblwebregistration.objects.get(id=id)
    form = editprofileupdateform(request.POST, instance=employee)
    for i in form:
        print("Error:", i, i.errors)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return HttpResponse("Updated Successfully")
    return render(request, 'editprofileupdate.html', {'employee': employee})


@login_required(login_url=webindex)
def editprofiledestroy(request, id):
    employee = tblwebregistration.objects.get(id=id)
    employee.delete()
    return HttpResponse("Deleted")


# **************************************** Review *****************************************

@login_required(login_url=webindex)
def reviewaddnew(request):
    if request.method == "POST":
        form = reviewform(request.POST)
        employees = tbladdreview.objects.all()
        print(form.fields)
        print("#############################################")
        print(error)
        if form.is_valid():
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            try:
                form.save()
                # return redirect(request, "editprofileview.html", {'employees': employees})
                return HttpResponseRedirect("/searchaddreview/")
            except:
                print(error)
                pass
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
    else:
        form = reviewform()
    return render(request, 'reviewindex.html', {'form': form})


def reviewindex(request):
    employees = tbladdreview.objects.all()
    return render(request, "editprofileview.html", {'employees': employees})

# **************************************** Suggestion *****************************************


@login_required(login_url=webindex)
def suggestionaddnew(request):
    if request.method == "POST":
        form = suggestionform(request.POST)
        employees = tblsuggestion.objects.all()
        print(form.fields)
        print("#############################################")
        print(error)
        if form.is_valid():
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            try:
                form.save()
                # return redirect(request, "editprofileview.html", {'employees': employees})
                # return HttpResponseRedirect("/searchaddreview/searchaddreview/")
            except:
                print(error)
                pass
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
    else:
        form = suggestionform()
    return render(request,'suggestionindex.html',{'form':form})


# def dbbackup(request):
#     import io
#     import sqlite3
#     con=sqlite3.connect('abc1.db')
#     with io.open('db.sqlite3','w')as f:
#         for linha in con.iterdump():
#             f.write('%s\n%linha')
#             con.close()

# ****************************************Web Download******************************

@login_required(login_url=webindex)
def webdownload(request):
    print("Before", request.user.is_authenticated)
    if request.user.is_authenticated:
        # sbid=request.GET.get('subject')
        subject_id = request.GET.get('subject_id')
        bookseries = request.GET.get('bookseries')
        classid_id = request.GET.get('classid_id')
        chapter_id = request.GET.get('chapter_id')

        subject = tblsubject.objects.all()
        bookseriesall=tblbookseries.objects.all()
        classidall = tblclass.objects.all()
        chapterall = tblchapter.objects.all()

    # # cd = tblwebregistration.objects.get(user=request.user)
        viewbook=tblviewbook.objects.filter(subject_id=subject_id,bookseries_id=bookseries,classid_id=classid_id)
        solution=tblsolution.objects.filter(subject_id=subject_id,bookseries_id=bookseries,classid_id=classid_id)
        lesson=tbllesson.objects.filter(subject_id=subject_id,bookseries_id=bookseries,classid_id=classid_id)

        print("viewbook: ",viewbook)

        d = { 'subject': subject,'subjectid': subject_id,'bookseriesall':bookseriesall, 'bookseriesid':bookseries,'classidall':classidall, 'classid': classid_id,'chapter_id':chapter_id,'chapterall':chapterall,'viewbook':viewbook,'solution':solution,'lesson':lesson}
        print("After",request.user.is_authenticated)
        return render(request, 'webs-2.html',d)
    print("Superafter", request.user.is_authenticated)
    return render(request, 'webs-1.html')