import pygame
import time
import sys

# Charger les images pour le joueur et le boss
Boss_img = pygame.image.load('mario_nega.png')
Goomba_img = pygame.image.load('para-goomba.png')
Para_Koopa_img = pygame.image.load('para-koopa.png')

# Initialisation de Pygame
pygame.init()

# Couleurs (pour la plateforme et autres objets si nécessaire)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)         

#Police
font = pygame.font.Font(None, 36)

# Charger et jouer le son de fond
pygame.mixer.music.load('Niveau.wav')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

# Titre du jeu  
pygame.display.set_caption("RIOMA")

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
            self.taille = 95
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
        """
        if self.choix == "Bowser":
            self.vie = 5
            self.nom = "Bowser"
            self.taille = 80
            self.speed = 5
            self.jump = 15
            self.img = Para_Koopa_img
            self.gravity = 0.5"""
            
            
class Boss:
    def __init__(self,vie=5,nom="Mario",taille=90,speed=5,jump=12,direction=-1):
        self.vie = vie
        self.nom = nom
        self.taille = taille
        self.speed = speed
        self.direction = direction
        
class Son:
    def __init__(self):
        self.volume = pygame.mixer.music.get_volume()

    def changer_volume(self, niveau):
        if 0.0 <= niveau <= 1.0:
            self.volume = niveau
            pygame.mixer.music.set_volume(self.volume)
        else:
            print("Le niveau de volume doit être compris entre 0.0 et 1.0.")


choix = str(input("Choisissez un perso (Goomba/Koopa):"))
Joueur = Joueur(choix)
Joueur.perso()
Boss = Boss()
gestion_son = Son()

# Définir les dimensions de la fenêtre
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
window = pygame.display.set_mode((width, height))

velocity_y = 0
player_x, player_y = 100, height - Joueur.taille - 100

# Redimensionner les images (facultatif, si nécessaire)
Boss_img = pygame.transform.scale(Boss_img, (Boss.taille, Boss.taille))
Joueur.img = pygame.transform.scale(Joueur.img, (Joueur.taille, Joueur.taille))

# Propriétés du boss
boss_x, boss_y = width - Boss.taille - 50, height - Boss.taille - 90  # Position initiale

# Propriétés de la plateforme
platform_height = 100

