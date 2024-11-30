# Generated by Django 4.2.16 on 2024-11-30 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xsitz_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hallno', models.CharField(blank=True, max_length=20, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('columns', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('exam_time', models.TimeField(blank=True, null=True)),
                ('no_of_students', models.CharField(blank=True, max_length=100, null=True)),
                ('duration_hours', models.PositiveSmallIntegerField(default=1)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestername', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='studenttable',
            name='auto_generate_registerno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='is_active',
            field=models.BooleanField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='registerno',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='Teacherseatingarrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.examdetails')),
                ('exam_hall', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.classroom')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.teachertable')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(blank=True, max_length=100, null=True)),
                ('subjectcode', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('autogeneratesubjectcode', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.branch')),
                ('semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Seatingarrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_name', models.CharField(blank=True, max_length=100, null=True)),
                ('seat_number', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_time', models.CharField(blank=True, max_length=100, null=True)),
                ('register_no', models.CharField(blank=True, max_length=100, null=True)),
                ('classroom_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.classroom')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.subject')),
            ],
        ),
        migrations.AddField(
            model_name='examdetails',
            name='exam_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.subject'),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.branch'),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xsitz_app.semester'),
        ),
        migrations.AddField(
            model_name='teachertable',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffsubject', to='xsitz_app.subject'),
        ),
    ]
