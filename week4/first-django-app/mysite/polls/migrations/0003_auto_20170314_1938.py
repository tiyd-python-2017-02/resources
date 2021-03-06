# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 19:38
from __future__ import unicode_literals

from django.db import migrations
import datetime
import csv

def load_data(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    for i in range(10):
        q = Question(question_text="question number: {}".format(i), pub_date="2017-03-14", am_i_stupid=True)
        q.save()



class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_am_i_stupid'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
