# Generated by Django 4.2.3 on 2023-07-17 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fadname', models.CharField(max_length=100)),
                ('image_url', models.TextField()),
                ('description', models.TextField()),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fadname', to='nostaldja.decades')),
            ],
        ),
    ]