def afficher_menu_volume():
    menu_running = True
    while menu_running:
        window.fill(WHITE)
        
        # Afficher les options de volume
        texte_volume = f"Volume actuel : {int(gestion_son.volume * 100)}%"
        texte_surface = font.render(texte_volume, True, BLACK)
        window.blit(texte_surface, (width // 2 - 100, height // 2 - 100))
        
        bouton_aug = pygame.Rect(width // 2 - 100, height // 2, 200, 50)
        bouton_dim = pygame.Rect(width // 2 - 100, height // 2 + 60, 200, 50)
        bouton_mute = pygame.Rect(width // 2 - 100, height // 2 + 120, 200, 50)
        
        pygame.draw.rect(window, GRAY, bouton_aug)
        pygame.draw.rect(window, GRAY, bouton_dim)
        pygame.draw.rect(window, GRAY, bouton_mute)
        
        window.blit(font.render("Volume +", True, BLACK), (width // 2 - 50, height // 2 + 10))
        window.blit(font.render("Volume -", True, BLACK), (width // 2 - 50, height // 2 + 70))
        window.blit(font.render("Mute", True, BLACK), (width // 2 - 30, height // 2 + 130))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bouton_aug.collidepoint(event.pos):
                    gestion_son.changer_volume(min(gestion_son.volume + 0.1, 1.0))
                elif bouton_dim.collidepoint(event.pos):
                    gestion_son.changer_volume(max(gestion_son.volume - 0.1, 0.0))
                elif bouton_mute.collidepoint(event.pos):
                    gestion_son.changer_volume(0.0)

def afficher_menu_principal():
    menu_running = True
    selected_player = 1  # 1 pour Mario, 2 pour un autre personnage
    bouton_largeur = 300  # Largeur uniforme des boutons
    bouton_hauteur = 60   # Hauteur uniforme des boutons
    espace_vertical = 20  # Espace vertical entre les boutons
    
    # Calculer la position de départ pour les boutons
    bouton_1_y = height // 2 - 40  # Position du premier bouton

    while menu_running:
        window.fill(WHITE)
        
        # Afficher le titre du jeu
        titre_surface = pygame.image.load("RIOMA blanc.png")
        titre_width = titre_surface.get_width()  # Obtenez la largeur du titre
        titre_x = (width - titre_width) // 2  # Calculez la position X pour centrer le titre
        window.blit(titre_surface, (titre_x, height // 5))  # Affichez le titre centré

        # Texte pour les boutons
        texte_volume = "Réglage du Volume"
        texte_personnage = "Choisir Personnage"
        texte_jouer = "Jouer"
        
        # Calculer la position pour centrer le texte sur chaque bouton
        bouton_volume = pygame.Rect(width // 2 - bouton_largeur // 2, bouton_1_y, bouton_largeur, bouton_hauteur)
        bouton_personnage = pygame.Rect(width // 2 - bouton_largeur // 2, bouton_1_y + bouton_hauteur + espace_vertical, bouton_largeur, bouton_hauteur)
        bouton_jouer = pygame.Rect(width // 2 - bouton_largeur // 2, bouton_1_y + 2 * (bouton_hauteur + espace_vertical), bouton_largeur, bouton_hauteur)

        # Dessiner les boutons avec la même taille
        pygame.draw.rect(window, GRAY, bouton_volume)
        pygame.draw.rect(window, GRAY, bouton_personnage)
        pygame.draw.rect(window, GRAY, bouton_jouer)

        # Afficher le texte centré dans chaque bouton
        window.blit(font.render(texte_volume, True, BLACK), 
                    (bouton_volume.x + (bouton_largeur - font.size(texte_volume)[0]) // 2, 
                     bouton_volume.y + (bouton_hauteur - font.size(texte_volume)[1]) // 2))
        
        window.blit(font.render(texte_personnage, True, BLACK), 
                    (bouton_personnage.x + (bouton_largeur - font.size(texte_personnage)[0]) // 2, 
                     bouton_personnage.y + (bouton_hauteur - font.size(texte_personnage)[1]) // 2))
        
        window.blit(font.render(texte_jouer, True, BLACK), 
                    (bouton_jouer.x + (bouton_largeur - font.size(texte_jouer)[0]) // 2, 
                     bouton_jouer.y + (bouton_hauteur - font.size(texte_jouer)[1]) // 2))

        # Afficher l'image du personnage sélectionné, mais cette fois en plus grand
        if selected_player == 1:
            # Afficher l'image de Mario en grand
            window.blit(Joueur.img, (width // 4 - 100, height - 250))  # Positionner à gauche
        elif selected_player == 2:
            # Afficher l'autre personnage en grand
            window.blit(Joueur.img, (3 * width // 4 - 100, height - 250))  # Positionner à droite

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_running = False
                elif event.key == pygame.K_LEFT:
                    selected_player = 1  # Sélectionner Mario
                elif event.key == pygame.K_RIGHT:
                    selected_player = 2  # Sélectionner autre personnage
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bouton_volume.collidepoint(event.pos):
                    afficher_menu_volume()
                elif bouton_personnage.collidepoint(event.pos):
                    # Permet à l'utilisateur de sélectionner le personnage avec la souris
                    selected_player = 1 if selected_player == 2 else 2
                elif bouton_jouer.collidepoint(event.pos):
                    return selected_player  # Retourner le personnage sélectionné


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
                #time.sleep(1)
                if Boss.vie == 0:
                    print("Victoire! Le boss est vaincu!")
                    running = False

            # Si le boss touche le joueur autrement
            else:
                Joueur.vie -= 1
                print("Le joueur est touché! Vies restantes:", player_lives)
                #time.sleep(1)
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



selected_player = afficher_menu_principal()

Jouer(True,False,velocity_y,player_x,player_y,boss_x, boss_y)

# Quitter Pygame
pygame.quit()   
