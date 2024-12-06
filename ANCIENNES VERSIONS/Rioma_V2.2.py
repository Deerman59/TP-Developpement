import pygame
import time
import sys

# Charger les images pour le joueur et le boss
Boss_img = pygame.image.load('mario_negatif.png')
Goomba_img = pygame.image.load('goomba.png')
Para_Goomba_img = pygame.image.load('para-goomba.png')
Para_Koopa_img = pygame.image.load('para-koopa.png')
Bowser_img = pygame.image.load('bowser.png')

# Initialisation de Pygame
pygame.init()

# Couleurs (pour la plateforme et autres objets si nécessaire)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Police
font = pygame.font.Font(None, 36)

# Charger et jouer le son de fond
pygame.mixer.music.load('musique menu.wav')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)

# Titre du jeu
pygame.display.set_caption("RIOMA")

class Joueur:
    def __init__(self, choix="", vie=0, nom="", taille=0, speed=0, jump=0, img="", gravity=0.5):
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
            self.img = Para_koopa_img
            self.gravity = 0.2
        if self.choix == "Bowser":
            self.vie = 5
            self.nom = "Bowser"
            self.taille = 160
            self.speed = 5
            self.jump = 15
            self.img = Bowser_img
            self.gravity = 0.5


class Boss:
    def __init__(self, vie=5, nom="Mario", taille=95, speed=5, jump=12, direction=-1):
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


def afficher_menu_principal():
    menu_running = True
    selected_player = None

    # Définir les dimensions des boutons
    bouton_largeur = 300
    bouton_hauteur = 60
    espace_vertical = 20
    bouton_x = (width - bouton_largeur) // 2

    while menu_running:
        window.fill(WHITE)

        # Titre
        titre_surface = font.render("RIOMA", True, BLACK)
        window.blit(titre_surface, (width // 2 - titre_surface.get_width() // 2, 100))

        # Boutons pour les personnages
        boutons = [
            pygame.Rect(bouton_x, 200, bouton_largeur, bouton_hauteur),
            pygame.Rect(bouton_x, 200 + bouton_hauteur + espace_vertical, bouton_largeur, bouton_hauteur),
            pygame.Rect(bouton_x, 200 + 2 * (bouton_hauteur + espace_vertical), bouton_largeur, bouton_hauteur),
            pygame.Rect(bouton_x, 200 + 3 * (bouton_hauteur + espace_vertical), bouton_largeur, bouton_hauteur),
        ]

        textes = ["Choisir Goomba", "Choisir Koopa", "Choisir Bowser", "Réglage Volume"]

        # Afficher les boutons et textes
        for i, bouton in enumerate(boutons):
            pygame.draw.rect(window, GRAY, bouton)
            texte_surface = font.render(textes[i], True, BLACK)
            window.blit(texte_surface, (bouton.x + (bouton_largeur - texte_surface.get_width()) // 2,
                                        bouton.y + (bouton_hauteur - texte_surface.get_height()) // 2))

        pygame.display.flip()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boutons[0].collidepoint(event.pos):
                    return "Goomba"
                elif boutons[1].collidepoint(event.pos):
                    return "Koopa"
                elif boutons[2].collidepoint(event.pos):
                    return "Bowser"
                elif boutons[3].collidepoint(event.pos):
                    afficher_menu_volume()


def afficher_menu_volume():
    menu_running = True
    while menu_running:
        window.fill(WHITE)

        texte_volume = f"Volume actuel : {int(gestion_son.volume * 100)}%"
        texte_surface = font.render(texte_volume, True, BLACK)
        window.blit(texte_surface, (width // 2 - 100, height // 2 - 100))

        boutons = [
            pygame.Rect(width // 2 - 100, height // 2, 200, 50),
            pygame.Rect(width // 2 - 100, height // 2 + 60, 200, 50),
            pygame.Rect(width // 2 - 100, height // 2 + 120, 200, 50),
        ]
        textes = ["Volume +", "Volume -", "Mute"]

        for i, bouton in enumerate(boutons):
            pygame.draw.rect(window, GRAY, bouton)
            window.blit(font.render(textes[i], True, BLACK), (bouton.x + 50, bouton.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boutons[0].collidepoint(event.pos):
                    gestion_son.changer_volume(min(gestion_son.volume + 0.1, 1.0))
                elif boutons[1].collidepoint(event.pos):
                    gestion_son.changer_volume(max(gestion_son.volume - 0.1, 0.0))
                elif boutons[2].collidepoint(event.pos):
                    gestion_son.changer_volume(0.0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu_running = False


# Définir les dimensions de la fenêtre
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
window = pygame.display.set_mode((width, height))

# Gestion du son
gestion_son = Son()

# Initialisation du personnage choisi
choix_personnage = afficher_menu_principal()
Joueur = Joueur(choix_personnage)
Joueur.perso()

# Position initiale du joueur
player_x, player_y = 100, height - Joueur.taille - 100
velocity_y = 0
is_jumping = False

# Position initiale du boss
Boss = Boss()
boss_x, boss_y = width - Boss.taille - 50, height - Boss.taille - 90

# Lancer le jeu
def Jouer(running, is_jumping, velocity_y, player_x, player_y, boss_x, boss_y, dernier_temps_perte_vie):
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

        # Vérifier si le joueur touche le sol
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

        # Collision entre le joueur et le boss
        if detecter_collision(player_x, player_y, boss_x, boss_y):
            temps_actuel = pygame.time.get_ticks()
            # Si le joueur saute sur la tête du boss
            if (player_y + Joueur.taille - 5 < boss_y + Joueur.taille) and (temps_actuel - dernier_temps_perte_vie >= delai_collision):
                Boss.vie -= 1
                dernier_temps_perte_vie = temps_actuel
                print("Boss touché! Vies restantes:", Boss.vie)
                if Boss.vie == 0:
                    print("Victoire! Le boss est vaincu!")
                    running = False

            # Si le boss touche le joueur autrement
            elif temps_actuel - dernier_temps_perte_vie >= delai_collision:
                Joueur.vie -= 1
                dernier_temps_perte_vie = temps_actuel
                print("Le joueur est touché! Vies restantes:", Joueur.vie)
                if Joueur.vie == 0:
                    print("Game Over! Le boss a gagné.")
                    running = False

        # Remplir l'écran avec une couleur blanche
        window.fill(WHITE)

        # Dessiner la plateforme
        pygame.draw.rect(window, GREEN, (0, height - platform_height, width, platform_height))

        # Dessiner le joueur (image)
        window.blit(Joueur.img, (player_x, player_y))

        # Dessiner le boss (image)
        window.blit(Boss_img, (boss_x, boss_y))

        # Afficher les vies du joueur et du boss
        texte_joueur = font.render(f"Vies Joueur: {Joueur.vie}", True, BLACK)
        texte_boss = font.render(f"Vies Boss: {Boss.vie}", True, BLACK)
        window.blit(texte_joueur, (10, 10))
        window.blit(texte_boss, (10, 50))

        # Mettre à jour l'affichage
        pygame.display.update()

        # Limiter le nombre de FPS (images par seconde)
        pygame.time.Clock().tick(60)


# Sélectionnez le personnage via le menu principal
choix = afficher_menu_principal()

# Initialisez le joueur avec le personnage choisi
joueur_actuel = Joueur(choix)  # Utilisation d'un nom distinct pour l'instance
joueur_actuel.perso()

# Lancez le jeu
Jouer(True, False, velocity_y, player_x, player_y, boss_x, boss_y, dernier_temps_perte_vie)


pygame.quit()
