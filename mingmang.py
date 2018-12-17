# Premier projet de Python - Deuxième jeu - MINGMANG
# Projet Individuel - 291756 - Camille LAMOUREUX

# Fonction d'initialisation du plateau
def newboard(n) :
    board = []                                                                                                         
    for i in range(0, n):
        board.append([0] * n)
    for i in range(0, n):
        board[0][i] = 2
    for i in range(0, n):
        board[n - 1][i] = 1
    for i in range(0, n):
        board[i][0] = 1
    for i in range(0, n):
        board[i][n - 1] = 2
    return board


# Fonction d'assignement des symboles pour l'affichage
def symbole(case):
    if case == 1:
        return "o"
    elif case == 2:
        return "x"
    else:
        return "."


# #Procédure d'affichage du plateau de jeu
def display(board,n):
    for ligne in range(0,n):
        for colonne in range(0,n):
            print(symbole(board[ligne][colonne]), end="    ")
        print("\n")


#Fonction de vérification de la sélection d'un pion à déplacer
def possiblePawn(board,n,player,i,j) :
    if board[i-1][j-1] == player:                                                                                       # Un pion est sélectionnable s'il apparatient au joueur dont c'est le tour                                                                                    # Si le pion de la case sélectionnée appartient bien au joueur
        if i == 1:                                                                                                      # Si le pion est sur la première ligne (et qu'il ne peut donc pas se déplacer vers le haut)
            if board[i-1][j-2] == 0 or board[i][j-1] == 0 or board[i-1][j] == 0:                                        # On vérifie si au moins une des trois autres cases autour de lui est libre
                return True
        elif j == 1 and i == 1:                                                                                         # Si le pion est dans le coin en haut à gauche (et donc qu'il ne peut pas se déplacer vers la gauche et le haut)
            if board[i][j-1] == 0 or board[i-1][j] == 0:                                                                # On vérifie si au moins une des deux autres cases autour de lui est libre
                return True
        elif j == 1 and i == n :                                                                                        # Si le pion est dans le coin en bas à gauche (et donc qu'il ne peut pas se déplacer vers la gauche et le bas)
            if board[i-2][j-1] == 0 or board[i-1][j] == 0:                                                              # On vérifie si au moins une des deux autres cases autour de lui est libre
                return True
        elif j == n and i == 1 :                                                                                        # Si le pion est dans le coin en haut à droite (et donc qu'il ne peut pas se déplacer vers la droite et le haut)
            if board[i-2][j-1] == 0 or board[i-1][j] == 0:                                                              # On vérifie si au moins une des deux autres cases autour de lui est libre
                return True
        elif j == 1:                                                                                                    # Si le pion est sur la première colonne (et donc qu'il ne peut pas se déplacer vers la gauche)
            if board[i-2][j-1] == 0 or board[i][j-1] == 0 or board[i-1][j] == 0:                                        # On vérifie si au moins une des trois autres cases autour de lui est libre
                return True
        if i == n:                                                                                                      # Si le pion est sur la dernière ligne (et qu'il ne peut donc pas se déplacer vers le bas)
            if board[i-1][j-2] == 0 or board[i-2][j-1] == 0 or board[i-1][j] == 0:                                      # On vérifie si au moins une des trois autres cases autour de lui est libre
                return True
        elif j == n:                                                                                                    # Si le pion est sur la dernière colonne (et donc qu'il ne peut pas se déplacer vers la droite)
            if board[i-2][j-1] == 0 or board[i][j-1] == 0 or board[i-1][j-2] == 0:                                      # On vérifie si au moins une des trois autres cases autour de lui est libre
                return True
        elif j == n and i == n :                                                                                        # Si le pion est dans le coin en bas à droite (et donc qu'il ne peut pas se déplacer vers la droite et le bas)
            if board[i-2][j-1] == 0 or board[i-1][j-2] == 0:                                                            # On vérifie si au moins une des deux autres cases autour de lui est libre
                return True
        elif board[i-2][j-1] == 0 or board[i-1][j-2] == 0 or board[i][j-1] == 0 or board[i-1][j] == 0:                  # Sinon,On vérifie si au moins une des quatres cases autour de lui est libre
            return True
    return False


#Fonction de sélection d'un pion à déplacer
def selectPawn(board,n,player) :
    i = int(input("Selectionner la ligne de votre pion à déplacer : \n "))
    j = int(input("Selectionner la colonne de votre pion à déplacer : \n "))
    while not possiblePawn(board,n,player,i,j):
        print("Saisie invalide, merci de recommencer : ")
        i = int(input("Sélectionner la ligne de votre pion à déplacer : \n "))
        j = int(input("Sélectionner la colonne de votre pion à déplacer : \n "))
    return i,j


