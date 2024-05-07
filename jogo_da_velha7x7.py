import pygame
import time

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

pygame.init()

largura, altura = 700, 700
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Velha 7x7")
window.fill(branco)

espaco = largura // 7
for i in range(1, 7):
    pygame.draw.line(window, preto, (espaco * i, 0), (espaco * i, altura), 5)
    pygame.draw.line(window, preto, (0, espaco * i), (largura, espaco * i), 5)

def desenhar_x(x, y):
    pygame.draw.line(window, vermelho, (x - 50, y - 50), (x + 50, y + 50), 10)
    pygame.draw.line(window, vermelho, (x + 50, y - 50), (x - 50, y + 50), 10)

def desenhar_o(x, y):
    pygame.draw.circle(window, azul, (x, y), 50, 10)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(7):
        for j in range(4):
            if tabuleiro[i][j] == tabuleiro[i][j+1] == tabuleiro[i][j+2] == tabuleiro[i][j+3] == jogador:
                return True
            
            if tabuleiro[j][i] == tabuleiro[j+1][i] == tabuleiro[j+2][i] == tabuleiro[j+3][i] == jogador:
                return True
    for i in range(4):
        for j in range(4):
            if tabuleiro[i][j] == tabuleiro[i+1][j+1] == tabuleiro[i+2][j+2] == tabuleiro[i+3][j+3] == jogador:
                return True
    for i in range(3, 7):
        for j in range(4):
            if tabuleiro[i][j] == tabuleiro[i-1][j+1] == tabuleiro[i-2][j+2] == tabuleiro[i-3][j+3] == jogador:
                return True
    return False

def reiniciar_jogo():
    global tabuleiro, jogador_atual
    tabuleiro = [[0]*7 for _ in range(7)]  
    jogador_atual = 1
    window.fill(branco)  
    for i in range(1, 7): 
        pygame.draw.line(window, preto, (espaco * i, 0), (espaco * i, altura), 5)
        pygame.draw.line(window, preto, (0, espaco * i), (largura, espaco * i), 5)
    pygame.display.update()

tabuleiro = [[0]*7 for _ in range(7)]  
jogador_atual = 1
ultimo_reset = time.time()

terminado = False
while not terminado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminado = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not terminado:
            if pygame.mouse.get_pressed()[0]:  
                mouseX, mouseY = pygame.mouse.get_pos()
                coluna = mouseX // espaco
                linha = mouseY // espaco
                if tabuleiro[linha][coluna] == 0:  
                    tabuleiro[linha][coluna] = jogador_atual
                    if jogador_atual == 1:
                        desenhar_x(coluna * espaco + espaco // 2, linha * espaco + espaco // 2)
                        if verificar_vitoria(tabuleiro, 1):
                            print("Jogador X venceu!")
                            ultimo_reset = time.time()  
                    else:
                        desenhar_o(coluna * espaco + espaco // 2, linha * espaco + espaco // 2)
                        if verificar_vitoria(tabuleiro, -1):
                            print("Jogador O venceu!")
                            ultimo_reset = time.time()
                    jogador_atual *= -1 
    if time.time() - ultimo_reset >= 10: 
        reiniciar_jogo()  
        ultimo_reset = time.time()
    pygame.display.update()

pygame.quit()
