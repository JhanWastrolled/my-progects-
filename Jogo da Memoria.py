import PySimpleGUI as sg
from random import randint
from time import sleep

sg.theme('darkamber')

def Ganha_perde(acertos = 0):
    while acertos < 9:
      numbers.append(Nums(numbers))
      numberstring = [str(a) for a in numbers]
      Anims(numberstring)       
            
            
      numberespon = [f'0{e}' for e in numberstring]
      print(Verific(numberespon))
      janela.refresh()
      if Verific(numberespon) == True:
        acertos += 1
      else:
          print('erro grotesco')
          return False
    print('ganhou')
    return True
    
        

def Nums(numbers):
    while True:
        num = randint(1, 9)
        if num not in numbers:
            break
    return num

def Anims(numberstring):
    for i in numberstring:
            janela[i].update(button_color=('gray', 'gray'))
            janela.refresh()
            sleep(0.75)
            print(i)
            janela[i].update(button_color=('black', 'black'))
            janela.refresh()
            sleep(0.25)



def Verific(numberespon):
    for i in numberespon:
      resp, _ = janela.read()
      print(resp)
      if resp != i:
        print('errou')
        return False
      else:
          print('acertou')
    return True






       


layout = [
    [sg.Button(key='1', size=(5, 3), button_color=('black', 'black')),
      sg.Button(key='2', size=(5, 3), button_color=('black', 'black')),
        sg.Button(key='3', size=(5, 3), button_color=('black', 'black')),
          sg.Column([], size=(10, 100), element_justification='c'), sg.Button(key='01', size=2), sg.Button(key='02', size=2), sg.Button(key='03', size=2)],
    [sg.Button(key='4', size=(5, 3), button_color=('black', 'black')),
      sg.Button(key='5', size=(5, 3), button_color=('black', 'black')),
        sg.Button(key='6', size=(5, 3), button_color=('black', 'black')),
          sg.Column([], size=(10, 100), element_justification='c'), sg.Button(key='04', size=2), sg.Button(key='05', size=2), sg.Button(key='06', size=2)],
    [sg.Button(key='7', size=(5, 3), button_color=('black', 'black')),
      sg.Button(key='8', size=(5, 3), button_color=('black', 'black')),
        sg.Button(key='9', size=(5, 3), button_color=('black', 'black')),
        sg.Column([], size=(10, 100), element_justification='c'), sg.Button(key='07', size=2), sg.Button(key='08', size=2), sg.Button(key='09', size=2)],
    [sg.Button('Começar', key='cmc')]
]


janela = sg.Window('Jogo da Memoria', layout)


numbers = []


while True:
    
    ev, val = janela.read()
    if ev == sg.WINDOW_CLOSED:
        break
    if ev == 'cmc':
      Ganha_perde(acertos=0)
      janela.refresh()
          
          
      
             
  