#Fonction de vérification de la sélection de la case sur laquelle mettre le pion
def possibleDestination(board,n,i,j,k,l) :
    if board[k-1][l-1] == 0 and (k == i or l == j):
        # Si on cherche à déplacer un pion sur la même ligne
        if k == i:
            colonne = k
            # Si la colonne de destination est à droite de la colonne de départ
            if l < j:
                for ligne in range(l-1,j-1):
                    if board[ligne][colonne] != 0:
                        return False
                return True
            # Si elle est à gauche
            elif l > j:
                for ligne in range(j-1,l-1):
                    if board[ligne][colonne] != 0:
                        return False
                return True
        # Si on cherche à déplacer un pion sur la même colonne
        elif l == j:
            ligne = l
            # Si la ligne de destination est en dessous de la ligne de départ
            if k < i:
                for colonne in range(k-1,i-1):
                    if board[ligne][colonne] != 0:
                        return False
                return True
            # Si la ligne de destination est au dessus de la ligne de départ
            elif  k > i:
                for colonne in range(i-1,k-1):
                    if board[ligne][colonne] != 0:
                        return False
                return True
    else:
        return False


#Fonction de sélection de la case sur laquelle mettre le pion
def selectDestination(board,n,i,j) :
    k = int(input("Selectionner la ligne où mettre votre pion \n "))
    l = int(input("Selectionner la colonne où mettre votre pion \n "))
    while not possibleDestination(board, n, i, j, k, l):
        print("Saisie invalide, merci de recommencer :")
        k = int(input("Sélectionner la ligne où mettre votre pion \n "))
        l = int(input("Sélectionner la colonne où mettre votre pion \n "))
    return k,l


# Prodédure de conversion des pions après un déplacement
def conversion(board, pion_to_convert):
    for element in pion_to_convert:
        if board[element[0]][element[1]] == 1 :
            board[element[0]][element[1]] = 2
        elif board[element[0]][element[1]] == 2:
            board[element[0]][element[1]] = 1


# Procédure qui réalise le déplacement et les potentiels changements occasionnés
def move(board,n,player,i,j,k,l) :
    board[i-1][j-1] = 0
    board[k-1][l-1] = player
    pion_to_convert = []
    # Gestion des changements occasionnés par le déplacement
    # On test les cases à gauche du pion qui vient d'être déplacé
    for i in range(l-2,0,-1):
        if board[k-1][i] == 0:
            break
        elif board[k-1][i] == player:
            conversion(board, pion_to_convert)
        else :
            pion_to_convert.append([k-1,i])
    # On test les cases à droite du pion qui vient d'être déplacé
    for i in range(l,n):
        if board[k-1][i] == 0:
            break
        elif board[k - 1][i] == player:
            conversion(board, pion_to_convert)
        else:
            pion_to_convert.append([k - 1, i])
    # On test les cases en dessous du pion qui vient d'être déplacé
    for i in range(k,n):
        if board[l-1][i] == 0:
            break
        elif board[l-1][i] == player:
            conversion(board, pion_to_convert)
        else :
            pion_to_convert.append([k-1,i])
    # On test les cases au dessus du pion qui vient d'être déplacé
    for i in range(k-2,0,-1):
        if board[k - 1][i] == 0:
            break
        elif board[l-1][i] == player:
            conversion(board, pion_to_convert)

        else:
            pion_to_convert.append([k - 1, i])

# Fonction qui vérifie si l'un des joueurs à perdu
def lose(board,n,player) :
    for ligne in board:
        for colonne in ligne:
            if colonne == player :
                return False
            else:
                return True


# Fonction qui retourne le numéro du joueur
def actual_player(tour):
    if tour % 2 == 0:
        return 2
    else:
        return 1


# Fonction qui retourne le numéro du joueur gagnant
def winner(tour):
    if tour%2 == 0:
        return "1"
    else :
        return "2"


#Procédure qui permet la partie en utilisant toutes les fonctions/procédures ci-dessus
def mingmang(n) :
    board = newboard(n)
    tour = 1
    player = actual_player(tour)
    while not lose(board,n,player):
        display(board, n)
        # Déduction du joueur dont c'est le tour
        player = actual_player(tour)
        print("\nTour du joueur", player)

        # Demande des valeurs pour réaliser le déplacement
        i,j = selectPawn(board,n,player)
        k,l = selectDestination(board,n,i,j)

        # Réalisation du déplacement
        move(board,n,player,i,j,k,l)

        # Mise à jour du nombre de tours
        tour += 1

        # Affichage du nom du joueur gagnant
    display(board, n)
    print("Le joueur ", winner(tour), " a gagné !")


# Appel de la procédure permettant de jouer
n = int(input("Veuillez saisir les dimensions de votre plateau de jeu :"))
mingmang(n)