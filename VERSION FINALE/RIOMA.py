import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Charger les images pour le joueur et le boss
Boss_imgG = pygame.image.load('Images/mario négatif reverse.png')
Boss_imgD = pygame.image.load('Images/mario négatif.png')
Boss_imgDH = pygame.image.load('Images/mario négatif jumping.png')
Boss_imgGH = pygame.image.load('Images/mario négatif reverse jumping.png')
Goomba_img = pygame.image.load('Images/para-goomba.png')
Goomba_imgD = pygame.image.load('Images/para-goomba right looking.png')
Goomba_imgG = pygame.image.load('Images/para-goomba left looking.png')
Goomba_imgH = pygame.image.load('Images/para-goomba jumping.png')
Para_Koopa_imgD = pygame.image.load('Images/para-koopa.png')
Para_Koopa_imgG = pygame.image.load('Images/para-koopa reverse.png')
Para_Koopa_imgGH = pygame.image.load('Images/para-koopa jumping reverse.png')
Para_Koopa_imgDH = pygame.image.load('Images/para-koopa jumping.png')
Bowser_imgD = pygame.image.load('Images/bowser.png')
Bowser_imgG = pygame.image.load('Images/bowser reverse.png')
Bowser_imgGH = pygame.image.load('Images/bowser reverse jumping.png')
Bowser_imgDH = pygame.image.load('Images/bowser jumping.png')
Chomp_imgG = pygame.image.load('Images/chomp reverse.png')
Chomp_imgD = pygame.image.load('Images/chomp.png')
Chomp_imgGH = pygame.image.load('Images/chomp reverse jumping.png')
Chomp_imgDH = pygame.image.load('Images/chomp jumping.png')
Boo_imgG = pygame.image.load('Images/boo reverse.png')
Boo_imgD = pygame.image.load('Images/boo.png')
Toad_img = pygame.image.load('Images/toad négatif.png')
Boss_song_jump_S = 'Sons/rioma jump.wav'
Bowser_song_jump_S = 'Sons/bowser jump.wav'
GoombaKoopaChomp_S = 'Sons/koopagoombachomp jump.wav'
Boo_song_jump_S = 'Sons/boo jump.wav'
PV0 = pygame.image.load('Images/barre de vie 0.png')
PV1 = pygame.image.load('Images/barre de vie 1.png')
PV2 = pygame.image.load('Images/barre de vie 2.png')
PV3 = pygame.image.load('Images/barre de vie 3.png')
PV4 = pygame.image.load('Images/barre de vie 4.png')
PV5 = pygame.image.load('Images/barre de vie 5.png')
PV6 = pygame.image.load('Images/barre de vie 6.png')
PVB0 = pygame.image.load('Images/barre de vie 6.png')
PVB1 = pygame.image.load('Images/barre de vie 5.png')
PVB2 = pygame.image.load('Images/barre de vie 4.png')
PVB3 = pygame.image.load('Images/barre de vie 3.png')
PVB4 = pygame.image.load('Images/barre de vie 2.png')
PVB5 = pygame.image.load('Images/barre de vie 1.png')
PVB6 = pygame.image.load('Images/barre de vie 0.png')

# Couleurs (pour la plateforme et autres objets si nécessaire)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)        

# Police
police = pygame.font.Font(None, 36)

# Charger et jouer le son de fond
pygame.mixer.music.load('Sons/musique menu.wav')
Boss_song_jump = pygame.mixer.Sound(Boss_song_jump_S)
Bowser_song_jump = pygame.mixer.Sound(Bowser_song_jump_S)
GoombaKoopaChomp = pygame.mixer.Sound(GoombaKoopaChomp_S)
Boo_song_jump = pygame.mixer.Sound(Boo_song_jump_S)
pygame.mixer.Sound.set_volume(Boss_song_jump, 0.2)
pygame.mixer.Sound.set_volume(Boo_song_jump, 0.2)
pygame.mixer.Sound.set_volume(Bowser_song_jump, 0.2)
pygame.mixer.Sound.set_volume(GoombaKoopaChomp, 0.2)
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)
fond = pygame.image.load('Fonds/backgroundNiveau.png')
fond_menu = pygame.image.load('Fonds/backgroundMenu.png')
fond_victoire = pygame.image.load('Fonds/Victory screen.png')
fond_défaite = pygame.image.load('Fonds/Defeat screen.png')

