# Generated by Django 3.2.8 on 2021-11-21 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_alter_topologyimages_topology_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topology_image', models.FileField(blank=True, null=True, upload_to='network_topology/%Y/%m/%d/')),
            ],
        ),
        migrations.RemoveField(
            model_name='topologyimages',
            name='topology_image',
        ),
        migrations.AddField(
            model_name='topologyimages',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images_svg', to='network.imagemodel'),
        ),
    ]
