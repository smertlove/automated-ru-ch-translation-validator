# Generated by Django 4.0.4 on 2023-04-22 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Lessons',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='ChineseRegexp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('regexp', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UI.lesson')),
            ],
            options={
                'verbose_name_plural': 'Chinese Regexps',
                'ordering': ['lesson', 'number'],
            },
        ),
    ]
