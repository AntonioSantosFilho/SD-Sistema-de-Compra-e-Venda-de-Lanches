from django.core.management.base import BaseCommand
from faker import Faker
from lojaapp.models import Usuario, Vendedor, Produto, Pedido, Avaliacao, Chat, Notificacao, Pagamento
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados falsos usando o Faker'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')

        # Popula Usuarios (compradores e vendedores)
        usuarios = []
        for _ in range(10):
            usuario = Usuario.objects.create(
                nome=fake.name(),
                email=fake.email(),
                telefone=fake.phone_number(),
                is_vendedor=random.choice([True, False])
            )
            usuarios.append(usuario)

            # Cria um vendedor se o usuário for um vendedor
            if usuario.is_vendedor:
                Vendedor.objects.create(
                    usuario=usuario,
                    localizacao=fake.address(),
                    telefone=fake.phone_number(),
                    foto=None,  # Defina fotos reais se necessário
                    status=random.choice([True, False])
                )

        # Popula Produtos para cada vendedor
        vendedores = Vendedor.objects.all()
        produtos = []
        for _ in range(30):
            vendedor = random.choice(vendedores)
            produto = Produto.objects.create(
                vendedor=vendedor,
                nome=fake.word(),
                descricao=fake.sentence(),
                preco=random.uniform(10.0, 100.0),
                disponibilidade=random.choice([True, False]),
                imagem=None  # Defina imagens reais se necessário
            )
            produtos.append(produto)

        # Popula Pedidos para compradores
        compradores = Usuario.objects.filter(is_vendedor=False)
        for _ in range(20):
            comprador = random.choice(compradores)
            produto = random.choice(produtos)
            Pedido.objects.create(
                comprador=comprador,
                vendedor=produto.vendedor,
                produto=produto,
                preco_total=produto.preco,
                status=random.choice(['pendente', 'concluido']),
            )

        # Popula Avaliações
        for _ in range(15):
            produto = random.choice(produtos)
            avaliador = random.choice(compradores)
            Avaliacao.objects.create(
                produto=produto,
                avaliador=avaliador,
                nota=random.randint(1, 5),  # Nota de 1 a 5
                comentario=fake.text(),
                data_avaliacao=fake.date_time_this_year()
            )

        # Popula Chats entre vendedores e compradores
        for _ in range(10):
            comprador = random.choice(compradores)
            vendedor = random.choice(vendedores)
            Chat.objects.create(
                comprador=comprador,
                vendedor=vendedor,
                mensagem=fake.text(),
                data_horario=fake.date_time_this_year()
            )

        # Popula Notificações para usuários
        for _ in range(20):
            usuario = random.choice(usuarios)
            Notificacao.objects.create(
                usuario=usuario,
                mensagem=fake.sentence(),
                enviado_em=fake.date_time_this_year()
            )

        # Popula Pagamentos para produtos
        for _ in range(15):
            produto = random.choice(produtos)
            Pagamento.objects.create(
                produto=produto,
                tipo_pagamento=random.choice(['cartao', 'boleto']),
                pago_em=fake.date_time_this_year()
            )

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
