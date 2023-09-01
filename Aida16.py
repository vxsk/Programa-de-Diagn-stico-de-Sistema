import psutil
import platform
import GPUtil
from tkinter import *


def mostrar_informacoes_cpu():

    textocpu = f'''Processador:
    Nome: {platform.processor()}
    Frequência: {psutil.cpu_freq().max:.2f} MHz
    Número de núcleos físicos: {psutil.cpu_count(logical=False)}
    Número de núcleos lógicos: {psutil.cpu_count(logical=True)}'''

    texto_informacoes_cpu["text"] = textocpu


def mostrar_informacoes_gpu():
    gpus = GPUtil.getGPUs()
    for gpu in gpus:

        textogpu = f'''GPU:
        Nome: {gpu.name}
        Memória total: {gpu.memoryTotal:.0f} MB
        Utilização de memória: {gpu.memoryUsed:.0f} MB
        Utilização da GPU: {gpu.load*100:.2f} %'''

    texto_informacoes_gpu["text"] = textogpu


def mostrar_informacoes_mem():

    mem = psutil.virtual_memory()
    textomem = f'''Memoria RAM:
    Total de memória RAM: {mem.total / (1024*1024*1024):.2f} GB
    Memória RAM disponível: {mem.available / (1024*1024*1024):.2f} GB
    Porcentagem de uso da memoria RAM: {mem.percent}%\n'''

    texto_informacoes_mem["text"] = textomem


def mostrar_informacoes_os():

        os_nome = platform.system()
        os_versao = platform.version()
        os_arquitetura = platform.architecture()[0]
        os_maquina = platform.machine()
        os_edicao = platform.win32_edition()

        textoos = f'''Sistema Operacional:
        Versão: {os_nome} {os_versao} {os_edicao}
        Arquitetura: {os_arquitetura}s
        Máquina: {os_maquina}'''

        texto_informacoes_os["text"] = textoos

janela = Tk()
janela.title("Aida16")

texto_orientacao = Label(janela, text="Suas informações estão abaixo:")
texto_orientacao.grid(column=0, row=0)

botaocpu = Button(janela, text="Mostrar informaçoes da CPU", command=mostrar_informacoes_cpu)
botaocpu.grid(column=0, row=1)

texto_informacoes_cpu = Label(janela, text="")
texto_informacoes_cpu.grid(column=0, row=2)

botaomem = Button(janela, text="Mostrar informaçoes da Memoria Ram:", command=mostrar_informacoes_mem)
botaomem.grid(column=0, row=3)

texto_informacoes_mem = Label(janela, text="")
texto_informacoes_mem.grid(column=0, row=4)

botaogpu = Button(janela, text="Mostrar informacoes da GPU:", command=mostrar_informacoes_gpu)
botaogpu.grid(column=0, row=5)

texto_informacoes_gpu = Label(janela, text="")
texto_informacoes_gpu.grid(column=0, row=6)

botaoos = Button(janela, text="Mostrar informacoes do sistema operacional:", command=mostrar_informacoes_os)
botaoos.grid(column=0, row=7)

texto_informacoes_os = Label(janela, text="")
texto_informacoes_os.grid(column=0, row=8)

janela.mainloop()
