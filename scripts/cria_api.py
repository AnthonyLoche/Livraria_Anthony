#!/usr/bin/env python3
import os
import sys


def capitalize_nome(nome):
    return nome.capitalize()


def create_files(entidade):
    entidade_cap = capitalize_nome(entidade)

    print(f'Criando arquivos para {entidade_cap}...')

    # Diretórios
    paths = {
        "model": f"core/models/{entidade}.py",
        "serializer": f"core/serializers/{entidade}.py",
        "view": f"core/views/{entidade}.py",
    }

    # Conteúdo dos arquivos
    model_content = f"""from django.db import models

class {entidade_cap}(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
"""

    serializer_content = f"""from rest_framework.serializers import ModelSerializer
from core.models.{entidade} import {entidade_cap}

class {entidade_cap}Serializer(ModelSerializer):
    class Meta:
        model = {entidade_cap}
        fields = "__all__"
"""

    view_content = f"""from rest_framework.viewsets import ModelViewSet
from core.models.{entidade} import {entidade_cap}
from core.serializers.{entidade} import {entidade_cap}Serializer

class {entidade_cap}ViewSet(ModelViewSet):
    queryset = {entidade_cap}.objects.all()
    serializer_class = {entidade_cap}Serializer
"""

    contents = {
        paths["model"]: model_content,
        paths["serializer"]: serializer_content,
        paths["view"]: view_content,
    }

    # Cria arquivos com conteúdo
    for filepath, content in contents.items():
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Arquivo criado: {filepath}")

    print()  # Adiciona uma linha em branco antes das mensagens de atualização
    update_init(f"core/models/__init__.py", entidade, entidade_cap)
    update_init(f"core/serializers/__init__.py", entidade, f"{entidade_cap}Serializer")
    update_init(f"core/views/__init__.py", entidade, f"{entidade_cap}ViewSet")


def update_init(init_path, entidade, import_name):
    os.makedirs(os.path.dirname(init_path), exist_ok=True)

    if not os.path.exists(init_path):
        with open(init_path, 'w') as f:
            f.write(f"from .{entidade} import {import_name}\n")
    else:
        with open(init_path, 'a') as f:
            f.write(f"from .{entidade} import {import_name}\n")
    print(f"Atualizado: {init_path}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Uso: python {sys.argv[0]} <nome_da_entidade>')
        sys.exit(1)

    entidade = sys.argv[1].lower()
    create_files(entidade)
