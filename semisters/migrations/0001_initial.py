# Generated by Django 4.2.2 on 2023-08-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fourtwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htno', models.TextField(blank=True, db_column='Htno', null=True)),
                ('subcode', models.TextField(blank=True, db_column='Subcode', null=True)),
                ('subname', models.TextField(blank=True, db_column='Subname', null=True)),
                ('grade', models.TextField(blank=True, db_column='Grade', null=True)),
                ('credits', models.IntegerField(blank=True, db_column='Credits', null=True)),
            ],
            options={
                'db_table': 'fourtwo',
                'managed': False,
            },
        ),
    ]
