# Generated by Django 3.1.2 on 2020-10-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.CharField(db_index=True, help_text='The gid of this object in Asana.', max_length=31, null=True)),
                ('name', models.CharField(max_length=1024, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
