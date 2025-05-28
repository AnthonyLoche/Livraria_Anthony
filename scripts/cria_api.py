#!/usr/bin/env python3
import os
import sys


def create_files(entidade):
    print(f'Criando e abrindo arquivos para {entidade}...')
    # Lista de comandos
    commands = [
        f'touch \
            core/models/{entidade}.py \
            core/serializers/{entidade}.py \
            core/views/{entidade}.py',
    ]

    # Executa cada comando
    for cmd in commands:
        os.system(cmd)


if __name__ == '__main__':
    ARG_COUNT = 2
    if len(sys.argv) != ARG_COUNT:
        print(f'Uso: python {sys.argv[0]} <parametro>')
        sys.exit(1)

    parametro = sys.argv[1]
    create_files(parametro)
