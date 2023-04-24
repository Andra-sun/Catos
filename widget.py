import tkinter as tk

class VidasWidget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.lives_file = 'lives.txt'  # nome do arquivo de texto para armazenar as vidas
        self.load_lives()  # carrega o número atual de vidas
        self.create_widgets()

        # adiciona evento para quando a janela principal for fechada
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        
        # cria o widget que exibe as imagens dos corações
        self.hearts_frame = tk.Frame(self)
        self.hearts_frame.pack(side='left')
        self.heart_images = [
            tk.PhotoImage(file="gatos/corazon.gif") for _ in range(self.lives)
        ]
        for image in self.heart_images:
            tk.Label(self.hearts_frame, image=image, bg='#f9b5f9').pack(side='left')

    def lose_life(self):
        self.lives -= 1
        if self.lives >= 0:
            self.heart_images.pop()

    def load_lives(self):
        try:
            with open(self.lives_file, 'r') as f:
                self.lives = int(f.readline())
                if self.lives < 0:  # verificação adicional
                    self.lives = 7
        except (FileNotFoundError, ValueError):  # tratamento de exceções adicionais
            self.lives = 7
        
    def save_lives(self):
        with open(self.lives_file, 'w') as f:
            f.write(str(self.lives))

    def reset_lives(self):
        self.lives = 14
        self.save_lives()
        self.refresh_hearts()

    def on_close(self):
        self.master.destroy()  # fecha a janela principal
        self.reset_lives()  # reinicia a contagem de vida
