# Überlegen wegen modellieren: einfach array mit 52 stellen anlegen, dann mit mod die 4 farben herauskommen, dividieren usw.
# oder klasse anlegen

global cards
cards=[]

for i in range(52):
    cards.append(i)


def color(i):
    return cards[i]

print(color(50))