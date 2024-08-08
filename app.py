import pygame
import random

pygame.init()

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Corra Game")

PRETO =(0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

fonte = pygame.font.SysFont(None, 36)

PERSONAGEM_LARGURA, PERSONAGEM_ALTURA = 50, 50
personagem = pygame.Rect(LARGURA // 2, ALTURA // 2, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA)
personagem_cor= VERDE
poder_personagem = 1
velocidade_personagem = 5