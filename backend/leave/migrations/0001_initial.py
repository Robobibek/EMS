# Generated by Django 5.0.4 on 2024-05-16 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('leaveid', models.IntegerField(primary_key=True, serialize=False)),
                ('leave_date', models.DateField(blank=True, null=True)),
                ('leave_msg', models.TextField()),
                ('leave_status', models.BooleanField(default=False)),
                ('stuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.students')),
            ],
        ),
    ]
