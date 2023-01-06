from PySimpleGUI import PySimpleGUI as sg
#Layoult
sg.theme ('reddit')
Layoult = [
    [sg.Text('Usuário'), sg.Input(key= 'usuário', size = (20,1))],
    [sg.Text('Senha'), sg.Input(key= 'senha', password_char= '*', size = (20,1))],
    [sg.Checkbox ('Deseja salvar o login?')],
    [sg.Button ('Entrar')],
    
]
#Janelas 
janela = sg.Window ('Tela de Login', Layoult)

#Ler os eventos que acontecem na tela 
while True: 
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuário'] == 'ícaro' and valores ['senha'] == '12345':
            print ('Seja Bem-Vindo!')
