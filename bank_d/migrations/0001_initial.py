# Generated by Django 2.2.5 on 2019-09-15 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('name', models.CharField(max_length=49)),
                ('bankid', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Branchs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11, unique=True)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_d.Banks')),
            ],
            options={
                'verbose_name': 'Branch',
                'ordering': ('branch',),
                'verbose_name_plural': 'Branch',
            },
        ),
    ]
