# Generated by Django 3.1.7 on 2021-05-05 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colleges', '0003_auto_20210505_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Colleges_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=50)),
                ('college_address', models.CharField(max_length=100)),
                ('college_image', models.ImageField(upload_to='College_Images')),
            ],
        ),
        migrations.CreateModel(
            name='Degree_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stream_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.branch_model')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.degree_model')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.stream_model')),
            ],
        ),
        migrations.CreateModel(
            name='College_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.colleges_model')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleges.course_model')),
            ],
        ),
    ]
