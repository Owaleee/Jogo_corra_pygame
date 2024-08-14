import pygame
import random

pygame.init()

LARGURA, ALTURA = 1366, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Corra Game")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)

fonte = pygame.font.SysFont(None, 36)

PERSONAGEM_LARGURA, PERSONAGEM_ALTURA = 50, 50

# Carregue a imagem do personagem
imagem_personagem = pygame.image.load('Player.png')
imagem_personagem = pygame.transform.scale(imagem_personagem, (PERSONAGEM_LARGURA, PERSONAGEM_ALTURA))
personagem = pygame.Rect(LARGURA // 2, ALTURA // 2, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA)

poder_personagem = 1
velocidade_personagem = 5

INIMIGO_LARGURA, INIMIGO_ALTURA = 50, 50
imagem_inimigo = pygame.image.load('Inimigo.png')
imagem_inimigo = pygame.transform.scale(imagem_inimigo, (INIMIGO_LARGURA, INIMIGO_ALTURA))

ITEM_LARGURA, ITEM_ALTURA = 30, 30
item = pygame.Rect(random.randint(0, LARGURA - ITEM_LARGURA), random.randint(0, ALTURA - ITEM_ALTURA), ITEM_LARGURA, ITEM_ALTURA)
item_cor = AZUL

# Variáveis de controle
inimigos = []
tempo_de_jogo = 0
imagem_invertida = False

def criar_inimigo():
    x = random.randint(0, LARGURA - INIMIGO_LARGURA)
    y = random.randint(0, ALTURA - INIMIGO_ALTURA)
    return pygame.Rect(x, y, INIMIGO_LARGURA, INIMIGO_ALTURA)

def desenhar_tudo():
    tela.fill(PRETO)
    tela.blit(imagem_personagem, (personagem.x, personagem.y))
    
    for inimigo in inimigos:
        tela.blit(imagem_inimigo, (inimigo.x, inimigo.y))
    
    pygame.draw.rect(tela, item_cor, item)

    texto_personagem = fonte.render(f"Poder do Personagem: {poder_personagem}", True, BRANCO)
    texto_tempo = fonte.render(f"Tempo: {tempo_de_jogo // 1000}s", True, BRANCO)

    tela.blit(texto_personagem, (10, 10))
    tela.blit(texto_tempo, (10, 50))

    pygame.display.flip()

def main():
    global poder_personagem, tempo_de_jogo, item, imagem_personagem, imagem_invertida
    clock = pygame.time.Clock()
    rodando = True
    game_over = False

    # Criar os primeiros inimigos
    for _ in range(5):
        inimigos.append(criar_inimigo())

    while rodando:
        tempo_de_jogo += clock.get_time()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        if not game_over:
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                personagem.x -= velocidade_personagem
                if not imagem_invertida:
                    imagem_personagem = pygame.transform.flip(imagem_personagem, True, False)  # Inverter horizontalmente
                    imagem_invertida = True
            elif teclas[pygame.K_RIGHT]:
                personagem.x += velocidade_personagem
                if imagem_invertida:
                    imagem_personagem = pygame.transform.flip(imagem_personagem, True, False)  # Reverter a inversão
                    imagem_invertida = False

            if teclas[pygame.K_UP]:
                personagem.y -= velocidade_personagem
            if teclas[pygame.K_DOWN]:
                personagem.y += velocidade_personagem

            # Movimento de cada inimigo em direção ao personagem
            for inimigo in inimigos:
                if inimigo.x < personagem.x:
                    inimigo.x += velocidade_personagem // 2
                elif inimigo.x > personagem.x:
                    inimigo.x -= velocidade_personagem // 2
                
                if inimigo.y < personagem.y:
                    inimigo.y += velocidade_personagem // 2
                elif inimigo.y > personagem.y:
                    inimigo.y -= velocidade_personagem // 2
                
                if personagem.colliderect(inimigo):
                    game_over = True
                    print("Game Over")

            # Colisão com o item de poder
            if personagem.colliderect(item):
                poder_personagem += 2
                item.x = random.randint(0, LARGURA - ITEM_LARGURA)
                item.y = random.randint(0, ALTURA - ITEM_ALTURA)
                print(f"Você encontrou um item! Seu poder agora é {poder_personagem}")

            # Aumentar a dificuldade ao longo do tempo
            if tempo_de_jogo % 5000 == 0:  # A cada 5 segundos
                for _ in range(3):
                    inimigos.append(criar_inimigo())

        desenhar_tudo()

        if game_over:
            texto_game_over = fonte.render("Game Over", True, BRANCO)
            tela.blit(texto_game_over, (LARGURA // 2 - texto_game_over.get_width() // 2, ALTURA // 2 - texto_game_over.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            rodando = False
        
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
