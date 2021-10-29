from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from master.models import *

# Create your models here.


class tbldownload(models.Model):
    subject = models.ForeignKey(tblsubject, on_delete=models.CASCADE, null=False, blank=False)
    bookseries = models.ForeignKey(tblbookseries, on_delete=models.CASCADE, null=False, blank=False)
    classid = models.ForeignKey(tblclass, on_delete=models.CASCADE, null=False, blank=False)

class tblwebregistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # school=models.ForeignKey(tblschool, on_delete=models.CASCADE, null=True, blank=True)
    # subject=models.ForeignKey(tblsubject, on_delete=models.CASCADE, null=True, blank=True)
    # series=models.ForeignKey(tblbookseries, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.BigIntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'tblwebregistration'
        verbose_name = 'Websupport Registration'

    def __str__(self):
        return self.user


class tblviewbook(models.Model):
    subject = models.ForeignKey(tblsubject, on_delete=models.CASCADE, null=False, blank=False)
    bookseries = models.ForeignKey(tblbookseries, on_delete=models.CASCADE, null=False, blank=False)
    classid = models.ForeignKey(tblclass, on_delete=models.CASCADE, null=False, blank=False)
    viewbook=models.FileField(upload_to='viewbook',validators=[FileExtensionValidator( ['pdf'] ) ])

    class Meta:
        db_table = 'tblviewbook'
        verbose_name = 'Viewbook'

    def __str__(self):
        return str(self.viewbook)


class tblsolution(models.Model):
    subject = models.ForeignKey(tblsubject, on_delete=models.CASCADE, null=False, blank=False)
    bookseries = models.ForeignKey(tblbookseries, on_delete=models.CASCADE, null=False, blank=False)
    classid = models.ForeignKey(tblclass, on_delete=models.CASCADE, null=False, blank=False)
    solution=models.FileField(upload_to='solution',validators=[FileExtensionValidator( ['pdf'] ) ])

    class Meta:
        db_table = 'tblsolution'
        verbose_name = 'Solution'

    def __str__(self):
        return str(self.solution)


class tbllesson(models.Model):
    subject = models.ForeignKey(tblsubject, on_delete=models.CASCADE, null=False, blank=False)
    bookseries = models.ForeignKey(tblbookseries, on_delete=models.CASCADE, null=False, blank=False)
    classid = models.ForeignKey(tblclass, on_delete=models.CASCADE, null=False, blank=False)
    lesson=models.FileField(upload_to='lesson', validators=[FileExtensionValidator( ['pdf'] ) ])

    class Meta:
        db_table = 'tbllesson'
        verbose_name = 'Lesson'

    def __str__(self):
        return str(self.lesson)


class tblworksheet(models.Model):
    worksheet1=models.FileField(upload_to='worksheet1', validators=[FileExtensionValidator( ['pdf'] ) ])
    worksheet2=models.FileField(upload_to='worksheet2', validators=[FileExtensionValidator( ['pdf'] ) ],null=True,blank=True)
    subject = models.ForeignKey(tblsubject, on_delete=models.CASCADE, null=False, blank=False)
    bookseries = models.ForeignKey(tblbookseries, on_delete=models.CASCADE, null=False, blank=False)
    classid = models.ForeignKey(tblclass, on_delete=models.CASCADE, null=False, blank=False)
    chapter=models.ForeignKey(tblchapter,on_delete=models.CASCADE, null=False, blank=False)
    class Meta:
        db_table = 'tblworksheet'
        verbose_name = 'Worksheet'

    def __str__(self):
        return str(self.id)


class tbladdreview(models.Model):

    reviewid=models.AutoField(primary_key=True)
    review=models.CharField(max_length=500)
    rating=models.IntegerField()

    class Meta:
        db_table='tbladdreview'
        verbose_name = 'Add Review'

    def __str__(self):
        return str(self.reviewid)


class tblsuggestion(models.Model):
    suggestionid=models.AutoField(primary_key=True)
    suggestion=models.CharField(max_length=500)

    class Meta:
        db_table='tblsuggestion'
        verbose_name = 'Suggestion'

    def __str__(self):
        return str(self.suggestionid)

class ZipStored(models.Model):
    zip = models.FileField(upload_to="zip")