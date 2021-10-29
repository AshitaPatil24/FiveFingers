from django import forms
from .models import *

# class subjectform(forms.ModelForm):
#     class Meta:
#         model= tblsubject
#         fields='__all__'
#
# class subjectupdateform(forms.ModelForm):
#     class Meta:
#         model=tblsubject
#         fields=['name','description']
#
# class bookseriesform(forms.ModelForm):
#     class Meta:
#         model=tblbookseries
#         fields = '__all__'
#
# class classform(forms.ModelForm):
#     class Meta:
#         model=tblclass
#         fields = '__all__'

class downloadform(forms.ModelForm):
    class Meta:
        model=tbldownload
        fields = '__all__'

class viewbookform(forms.ModelForm):
    class Meta:
        model=tblviewbook
        fields = '__all__'

class viewbookupdateform(forms.ModelForm):
    class Meta:
        model=tblviewbook
        fields = ['viewbook']

class solutionform(forms.ModelForm):
    class Meta:
        model=tblsolution
        fields = '__all__'

class lessonform(forms.ModelForm):
    class Meta:
        model=tbllesson
        fields = '__all__'

# from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
#
# class AuthenticationForm(BaseAuthenticationForm):
#
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         user = User.objects.filter(username = username).first()
#         if user != None:
#             print(user)
#             if not user.is_superuser and not user.is_staff:
#                 account = Account.objects.filter(num_account = UserProfile.objects.filter(user__username = username).first().num_account).first()
#                 have_counter = Counter.objects.filter(num_account = account).all()
#                 if not have_counter:
#                     raise forms.ValidationError('Some text...')
#         return self.cleaned_data


class editprofileupdateform(forms.ModelForm):
    class Meta:
        model=tblwebregistration
        fields=['mobile']


class reviewform(forms.ModelForm):
    class Meta:
        model=tbladdreview
        fields='__all__'


class suggestionform(forms.ModelForm):
    class Meta:
        model=tblsuggestion
        fields='__all__'

# class chapterform(forms.ModelForm):
#     class Meta:
#         model=tblchapter
#         fields='__all__'

class worksheetform(forms.ModelForm):
    class Meta:
        model=tblworksheet
        fields='__all__'

class worksheetupdateform(forms.ModelForm):
    class Meta:
        model=tblworksheet
        fields=['worksheet1','worksheet2','subject','bookseries','classid','chapter']

class editprofileform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']

