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

INIMIGO_LARGURA, INIMIGO_ALTURA = 50, 50
inimigo = pygame.Rect(random.randint(0, LARGURA - INIMIGO_LARGURA), random.randint(0, ALTURA - INIMIGO_ALTURA), INIMIGO_LARGURA, INIMIGO_ALTURA)
poder_inimigo = poder_personagem + 1
velocidade_inimigo = 3

ITEM_LARGURA, ITEM_ALTURA = 30, 30
item = pygame.Rect(random.randint(0, LARGURA - ITEM_LARGURA), random.randint(0, ALTURA - ITEM_ALTURA), ITEM_LARGURA, ITEM_ALTURA)
item_cor = AZUL

def desenhar_tudo():
    tela.fill(PRETO)
    pygame.draw.rect(tela, personagem_cor, personagem)
    pygame.draw.rect(tela, VERMELHO, inimigo)
    pygame.draw.rect(tela, item_cor, item)

    texto_personagem = fonte.render(f"Poder do Personagem: {poder_personagem}", True, BRANCO)
    texto_inimigo = fonte.render(f"Poder do Inimigo: {poder_inimigo}", True, BRANCO)

    tela.blit(texto_personagem, (10, 10))
    tela.blit(texto_inimigo, (10, 50))

    pygame.display.flip()

def cria_novo_inimigo():
    global inimigo, poder_inimigo
    poder_inimigo = poder_personagem + 1
    inimigo.x = random.randint(0, LARGURA - INIMIGO_LARGURA)
    inimigo.y = random.randint(0, ALTURA - INIMIGO_ALTURA)

def main():
    global poder_personagem, item
    clock =pygame.time.Clock()
    rodando = True
    game_over = False

    cria_novo_inimigo()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        if not game_over:
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_LEFT]:
                personagem.x -= velocidade_personagem
            if teclas[pygame.K_RIGHT]:
                personagem.x += velocidade_personagem
            if teclas[pygame.K_UP]:
                personagem.y -= velocidade_personagem
            if teclas[pygame.K_DOWN]:
                personagem.y += velocidade_personagem

            #movimento do inimigo em direção ao personagem
            if inimigo.x < personagem.x:
                inimigo.x += velocidade_inimigo
            elif inimigo.x > personagem.x:
                inimigo.x -= velocidade_inimigo
            
            if inimigo.y < personagem.y:
                inimigo.y += velocidade_inimigo
            elif inimigo.y > personagem.y:
                inimigo.y -= velocidade_inimigo

            if personagem.colliderect(inimigo):
                if poder_personagem >= poder_inimigo:
                    print("Você derrotou o inimgo!")
                    poder_personagem += poder_inimigo
                    cria_novo_inimigo()
                else:
                    game_over = True
                    print("Game Over")
            
            if personagem.colliderect(item):
                poder_personagem += 2
                item.x = random.randint(0, LARGURA - ITEM_LARGURA)
                item.y = random.randint(0, ALTURA - ITEM_ALTURA)
                print(f"Você encontrou um item! Seu poder agora é {poder_personagem}")
        
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


