# Generated by Django 3.2.7 on 2021-09-23 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0002_auto_20210923_1735'),
        ('Commande', '0006_auto_20210923_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article_app.article'),
        ),
    ]