# Titre du jeu pour la fenêtre dans la barre des tâches
pygame.display.set_caption("RIOMA")

# Classe Joueur
class Joueur:
    
    def __init__(self,choix="",vie=0,nom="",taille=0,speed=0,jump=0,song_jump="",imgD="",imgDH="",imgG="",imgGH="",gravity=0.5):
        self.choix = choix
        self.vie = vie
        self.nom = nom
        self.taille = taille
        self.speed = speed
        self.jump = jump
        self.song_jump = song_jump
        self.imgD = imgD
        self.imgG = imgG
        self.imgDH = imgDH
        self.imgGH = imgGH
        self.gravity = gravity
        
    def perso(self):
        if self.choix == "Para-Goomba":
            self.vie = 6
            self.nom = "Para-Goomba"
            self.taille = 95
            self.speed = 10
            self.jump = 13
            self.song_jump = GoombaKoopaChomp
            self.imgD = Goomba_imgD
            self.imgG = Goomba_imgG
            self.imgDH = Goomba_imgH
            self.imgGH = Goomba_imgH
            self.gravity = 0.5
        if self.choix == "Para-Koopa":
            self.vie = 3
            self.nom = "Para-Koopa"
            self.taille = 80
            self.speed = 10
            self.jump = 28
            self.song_jump = GoombaKoopaChomp
            self.imgD = Para_Koopa_imgD
            self.imgG = Para_Koopa_imgG
            self.imgDH = Para_Koopa_imgDH
            self.imgGH = Para_Koopa_imgGH
            self.gravity = 1
        if self.choix == "Bowser":
            self.vie = 6
            self.nom = "Bowser"
            self.taille = 160
            self.speed = 8.5
            self.jump = 15
            self.song_jump = Bowser_song_jump
            self.imgD = Bowser_imgD
            self.imgG = Bowser_imgG
            self.imgDH = Bowser_imgDH
            self.imgGH = Bowser_imgGH
            self.gravity = 0.5
        if self.choix == "Chomp":
            self.vie = 3
            self.nom = "Chomp"
            self.taille = 120
            self.speed = 15
            self.jump = 15
            self.song_jump = GoombaKoopaChomp
            self.imgD = Chomp_imgD
            self.imgG = Chomp_imgG
            self.imgDH = Chomp_imgDH
            self.imgGH = Chomp_imgGH
            self.gravity = 0.5
        if self.choix == "Boo":
            self.vie = 3
            self.nom = "Boo"
            self.taille = 80
            self.speed = 10
            self.jump = 30
            self.song_jump = Boo_song_jump
            self.imgD = Boo_imgD
            self.imgG = Boo_imgG
            self.imgDH = Boo_imgD
            self.imgGH = Boo_imgG
            self.gravity = 1
            
# Classe Boss
class Boss:
    
    def __init__(self,vie=6,nom="Rioma",taille=90,speed=10,jump=15,direction=-1,gravity=0.5):
        self.vie = vie
        self.nom = nom
        self.taille = taille
        self.speed = speed
        self.jump = jump
        self.song_jump = Boss_song_jump
        self.direction = direction
        self.imgD = Boss_imgD
        self.imgG = Boss_imgG
        self.imgDH = Boss_imgDH
        self.imgGH = Boss_imgGH
        self.gravity = gravity

# Classe Toad
class Toad:
    
    def __init__(self,vie=1,nom="Toad",taille=70,speed=9,jump=1,direction=-1,gravity=0.5):
        self.vie = vie
        self.nom = nom
        self.taille = taille
        self.speed = speed
        self.jump = jump
        self.song_jump = Boss_song_jump
        self.direction = direction
        self.img = Toad_img
        self.gravity = gravity

# Classe Son
class Son:
    
    def __init__(self):
        self.volume = pygame.mixer.music.get_volume()

    def changer_volume(self, niveau):
        if 0.0 <= niveau <= 1.0:
            self.volume = niveau
            pygame.mixer.music.set_volume(self.volume)


Boss = Boss()
Toad = Toad()
gestion_son = Son()


