# Generated by Django 3.1.3 on 2020-11-25 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20201125_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.role', verbose_name='current_position'),
        ),
    ]
