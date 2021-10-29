from django.db import models
from django.core.validators import RegexValidator

# alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only characters are allowed.')

# Create your models here.
class tblsubject(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=50)
    class Meta:
        db_table='tblsubject'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='tblsubject')
        ]

        verbose_name = 'Subject'

    def __str__(self):
        return self.name

class tblbookseries(models.Model):
    subject=models.ForeignKey(tblsubject, on_delete=models.CASCADE, null=False, blank=False)
    name=models.CharField(max_length=30)
    class Meta:
        db_table='tblbookseries'
        verbose_name = 'Book Series'

    def __str__(self):
        return self.name


class tblclass(models.Model):
    name=models.CharField(max_length=30)

    class Meta:
        db_table = 'tblclass'
        verbose_name = 'Class'

    def __str__(self):
        return self.name


class tblchapter(models.Model):
    name = models.CharField(max_length=20)
    subject = models.ForeignKey(tblsubject, on_delete=models.CASCADE, null=False, blank=False)
    bookseries = models.ForeignKey(tblbookseries, on_delete=models.CASCADE, null=False, blank=False)
    classid = models.ForeignKey(tblclass, on_delete=models.CASCADE, null=False, blank=False)


    class Meta:
        db_table = 'tblchapter'
        verbose_name = 'Chapter'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='tblchapter')
        ]

    def __str__(self):
        return self.name

