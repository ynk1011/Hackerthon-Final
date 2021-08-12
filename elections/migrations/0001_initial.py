# Generated by Django 3.2 on 2021-08-10 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('name', models.CharField(default='', max_length=10)),
                ('introduction', models.TextField(default='', null=True)),
                ('party_number', models.IntegerField(default=1)),
                ('area', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('area', models.CharField(max_length=15)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('votes', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.candidate')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.poll')),
            ],
        ),
    ]