# Generated by Django 3.0.7 on 2020-06-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0046_site_name_remove_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouppagepermission',
            name='permission_type',
            field=models.CharField(choices=[('add', 'Add/edit pages you own'), ('edit', 'Edit any page'), ('publish', 'Publish any page'), ('bulk_delete', 'Delete pages with children'), ('view', 'View any page'), ('lock', "Lock/unlock pages you've locked"), ('unlock', 'Unlock any page')], max_length=20, verbose_name='permission type'),
        ),
    ]
