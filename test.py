
afisare = print

afisare("msdsdsd")

def tip(parametru):
    return type(parametru)

def boolian(parametru):
    if parametru == True:
        return "Adevarat"
    else:
        return "Pula ta....ca-i Fals!"

afisare(tip(2))

afisare(boolian(1 < 0))