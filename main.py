#This program will draw a participant's name with knowledge of how much tickets they bought.

import pandas as pd
from random import randrange


# Ouvrir le fichier Excel et lire les infos
df = pd.read_excel (r'/Users/jefflemieux/Desktop/tirageAuSort/test.xlsx')

# Create an empty list which will contain the tickets
tickets = []

# Read the dataset and produce the right number of tickets for each participant. This will add the name of the participant in the list
# for each of their tickets.
for index, row in df.iterrows():
    for i in range(int(row['Billets'])):
        tickets.append(row['Nom'])

# Select a random number in the range of the list size
winner = randrange(len(tickets))

print("The winner is: ", tickets[winner])