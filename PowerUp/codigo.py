import pyautogui
import time
# pyautogui.click - > clica em algum lugar
# pyautogui.press - > aperta 1 tecla
# pyautogui.write - > escrever um texto
# pyauotgui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 0.5


# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
time.sleep(1)
pyautogui.write("Chrome")   
pyautogui.press("enter")


# digitar o site
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# ESPERA 3 SEGUNDOS
time.sleep(3)


# Passo 2: Fazer login
# Preencher e-mail
pyautogui.click(x=-1140, y=143)
pyautogui.write("pythonimpressionador@gmail.com")

# Preencher senha
pyautogui.press("Tab")
pyautogui.write("123456#")
pyautogui.press("enter")


# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)


# Passo 4: Cadastrar 1 produto
for linha in tabela.index: # para cada linha da minha tabela

    pyautogui.click(x=-1178, y=21)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar para o próximo campo
    marca =  str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab") # passar para o próximo campo
    tipo =  str(tabela.loc[linha, "tipo"] )   
    pyautogui.write(tipo)

    pyautogui.press("tab") # passar para o próximo campo
    categoria = str(tabela.loc[linha, "categoria"]) # string = texto -> str()
    pyautogui.write(categoria)

    pyautogui.press("tab") # passar para o próximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") # passar para o próximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") # passar para o próximo campo
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")


    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos

# nan -> Not a number (valor vazio)

# pyautogui -> Fazer automações com python

# se if ("nome") for diferente (!) ou igual (=):
# se if ("nome") for maior (>) ou ou igual (=):
# se if ("nome") for menor (<) ou igual (=):