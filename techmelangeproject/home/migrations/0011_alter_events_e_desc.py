# Generated by Django 4.1.1 on 2022-12-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_contacts_delete_registration_remove_festdesc_fest_bg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='e_desc',
            field=models.CharField(max_length=1000),
        ),
    ]
