# Generated by Django 5.1.1 on 2024-09-29 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponibilidade', models.BooleanField(default=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produtos/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='usuarios/')),
                ('is_vendedor', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pagamento', models.CharField(choices=[('cartao', 'Cartão de Crédito'), ('boleto', 'Boleto Bancário')], max_length=50)),
                ('pago_em', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('enviado_em', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveIntegerField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('data_avaliacao', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.produto')),
                ('avaliador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='vendedores/')),
                ('status', models.BooleanField(default=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.vendedor'),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('concluido', 'Concluído')], max_length=50)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.produto')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.usuario')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('data_horario', models.DateTimeField(auto_now_add=True)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.usuario')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.vendedor')),
            ],
        ),
    ]