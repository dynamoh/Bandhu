# Generated by Django 2.2.13 on 2020-11-15 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bandhuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Ashram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('address', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='ashram/thumbnails/')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Bandhughar',
                'verbose_name_plural': 'Bandhughar',
                'unique_together': {('name', 'locality')},
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.TextField(max_length=1000, verbose_name='Tagline (Bold)')),
                ('description', models.TextField(max_length=3000)),
                ('picture', models.ImageField(upload_to='ashram/index')),
                ('banner_image', models.ImageField(upload_to='ashram/banner')),
            ],
            options={
                'verbose_name': 'Bandhughar Home Page',
                'verbose_name_plural': 'Bandhughar Home Page',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='ashram/')),
                ('approved', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ashram.Activity')),
                ('ashram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashram.Ashram')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
                ('topic', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=100)),
                ('agenda', models.TextField()),
                ('minutes', models.FileField(upload_to='ashram/meeting/%Y-%m-%d')),
                ('ashram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashram.Ashram')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('thumb', models.ImageField(upload_to='ashram/events')),
                ('date', models.DateField()),
                ('ashram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashram.Ashram')),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=13, verbose_name='Contact Number')),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashram.Meeting')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bandhuapp.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ashram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashram.Ashram')),
            ],
            options={
                'verbose_name_plural': 'Activity Categories',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ashram.ActivityCategory'),
        ),
    ]
