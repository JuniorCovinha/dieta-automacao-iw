import pyautogui as pa
import time
from pyscreeze import locateCenterOnScreen as lcos
from pyperclip import copy
import os

IMAGENS_DIR = r'C:\Users\Aline.Souza\PyCharmMiscProject\Imagens'

def localizar_clicar(imagem, click_type='left', retries=3, wait_time=3, confidence=0.9, teste=False):
    imagem_path = os.path.join(IMAGENS_DIR, imagem)
    for _ in range(retries):
        try:
            ximagem, yimagem = lcos(imagem_path, confidence=confidence, grayscale=False)
            if click_type == 'left':
                pa.click(ximagem, yimagem)
            elif click_type == 'right':
                pa.rightClick(ximagem, yimagem)
            elif click_type == 'move':
                pa.moveTo(ximagem, yimagem)
            return
        except Exception as e:
            print(f"Erro ao localizar a imagem {imagem} {e}")
            time.sleep(wait_time)
    if not teste:
        print(f"Falha ao localizar a imagem {imagem} após {retries} tentativas, ajuste a tela e aperte qualquer tecla")
        input()
        pa.hotkey("alt", "tab")
        ximagem, yimagem = lcos(imagem_path, confidence=confidence)
        if click_type == 'left':
            pa.click(ximagem, yimagem)
        elif click_type == 'right':
            pa.rightClick(ximagem, yimagem)

    else:
        pass

def copiar_colar(texto):
    copy(texto)
    time.sleep(0.3)
    pa.hotkey("ctrl", "v")

def funcao_input_int(mensagem):
    while True:
        numero = (input(mensagem))
        verificar_numero = numero.isnumeric()
        if verificar_numero is True:
            numero = int(numero)
            return numero

        else:
            print("\33[31m"+"Campo obrigatório, só é aceito números."+"\33[0;0m")
            time.sleep(0.3)

def gerador_etiquetas(cod, qnt):
    cod = str(cod)
    id_lote = cod[:8]
    qnt_str = str(qnt)
    quantidade_fator = qnt_str.zfill(4)
    etiqueta_completa = id_lote + quantidade_fator
    return etiqueta_completa


itens = []
pa.PAUSE = 0.9
login = "Lucas.Oliveira"
senha = "3103"
while True:
    etiqueta = funcao_input_int("Bipe o código de barras[Digite 0 para parar]: ")  # cod barras
    if etiqueta == 0:
        break
    if etiqueta > 0:
        quantidade = funcao_input_int("Digite a quantidade a ser baixada: ")
        etiqueta_atualizada = gerador_etiquetas(cod= etiqueta, qnt=quantidade)
        itens.append(etiqueta_atualizada)
localizar_clicar("IW_icone.png")
for i in itens:
    time.sleep(3)
    localizar_clicar("CodBarras.png")  #cod de barras
    copiar_colar(i)
    pa.press("enter")
    localizar_clicar("Checar.png")  #checar8013178500014

    localizar_clicar("PrimeiraLinhaDisp.png")    # 1° linha
    pa.hotkey("ctrl", "home")
    pa.press("right", presses=2)
    pa.press("backspace")
    pa.press("L", presses=6, interval=0.1)
    localizar_clicar("Dispensar.png")  #dispensar
    time.sleep(0.5)
    pa.hotkey("ctrl", "a")
    copiar_colar(login)  # ID pessoa
    localizar_clicar("Senha.png")  #senha
    copiar_colar(senha)
    time.sleep(0.5)
    localizar_clicar("OK.png")  #ok
    time.sleep(0.5)
    pa.press("enter")
pa.hotkey("alt", "tab")
protocolar = str(input("Protocolar? [S/N]"))
while protocolar not in "NnSs":
    protocolar = str(input("Apenas sim ou não! Protocolar? [S/N]"))
if protocolar in "Nn":
    print("Fim")
if protocolar in "Ss":
    volumes = int(input("Digite o número de volumes: "))
    diaent = int(input("Digite o dia da entrega: "))
    mesent = int(input("Digite o mês: "))
    pa.hotkey("alt", "tab")
    localizar_clicar("protocolos.png")  # protocolos
    time.sleep(1)
    localizar_clicar("PrimeiraLinha.png")  # 1° linha
    localizar_clicar("RegConf.png")  #reg conferencia
    pa.press("down")    #n° volumes
    pa.press("right")
    pa.press("backspace", presses=2)
    pa.PAUSE = 0.6
    copiar_colar(f"{volumes}")
    pa.press("down")
    pa.press("backspace", presses=3)
    copiar_colar(f"{diaent}/{mesent}/2025")
    pa.press("down", presses=1)
    pa.press("R", presses=2, interval=0.2)
    localizar_clicar("OK.png")
    copiar_colar(login)
    localizar_clicar("Senha.png")
    copiar_colar(senha)
    pa.press("enter", presses=2, interval=0.5)
    time.sleep(5)
    pa.press("tab", presses=5, interval=0.3)  # 1° linha
    pa.hotkey("ctrl", "home")
    localizar_clicar("Detalhes.png")   #detalhes
    pa.hotkey("alt", "tab")
    (input("Selecione os itens baixados, para continuar aperte qualquer tecla. "))
    localizar_clicar("IW_icone.png")  # abrir iw
    localizar_clicar("BarraAzul.png", click_type='right')  #linha azul
    pa.PAUSE = 0.1
    pa.press("down", presses=5)
    pa.press("right")
    pa.press("down")
    pa.press("enter")
    time.sleep(0.5)
    localizar_clicar("OK.png")  #ok
    time.sleep(0.3)
    localizar_clicar("Imprimir.png")   #imprim
    localizar_clicar("Copias.png")  #n° impress
    pa.press("backspace")
    copiar_colar("2")
    pa.press("enter")
    pa.hotkey("alt", "tab")
    prescricao= funcao_input_int("Digite a próxima prescrição: ")
    localizar_clicar("IW_icone.png")
    pa.PAUSE = 0.8
    localizar_clicar("X.png")
    localizar_clicar("Sair.png")
    time.sleep(2)
    localizar_clicar("Sair.png")
    localizar_clicar("Limpar.png")
    localizar_clicar("ID_presc.png")
    copiar_colar(prescricao)
    pa.press("enter")