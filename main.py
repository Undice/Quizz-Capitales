import random

def parcourirPays(pays_restants):
    pays_choisi = random.choice(list(pays_restants.keys()))

    return pays_choisi

def poserQuestion(score, pays, capitale):
    reponse = input(f"Quelle est la capitale de {pays} ? ")

    if reponse.strip().lower() == capitale.lower():
        score += 1

    return score

pays = {
    "France": "Paris",
    "Italie": "Rome",
    "Espagne": "Madrid"
}

pays_restants = pays.copy()

nb_questions = input("Combien de questions voulez-vous faire aujourd'hui ? ")
question = 1
score = 0

while question <= int(nb_questions):
    print(f"Question {question} :")
    # Parcourir une fois le disctionnaire et supprimer le pays quand il est cité
    pays_choisi = parcourirPays(pays_restants)
    score = poserQuestion(score, pays_choisi, pays_restants[pays_choisi])

    del pays_restants[pays_choisi]

    question += 1

print(f"Vous avez fait un score de {score}/{nb_questions}")