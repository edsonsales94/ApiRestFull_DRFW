# Generated by Django 4.0.6 on 2022-07-12 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_modelos_modelo_rename_produtos_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriaproduto',
            name='produtoCategoria',
        ),
        migrations.RemoveField(
            model_name='modelo',
            name='modeloProduto',
        ),
        migrations.AddField(
            model_name='produto',
            name='modeloProduto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.modelo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='produtoCategoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.categoriaproduto'),
            preserve_default=False,
        ),
    ]
