<<<<<<< HEAD
# Generated by Django 3.1 on 2021-04-10 22:17
=======
# Generated by Django 3.1.1 on 2021-04-10 20:17
>>>>>>> c22cde33bf748086214e9f63e6719d70fdb81268

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0025_merge_20210410_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(blank=True, default='', max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.video')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
