# Generated by Django 2.2.13 on 2021-04-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0015_domainaddress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="domainaddress",
            name="first_emailed_at",
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]
