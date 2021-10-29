from django import forms
from prompt_toolkit.validation import ValidationError

from .models import *

class subjectform(forms.ModelForm):
    class Meta:
        model= tblsubject
        fields='__all__'

class subjectupdateform(forms.ModelForm):
    class Meta:
        model=tblsubject
        fields=['name','description']

class bookseriesform(forms.ModelForm):
    class Meta:
        model=tblbookseries
        fields = '__all__'

class bookseriesupdateform(forms.ModelForm):
    class Meta:
        model=tblbookseries
        fields = ['name']

class classform(forms.ModelForm):
    class Meta:
        model=tblclass
        fields = '__all__'

class chapterform(forms.ModelForm):
    class Meta:
        model=tblchapter
        fields='__all__'

        # def clean_category(self):
        #     category = self.cleaned_data.get('name')
        #     if not category:
        #         raise forms.ValidationError('This field is required')
        #     # return category
        #
        #     for instance in tblchapter.objects.all():
        #         if instance.category == category:
        #             raise forms.ValidationError(str(category) + ' is already created')
        #     return category


class chapterupdateform(forms.ModelForm):
    class Meta:
        model=tblchapter
        fields=['name']
