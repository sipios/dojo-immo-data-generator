import csv
import random


# Function to generate a random French title
def generate_title():
    titles = [
        "Devenez Copropriétaire d'un Bijou Immobilier : Investissement Participatif Exceptionnel !",
        "Saisissez l'Opportunité d'Investissement Collectif : Rejoignez notre Projet Immobilier Prometteur !",
        "Devenez Acteur de l'Immobilier : Investissement Participatif Rentable et Éthique !",
        "Multipliez vos Chances de Succès : Investissement Collectif dans un Portefeuille Immobilier Diversifié !",
        "Participez à notre Aventure Immobilière : Rendement Élevé avec l'Investissement Participatif !",
        "Investissement Immobilier Ouvert à Tous : Réalisez vos Projets avec notre Plateforme Participative !",
        "Rentabilité Assurée : Investissement Collectif dans des Propriétés Haut de Gamme !",
        "Joignez-vous à notre Communauté d'Investisseurs : Investissement Participatif dans des Quartiers en Pleine Expansion !",
        "Faites Croître votre Portefeuille : Investissement Participatif dans des Biens Immobiliers à Fort Potentiel !",
        "Investissez en Toute Sérénité : Profitez de la Sécurité et de la Rentabilité de l'Investissement Participatif Immobilier !"
    ]
    return random.choice(titles)


def generate_scoring(label):
    if label == "PARTICIPATIVE":
        return 1
    else:
        return 4


# Function to generate a random row
def generate_row(id):
    deed_type = random.choice(["PARTICIPATIVE", "APARTMENT"])
    amount = random.randint(1000, 10000)
    if deed_type == "APARTMENT":
        amount = random.randint(3000,10000)
    amount = amount - (amount % 100)  # Ensure it's a multiple of 100
    rent = int(round(random.uniform(0.10, 0.15) * amount, 0))
    label = generate_title()
    image_id = random.randint(1, 230)
    image = f"image{image_id}.jpg"
    scoring = generate_scoring(deed_type)
    last_score_update = f"2023-09-{random.randint(1, 30)}"

    return [id, amount, rent, label, image, deed_type, scoring, last_score_update]


# Number of rows
num_rows = 200  # Change this to your desired number of rows

# Create and write to the CSV file
with open('real_estate_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "amount", "rent", "label", "image", "deed_type", "scoring", "last_score_update"])
    start_index: int = 0
    for i in range(1, num_rows + 1):
        row = generate_row(i + start_index)
        writer.writerow(row)

print("CSV file 'real_estate_data.csv' has been generated.")
