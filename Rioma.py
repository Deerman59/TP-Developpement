import pygame
import time

# Charger les images pour le joueur et le boss
Boss_img = pygame.image.load('mario_negatif.png')
Goomba_img = pygame.image.load('para-goomba.png')
Para_Koopa_img = pygame.image.load('para-koopa.png')

class Joueur:
    def __init__(self,choix="",vie=0,nom="",taille=0,speed=0,jump=0,img="",gravity=0.5):
        self.choix = choix
        self.vie = vie
        self.nom = nom
        self.taille = taille
        self.speed = speed
        self.jump = jump
        self.img = img
        self.gravity = gravity
    def perso(self):
        if self.choix == "Goomba":
            self.vie = 5
            self.nom = "Goomba"
            self.taille = 100
            self.speed = 5
            self.jump = 13
            self.img = Goomba_img
            self.gravity = 0.5
        if self.choix == "Koopa":
            self.vie = 3
            self.nom = "Para-Koopa"
            self.taille = 80
            self.speed = 5
            self.jump = 15
            self.img = Para_Koopa_img
            self.gravity = 0.2
    
        
class Boss:
    def __init__(self,vie=5,nom="Mario",taille=75,speed=5,jump=12,direction=-1):
        self.vie = vie
        self.nom = nom
        self.taille = taille
        self.speed = speed
        self.direction = direction


choix = str(input("Choisissez un perso (Goomba/Koopa):"))
Joueur = Joueur(choix)
Joueur.perso()
Boss = Boss()
print(Joueur.nom)
print(Boss.nom)

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
width, height = 1600, 900
window = pygame.display.set_mode((width, height))

# Titre du jeu  
pygame.display.set_caption("Niveau de Boss - Mario")

# Couleurs (pour la plateforme et autres objets si nécessaire)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)          

velocity_y = 0
player_x, player_y = 100, height - Joueur.taille - 100

# Redimensionner les images (facultatif, si nécessaire)
Boss_img = pygame.transform.scale(Boss_img, (Boss.taille, Boss.taille))
Joueur.img = pygame.transform.scale(Joueur.img, (Joueur.taille, Joueur.taille))

# Propriétés du boss
boss_x, boss_y = width - Boss.taille - 50, height - Boss.taille - 100  # Position initiale

# Propriétés de la plateforme
platform_height = 100

def Jouer(running,is_jumping,velocity_y,player_x,player_y,boss_x, boss_y):
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False               
        # Récupérer l'état des touches
        keys = pygame.key.get_pressed()

        # Déplacement du joueur à gauche ou à droite
        if keys[pygame.K_LEFT]:
            player_x -= Joueur.speed
        if keys[pygame.K_RIGHT]:
            player_x += Joueur.speed

        # Sauter
        if not is_jumping and keys[pygame.K_SPACE]:
            is_jumping = True
            velocity_y = -Joueur.jump

        # Gérer le saut (gravité)
        if is_jumping:
            player_y += velocity_y
            velocity_y += Joueur.gravity

        if player_y >= height - Joueur.taille - platform_height:
            player_y = height - Joueur.taille - platform_height
            is_jumping = False

        # Empêcher le joueur de sortir de la fenêtre
        if player_x < 0:
            player_x = 0
        if player_x > width - Joueur.taille:
            player_x = width - Joueur.taille

        # Déplacement du boss
        boss_x += Boss.speed * Boss.direction

        # Changer la direction du boss lorsqu'il touche les bords de la fenêtre
        if boss_x <= 0 or boss_x >= width - Boss.taille:
            Boss.direction *= -1

        # Vérification de la collision entre le joueur et le boss (sauter sur la tête)
        if (player_x + Joueur.taille > boss_x and player_x < boss_x + Boss.taille and player_y + Joueur.taille > boss_y and player_y < boss_y + Boss.taille):
            # Si le joueur saute sur le boss
            if player_y + Joueur.taille - 5 < boss_y + Joueur.taille:
                Boss.vie -= 1
                print("Boss touché! Vies restantes:", Boss.vie)
                if Boss.vie == 0:
                    print("Victoire! Le boss est vaincu!")
                    running = False

            # Si le boss touche le joueur autrement
            else:
                Joueur.vie -= 1
                print("Le joueur est touché! Vies restantes:", player_lives)
                if Joueur.vie == 0:
                    print("Game Over! Le boss a gagné.")
                    running = False

        # Remplir l'écran avec une couleur blanche
        window.fill(WHITE)

        # Dessiner la plateforme
        pygame.draw.rect(window, GREEN, (0, height - platform_height, width, platform_height))

        # Dessiner le joueur (image à la place du rectangle)
        window.blit(Joueur.img, (player_x, player_y))

        # Dessiner le boss (image à la place du rectangle)
        window.blit(Boss_img, (boss_x, boss_y))

        # Mettre à jour l'affichage
        pygame.display.update()

        # Limiter le nombre de FPS (images par seconde)
        pygame.time.Clock().tick(90)


Jouer(True,False,velocity_y,player_x,player_y,boss_x, boss_y)

# Quitter Pygame
pygame.quit()   
