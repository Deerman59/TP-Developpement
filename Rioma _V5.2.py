import pygame
import time
import sys
import random

# Initialisation de Pygame
pygame.init()

# Charger les images pour le joueur et le boss
Boss_imgG = pygame.image.load('mario négatif-reverse.png')
Boss_imgD = pygame.image.load('mario négatif.png')
Boss_imgDH = pygame.image.load('mario négatif jumping.png')
Boss_imgGH = pygame.image.load('mario négatif-reverse jumping.png')
Goomba_img = pygame.image.load('para-goomba.png')
Goomba_imgD = pygame.image.load('para-goomba right looking.png')
Goomba_imgG = pygame.image.load('para-goomba left looking.png')
Goomba_imgH = pygame.image.load('para-goomba jumping.png')
Para_Koopa_imgD = pygame.image.load('para-koopa.png')
Para_Koopa_imgG = pygame.image.load('para-koopa_g.png')
Para_Koopa_imgDH = pygame.image.load('para-koopa_jumping_d_h.png')
Para_Koopa_imgGH = pygame.image.load('para-koopa_jumping_g_h.png')
Bowser_imgG = pygame.image.load('bowserG.png')
Bowser_imgD = pygame.image.load('bowserD.png')
Chomp_imgD = pygame.image.load('chomp reverse.png')
Chomp_imgG = pygame.image.load('chomp.png')
Chomp_imgDH = pygame.image.load('chomp reverse jumping.png')
Chomp_imgGH = pygame.image.load('chomp jumping.png')
Boo_imgD = pygame.image.load('boo reverse.png')
Boo_imgG = pygame.image.load('boo.png')
Toad_img = pygame.image.load('toad négatif.png')
Boss_song_jump_S = 'RIOMA jump sound mario négatif.wav'
Bowser_song_jump_S = 'RIOMA jump sound bowser.wav'
GoombaKoopa_song_jump_S = 'RIOMA jump sound parakoopa goomba.wav'
Boo_song_jump_S = 'boo sound.wav'
PV0 = pygame.image.load('barre de vie 0.png')
PV1 = pygame.image.load('barre de vie 1.png')
PV2 = pygame.image.load('barre de vie 2.png')
PV3 = pygame.image.load('barre de vie 3.png')
PV4 = pygame.image.load('barre de vie 4.png')
PV5 = pygame.image.load('barre de vie 5.png')
PV6 = pygame.image.load('barre de vie 6.png')
PVB0 = pygame.image.load('barre de vie 6.png')
PVB1 = pygame.image.load('barre de vie 5.png')
PVB2 = pygame.image.load('barre de vie 4.png')
PVB3 = pygame.image.load('barre de vie 3.png')
PVB4 = pygame.image.load('barre de vie 2.png')
PVB5 = pygame.image.load('barre de vie 1.png')
PVB6 = pygame.image.load('barre de vie 0.png')

# Couleurs (pour la plateforme et autres objets si nécessaire)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)         

#Police
font = pygame.font.Font(None, 36)

# Charger et jouer le son de fond
pygame.mixer.music.load('Niveau.wav')
Boss_song_jump = pygame.mixer.Sound(Boss_song_jump_S)
Bowser_song_jump = pygame.mixer.Sound(Bowser_song_jump_S)
GoombaKoopa_song_jump = pygame.mixer.Sound(GoombaKoopa_song_jump_S)
Boo_song_jump = pygame.mixer.Sound(Boo_song_jump_S)
pygame.mixer.Sound.set_volume(Boss_song_jump, 0.1)
pygame.mixer.Sound.set_volume(Bowser_song_jump, 0.1)
pygame.mixer.Sound.set_volume(GoombaKoopa_song_jump, 0.1)
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)
fond = pygame.image.load('backgroundRIOMA3.png')
fond_menu = pygame.image.load('backgroundMenu.png')

