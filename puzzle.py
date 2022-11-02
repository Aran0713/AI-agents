from logic import *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

symbols = []

knowledge = And()

for person in people:
    for house in houses:
        symbols.append(Symbol(str(person) + str(house)))

# Each person belongs to a house.
for person in people:
    knowledge.add( Or(Symbol(str(person) + "Gryffindor"), Symbol(str(person) + "Hufflepuff"), Symbol(str(person) + "Ravenclaw"), Symbol(str(person) + "Slytherin") ))                                                

# Only one house per person.
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add( Implication(Symbol(str(person)+str(h1)), Not(Symbol(str(person)+str(h2))) ))

# Only one person per house.
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(str(p1) + str(house)), Not(Symbol(str(p2) + str(house) )))
                )

knowledge.add(
    Or(Symbol("GilderoyGryffindor"), Symbol("GilderoyRavenclaw"))
)

knowledge.add(
    Not(Symbol("PomonaSlytherin"))
)

knowledge.add(
    Symbol("MinervaGryffindor")
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
