# Generated by Django 4.0.4 on 2022-05-08 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('product_url', models.URLField(max_length=1000, primary_key=True, serialize=False)),
                ('product_url_created_at', models.DateField()),
                ('product_url_image', models.URLField(max_length=1000)),
                ('store_url', models.URLField(max_length=1000)),
                ('total_vendas', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Produtos',
                'db_table': 'Produto',
                'ordering': ['product_url'],
            },
        ),
        migrations.CreateModel(
            name='DataConsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consult_date', models.DateField()),
                ('c', models.IntegerField()),
                ('produto', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='produtos.produtos')),
            ],
            options={
                'verbose_name_plural': 'Data de Consulta',
                'db_table': 'DataConsulta',
                'ordering': ['consult_date'],
            },
        ),
    ]
