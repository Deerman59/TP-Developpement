import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Obtenir les dimensions de l'écran de l'utilisateur pour un affichage en plein écran
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h

# Définir la fenêtre en plein écran
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("RIOMA")

# Couleurs
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Charger les images
player_img_1 = pygame.image.load('super-mario-bros-mario.png')
player_img_2 = pygame.image.load('mario_negatif.png')
boss_img = pygame.image.load('goomba.png')

# Redimensionner les images
player_img_1 = pygame.transform.scale(player_img_1, (1200, 1600))
player_img_2 = pygame.transform.scale(player_img_2, (1200, 1600))
boss_img = pygame.transform.scale(boss_img, (80, 80))

# Propriétés du joueur
player_x, player_y = 100, height - 50 - 100
player_speed = 5
jump_height = 10
is_jumping = False
gravity = 0.5
velocity_y = 0

# Propriétés du boss
boss_x, boss_y = width - 80 - 50, height - 80 - 100
boss_speed = 4
boss_direction = -1

# Propriétés de la plateforme
platform_height = 100

# Variables du jeu
player_lives = 3
boss_lives = 3

# Police
font = pygame.font.Font(None, 36)

# Charger et jouer le son de fond
pygame.mixer.music.load('Niveau.wav')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

# Classe de gestion du son
class Son:
    def __init__(self):
        self.volume = pygame.mixer.music.get_volume()

    def changer_volume(self, niveau):
        if 0.0 <= niveau <= 1.0:
            self.volume = niveau
            pygame.mixer.music.set_volume(self.volume)
        else:
            print("Le niveau de volume doit être compris entre 0.0 et 1.0.")

gestion_son = Son()

# Fonction pour afficher le menu du volume
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

# Fonction pour afficher le menu principal avec des boutons espacés
def afficher_menu_principal():
    menu_running = True
    selected_player = 1  # 1 pour Mario, 2 pour un autre personnage
    bouton_largeur = 300  # Largeur uniforme des boutons
    bouton_hauteur = 60   # Hauteur uniforme des boutons
    espace_vertical = 20  # Espace vertical entre les boutons
    
    # Calculer la position de départ pour les boutons
    bouton_1_y = height // 2 - 40  # Position du premier bouton

    # Redimensionner les images des personnages pour les afficher en plus grand
    player_img_1_grand = pygame.transform.scale(player_img_1, (200, 200))
    player_img_2_grand = pygame.transform.scale(player_img_2, (200, 200))

    while menu_running:
        window.fill(WHITE)
        
        # Afficher le titre du jeu
        titre_surface = pygame.image.load("RIOMA.png")
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
            window.blit(player_img_1_grand, (width // 4 - 100, height - 250))  # Positionner à gauche
        elif selected_player == 2:
            # Afficher l'autre personnage en grand
            window.blit(player_img_2_grand, (3 * width // 4 - 100, height - 250))  # Positionner à droite

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


# Boucle principale du jeu
def jeu():
    running = True
    player_img = player_img_1  # Par défaut, Mario
    while running:
        window.fill(WHITE)
        
        # Dessiner la plateforme
        pygame.draw.rect(window, GREEN, (0, height - platform_height, width, platform_height))

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:  # Appuyer sur 'M' pour ouvrir le menu de volume
                    afficher_menu_volume()

        # Récupérer l'état des touches
        keys = pygame.key.get_pressed()

        # Déplacement du joueur à gauche ou à droite
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Sauter
        if not is_jumping and keys[pygame.K_SPACE]:
            is_jumping = True
            velocity_y = -jump_height

        # Gérer le saut (gravité)
        if is_jumping:
            player_y += velocity_y
            velocity_y += gravity

            if player_y >= height - 50 - platform_height:
                player_y = height - 50 - platform_height
                is_jumping = False

        # Empêcher le joueur de sortir de la fenêtre
        if player_x < 0:
            player_x = 0
        if player_x > width - 50:
            player_x = width - 50

        # Déplacement du boss
        boss_x += boss_speed * boss_direction

        # Changer la direction du boss lorsqu'il touche les bords de la fenêtre
        if boss_x <= 0 or boss_x >= width - 80:
            boss_direction *= -1

        # Dessiner le joueur et le boss
        window.blit(player_img, (player_x, player_y))
        window.blit(boss_img, (boss_x, boss_y))

        # Vérification de la collision entre le joueur et le boss
        if (player_x + 50 > boss_x and player_x < boss_x + 80 and
                player_y + 50 > boss_y and player_y < boss_y + 80):
            if player_y + 50 - 5 < boss_y:
                boss_lives -= 1
                print("Boss touché! Vies restantes:", boss_lives)
                if boss_lives == 0:
                    print("Victoire! Le boss est vaincu!")
                    running = False
            else:
                player_lives -= 1
                print("Le joueur est touché! Vies restantes:", player_lives)
                if player_lives == 0:
                    print("Game Over! Le boss a gagné.")
                    running = False

        # Afficher les vies restantes
        vies_surface = font.render(f"Vies du joueur: {player_lives} | Vies du boss: {boss_lives}", True, BLACK)
        window.blit(vies_surface, (50, 50))

        # Mettre à jour l'affichage
        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Lancer le menu principal
selected_player = afficher_menu_principal()

# Lancer le jeu
jeu()

# Quitter Pygame
pygame.quit()
sys.exit()