# Titre du jeu  
pygame.display.set_caption("RIOMA")

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
        if self.choix == "Goomba":
            self.vie = 6
            self.nom = "Goomba"
            self.taille = 95
            self.speed = 5
            self.jump = 13
            self.song_jump = GoombaKoopa_song_jump
            self.imgD = Goomba_imgD
            self.imgG = Goomba_imgG
            self.imgDH = Goomba_imgH
            self.imgGH = Goomba_imgH
            self.gravity = 0.5
        if self.choix == "Koopa":
            self.vie = 3
            self.nom = "Para-Koopa"
            self.taille = 80
            self.speed = 5
            self.jump = 15
            self.song_jump = GoombaKoopa_song_jump
            self.imgD = Para_Koopa_imgD
            self.imgG = Para_Koopa_imgG
            self.imgDH = Para_Koopa_imgDH
            self.imgGH = Para_Koopa_imgGH
            self.gravity = 0.2
        if self.choix == "Bowser":
            self.vie = 6
            self.nom = "Bowser"
            self.taille = 160
            self.speed = 3.5
            self.jump = 15
            self.song_jump = Bowser_song_jump
            self.imgD = Bowser_imgD
            self.imgG = Bowser_imgG
            self.imgDH = Bowser_imgD
            self.imgGH = Bowser_imgG
            self.gravity = 0.5
        if self.choix == "Chomp":
            self.vie = 3
            self.nom = "Chomp"
            self.taille = 120
            self.speed = 10
            self.jump = 15
            self.song_jump = GoombaKoopa_song_jump
            self.imgD = Chomp_imgD
            self.imgG = Chomp_imgG
            self.imgDH = Chomp_imgDH
            self.imgGH = Chomp_imgGH
            self.gravity = 0.5
        if self.choix == "Boo":
            self.vie = 3
            self.nom = "Boo"
            self.taille = 80
            self.speed = 5
            self.jump = 15
            self.song_jump = Boo_song_jump
            self.imgD = Boo_imgD
            self.imgG = Boo_imgG
            self.imgDH = Boo_imgD
            self.imgGH = Boo_imgG
            self.gravity = 0.2
            
            
class Boss:
    def __init__(self,vie=6,nom="Mario",taille=90,speed=5,jump=15,song_jump='',direction=-1,imgD='',imgG='',imgDH='',imgGH='',gravity=0.5):
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

class Toad:
    def __init__(self,vie=1,nom="Toad",taille=70,speed=4,jump=1,song_jump='',direction=-1,imgD='',imgG='',imgDH='',imgGH='',gravity=0.5):
        self.vie = vie
        self.nom = nom
        self.taille = taille
        self.speed = speed
        self.jump = jump
        self.song_jump = Boss_song_jump
        self.direction = direction
        self.img = Toad_img
        self.gravity = gravity
        
class Son:
    def __init__(self):
        self.volume = pygame.mixer.music.get_volume()

    def changer_volume(self, niveau):
        if 0.0 <= niveau <= 1.0:
            self.volume = niveau
            pygame.mixer.music.set_volume(self.volume)
        else:
            print("Le niveau de volume doit être compris entre 0.0 et 1.0.")


choix = str(input("Choisissez un perso (Goomba/Koopa/Bowser/Chomp/Boo):"))
Joueur = Joueur(choix)
Joueur.perso()
Boss = Boss()
Toad = Toad()
gestion_son = Son()

# Définir les dimensions de la fenêtre
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
window = pygame.display.set_mode((width, height))

velocity_y = 0
velocity_y_B = 0
velocity_y_T = 0

# Redimensionner les images (facultatif, si nécessaire)
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
fond_menu = pygame.transform.scale(fond_menu, (width, height))
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

# Propriétés de la plateforme
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

