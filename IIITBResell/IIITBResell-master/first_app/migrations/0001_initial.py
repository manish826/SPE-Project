# Generated by Django 2.1.7 on 2019-04-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=120)),
                ('Category', models.CharField(choices=[('sport', 'SPORT'), ('electronic', 'ELECTRONIC'), ('other', 'OTHER')], default='other', max_length=120)),
                ('Description', models.CharField(max_length=120)),
                ('Price', models.PositiveIntegerField()),
                ('Negotiation', models.CharField(max_length=120)),
                ('Picture', models.ImageField(null=True, upload_to='product/img/')),
            ],
        ),
    ]
