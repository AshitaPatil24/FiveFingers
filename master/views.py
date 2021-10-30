from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from transaction.views import webindex

# Create your views here.

# ************************************** SUBJECT******************************************

# @login_required(login_url=webindex)
# def subjectaddnew(request):
#     if request.method == "POST":
#         form = subjectform(request.POST)
#         employees = tblsubject.objects.all()
#         if form.is_valid():
#             try:
#                 form.save()
#                 return HttpResponseRedirect("/searchsubject/")
#             except:
#                 pass
#     else:
#         form = subjectform()
#     return render(request,'subjectindex.html',{'form':form})

@login_required(login_url=webindex)
def subjectaddnew(request):
    if request.method == "POST":
        form = subjectform(request.POST)
        cnt = tblsubject.objects.filter(name=request.POST["name"],description=request.POST["description"]).count()
        if (cnt <= 0):

            if form.is_valid():
                form.save()
                return render(request, 'subjectindex.html', {'form': form, 'success': " Data Inserted Successfully!"})
            else:
                return render(request, 'subjectindex.html', {'form': form, 'error': "Insert Correct Subject Name!"})
        else:
                return render(request, 'subjectindex.html', {'form': form, 'error': "Data already Exists!"})

    else:
        form = subjectform()
        return render(request,'subjectindex.html',{'form':form,'error': " "})


@login_required(login_url=webindex)
def subjectindex(request):
    employees = tblsubject.objects.all()
    return render(request,"subjectview.html",{'employees':employees})


@login_required(login_url=webindex)
def subjectupdate(request, id):
    employee = tblsubject.objects.get(id=id)
    form = subjectupdateform(request.POST, instance=employee)
    for i in form:
        print("Error:", i, i.errors)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return HttpResponse("Updated Successfully")
    return render(request, 'subjectupdate.html', {'employee': employee})


@login_required(login_url=webindex)
def subjectdestroy(request, id):
    employee = tblsubject.objects.get(id=id)
    employee.delete()
    return HttpResponse("Deleted")

# ************************************** Book Series ******************************************


# @login_required(login_url=webindex)
# def bookseriesaddnew(request):
#     if request.method == "POST":
#         form = bookseriesform(request.POST)
#         employees = tblbookseries.objects.all()
#         if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect("/searchbookseries/")
#         else:
#                 messages.error(request,'invalidform submission.')
#                 messages.error(request,form.errors)
#
#     else:
#         form = bookseriesform()
#     return render(request,'seriesindex.html',{'form':form})

@login_required(login_url=webindex)
def bookseriesaddnew(request):
    if request.method == "POST":
        form = bookseriesform(request.POST)
        cnt = tblbookseries.objects.filter(name=request.POST["name"],subject=request.POST["subject"]).count()
        if (cnt <= 0):

            if form.is_valid():
                form.save()
                # return HttpResponseRedirect("/searchbookseries/")
                return render(request, 'seriesindex.html', {'form': form, 'success': " Data Inserted Successfully!"})
            else:
                return render(request, 'seriesindex.html', {'form': form, 'error': "Insert Correct Bookseries Name!"})
        else:
                return render(request, 'seriesindex.html', {'form': form, 'error': "Data already Exists!"})

    else:
        form = bookseriesform()
        return render(request,'seriesindex.html',{'form':form,'error': ""})





@login_required(login_url=webindex)
def bookseriesindex(request):
    employees = tblbookseries.objects.all()
    return render(request,"seriesview.html",{'employees':employees})


@login_required(login_url=webindex)
def bookseriesupdate(request, id,subject):
    subject = subject.replace("%20", " ")
    employee = tblbookseries.objects.get(id=id)
    print(subject)
    form = bookseriesupdateform(request.POST, instance = employee)
    for i in form:
        print("Error:", i, i.errors)
    print(form.is_valid())
    if form.is_valid():
        sub = tblsubject.objects.get(name=subject)
        # book= tblbookseries.objects.get(name=bookseries)
        # cls = tblclass.objects.get(name=classid)
        print(request.POST['name'])
        tblbookseries.objects.filter(id=id).update(subject=sub,name=request.POST['name'])
        return HttpResponse("Updated Successfully")
    print(subject)
    return render(request, 'seriesupdate.html', {'employee': employee,'subject1':subject})