def afficher_menu_volume():
    menu_running = True
    while menu_running:
        window.blit(fond_menu, (0,0))
        
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
    window.blit(fond_menu, (0,0))
    while menu_running:
        
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
            window.blit(Joueur.imgD, (width // 4 - 100, height - 250))  # Positionner à gauche
        elif selected_player == 2:
            # Afficher l'autre personnage en grand
            window.blit(Joueur.imgG, (3 * width // 4 - 100, height - 250))  # Positionner à droite

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
    img_J_L_H = False
    img_J_R_H = False
    Toad_spawn = False
    Toad_touché = False
    Nb_Toad = 0
    velocity_y_T = -Toad.jump
    global velocity_y
    global velocity_y_B
    global player_x
    global player_y
    global boss_x
    global boss_y
    global toad_x
    global toad_y
    global dernier_temps_perte_vie
    global dernier_temps_perte_vie_T
    global clignotement_actif
    global temps_debut_clignotement
    global duree_clignotement
    global tpsJR 
    global tpsJL
    global tps_chg
    global tps_avt_chg
    global tpsTM
    global tpsTS
    global tpsT
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False               
        # Récupérer l'état des touches
        keys = pygame.key.get_pressed()
        
        window.blit(fond, (0,0))
        
        # Déplacement du joueur à gauche ou à droite
        if keys[pygame.K_LEFT] and not keys[pygame.K_LSHIFT]:
            player_x -= Joueur.speed
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LSHIFT]:
            player_x += Joueur.speed
        if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
            player_x -= Joueur.speed*1.6
        if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
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
        
        if not is_jumping_B and random.randint(1,400) == 400:
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
            """
            tpsT = pygame.time.get_ticks()
            Toad.direction = -1
            if tpsTM+4500 > tpsTS or (Nb_Toad == 0 and (0 < tpsT < 1500)):
                toad_x += (Toad.speed-5) * Toad.direction
            else:"""
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
                        print("Victoire! Le boss est vaincu!")
                        running = False
            # Si le boss touche le joueur autrement
            elif temps_actuel - dernier_temps_perte_vie >= delai_collision:
                Joueur.vie -= 1
                dernier_temps_perte_vie = temps_actuel
                cligno_J = True
                clignotement_actif = True  # Activer le mode clignotement
                temps_debut_clignotement = temps_actuel  # Enregistrer le début du clignotement
                if Joueur.vie == 0:
                    print("Game Over! Le boss a gagné.")
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
                    print("Game Over! Le boss a gagné.")
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
            if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                img_J_R = False
                img_J_L = False
                img_J_L_H = False
                img_J_R_H = False
            if keys[pygame.K_RIGHT] or img_J_R:
                tpsJR = pygame.time.get_ticks()
                if (keys[pygame.K_RIGHT] or img_J_R) and not is_jumping and tpsJL != tpsJR:
                    img_J_R = True
                    window.blit(Joueur.imgD, (player_x, player_y))
            if keys[pygame.K_LEFT] or img_J_L:
                tpsJL = pygame.time.get_ticks()
                if (keys[pygame.K_LEFT] or img_J_L) and not is_jumping and tpsJL != tpsJR:
                    img_J_L = True
                    window.blit(Joueur.imgG, (player_x, player_y))
            if is_jumping and tpsJL > tpsJR:
                img_J_L_H = True
                window.blit(Joueur.imgGH, (player_x, player_y))
            if is_jumping and tpsJR >= tpsJL:
                img_J_R_H = True
                window.blit(Joueur.imgDH, (player_x, player_y))
            if (not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not is_jumping) and tpsJL > tpsJR:
                window.blit(Joueur.imgG, (player_x, player_y))
            if (not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not is_jumping) and tpsJR >= tpsJL:
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
        texteViesBoss = police.render(f"Boss", True, (0, 0, 0))
        texteViesJoueur = police.render(f"Joueur", True, (0, 0, 0))
        window.blit(texteViesBoss, (1250, 80))
        window.blit(texteViesJoueur, (20, 80))

        # Mettre à jour l'affichage
        pygame.display.update()

        # Limiter le nombre de FPS (images par seconde)
        pygame.time.Clock().tick(600)


selected_player = afficher_menu_principal()

Jouer()

# Quitter Pygame
pygame.quit()
