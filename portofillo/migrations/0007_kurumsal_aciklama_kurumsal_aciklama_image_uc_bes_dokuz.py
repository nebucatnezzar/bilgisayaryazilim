# Generated by Django 3.2.4 on 2022-09-17 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofillo', '0006_auto_20220918_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurumsal_aciklama',
            name='kurumsal_aciklama_image_uc_bes_dokuz',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
    ]
