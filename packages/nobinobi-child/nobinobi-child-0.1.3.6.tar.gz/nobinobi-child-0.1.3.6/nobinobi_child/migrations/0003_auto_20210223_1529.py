# Generated by Django 3.1.5 on 2021-02-23 14:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('auth', '0012_alter_user_first_name_max_length'),
		('nobinobi_staff', '0010_auto_20201029_1500'),
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
		('nobinobi_child', '0002_fix_for_dj4'),
	]

	operations = [
		migrations.AddField(
			model_name='classroom',
			name='allowed_group_login',
			field=models.ManyToManyField(related_name='classroom_group_login', to='auth.Group',
										 verbose_name='Allowed group login'),
		),
	]
