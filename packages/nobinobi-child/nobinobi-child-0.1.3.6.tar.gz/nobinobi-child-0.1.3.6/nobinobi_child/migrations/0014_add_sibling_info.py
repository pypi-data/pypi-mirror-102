#  Copyright (C) 2020 <Florian Alu - Prolibre - https://prolibre.com
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Generated by Django 2.2 on 2020-03-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_child', '0013_add_pediatrician'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='sibling_birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Sibling birth date'),
        ),
        migrations.AddField(
            model_name='child',
            name='sibling_institution',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name="Sibling's institution"),
        ),
        migrations.AddField(
            model_name='child',
            name='sibling_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Sibling's name and first name"),
        ),
    ]
