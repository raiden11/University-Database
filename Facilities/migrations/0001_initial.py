# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(blank=True, max_length=200, null=True)),
                ('RenewalsLeft', models.SmallIntegerField(blank=True, default=3, null=True)),
                ('IssueId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.Student', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SportsName', models.CharField(blank=True, choices=[('Football', 'Football'), ('Cricket', 'Cricket'), ('Volleyball', 'Volleyball'), ('Basketball', 'Basketball'), ('Tennis', 'Tennis'), ('Badminton', 'Badminton'), ('Chess', 'Chess'), ('None', 'None')], default='None', max_length=100, null=True)),
                ('NumberOfItems', models.IntegerField(blank=True, default=0, null=True)),
                ('IssueID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.Student', unique=True)),
            ],
        ),
    ]
