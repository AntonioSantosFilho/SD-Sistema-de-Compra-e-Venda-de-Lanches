# Generated by Django 5.1.3 on 2024-12-08 19:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_alter_usuario_email_alter_usuario_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='registro.produto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chat',
            name='comprador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comprador_chats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedor_chats', to='registro.vendedor'),
        ),
    ]