import math

def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees_deci = secondes / 31536000
    annees = math.floor(annees_deci)

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines_deci = ( annees_deci % 1 ) * 52
    semaines = math.floor(semaines_deci)

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours_deci = ( semaines_deci % 1 ) * 7
    jours = math.floor(jours_deci)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures_deci = ( jours_deci % 1 ) * 24
    heures = math.floor(heures_deci)

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes_deci = (heures_deci % 1 ) * 60
    minutes = math.floor(minutes_deci)

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes_deci = (minutes_deci % 1) * 60
    secondes = math.floor(secondes_deci)

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)


    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    decomposer(secondes)
