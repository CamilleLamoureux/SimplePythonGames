# Premier projet de Python - Premier jeu - NIMBLE
# Projet Individuel - 291756 - Camille LAMOUREUX


# Importation des bibliothèques nécessaires
from random import randint

# Fonction de vérification des données pour la création du plateau
def possibleBoard(n, p):
    if n > 2 and p > 0:                                                                                                 
        return True
    else:
        return False


# Fonction de création du plateau initial
def newboard(n, p):
    board = [0]                                                                                                        
    for i in range(1, n):
        board.append(randint(0, p))                                                                                    
    return board


# Procédure d'affichage du plateau
def display(board, n):
    numero_case = []                                                                                                    
    for i in range(1, n + 1):
        numero_case.append(i)
    print(*board, sep="  |  ")                                                                                         
    print("------"*len(board))
    print(*numero_case, sep="  |  ")                                                                                    


# Fonction de vérification de la case de départ sélectionnée
def possibleSquare(board, n, i):
    if i > n or board[i - 1] == 0 or i == 1:                                                                           
        return False
    else:
        return True


# Fonction de sélection de la case de départ
def selectSquare(board, n):
    i = int(input("Selectionnez la case sur laquelle prendre le pion : "))
    while not possibleSquare(board, n, i):                                                                              
        i = int(input("Saisie invalide, selectionnez la case sur laquelle prendre le pion : "))
    return i                                                                                                           


# Focntion de vérification de la case d'arrivé sélectionnée
def possibleDestination(board, n, i, j):
    if i <= j or j < 1:                                                                                                 
        return False
    else:
        return True


# Fonction de sélection de la case d'arrivé
def selectDestination(board, n, i):
    j = int(input("Selectionnez la case sur laquelle mettre le pion : "))
    while not possibleDestination(board, n, i, j):                                                                      
        j = int(input("Saisie invalide, selectionnez la case sur laquelle mettre le pion : "))
    return j                                                                                                            


# Procédure qui déplace le pion
def move(board, n, i, j):
    board[i - 1] -= 1                                                                                                   
    board[j - 1] += 1                                                                                                   


# Fonction qui vérifie si un des joueurs à perdu
def lose(board, n):
    for i in range(1, n):                                                                                              
        if board[i] != 0:
            return False                                                                                                
    return True


# Fonction qui retourne le numéro du joueur gagnant
def winner(deplacement):
    if deplacement%2 == 0:                                                                                              
        return "1"                                                                                                     
    else :                                                                                                              
        return "2"                                                                                                      


# Prodédure qui fait le déroulement du jeu
def nimble():

    #Initialisation du plateau
    print("Veuillez saisir vos paramètres de jeu : ")
    n = int(input("Nombre de case (supérieur à 2) : "))
    p = int(input("Nombre de pion maximum dans une case : "))
    while not possibleBoard(n, p):
        print("Saisie invalide, merci de recommencer : ")
        n = int(input("Nombre de case (supérieur à 2) : "))
        p = int(input("Nombre de pion maximum dans une case : "))
    board = newboard(n, p)

    #Initialisation du nombre de tours de jeu
    tour = 1

    #Lancement de la partie
    while not lose(board, n):
        # Affichage du tableau généré
        display(board, n)

        # Déduction du joueur dont c'est le tour
        if tour%2 == 0:
            player = 2
        else :
            player = 1

        print("\nTour du joueur", player)

        # Demande des valeurs pour réaliser le déplacement
        i = selectSquare(board, n)
        j = selectDestination(board, n, i)

        # Réalisation du déplacement
        move(board, n, i, j)

        # Mise à jour du nombre de tours
        tour += 1

    # Affichage du nom du joueur gagnant
    display(board,n)
    print("Le joueur ",winner(tour)," a gagné !")


# Appel de la procédure nimble afin de pouvoir lancer une partie
nimble()
