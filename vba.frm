VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm1 
   Caption         =   "UserForm1"
   ClientHeight    =   5940
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   10800
   OleObjectBlob   =   "vba.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
' Evento que � disparado quando o formul�rio � inicializado
Private Sub UserForm_Initialize()
    ' Popula o ComboBox (DropList) com itens
    ComboBox1.AddItem "Benefici�rio 1"
    ComboBox1.AddItem "Benefici�rio 2"
    ComboBox1.AddItem "Benefici�rio 3"
    
    ' Popula o ComboBox (DropList) com itens
    ComboBox2.AddItem "Compra"
    ComboBox2.AddItem "Consumo"

    ' Popula o ComboBox (DropList) com itens
    ComboBox3.AddItem "�tico"
    ComboBox3.AddItem "Gen�rico/Similar"
    ComboBox3.AddItem "Perfumaria"
End Sub
' Evento para capturar a a��o quando o bot�o � clicado
Private Sub CommandButton1_Click()
    ' Verifica se algo foi selecionado no ComboBox
    If ComboBox1.Value <> "" Then
        ' Exibe uma mensagem com a op��o selecionada
        MsgBox "Voc� selecionou: " & ComboBox1.Value
    Else
        ' Caso nada seja selecionado, exibe uma mensagem de aviso
        MsgBox "Por favor, selecione uma op��o."
    End If
End Sub
