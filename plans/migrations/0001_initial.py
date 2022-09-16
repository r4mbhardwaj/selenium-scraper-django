# Generated by Django 3.2.12 on 2022-09-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extra_data', models.TextField(null=True)),
                ('benifits', models.JSONField(null=True)),
            ],
        ),
    ]