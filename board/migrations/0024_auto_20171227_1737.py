# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('board', '0023_scoreboard_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cell', models.CharField(max_length=20)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_board.action_set+', to='contenttypes.ContentType')),
                ('scoreboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Scoreboard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='tempbool',
            name='board',
        ),
        migrations.DeleteModel(
            name='TempBool',
        ),
    ]