# Fonction pour afficher le menu volume
def afficher_menu_volume():
    volume_actif = True
    volume = 50  # 50 % par défaut
    son = Son()  # Crée une instance de la classe Son
    son.changer_volume(volume / 100.0)  # Initialisation du volume au niveau de 50%

    while volume_actif:
        window.fill(BLACK)

        # Afficher le texte du volume
        police = pygame.font.Font(None, 50)
        texte_volume = police.render(f"Volume : {volume}%", True, WHITE)
        window.blit(texte_volume, (width // 2 - texte_volume.get_width() // 2, height // 2 - 50))

        # Instructions pour ajuster le volume
        texte_instruction = police.render("Appuyez sur Haut/Bas pour ajuster", True, WHITE)
        window.blit(texte_instruction, (width // 2 - texte_instruction.get_width() // 2, height // 2 + 50))

        # Instruction pour revenir
        texte_retour = police.render("Appuyez sur Echap pour revenir", True, WHITE)
        window.blit(texte_retour, (width // 2 - texte_retour.get_width() // 2, height // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    volume_actif = False
                elif event.key == pygame.K_UP and volume < 100:
                    volume += 10
                    son.changer_volume(volume / 100.0)  # Changer le volume
                elif event.key == pygame.K_DOWN and volume > 0:
                    volume -= 10
                    son.changer_volume(volume / 100.0)  # Changer le volume

# Fonction pour afficher le menu pause
def afficher_menu_pause():
    pause_actif = True
    while pause_actif:
        window.fill(BLACK)
        police = pygame.font.Font(None, 50)

        texte_reprendre = police.render("R - Reprendre le jeu", True, WHITE)
        texte_volume = police.render("M - Changer le volume", True, WHITE)

        window.blit(texte_reprendre, (width // 2 - texte_reprendre.get_width() // 2, height // 2 - 50))
        window.blit(texte_volume, (width // 2 - texte_volume.get_width() // 2, height // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pause_actif = False
                elif event.key == pygame.K_m:
                    afficher_menu_volume()
                    

# Fonction pour afficher le menu quitter
def afficher_menu_quitter():
    quitter_actif = True
    while quitter_actif:
        window.fill(BLACK)
        police = pygame.font.Font(None, 50)

        texte_confirmer = police.render("Voulez-vous quitter ?", True, WHITE)
        texte_oui = police.render("O - Oui", True, WHITE)
        texte_non = police.render("N - Non", True, WHITE)

        window.blit(texte_confirmer, (width // 2 - texte_confirmer.get_width() // 2, height // 2 - 50))
        window.blit(texte_oui, (width // 2 - texte_oui.get_width() // 2, height // 2 + 10))
        window.blit(texte_non, (width // 2 - texte_non.get_width() // 2, height // 2 + 70))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_n:
                    quitter_actif = False
                  
                  
def afficher_menu_principal():
    menu_actif = True
    while menu_actif:
        # Effacer l'écran et afficher l'arrière-plan du menu
        window.blit(fond_menu, (0, 0))

        # Charger et afficher l'image "RIOMA blanc.png"
        image_rioma = pygame.image.load("Images/RIOMA blanc.png")
        window.blit(image_rioma, (width // 2 - image_rioma.get_width() // 2, 100)) 

        # Texte "Menu Principal" sous l'image, avec plus d'espace
        police_titre = pygame.font.Font(None, 80)
        titre = police_titre.render("Menu Principal", True, WHITE)
        window.blit(titre, (width // 2 - titre.get_width() // 2, image_rioma.get_height() + 150))

        # Dessiner le bouton "Jouer"
        bouton_jouer_rect = pygame.Rect(width // 2 - 100, image_rioma.get_height() + 350, 200, 50) 
        pygame.draw.rect(window, WHITE, bouton_jouer_rect)
        police_bouton = pygame.font.Font(None, 50)
        texte_bouton = police_bouton.render("Jouer", True, BLACK)
        window.blit(texte_bouton, (bouton_jouer_rect.x + 50, bouton_jouer_rect.y + 5))

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bouton_jouer_rect.collidepoint(event.pos):
                    return afficher_menu_personnages()

        pygame.display.flip()
        
def afficher_tutoriel():
    tutoriel_actif = True

    # Texte explicatif du tutoriel
    titre_tutoriel = "Tutoriel :"
    texte_tutoriel = [
        "Bienvenue dans Rioma !",
        "- Utilisez Q et D pour vous déplacer",
        "- Maintenez la touche SHIFT gauche si vous souhaitez aller plus vite",
        "- Appuyez sur la barre d'espace pour sauter",
        "- La touche M permet d'afficher le Menu pause et de modifier le son",
        "- Avec la touche échap, il est également possible de quitter le jeu",
        "- Évitez de vous faire toucher par les ennemis",
        "- Votre objectif est de sauter sur la tête des ennemis pour qu'ils perdent de la vie...",
        "",
        "Bonne chance !",
    ]

    # Bouton "J'ai compris !"
    bouton_texte = "J'ai compris !"
    bouton_largeur = 200
    bouton_hauteur = 50

    while tutoriel_actif:
        # Effacer l'écran
        window.fill(BLACK)

        # Afficher le titre
        police_titre = pygame.font.Font(None, 60)
        titre = police_titre.render(titre_tutoriel, True, WHITE)
        window.blit(titre, (width // 2 - titre.get_width() // 2, 50))

        # Afficher le texte explicatif
        police_texte = pygame.font.Font(None, 40)
        y_texte = 150
        for ligne in texte_tutoriel:
            if ligne in ["Bienvenue dans Rioma !", "Bonne chance !"]:
                # Centrer ces phrases spécifiques
                texte = police_texte.render(ligne, True, WHITE)
                window.blit(texte, (width // 2 - texte.get_width() // 2, y_texte))  # Centrer horizontalement
            else:
                # Aligner les autres lignes à gauche
                texte = police_texte.render(ligne, True, WHITE)
                window.blit(texte, (200, y_texte))  # Aligner à gauche
            y_texte += 50  # Espace vertical entre les lignes

        # Dessiner le bouton "J'ai compris !"
        x_bouton = (width - bouton_largeur) // 2
        y_bouton = y_texte + 50
        bouton_rect = pygame.Rect(x_bouton, y_bouton, bouton_largeur, bouton_hauteur)
        pygame.draw.rect(window, WHITE, bouton_rect)

        # Ajouter le texte sur le bouton
        texte_bouton = police_texte.render(bouton_texte, True, BLACK)
        bouton_texte_x = x_bouton + (bouton_largeur - texte_bouton.get_width()) // 2
        bouton_texte_y = y_bouton + (bouton_hauteur - texte_bouton.get_height()) // 2
        window.blit(texte_bouton, (bouton_texte_x, bouton_texte_y))

        pygame.display.flip()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bouton_rect.collidepoint(event.pos):
                    tutoriel_actif = False  # Fermer le tutoriel


def afficher_menu_personnages():
    menu_actif = True

    personnages = [
        {"nom": "Para-Goomba", "image": Goomba_imgD},
        {"nom": "Para-Koopa", "image": Para_Koopa_imgD},
        {"nom": "Bowser", "image": Bowser_imgD},
        {"nom": "Chomp", "image": Chomp_imgD},
        {"nom": "Boo", "image": Boo_imgD},
    ]

    while menu_actif:
        # Effacer l'écran
        window.blit(fond_menu, (0, 0))

        # Texte "Choisir un Personnage"
        police_titre = pygame.font.Font(None, 70)
        titre = police_titre.render("Choisir un Personnage", True, WHITE)
        window.blit(titre, (width // 2 - titre.get_width() // 2, 50))

        # Afficher les personnages en grille
        marge = 20
        taille_case = 150
        x_depart = (width - (taille_case + marge) * 3) // 2
        y_depart = 150
        for i, personnage in enumerate(personnages):
            x = x_depart + (i % 3) * (taille_case + marge)
            y = y_depart + (i // 3) * (taille_case + marge)
            case_rect = pygame.Rect(x, y, taille_case, taille_case)

            # Dessiner le cadre
            pygame.draw.rect(window, WHITE, case_rect, 2)

            # Afficher l'image
            image_redim = pygame.transform.scale(personnage["image"], (taille_case - 10, taille_case - 10))
            window.blit(image_redim, (x + 5, y + 5))

            # Afficher le nom
            police_nom = pygame.font.Font(None, 30)
            texte_nom = police_nom.render(personnage["nom"], True, WHITE)
            texte_x = x + (taille_case - texte_nom.get_width()) // 2
            texte_y = y + taille_case
            window.blit(texte_nom, (texte_x, texte_y))

        pygame.display.flip()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, personnage in enumerate(personnages):
                    x = x_depart + (i % 3) * (taille_case + marge)
                    y = y_depart + (i // 3) * (taille_case + marge)
                    case_rect = pygame.Rect(x, y, taille_case, taille_case)
                    if case_rect.collidepoint(event.pos):
                        return personnage["nom"]  # Retourner le nom du personnage sélectionné



# Vérification de la collision entre le joueur et le boss (sauter sur la tête)
def detecter_collision():
    global player_x
    global player_y
    global boss_x
    global boss_y
    if (player_x + Joueur.taille > boss_x and player_x < boss_x + Boss.taille and player_y + Joueur.taille > boss_y and player_y < boss_y + Boss.taille):
        return True
    else:
        return False
    
def detecter_collision_Toad():
    global player_x
    global player_y
    global boss_x
    global boss_y
    if (player_x + Joueur.taille > toad_x and player_x < toad_x + Toad.taille and player_y + Joueur.taille > toad_y and player_y < toad_y + Toad.taille):
        return True
    else:
        return False

def Jouer():
   # Initialisez le jeu avec le personnage sélectionné
    running = True
    is_jumping = False
    is_jumping_B = False
    is_jumping_T = False
    visible_J = True
    visible_B = True
    cligno_B = False
    cligno_J = False
    img_J_R = False
    img_J_L = False
    Toad_spawn = False
    Toad_touché = False
    Nb_Toad = 0
    velocity_y_T = -Toad.jump
    global velocity_y, velocity_y_B
    global player_x, player_y
    global boss_x, boss_y
    global toad_x, toad_y
    global dernier_temps_perte_vie, dernier_temps_perte_vie_T
    global clignotement_actif, temps_debut_clignotement, duree_clignotement
    global tpsJR, tpsJL, tpsTM, tpsTS, tpsT
    global tps_chg, tps_avt_chg
    while running:
        window.blit(fond, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    afficher_menu_pause()
                elif event.key == pygame.K_ESCAPE:
                    afficher_menu_quitter()
        
        # Récupérer l'état des touches
        keys = pygame.key.get_pressed()
        # Déplacement du joueur à gauche ou à droite
        if keys[pygame.K_q] and not keys[pygame.K_LSHIFT]:
            player_x -= Joueur.speed
        if keys[pygame.K_d] and not keys[pygame.K_LSHIFT]:
            player_x += Joueur.speed
        if keys[pygame.K_q] and keys[pygame.K_LSHIFT]:
            player_x -= Joueur.speed*1.6
        if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
            player_x += Joueur.speed*1.6

        # Sauter
        if not is_jumping and keys[pygame.K_SPACE]:
            is_jumping = True
            pygame.mixer.Sound.play(Joueur.song_jump)
            velocity_y = -Joueur.jump

        # Gérer le saut (gravité)
        if is_jumping:
            player_y += velocity_y
            velocity_y += Joueur.gravity
        if player_y >= height - Joueur.taille - platform_height:
            player_y = height - Joueur.taille - platform_height
            is_jumping = False

        # Empêcher le joueur de sortir de la fenêtre
        if player_x < 45:
            player_x = 45
        if player_x > width - 45 - Joueur.taille:
            player_x = width - 45 - Joueur.taille

        # Déplacement du boss
        boss_x += Boss.speed * Boss.direction
        
        tps_avt_chg = pygame.time.get_ticks()
        
        if boss_x > player_x and tps_chg < tps_avt_chg-1500:
            tps_chg = pygame.time.get_ticks()
            Boss.direction = -1
        if boss_x < player_x and tps_chg < tps_avt_chg-1500:
            tps_chg = pygame.time.get_ticks()
            Boss.direction = 1

        # Changer la direction du boss lorsqu'il touche les bords de la fenêtre
        if boss_x <= 45 or boss_x >= width - 45 - Boss.taille:
            Boss.direction *= -1
        
        if not is_jumping_B and random.randint(0, 400) == 400 :
            is_jumping_B = True
            pygame.mixer.Sound.play(Boss.song_jump)
            velocity_y_B = -Boss.jump
        
        if is_jumping_B:
            boss_y += velocity_y_B
            velocity_y_B += Boss.gravity
        if boss_y >= height - Boss.taille - platform_height:
            boss_y = height - Boss.taille - platform_height
            is_jumping_B = False
            
        if Boss.vie <= 3 and Nb_Toad <= 5 and tpsTM+3000 < tpsTS:
            Toad_spawn = True
            is_jumping_T = True
            toad_x += Toad.speed * Toad.direction
        
        if Toad_spawn == True :
            window.blit(Toad.img, (toad_x, toad_y))
            
        if is_jumping_T:
            toad_y += velocity_y_T
            velocity_y_T += Toad.gravity
        if toad_y >= height - Toad.taille - platform_height:
            toad_y = height - Toad.taille - platform_height
            is_jumping_T = False
        
        tpsTS = pygame.time.get_ticks()
        
        if toad_x <= 45 or toad_x >= width - 45 - Toad.taille and Toad_spawn == True and is_jumping_T == False and tpsTM > 4500:
            Toad.direction *= -1
            
        if Toad_spawn == True and Toad_touché == True and tpsTM+3000 < tpsTS:
            Toad_spawn = False
            Toad_touché = False
            velocity_y_T = -Toad.jump
            toad_x, toad_y = width - 40, height - 680
            Nb_Toad += 1
            tpsTM = pygame.time.get_ticks()
            
            
        if detecter_collision():
            temps_actuel = pygame.time.get_ticks()
            if (player_y + Joueur.taille < boss_y + Boss.taille -50) and (temps_actuel - dernier_temps_perte_vie >= delai_collision):
                    Boss.vie -= 1
                    dernier_temps_perte_vie = temps_actuel
                    cligno_B = True
                    clignotement_actif = True  # Activer le mode clignotement
                    temps_debut_clignotement = temps_actuel  # Enregistrer le début du clignotement
                    if Boss.vie == 0:
                        # Affichage de l'écran de victoire quand la vie du boss atteint 0
                        print("Victoire ! Le boss est vaincu !")
                        victoire_rect = fond_victoire.get_rect(center=(width // 2, height // 2))
                        window.blit(fond_victoire, victoire_rect.topleft)
                        pygame.display.update()
                        pygame.mixer.music.load('Sons/Victory theme.mp3')
                        pygame.mixer.music.play(1)
                        pygame.time.delay(5000)
                        running = False

            # Si le boss touche le joueur autrement
            elif temps_actuel - dernier_temps_perte_vie >= delai_collision:
                Joueur.vie -= 1
                dernier_temps_perte_vie = temps_actuel
                cligno_J = True
                clignotement_actif = True  # Activer le mode clignotement
                temps_debut_clignotement = temps_actuel  # Enregistrer le début du clignotement
                if Joueur.vie == 0:
                    # Affichage de l'écran de défaite quand la vie du joueur atteint 0
                    print("Game Over ! Le boss t'as tué...")
                    defaite_rect = fond_défaite.get_rect(center=(width // 2, height // 2))
                    window.blit(fond_défaite, defaite_rect.topleft)
                    pygame.display.update()
                    pygame.mixer.music.load('Sons/Defeat theme.mp3')
                    pygame.mixer.music.play(1)
                    pygame.time.delay(5000)
                    running = False
                    
        if detecter_collision_Toad():
            temps_actuel = pygame.time.get_ticks()
            if (player_y + Joueur.taille < toad_y + Toad.taille -50) and (temps_actuel - dernier_temps_perte_vie_T >= delai_collision):
                Toad_touché = True
            # Si le boss touche le joueur autrement
            elif temps_actuel - dernier_temps_perte_vie_T >= delai_collision:
                Joueur.vie -= 1
                dernier_temps_perte_vie = temps_actuel
                dernier_temps_perte_vie_T = temps_actuel
                cligno_J = True
                clignotement_actif = True  # Activer le mode clignotement
                temps_debut_clignotement = temps_actuel  # Enregistrer le début du clignotement
                if Joueur.vie == 0:
                    #Affichage de l'écran de défaite quand la vie du joueur atteint 0
                    print("Game Over ! Le méchant Toad t'as tué...")
                    defaite_rect = fond_défaite.get_rect(center=(width // 2, height // 2))
                    window.blit(fond_défaite, defaite_rect.topleft)
                    pygame.display.update()
                    pygame.mixer.music.load('Sons/Defeat theme.mp3')
                    pygame.mixer.music.play(1)
                    pygame.time.delay(5000)
                    running = False
        
        if clignotement_actif:
            if cligno_J:
                temps_actuel = pygame.time.get_ticks()
                # Alterner entre visible/invisible toutes les 200 ms
                visible_J = (temps_actuel // 200) % 2 == 0
                # Désactiver le clignotement après la durée spécifiée
                if temps_actuel - temps_debut_clignotement >= duree_clignotement:
                    clignotement_actif = False
                    cligno_J = False
                    visible_J = True  # Le personnage redevient toujours visible après le clignotement
            else:
                visible_J = True  # Si pas de clignotement, le personnage est toujours visible
            if cligno_B:
                temps_actuel = pygame.time.get_ticks()
                # Alterner entre visible/invisible toutes les 200 ms
                visible_B = (temps_actuel // 200) % 2 == 0
                # Désactiver le clignotement après la durée spécifiée
                if temps_actuel - temps_debut_clignotement >= duree_clignotement:
                    clignotement_actif = False
                    cligno_B = False
                    visible_B = True  # Le personnage redevient toujours visible après le clignotement
            else:
                visible_B = True  # Si pas de clignotement, le personnage est toujours visible
        
        # Dessiner le personnage (s'il est visible)
        if visible_J:
            if keys[pygame.K_d] or keys[pygame.K_q]:
                img_J_R = False
                img_J_L = False
                img_J_L_H = False
                img_J_R_H = False
            if keys[pygame.K_d] or img_J_R:
                tpsJR = pygame.time.get_ticks()
                if (keys[pygame.K_d] or img_J_R) and not is_jumping and tpsJL != tpsJR:
                    img_J_R = True
                    window.blit(Joueur.imgD, (player_x, player_y))
            if keys[pygame.K_q] or img_J_L:
                tpsJL = pygame.time.get_ticks()
                if (keys[pygame.K_q] or img_J_L) and not is_jumping and tpsJL != tpsJR:
                    img_J_L = True
                    window.blit(Joueur.imgG, (player_x, player_y))
            if is_jumping and tpsJL > tpsJR:
                img_J_L_H = True
                window.blit(Joueur.imgGH, (player_x, player_y))
            if is_jumping and tpsJR >= tpsJL:
                img_J_R_H = True
                window.blit(Joueur.imgDH, (player_x, player_y))
            if (not keys[pygame.K_d] and not keys[pygame.K_q] and not is_jumping) and tpsJL > tpsJR:
                window.blit(Joueur.imgG, (player_x, player_y))
            if (not keys[pygame.K_d] and not keys[pygame.K_q] and not is_jumping) and tpsJR >= tpsJL:
                window.blit(Joueur.imgD, (player_x, player_y))
        
        if visible_B:
            if Boss.direction == 1 and not is_jumping_B:
                window.blit(Boss.imgD, (boss_x, boss_y))
            if Boss.direction == -1 and not is_jumping_B:
                window.blit(Boss.imgG, (boss_x, boss_y))
            if is_jumping_B and Boss.direction == 1:
                window.blit(Boss.imgDH, (boss_x, boss_y))
            if is_jumping_B and Boss.direction == -1:
                window.blit(Boss.imgGH, (boss_x, boss_y))
            
        if Joueur.vie == 6 :
            window.blit(PV6, (20, 20))
        if Joueur.vie == 5 :
            window.blit(PV5, (20, 20))
        if Joueur.vie == 4 :
            window.blit(PV4, (20, 20))
        if Joueur.vie == 3 :
            window.blit(PV3, (20, 20))
        if Joueur.vie == 2 :
            window.blit(PV2, (20, 20))
        if Joueur.vie == 1 :
            window.blit(PV1, (20, 20))
        if Joueur.vie == 0 :
            window.blit(PV0, (20, 20))
            
        if Boss.vie == 6 :
            window.blit(PVB6, (1250, 20))
        if Boss.vie == 5 :
            window.blit(PVB5, (1250, 20))
        if Boss.vie == 4 :
            window.blit(PVB4, (1250, 20))
        if Boss.vie == 3 :
            window.blit(PVB3, (1250, 20))
        if Boss.vie == 2 :
            window.blit(PVB2, (1250, 20))
        if Boss.vie == 1 :
            window.blit(PVB1, (1250, 20))
        if Boss.vie == 0 :
            window.blit(PVB0, (1250, 20))
            
        police = pygame.font.Font(None, 45)
        texteViesBoss = police.render(f"Boss", True, BLACK)
        texteViesJoueur = police.render(f"Joueur", True, BLACK)
        window.blit(texteViesBoss, (1250, 80))
        window.blit(texteViesJoueur, (20, 80))

        # Mettre à jour l'affichage
        pygame.display.update()

        # Limiter le nombre de FPS (images par seconde)
        pygame.time.Clock().tick(60)
        
        
# Définir les dimensions de la fenêtre
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
window = pygame.display.set_mode((width, height))

fond_menu = pygame.transform.scale(fond_menu, (width, height))

selected_player = afficher_menu_principal()

Joueur = Joueur(selected_player)
Joueur.perso()

velocity_y = 0
velocity_y_B = 0
velocity_y_T = 0

# Redimensionner les images (sinon images trop grandes)
Boss.imgD = pygame.transform.scale(Boss_imgD, (Boss.taille, Boss.taille))
Boss.imgG = pygame.transform.scale(Boss_imgG, (Boss.taille, Boss.taille))
Boss.imgDH = pygame.transform.scale(Boss_imgDH, (Boss.taille, Boss.taille))
Boss.imgGH = pygame.transform.scale(Boss_imgGH, (Boss.taille, Boss.taille))
Joueur.imgD = pygame.transform.scale(Joueur.imgD, (Joueur.taille, Joueur.taille))
Joueur.imgG = pygame.transform.scale(Joueur.imgG, (Joueur.taille, Joueur.taille))
Joueur.imgDH = pygame.transform.scale(Joueur.imgDH, (Joueur.taille, Joueur.taille))
Joueur.imgGH = pygame.transform.scale(Joueur.imgGH, (Joueur.taille, Joueur.taille))
Toad.img = pygame.transform.scale(Toad_img, (Toad.taille, Toad.taille))
fond = pygame.transform.scale(fond, (width, height))
PV0 = pygame.transform.scale(PV0, (250, 50))
PV1 = pygame.transform.scale(PV1, (250, 50))
PV2 = pygame.transform.scale(PV2, (250, 50))
PV3 = pygame.transform.scale(PV3, (250, 50))
PV4 = pygame.transform.scale(PV4, (250, 50))
PV5 = pygame.transform.scale(PV5, (250, 50))
PV6 = pygame.transform.scale(PV6, (250, 50))
PVB0 = pygame.transform.scale(PV6, (250, 50))
PVB1 = pygame.transform.scale(PV5, (250, 50))
PVB2 = pygame.transform.scale(PV4, (250, 50))
PVB3 = pygame.transform.scale(PV3, (250, 50))
PVB4 = pygame.transform.scale(PV2, (250, 50))
PVB5 = pygame.transform.scale(PV1, (250, 50))
PVB6 = pygame.transform.scale(PV0, (250, 50))

# Hauteur de la plateforme
platform_height = 70

player_x, player_y = 100, height - Joueur.taille - platform_height
boss_x, boss_y = width - Boss.taille - 50, height - Boss.taille - platform_height  # Position initiale
toad_x, toad_y = width - 40, height - 680

delai_collision = 3000
dernier_temps_perte_vie = pygame.time.get_ticks()
dernier_temps_perte_vie_T = pygame.time.get_ticks()
clignotement_actif = False  # Indique si le personnage est en mode clignotement
temps_debut_clignotement = 0  # Temps de début du clignotement
duree_clignotement = delai_collision  # Durée totale du clignotement (ici, 3 secondes)
tpsJR = 0
tpsJL = 0
tps_chg = 0
tps_avt_chg = 0
tpsTM = 0
tpsTS = 0
tpsT = 0
         
afficher_tutoriel()
Jouer()

# Quitter Pygame
pygame.quit()