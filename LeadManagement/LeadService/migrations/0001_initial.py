# Generated by Django 3.1.2 on 2020-10-17 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person_name', models.CharField(max_length=200)),
                ('phone_numer', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=2000)),
                ('source', models.CharField(max_length=200)),
                ('current_stage', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FollowUpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_up_date', models.DateField()),
                ('response', models.CharField(max_length=2000)),
                ('medium_used', models.CharField(choices=[('Call', 'Call'), ('Whatsapp', 'Whatsapp'), ('Email', 'Email')], max_length=20)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeadService.leadmodel')),
            ],
        ),
    ]