@login_required(login_url=webindex)
def bookseriesdestroy(request, id):
    employee = tblbookseries.objects.get(id=id)
    employee.delete()
    return HttpResponse("Deleted")


# ************************************** Class ******************************************

# @login_required(login_url=webindex)
# def classaddnew(request):
#     if request.method == "POST":
#         form = classform(request.POST)
#         employees = tblclass.objects.all()
#         if form.is_valid():
#
#             # try:
#                 form.save()
#                 return HttpResponseRedirect("/searchclass/")
#             # except:
#             #     pass
#         else:
#                 messages.error(request,'invalidform submission.')
#                 messages.error(request,form.errors)
#
#     else:
#         form = classform()
#     return render(request,'classindex.html',{'form':form})


@login_required(login_url=webindex)
def classaddnew(request):
    if request.method == "POST":
        form = classform(request.POST)
        cnt = tblclass.objects.filter(name=request.POST["name"]).count()
        if (cnt <= 0):

            if form.is_valid():
                form.save()
                # return HttpResponseRedirect("/searchclass/")
                return render(request, 'classindex.html', {'form': form, 'success': " Data Inserted Successfully!"})
            else:
                return render(request, 'classindex.html', {'form': form, 'error': "Insert Correct Chapter Name!"})
        else:
            return render(request, 'classindex.html', {'form': form, 'error': "Data already Exists!"})

    else:
        form = classform()
        return render(request,'classindex.html',{'form':form,'error': " "})



@login_required(login_url=webindex)
def classindex(request):
    employees = tblclass.objects.all()
    return render(request,"classview.html",{'employees':employees})


@login_required(login_url=webindex)
def classupdate(request, pk):
    employee = tblclass.objects.get(pk=pk)
    form = classform(request.POST, instance = employee)
    for i in form:
        print("Error:", i, i.errors)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return HttpResponse("Updated Successfully")
    return render(request, 'classupdate.html', {'employee': employee})


@login_required(login_url=webindex)
def classdestroy(request, pk):
    employee = tblclass.objects.get(pk=pk)
    employee.delete()
    return HttpResponse("Deleted")

#***************************************CHAPTER*****************************************************************



@login_required(login_url=webindex)
def chapteraddnew(request):
    if request.method == "POST":
        form = chapterform(request.POST)
        cnt = tblchapter.objects.filter(name=request.POST["name"],subject=request.POST["subject"],bookseries=request.POST["bookseries"],classid=request.POST["classid"]).count()
        if (cnt <= 0):

            if form.is_valid():
                form.save()
                # return HttpResponseRedirect("/searchchapter/")
                return render(request, 'chapterindex.html', {'form': form, 'success': " Data Inserted Successfully!"})
            else:
                return render(request, 'chapterindex.html', {'form': form, 'error': "Insert Correct Chapter Name!"})
        else:
                return render(request, 'chapterindex.html', {'form': form, 'error': "Data already Exists!"})

    else:
        form = chapterform()
        return render(request,'chapterindex.html',{'form':form,'error': " "})



@login_required(login_url=webindex)
def chapterindex(request):
    employees = tblchapter.objects.all()
    return render(request,"chapterview.html",{'employees':employees})


@login_required(login_url=webindex)
def chapterupdate(request, id,subject,bookseries,classid):
    subject = subject.replace("%20", " ")
    bookseries = bookseries.replace("%20", " ")
    classid = classid.replace("%20", " ")
    employee = tblchapter.objects.get(id=id)
    print(subject)
    form = chapterupdateform(request.POST, instance = employee)
    for i in form:
        print("Error:", i, i.errors)
    print(form.is_valid())
    if form.is_valid():
        sub = tblsubject.objects.get(name=subject)
        book= tblbookseries.objects.get(name=bookseries)
        cls = tblclass.objects.get(name=classid)
        print(request.POST['name'])
        tblchapter.objects.filter(id=id).update(subject=sub,bookseries=book ,classid=cls ,name=request.POST['name'])
        return HttpResponse("Updated Successfully")
    print(subject)
    return render(request, 'chapterupdate.html', {'employee': employee,'subject1':subject,'bookseries':bookseries,'classid':classid})


@login_required(login_url=webindex)
def chapterdestroy(request, id):
    employee = tblchapter.objects.get(id=id)
    employee.delete()
    return HttpResponse("Deleted")

