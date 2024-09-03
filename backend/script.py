# -*- coding: utf-8 -*-
import os
import subprocess


class runBackend():
    def __init__(self):
        # Define o diretório de trabalho
        work_dir = r'C:\temp'

        # Comando Abaqus a ser executado
        abaqus_command = r'abaqus cae noGUI=S:/Junior/Abaqus+Python/PythonScriptforAbaqus/backend/main.py'

        # Muda para o diretório especificado
        os.chdir(work_dir)

        # Executa o comando Abaqus
        result = subprocess.run(abaqus_command, shell=True, check=True)

        # Verifica o retorno do comando
        if result.returncode == 0:
            print("Comando executado com sucesso!")
        else:
            print("Ocorreu um erro ao executar o comando.")
        

# run = runBackend()

