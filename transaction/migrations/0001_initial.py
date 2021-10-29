# Generated by Django 3.2.5 on 2021-10-21 06:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbladdreview',
            fields=[
                ('reviewid', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Add Review',
                'db_table': 'tbladdreview',
            },
        ),
        migrations.CreateModel(
            name='tblsuggestion',
            fields=[
                ('suggestionid', models.AutoField(primary_key=True, serialize=False)),
                ('suggestion', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Suggestion',
                'db_table': 'tblsuggestion',
            },
        ),
        migrations.CreateModel(
            name='tblworksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worksheet1', models.FileField(upload_to='worksheet1', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('worksheet2', models.FileField(upload_to='worksheet2', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('bookseries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblbookseries')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblchapter')),
                ('classid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblclass')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblsubject')),
            ],
            options={
                'verbose_name': 'Worksheet',
                'db_table': 'tblworksheet',
            },
        ),
        migrations.CreateModel(
            name='tblwebregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Websupport Registration',
                'db_table': 'tblwebregistration',
            },
        ),
        migrations.CreateModel(
            name='tblviewbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewbook', models.FileField(upload_to='viewbook', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('bookseries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblbookseries')),
                ('classid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblclass')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblsubject')),
            ],
            options={
                'verbose_name': 'Viewbook',
                'db_table': 'tblviewbook',
            },
        ),
        migrations.CreateModel(
            name='tblsolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.FileField(upload_to='solution', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('bookseries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblbookseries')),
                ('classid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblclass')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblsubject')),
            ],
            options={
                'verbose_name': 'Solution',
                'db_table': 'tblsolution',
            },
        ),
        migrations.CreateModel(
            name='tbllesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.FileField(upload_to='lesson', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('bookseries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblbookseries')),
                ('classid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblclass')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblsubject')),
            ],
            options={
                'verbose_name': 'Lesson',
                'db_table': 'tbllesson',
            },
        ),
        migrations.CreateModel(
            name='tbldownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookseries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblbookseries')),
                ('classid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblclass')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.tblsubject')),
            ],
        ),
    ]