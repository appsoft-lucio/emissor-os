import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def salvar_pdf(os_texto):
    # Cria o diretório onde as OSs serão salvas, se não existir
    os_dir = "os_emitidas"
    os.makedirs(os_dir, exist_ok=True)

    # Nome do arquivo com base na data e hora
    filename = os.path.join(os_dir, f"OS_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf")
    c = canvas.Canvas(filename)
    lines = os_texto.split("\n")
    y = 800  # Posição inicial no eixo Y
    for line in lines:
        c.drawString(50, y, line)
        y -= 20  # Move para a linha de baixo
    c.save()
    messagebox.showinfo("Sucesso", f"OS salva como: {filename}")

def visualizar_os():
    # Coleta os dados dos campos de entrada
    trabalhador_nome = input_trabalhador_nome.get()
    trabalhador_cnpj = input_trabalhador_cnpj.get()
    trabalhador_telefone = input_trabalhador_telefone.get()
    trabalhador_descricao = input_trabalhador_descricao.get()
    trabalhador_prazo = input_trabalhador_prazo.get()

    cliente_nome = input_cliente_nome.get()
    cliente_telefone = input_cliente_telefone.get()
    cliente_endereco = input_cliente_endereco.get()

    # Gerar o texto da OS
    os_texto = f"""
    Ordem de Serviço
    -----------------------------
    Dados do Trabalhador:
    Nome: {trabalhador_nome}
    CNPJ: {trabalhador_cnpj}
    Telefone: {trabalhador_telefone}
    Descrição do Trabalho: {trabalhador_descricao}
    Prazo: {trabalhador_prazo}

    Dados do Cliente:
    Nome: {cliente_nome}
    Telefone: {cliente_telefone}
    Endereço: {cliente_endereco}
    """

    # Exibir a prévia em uma nova janela
    janela_previa = tk.Toplevel(root)
    janela_previa.title("Prévia da Ordem de Serviço")
    janela_previa.geometry("600x400")

    texto_previa = tk.Text(janela_previa, wrap=tk.WORD, font=("Arial", 10))
    texto_previa.insert(tk.END, os_texto)
    texto_previa.config(state=tk.DISABLED)
    texto_previa.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Função para salvar e fechar
    def confirmar_e_salvar():
        salvar_pdf(os_texto)  # Aqui é onde a função de salvar é chamada
        janela_previa.destroy()

    # Botões na janela de pré-visualização
    botao_salvar = tk.Button(janela_previa, text="Salvar OS", command=confirmar_e_salvar, bg="green", fg="white")
    botao_visualizar = tk.Button(janela_previa, text="Visualizar OS", command=visualizar_os, bg="blue", fg="white")

    # Organizando os botões dentro da janela usando grid
    botao_salvar.grid(row=1, column=1, padx=10, pady=10)  # Salvar à direita
    botao_visualizar.grid(row=1, column=0, padx=10, pady=10)  # Visualizar à esquerda

# Janela principal
root = tk.Tk()
root.title("Emissor de OS")
root.geometry("400x400")

# Campos de entrada para dados do trabalhador
tk.Label(root, text="Nome do Trabalhador:").pack(pady=5)
input_trabalhador_nome = tk.Entry(root, width=40)
input_trabalhador_nome.pack(pady=5)

tk.Label(root, text="CNPJ do Trabalhador:").pack(pady=5)
input_trabalhador_cnpj = tk.Entry(root, width=40)
input_trabalhador_cnpj.pack(pady=5)

tk.Label(root, text="Telefone do Trabalhador:").pack(pady=5)
input_trabalhador_telefone = tk.Entry(root, width=40)
input_trabalhador_telefone.pack(pady=5)

tk.Label(root, text="Descrição do Trabalho:").pack(pady=5)
input_trabalhador_descricao = tk.Entry(root, width=40)
input_trabalhador_descricao.pack(pady=5)

tk.Label(root, text="Prazo para Execução:").pack(pady=5)
input_trabalhador_prazo = tk.Entry(root, width=40)
input_trabalhador_prazo.pack(pady=5)

# Campos de entrada para dados do cliente
tk.Label(root, text="Nome do Cliente:").pack(pady=5)
input_cliente_nome = tk.Entry(root, width=40)
input_cliente_nome.pack(pady=5)

tk.Label(root, text="Telefone do Cliente:").pack(pady=5)
input_cliente_telefone = tk.Entry(root, width=40)
input_cliente_telefone.pack(pady=5)

tk.Label(root, text="Endereço do Cliente:").pack(pady=5)
input_cliente_endereco = tk.Entry(root, width=40)
input_cliente_endereco.pack(pady=5)

# Botão para abrir a pré-visualização da OS
botao_visualizar_os = tk.Button(root, text="Visualizar OS", command=visualizar_os, bg="blue", fg="white")
botao_visualizar_os.pack(pady=20)

root.mainloop()
