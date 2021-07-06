# Finds and return the age in increments of 0.5 years

from datetime import datetime, date

from dateutil import relativedelta

date_of_birth = datetime.strptime(input("Date of birth (dd mm yyyy) --->"), "%d %m %Y")


def calculate_age(born):
    today = date.today()
    diff = relativedelta.relativedelta(today, date_of_birth)
    years = diff.years
    months = diff.months
    age = years

    if months >= 6:
        return age + 0.5
    else:
        return age


chrono_age = calculate_age(date_of_birth)

print(chrono_age)

CGscore = int(input("Pontuacao Complemento Gravuras: --->"))
Infscore = int(input("Pontuacao Informacao: --->"))
Codscore = int(input("Pontuacao Codigo: --->"))
Semscore = int(input("Pontuacao Semelhancas: --->"))
DGscore = int(input("Pontuacao Disposicao de Gravuras: --->"))
Ariscore = int(input("Pontuacao Aritmetica: --->"))
Cubscore = int(input("Pontuacao Cubos: --->"))
Vocscore = int(input("Pontuacao Vocubulario: --->"))
COscore = int(input("Pontuacao Composicao Objetos: --->"))
Compscore = int(input("Pontuacao Compreencao: --->"))
PSscore = int(input("Pontuacao Pesquisa de Simbolos: --->"))
MDscore = int(input("Pontuacao Memoria de Digitos: --->"))
Labscore = int(input("Pontuacao Labirintos: --->"))

standardized_scores = []
QIverbal = []  # verbal
QIrealizacao = []  # escala realizacao
QIcv = []  # compreensao verbal
QIop = []  # organizacao perceptiva
QIvp = []  # velocidade precessamento


def find_standardized_CGscore():
    if chrono_age == 6:
        if CGscore <= 6:
            standardized_CGscore = CGscore + 1
        elif 7 <= CGscore <= 8:
            standardized_CGscore = 8
        elif CGscore == 9:
            standardized_CGscore = 9
        elif 10 <= CGscore <= 11:
            standardized_CGscore = 10
        elif 12 <= CGscore <= 19:
            standardized_CGscore = CGscore - 1
        else:
            standardized_CGscore = 19

    if chrono_age == 6.5:
        if CGscore <= 2:
            standardized_CGscore = CGscore + 1
        elif 3 <= CGscore <= 4:
            standardized_CGscore = 4
        elif 5 <= CGscore <= 7:
            standardized_CGscore = CGscore
        elif 8 <= CGscore <= 9:
            standardized_CGscore = 8
        elif CGscore == 10:
            standardized_CGscore = 9
        elif 11 <= CGscore <= 12:
            standardized_CGscore = 10
        elif 13 <= CGscore <= 16:
            standardized_CGscore = CGscore - 2
        elif 17 <= CGscore <= 18:
            standardized_CGscore = 15
        elif 20 <= CGscore <= 21:
            standardized_CGscore = CGscore - 3
        else:
            standardized_CGscore = 19

    if chrono_age == 7:
        if 0 <= CGscore <= 3:
            standardized_CGscore = 1
        elif 4 <= CGscore <= 9:
            standardized_CGscore = CGscore - 2
        elif 10 <= CGscore <= 11:
            standardized_CGscore = 8
        elif 12 <= CGscore <= 21:
            standardized_CGscore = CGscore - 3
        else:
            standardized_CGscore = 19

    if chrono_age == 7.5:
        if CGscore <= 3:
            standardized_CGscore = 1
        elif CGscore == 4:
            standardized_CGscore = 2
        elif 5 <= CGscore <= 6:
            standardized_CGscore = 3
        elif 7 <= CGscore <= 10:
            standardized_CGscore = CGscore - 3
        elif 11 <= CGscore <= 12:
            standardized_CGscore = 8
        elif 13 <= CGscore <= 22:
            standardized_CGscore = CGscore - 4
        else:
            standardized_CGscore = 19

    if chrono_age == 8:
        if 0 <= CGscore <= 5:
            standardized_CGscore = 1
        elif 6 <= CGscore <= 7:
            standardized_CGscore = CGscore - 4
        elif 8 <= CGscore <= 9:
            standardized_CGscore = 4
        elif 10 <= CGscore <= 14:
            standardized_CGscore = CGscore - 5
        elif 15 <= CGscore <= 16:
            standardized_CGscore = 10
        elif CGscore == 17:
            standardized_CGscore = 11
        elif 18 <= CGscore <= 23:
            standardized_CGscore = CGscore - 5
        else:
            standardized_CGscore = 19

    if chrono_age == 8.5:
        if 0 <= CGscore <= 6:
            standardized_CGscore = 1
        elif 7 <= CGscore <= 14:
            standardized_CGscore = CGscore - 5
        elif 15 <= CGscore <= 16:
            standardized_CGscore = 10
        elif 17 <= CGscore <= 24:
            standardized_CGscore = CGscore - 6
        else:
            standardized_CGscore = 19

    if chrono_age == 9:
        if 0 <= CGscore <= 6:
            standardized_CGscore = 1
        elif 7 <= CGscore <= 11:
            standardized_CGscore = CGscore - 5
        elif 12 <= CGscore <= 13:
            standardized_CGscore = 7
        elif CGscore == 14:
            standardized_CGscore = 8
        elif 15 <= CGscore <= 16:
            standardized_CGscore = 9
        elif CGscore == 17:
            standardized_CGscore = 10
        elif 18 <= CGscore <= 20:
            standardized_CGscore = CGscore - 6
        elif 21 <= CGscore <= 22:
            standardized_CGscore = 15
        elif 23 <= CGscore <= 24:
            standardized_CGscore = CGscore - 7
        elif 25 <= CGscore <= 27:
            standardized_CGscore = 18
        else:
            standardized_CGscore = 19

    if chrono_age == 9.5:
        if 0 <= CGscore <= 7:
            standardized_CGscore = 1
        elif 8 <= CGscore <= 10:
            standardized_CGscore = CGscore - 6
        elif 11 <= CGscore <= 12:
            standardized_CGscore = 5
        elif 13 <= CGscore <= 19:
            standardized_CGscore = CGscore - 7
        elif 20 <= CGscore <= 21:
            standardized_CGscore = 13
        elif 22 <= CGscore <= 25:
            standardized_CGscore = CGscore - 8
        elif 26 <= CGscore <= 27:
            standardized_CGscore = 18
        else:
            standardized_CGscore = 19

    if chrono_age == 10:
        if 0 <= CGscore <= 9:
            standardized_CGscore = 1
        elif 10 <= CGscore <= 16:
            standardized_CGscore = CGscore - 8
        elif 17 <= CGscore <= 18:
            standardized_CGscore = 9
        elif 19 <= CGscore <= 20:
            standardized_CGscore = CGscore - 9
        elif 21 <= CGscore <= 22:
            standardized_CGscore = CGscore - 8
        elif 22 <= CGscore <= 24:
            standardized_CGscore = 15
        elif 25 <= CGscore <= 27:
            standardized_CGscore = CGscore - 9
        else:
            standardized_CGscore = 19

    if chrono_age == 10.5:
        if 0 <= CGscore <= 9:
            standardized_CGscore = 1
        elif 10 <= CGscore <= 15:
            standardized_CGscore = CGscore - 8
        elif 16 <= CGscore <= 17:
            standardized_CGscore = 8
        elif 18 <= CGscore <= 19:
            standardized_CGscore = 9
        elif CGscore == 20:
            standardized_CGscore = 10
        elif 21 <= CGscore <= 27:
            standardized_CGscore = CGscore - 9
        else:
            standardized_CGscore = 19

    if chrono_age == 11:
        if 0 <= CGscore <= 9:
            standardized_CGscore = 1
        elif 10 <= CGscore <= 13:
            standardized_CGscore = CGscore - 8
        elif 14 <= CGscore <= 15:
            standardized_CGscore = 6
        elif 16 <= CGscore <= 17:
            standardized_CGscore = CGscore - 9
        elif 18 <= CGscore <= 19:
            standardized_CGscore = 9
        elif 20 <= CGscore <= 23:
            standardized_CGscore = CGscore - 10
        elif 24 <= CGscore <= 27:
            standardized_CGscore = CGscore - 9
        else:
            standardized_CGscore = 19

    if chrono_age == 11.5:
        if 0 <= CGscore <= 10:
            standardized_CGscore = 1
        elif 11 <= CGscore <= 16:
            standardized_CGscore = CGscore - 9
        elif 17 <= CGscore <= 18:
            standardized_CGscore = 8
        elif 19 <= CGscore <= 20:
            standardized_CGscore = 9
        elif CGscore == 21:
            standardized_CGscore = 10
        elif 22 <= CGscore <= 28:
            standardized_CGscore = CGscore - 10
        else:
            standardized_CGscore = 19

    if chrono_age == 12:
        if 0 <= CGscore <= 11:
            standardized_CGscore = 1
        elif 12 <= CGscore <= 18:
            standardized_CGscore = CGscore - 10
        elif 19 <= CGscore <= 20:
            standardized_CGscore = 9
        elif CGscore == 21:
            standardized_CGscore = 10
        elif 22 <= CGscore <= 28:
            standardized_CGscore = CGscore - 10
        else:
            standardized_CGscore = 19

    if chrono_age == 12.5:
        if 0 <= CGscore <= 12:
            standardized_CGscore = 1
        elif 13 <= CGscore <= 18:
            standardized_CGscore = CGscore - 11
        elif 19 <= CGscore <= 20:
            standardized_CGscore = 8
        elif CGscore == 21:
            standardized_CGscore = 9
        elif 22 <= CGscore <= 23:
            standardized_CGscore = CGscore - 11
        elif 24 <= CGscore <= 28:
            standardized_CGscore = CGscore - 10
        else:
            standardized_CGscore = 19

    if chrono_age == 13:
        if 0 <= CGscore <= 12:
            standardized_CGscore = 1
        elif 13 <= CGscore <= 18:
            standardized_CGscore = CGscore - 11
        elif 19 <= CGscore <= 20:
            standardized_CGscore = 8
        elif CGscore == 21:
            standardized_CGscore = 9
        elif 22 <= CGscore <= 24:
            standardized_CGscore = CGscore - 11
        elif 25 <= CGscore <= 28:
            standardized_CGscore = CGscore - 10
        else:
            standardized_CGscore = 19

    if chrono_age == 13.5:
        if 0 <= CGscore <= 12:
            standardized_CGscore = 1
        elif 13 <= CGscore <= 17:
            standardized_CGscore = CGscore - 11
        elif 18 <= CGscore <= 19:
            standardized_CGscore = 7
        elif 20 <= CGscore <= 22:
            standardized_CGscore = CGscore - 12
        elif 23 <= CGscore <= 25:
            standardized_CGscore = CGscore - 11
        elif 26 <= CGscore <= 27:
            standardized_CGscore = CGscore - 10
        elif 28 <= CGscore <= 29:
            standardized_CGscore = 18
        else:
            standardized_CGscore = 19

    if chrono_age == 14:
        if 0 <= CGscore <= 13:
            standardized_CGscore = 1
        elif 14 <= CGscore <= 19:
            standardized_CGscore = CGscore - 12
        elif 20 <= CGscore <= 21:
            standardized_CGscore = 8
        elif 22 <= CGscore <= 23:
            standardized_CGscore = CGscore - 13
        elif 24 <= CGscore <= 25:
            standardized_CGscore = CGscore - 12
        elif 26 <= CGscore <= 30:
            standardized_CGscore = CGscore - 11

    if chrono_age == 14.5:
        if 0 <= CGscore <= 13:
            standardized_CGscore = 1
        elif 14 <= CGscore <= 19:
            standardized_CGscore = CGscore - 12
        elif 20 <= CGscore <= 21:
            standardized_CGscore = 8
        elif 22 <= CGscore <= 24:
            standardized_CGscore = CGscore - 13
        elif 25 <= CGscore <= 25:
            standardized_CGscore = CGscore - 12
        elif 27 <= CGscore <= 30:
            standardized_CGscore = CGscore - 11

    if chrono_age == 15:
        if 0 <= CGscore <= 13:
            standardized_CGscore = 1
        elif 14 <= CGscore <= 19:
            standardized_CGscore = CGscore - 12
        elif 20 <= CGscore <= 21:
            standardized_CGscore = 8
        elif 22 <= CGscore <= 24:
            standardized_CGscore = CGscore - 13
        elif 25 <= CGscore <= 30:
            standardized_CGscore = CGscore - 12

    if chrono_age == 15.5:
        if 0 <= CGscore <= 14:
            standardized_CGscore = 1
        elif 15 <= CGscore <= 24:
            standardized_CGscore = CGscore - 13
        elif 25 <= CGscore <= 30:
            standardized_CGscore = CGscore - 12

    if chrono_age == 16:
        if 0 <= CGscore <= 15:
            standardized_CGscore = 1
        elif 16 <= CGscore <= 17:
            standardized_CGscore = CGscore - 14
        elif 18 <= CGscore <= 20:
            standardized_CGscore = CGscore - 13
        elif 21 <= CGscore <= 22:
            standardized_CGscore = 8
        elif CGscore == 23:
            standardized_CGscore = 9
        elif CGscore == 24:
            standardized_CGscore = 11
        elif 25 <= CGscore <= 30:
            standardized_CGscore = CGscore - 12

    if chrono_age == 16.5:
        if 0 <= CGscore <= 15:
            standardized_CGscore = 1
        elif 16 <= CGscore <= 17:
            standardized_CGscore = CGscore - 14
        elif 18 <= CGscore <= 20:
            standardized_CGscore = CGscore - 13
        elif 21 <= CGscore <= 22:
            standardized_CGscore = 8
        elif 23 <= CGscore <= 26:
            standardized_CGscore = CGscore - 14
        elif 27 <= CGscore <= 30:
            standardized_CGscore = CGscore - 17

    standardized_scores.append(standardized_CGscore)
    QIrealizacao.append(standardized_CGscore)
    QIop.append(standardized_CGscore)


def find_standardized_Infscore():
    if chrono_age == 6:
        if 0 <= Infscore <= 2:
            standardized_Infscore = Infscore + 2
        elif Infscore == 3:
            standardized_Infscore = 6
        elif 4 <= Infscore <= 5:
            standardized_Infscore = Infscore + 4
        elif Infscore == 6:
            standardized_Infscore = 11
        elif Infscore == 7:
            standardized_Infscore = 13
        elif 8 <= Infscore <= 10:
            standardized_Infscore = Infscore + 7
        else:
            standardized_Infscore = 19

    if chrono_age == 6.5:
        if 0 <= Infscore <= 2:
            standardized_Infscore = Infscore + 2
        elif 3 <= Infscore <= 4:
            standardized_Infscore = Infscore + 3
        elif 5 <= Infscore <= 8:
            standardized_Infscore = Infscore + 4
        elif 9 <= Infscore <= 12:
            standardized_Infscore = Infscore + 5
        else:
            standardized_Infscore = 19

    if chrono_age == 7:
        if 0 <= Infscore <= 4:
            standardized_Infscore = Infscore + 1
        elif 5 <= Infscore <= 8:
            standardized_Infscore = Infscore + 2
        elif 9 <= Infscore <= 10:
            standardized_Infscore = Infscore + 3
        elif 11 <= Infscore <= 12:
            standardized_Infscore = Infscore + 4
        elif Infscore == 13:
            standardized_Infscore = 18
        else:
            standardized_Infscore = 19

    if chrono_age == 7.5:
        if Infscore == 0:
            standardized_Infscore = 1
        elif 1 <= Infscore <= 2:
            standardized_Infscore = 2
        elif 3 <= Infscore <= 4:
            standardized_Infscore = Infscore
        elif 5 <= Infscore <= 10:
            standardized_Infscore = Infscore + 1
        elif 11 <= Infscore <= 13:
            standardized_Infscore = Infscore + 2
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 16
        elif 16 <= Infscore <= 17:
            standardized_Infscore = Infscore + 1
        else:
            standardized_Infscore = 19

    if chrono_age == 8:
        if 0 <= Infscore <= 2:
            standardized_Infscore = 1
        elif 3 <= Infscore <= 4:
            standardized_Infscore = 2
        elif 5 <= Infscore <= 6:
            standardized_Infscore = Infscore - 2
        elif 7 <= Infscore <= 11:
            standardized_Infscore = Infscore - 1
        elif 12 <= Infscore <= 15:
            standardized_Infscore = Infscore
        elif 16 <= Infscore <= 17:
            standardized_Infscore = Infscore - 1
        else:
            standardized_Infscore = 19

    if chrono_age == 8.5:
        if 0 <= Infscore <= 2:
            standardized_Infscore = 1
        elif 3 <= Infscore <= 4:
            standardized_Infscore = 2
        elif 5 <= Infscore <= 8:
            standardized_Infscore = Infscore - 2
        elif 9 <= Infscore <= 12:
            standardized_Infscore = Infscore - 1
        elif 13 <= Infscore <= 14:
            standardized_Infscore = 12
        elif 15 <= Infscore <= 17:
            standardized_Infscore = Infscore - 2
        elif 18 <= Infscore <= 19:
            standardized_Infscore = 16
        elif Infscore == 20:
            standardized_Infscore = 17
        elif 21 <= Infscore <= 22:
            standardized_Infscore = 18
        else:
            standardized_Infscore = 19

    if chrono_age == 9:
        if 0 <= Infscore <= 3:
            standardized_Infscore = 1
        elif 4 <= Infscore <= 10:
            standardized_Infscore = Infscore - 2
        elif 11 <= Infscore <= 12:
            standardized_Infscore = 9
        elif 13 <= Infscore <= 17:
            standardized_Infscore = Infscore - 3
        elif 18 <= Infscore <= 19:
            standardized_Infscore = 15
        elif Infscore == 20:
            standardized_Infscore = 16
        elif 21 <= Infscore <= 22:
            standardized_Infscore = 17
        elif Infscore == 23:
            standardized_Infscore = 18
        else:
            standardized_Infscore = 19

    if chrono_age == 9.5:
        if 0 <= Infscore <= 4:
            standardized_Infscore = 1
        elif 5 <= Infscore <= 13:
            standardized_Infscore = Infscore - 3
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 11
        elif 16 <= Infscore <= 18:
            standardized_Infscore = Infscore - 4
        elif 19 <= Infscore <= 20:
            standardized_Infscore = 15
        elif 21 <= Infscore <= 23:
            standardized_Infscore = Infscore - 5
        else:
            standardized_Infscore = 19

    if chrono_age == 10:
        if 0 <= Infscore <= 5:
            standardized_Infscore = 1
        elif 6 <= Infscore <= 13:
            standardized_Infscore = Infscore - 4
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 10
        elif 16 <= Infscore <= 23:
            standardized_Infscore = Infscore - 5
        else:
            standardized_Infscore = 19

    if chrono_age == 10.5:
        if 0 <= Infscore <= 5:
            standardized_Infscore = 1
        elif 6 <= Infscore <= 13:
            standardized_Infscore = Infscore - 4
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 10
        elif 16 <= Infscore <= 23:
            standardized_Infscore = Infscore - 5
        else:
            standardized_Infscore = 19

    if chrono_age == 11:
        if 0 <= Infscore <= 6:
            standardized_Infscore = 1
        elif 7 <= Infscore <= 13:
            standardized_Infscore = Infscore - 5
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 9
        elif 16 <= Infscore <= 21:
            standardized_Infscore = Infscore - 6
        elif 22 <= Infscore <= 23:
            standardized_Infscore = Infscore - 5
        else:
            standardized_Infscore = 19

    if chrono_age == 11.5:
        if 0 <= Infscore <= 6:
            standardized_Infscore = 1
        elif Infscore == 7:
            standardized_Infscore = 2
        elif 8 <= Infscore <= 9:
            standardized_Infscore = 3
        elif Infscore == 10:
            standardized_Infscore = 4
        elif 11 <= Infscore <= 13:
            standardized_Infscore = Infscore - 5
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 9
        elif 16 <= Infscore <= 18:
            standardized_Infscore = Infscore - 6
        elif 19 <= Infscore <= 20:
            standardized_Infscore = 13
        elif 21 <= Infscore <= 24:
            standardized_Infscore = Infscore - 7
        elif 25 <= Infscore <= 26:
            standardized_Infscore = 18
        else:
            standardized_Infscore = 19

    if chrono_age == 12:
        if 0 <= Infscore <= 7:
            standardized_Infscore = 1
        elif 8 <= Infscore <= 15:
            standardized_Infscore = Infscore - 6
        elif 16 <= Infscore <= 17:
            standardized_Infscore = 10
        elif 18 <= Infscore <= 23:
            standardized_Infscore = Infscore - 7
        elif 24 <= Infscore <= 25:
            standardized_Infscore = 17
        elif 26 <= Infscore <= 27:
            standardized_Infscore = 18
        else:
            standardized_Infscore = 19

    if chrono_age == 12.5:
        if 0 <= Infscore <= 8:
            standardized_Infscore = 1
        elif 9 <= Infscore <= 10:
            standardized_Infscore = Infscore - 7
        elif 16 <= Infscore <= 17:
            standardized_Infscore = 10
        elif 11 <= Infscore <= 12:
            standardized_Infscore = Infscore - 6
        elif 13 <= Infscore <= 14:
            standardized_Infscore = 7
        elif Infscore == 15:
            standardized_Infscore = 8
        elif 16 <= Infscore <= 17:
            standardized_Infscore = 9
        elif 18 <= Infscore <= 19:
            standardized_Infscore = Infscore - 8
        elif 20 <= Infscore <= 21:
            standardized_Infscore = 12
        elif 22 <= Infscore <= 27:
            standardized_Infscore = Infscore - 9
        else:
            standardized_Infscore = 19

    if chrono_age == 13:
        if 0 <= Infscore <= 9:
            standardized_Infscore = 1
        elif 10 <= Infscore <= 13:
            standardized_Infscore = Infscore - 8
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 6
        elif 16 <= Infscore <= 17:
            standardized_Infscore = Infscore - 9
        elif 18 <= Infscore <= 19:
            standardized_Infscore = 9
        elif 20 <= Infscore <= 28:
            standardized_Infscore = Infscore - 10
        else:
            standardized_Infscore = 19

    if chrono_age == 13.5:
        if 0 <= Infscore <= 9:
            standardized_Infscore = 1
        elif 10 <= Infscore <= 11:
            standardized_Infscore = Infscore - 8
        elif 12 <= Infscore <= 13:
            standardized_Infscore = 4
        elif 14 <= Infscore <= 17:
            standardized_Infscore = Infscore - 9
        elif 18 <= Infscore <= 19:
            standardized_Infscore = 9
        elif 20 <= Infscore <= 28:
            standardized_Infscore = Infscore - 10
        else:
            standardized_Infscore = 19

    if chrono_age == 14:
        if 0 <= Infscore <= 9:
            standardized_Infscore = 1
        elif 10 <= Infscore <= 11:
            standardized_Infscore = Infscore - 8
        elif 12 <= Infscore <= 13:
            standardized_Infscore = 4
        elif 14 <= Infscore <= 16:
            standardized_Infscore = Infscore - 9
        elif 17 <= Infscore <= 18:
            standardized_Infscore = 8
        elif Infscore == 19:
            standardized_Infscore = 9
        elif 20 <= Infscore <= 21:
            standardized_Infscore = 10
        else:
            standardized_Infscore = Infscore - 11

    if chrono_age == 14.5:
        if 0 <= Infscore <= 10:
            standardized_Infscore = 1
        elif 11 <= Infscore <= 15:
            standardized_Infscore = Infscore - 9
        elif 16 <= Infscore <= 17:
            standardized_Infscore = 7
        elif Infscore == 18:
            standardized_Infscore = 8
        elif 19 <= Infscore <= 20:
            standardized_Infscore = 9
        else:
            standardized_Infscore = Infscore - 11

    if chrono_age == 15:
        if 0 <= Infscore <= 10:
            standardized_Infscore = 1
        elif 11 <= Infscore <= 13:
            standardized_Infscore = Infscore - 9
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 5
        elif 16 <= Infscore <= 17:
            standardized_Infscore = Infscore - 10
        elif 18 <= Infscore <= 19:
            standardized_Infscore = 8
        elif Infscore == 20:
            standardized_Infscore = 9
        elif 21 <= Infscore <= 22:
            standardized_Infscore = 10
        elif Infscore == 23:
            standardized_Infscore = 11
        else:
            standardized_Infscore = Infscore - 11

    if chrono_age == 15.5:
        if 0 <= Infscore <= 10:
            standardized_Infscore = 1
        elif Infscore == 11:
            standardized_Infscore = 2
        elif 12 <= Infscore <= 13:
            standardized_Infscore = 3
        elif Infscore == 14:
            standardized_Infscore = 4
        elif 15 <= Infscore <= 16:
            standardized_Infscore = 5
        elif 17 <= Infscore <= 19:
            standardized_Infscore = Infscore - 11
        elif 20 <= Infscore <= 21:
            standardized_Infscore = 9
        elif 22 <= Infscore <= 28:
            standardized_Infscore = Infscore - 12
        else:
            standardized_Infscore = Infscore - 11

    if chrono_age == 16:
        if 0 <= Infscore <= 10:
            standardized_Infscore = 1
        elif 11 <= Infscore <= 12:
            standardized_Infscore = 2
        elif Infscore == 13:
            standardized_Infscore = 3
        elif 14 <= Infscore <= 15:
            standardized_Infscore = 4
        elif 16 <= Infscore <= 17:
            standardized_Infscore = 5
        elif 18 <= Infscore <= 20:
            standardized_Infscore = Infscore - 12
        elif 21 <= Infscore <= 22:
            standardized_Infscore = 9
        elif 23 <= Infscore <= 24:
            standardized_Infscore = 10
        elif Infscore == 25:
            standardized_Infscore = 11
        elif 26 <= Infscore <= 28:
            standardized_Infscore = Infscore - 13
        else:
            standardized_Infscore = Infscore - 12

    if chrono_age == 16.5:
        if 0 <= Infscore <= 12:
            standardized_Infscore = 1
        elif 13 <= Infscore <= 14:
            standardized_Infscore = Infscore - 11
        elif 15 <= Infscore <= 16:
            standardized_Infscore = 4
        elif 17 <= Infscore <= 20:
            standardized_Infscore = Infscore - 12
        elif 21 <= Infscore <= 22:
            standardized_Infscore = 9
        elif 23 <= Infscore <= 24:
            standardized_Infscore = 10
        elif 25 <= Infscore <= 26:
            standardized_Infscore = Infscore - 14
        else:
            standardized_Infscore = Infscore - 13

    standardized_scores.append(standardized_Infscore)
    QIverbal.append(standardized_Infscore)
    QIcv.append(standardized_Infscore)


def find_standardized_Semscore():
    if chrono_age == 6:
        if Semscore == 0:
            standardized_Semscore = 5
        elif 1 <= Semscore <= 4:
            standardized_Semscore = Semscore + 6
        elif Semscore == 5:
            standardized_Semscore = 12
        elif 6 <= Semscore <= 7:
            standardized_Semscore = Semscore + 8
        elif 8 <= Semscore <= 9:
            standardized_Semscore = Semscore + 9
        else:
            standardized_Semscore = 19

    if chrono_age == 6.5:
        if Semscore == 0:
            standardized_Semscore = 5
        elif 1 <= Semscore <= 4:
            standardized_Semscore = Semscore + 6
        elif 5 <= Semscore <= 11:
            standardized_Semscore = Semscore + 7
        else:
            standardized_Semscore = 19

    if chrono_age == 7:
        if Semscore == 0:
            standardized_Semscore = 4
        elif 1 <= Semscore <= 6:
            standardized_Semscore = Semscore + 5
        elif 7 <= Semscore <= 8:
            standardized_Semscore = Semscore + 6
        elif 9 <= Semscore <= 11:
            standardized_Semscore = Semscore + 7
        else:
            standardized_Semscore = 19

    if chrono_age == 7.5:
        if 0 <= Semscore <= 1:
            standardized_Semscore = Semscore + 4
        elif 2 <= Semscore <= 11:
            standardized_Semscore = Semscore + 5
        elif 12 <= Semscore <= 13:
            standardized_Semscore = 17
        elif Semscore == 14:
            standardized_Semscore = 18
        else:
            standardized_Semscore = 19

    if chrono_age == 8:
        if 0 <= Semscore <= 4:
            standardized_Semscore = Semscore + 4
        elif 5 <= Semscore <= 6:
            standardized_Semscore = 9
        elif 7 <= Semscore <= 15:
            standardized_Semscore = Semscore + 3
        else:
            standardized_Semscore = 19

    if chrono_age == 8.5:
        if 0 <= Semscore <= 8:
            standardized_Semscore = Semscore + 3
        elif 9 <= Semscore <= 10:
            standardized_Semscore = 12
        elif 11 <= Semscore <= 12:
            standardized_Semscore = 13
        elif Semscore == 13:
            standardized_Semscore = 14
        elif 14 <= Semscore <= 16:
            standardized_Semscore = 15
        elif 17 <= Semscore <= 19:
            standardized_Semscore = Semscore + 1
        else:
            standardized_Semscore = 19

    if chrono_age == 9:
        if 0 <= Semscore <= 4:
            standardized_Semscore = Semscore + 3
        elif 5 <= Semscore <= 6:
            standardized_Semscore = 8
        elif Semscore == 7:
            standardized_Semscore = 9
        elif 8 <= Semscore <= 9:
            standardized_Semscore = 10
        elif 10 <= Semscore <= 11:
            standardized_Semscore = Semscore + 1
        elif 12 <= Semscore <= 13:
            standardized_Semscore = 13
        elif 14 <= Semscore <= 16:
            standardized_Semscore = 14
        elif 17 <= Semscore <= 20:
            standardized_Semscore = Semscore - 2
        else:
            standardized_Semscore = 19

    if chrono_age == 9.5:
        if 0 <= Semscore <= 1:
            standardized_Semscore = Semscore + 3
        elif 2 <= Semscore <= 3:
            standardized_Semscore = 5
        elif 4 <= Semscore <= 7:
            standardized_Semscore = Semscore + 2
        elif 8 <= Semscore <= 9:
            standardized_Semscore = 10
        elif 10 <= Semscore <= 11:
            standardized_Semscore = 11
        elif 12 <= Semscore <= 13:
            standardized_Semscore = 12
        elif 14 <= Semscore <= 15:
            standardized_Semscore = 13
        elif 16 <= Semscore <= 17:
            standardized_Semscore = 14
        elif 18 <= Semscore <= 21:
            standardized_Semscore = Semscore - 3
        else:
            standardized_Semscore = 19

    if chrono_age == 10:
        if 0 <= Semscore <= 1:
            standardized_Semscore = 3
        elif 2 <= Semscore <= 5:
            standardized_Semscore = Semscore + 2
        elif 6 <= Semscore <= 7:
            standardized_Semscore = 8
        elif 8 <= Semscore <= 9:
            standardized_Semscore = 9
        elif 10 <= Semscore <= 11:
            standardized_Semscore = 10
        elif 12 <= Semscore <= 13:
            standardized_Semscore = 11
        elif Semscore == 14:
            standardized_Semscore = 12
        elif 15 <= Semscore <= 16:
            standardized_Semscore = 13
        elif 17 <= Semscore <= 21:
            standardized_Semscore = Semscore - 3
        else:
            standardized_Semscore = 19

    if chrono_age == 10.5:
        if 0 <= Semscore <= 2:
            standardized_Semscore = Semscore + 2
        elif 3 <= Semscore <= 4:
            standardized_Semscore = 5
        elif 6 <= Semscore <= 7:
            standardized_Semscore = 7
        elif Semscore == 8:
            standardized_Semscore = 8
        elif 9 <= Semscore <= 10:
            standardized_Semscore = 9
        elif 11 <= Semscore <= 12:
            standardized_Semscore = 10
        elif 13 <= Semscore <= 14:
            standardized_Semscore = 11
        elif 15 <= Semscore <= 16:
            standardized_Semscore = 12
        elif Semscore == 17:
            standardized_Semscore = 13
        elif 18 <= Semscore <= 19:
            standardized_Semscore = 14
        elif 20 <= Semscore <= 23:
            standardized_Semscore = Semscore - 5
        else:
            standardized_Semscore = 19

    if chrono_age == 11:
        if 0 <= Semscore <= 1:
            standardized_Semscore = Semscore + 1
        elif 2 <= Semscore <= 3:
            standardized_Semscore = 3
        elif 4 <= Semscore <= 5:
            standardized_Semscore = 4
        elif 6 <= Semscore <= 8:
            standardized_Semscore = Semscore - 1
        elif 9 <= Semscore <= 10:
            standardized_Semscore = 8
        elif 11 <= Semscore <= 12:
            standardized_Semscore = 9
        elif 13 <= Semscore <= 14:
            standardized_Semscore = 10
        elif 15 <= Semscore <= 16:
            standardized_Semscore = 11
        elif 17 <= Semscore <= 18:
            standardized_Semscore = Semscore - 5
        elif 19 <= Semscore <= 20:
            standardized_Semscore = 14
        elif 21 <= Semscore <= 24:
            standardized_Semscore = Semscore - 6
        else:
            standardized_Semscore = 19

    if chrono_age == 11.5:
        if 0 <= Semscore <= 1:
            standardized_Semscore = 1
        elif Semscore == 2:
            standardized_Semscore = 2
        elif 3 <= Semscore <= 4:
            standardized_Semscore = 3
        elif 5 <= Semscore <= 6:
            standardized_Semscore = Semscore - 1
        elif 7 <= Semscore <= 8:
            standardized_Semscore = 6
        elif Semscore == 9:
            standardized_Semscore = 7
        elif 10 <= Semscore <= 11:
            standardized_Semscore = 8
        elif 12 <= Semscore <= 13:
            standardized_Semscore = 9
        elif 14 <= Semscore <= 15:
            standardized_Semscore = 10
        elif Semscore == 16:
            standardized_Semscore = 11
        elif 17 <= Semscore <= 18:
            standardized_Semscore = 12
        elif 19 <= Semscore <= 20:
            standardized_Semscore = Semscore - 6
        elif 21 <= Semscore <= 22:
            standardized_Semscore = 15
        elif 23 <= Semscore <= 25:
            standardized_Semscore = Semscore - 7
        else:
            standardized_Semscore = 19

    if chrono_age == 12:
        if 0 <= Semscore <= 2:
            standardized_Semscore = 1
        elif 3 <= Semscore <= 4:
            standardized_Semscore = 2
        elif 5 <= Semscore <= 7:
            standardized_Semscore = Semscore - 2
        elif 8 <= Semscore <= 9:
            standardized_Semscore = 6
        elif 10 <= Semscore <= 11:
            standardized_Semscore = 7
        elif 12 <= Semscore <= 13:
            standardized_Semscore = 8
        elif Semscore == 14:
            standardized_Semscore = 9
        elif 15 <= Semscore <= 16:
            standardized_Semscore = 10
        elif 17 <= Semscore <= 18:
            standardized_Semscore = Semscore - 6
        elif 19 <= Semscore <= 20:
            standardized_Semscore = 13
        elif 21 <= Semscore <= 25:
            standardized_Semscore = Semscore - 7
        else:
            standardized_Semscore = 19

    if chrono_age == 12.5:
        if 0 <= Semscore <= 4:
            standardized_Semscore = 1
        elif 5 <= Semscore <= 7:
            standardized_Semscore = Semscore - 3
        elif 8 <= Semscore <= 9:
            standardized_Semscore = 5
        elif Semscore == 10:
            standardized_Semscore = 6
        elif 11 <= Semscore <= 12:
            standardized_Semscore = 7
        elif 13 <= Semscore <= 14:
            standardized_Semscore = 8
        elif 15 <= Semscore <= 16:
            standardized_Semscore = Semscore - 6
        elif 17 <= Semscore <= 18:
            standardized_Semscore = 11
        elif Semscore == 19:
            standardized_Semscore = 12
        elif 20 <= Semscore <= 21:
            standardized_Semscore = 13
        elif 22 <= Semscore <= 24:
            standardized_Semscore = Semscore - 8
        elif Semscore == 25:
            standardized_Semscore = 18
        else:
            standardized_Semscore = 19

    if chrono_age == 13:
        if 0 <= Semscore <= 4:
            standardized_Semscore = 1
        elif 5 <= Semscore <= 6:
            standardized_Semscore = 2
        elif Semscore == 7:
            standardized_Semscore = 3
        elif 8 <= Semscore <= 9:
            standardized_Semscore = 4
        elif Semscore == 10:
            standardized_Semscore = 5
        elif 11 <= Semscore <= 12:
            standardized_Semscore = 6
        elif Semscore == 13:
            standardized_Semscore = 7
        elif 14 <= Semscore <= 15:
            standardized_Semscore = 8
        elif 16 <= Semscore <= 17:
            standardized_Semscore = 9
        elif 18 <= Semscore <= 26:
            standardized_Semscore = Semscore - 8
        else:
            standardized_Semscore = 19

    if chrono_age == 13.5:
        if 0 <= Semscore <= 5:
            standardized_Semscore = 1
        elif 6 <= Semscore <= 7:
            standardized_Semscore = Semscore - 4
        elif 8 <= Semscore <= 9:
            standardized_Semscore = 4
        elif 10 <= Semscore <= 11:
            standardized_Semscore = 5
        elif Semscore == 12:
            standardized_Semscore = 6
        elif 13 <= Semscore <= 14:
            standardized_Semscore = 7
        elif Semscore == 15:
            standardized_Semscore = 8
        elif 16 <= Semscore <= 17:
            standardized_Semscore = 9
        elif Semscore == 18:
            standardized_Semscore = 10
        elif 19 <= Semscore <= 20:
            standardized_Semscore = 11
        elif 21 <= Semscore <= 27:
            standardized_Semscore = Semscore - 9
        else:
            standardized_Semscore = 19

    if chrono_age == 14:
        if 0 <= Semscore <= 6:
            standardized_Semscore = 1
        elif 7 <= Semscore <= 8:
            standardized_Semscore = 2
        elif 9 <= Semscore <= 12:
            standardized_Semscore = Semscore - 6
        elif 13 <= Semscore <= 14:
            standardized_Semscore = 7
        elif 15 <= Semscore <= 16:
            standardized_Semscore = 8
        elif 17 <= Semscore <= 18:
            standardized_Semscore = 9
        elif Semscore == 19:
            standardized_Semscore = 10
        elif 20 <= Semscore <= 21:
            standardized_Semscore = 11
        elif 22 <= Semscore <= 28:
            standardized_Semscore = Semscore - 10
        else:
            standardized_Semscore = 19

    if chrono_age == 14.5:
        if 0 <= Semscore <= 6:
            standardized_Semscore = 1
        elif 7 <= Semscore <= 8:
            standardized_Semscore = 2
        elif 9 <= Semscore <= 10:
            standardized_Semscore = Semscore - 6
        elif 11 <= Semscore <= 12:
            standardized_Semscore = 5
        elif Semscore == 13:
            standardized_Semscore = 6
        elif 14 <= Semscore <= 15:
            standardized_Semscore = 7
        elif 16 <= Semscore <= 17:
            standardized_Semscore = 8
        elif Semscore == 18:
            standardized_Semscore = 9
        elif 19 <= Semscore <= 20:
            standardized_Semscore = 10
        elif 21 <= Semscore <= 25:
            standardized_Semscore = Semscore - 10
        elif 26 <= Semscore <= 27:
            standardized_Semscore = 16
        elif 28 <= Semscore <= 29:
            standardized_Semscore = Semscore - 11
        else:
            standardized_Semscore = 19

    if chrono_age == 15:
        if 0 <= Semscore <= 8:
            standardized_Semscore = 1
        elif 9 <= Semscore <= 11:
            standardized_Semscore = Semscore - 7
        elif 12 <= Semscore <= 13:
            standardized_Semscore = 5
        elif 14 <= Semscore <= 15:
            standardized_Semscore = Semscore - 8
        elif 16 <= Semscore <= 17:
            standardized_Semscore = 8
        elif 18 <= Semscore <= 19:
            standardized_Semscore = 9
        elif 20 <= Semscore <= 21:
            standardized_Semscore = 10
        elif 22 <= Semscore <= 26:
            standardized_Semscore = Semscore - 11
        elif 27 <= Semscore <= 28:
            standardized_Semscore = 16
        elif 29 <= Semscore <= 30:
            standardized_Semscore = Semscore - 12
        else:
            standardized_Semscore = 19

    if chrono_age == 15.5:
        if 0 <= Semscore <= 8:
            standardized_Semscore = 1
        elif 9 <= Semscore <= 10:
            standardized_Semscore = 2
        elif 11 <= Semscore <= 12:
            standardized_Semscore = Semscore - 8
        elif 13 <= Semscore <= 14:
            standardized_Semscore = 5
        elif Semscore == 15:
            standardized_Semscore = 6
        elif 16 <= Semscore <= 17:
            standardized_Semscore = 7
        elif Semscore == 18:
            standardized_Semscore = 8
        elif 19 <= Semscore <= 20:
            standardized_Semscore = 9
        elif 21 <= Semscore <= 23:
            standardized_Semscore = Semscore - 11
        elif 24 <= Semscore <= 25:
            standardized_Semscore = 13
        elif 26 <= Semscore <= 30:
            standardized_Semscore = Semscore - 12
        else:
            standardized_Semscore = 19

    if chrono_age == 16:
        if 0 <= Semscore <= 9:
            standardized_Semscore = 1
        elif 10 <= Semscore <= 11:
            standardized_Semscore = 2
        elif 12 <= Semscore <= 13:
            standardized_Semscore = 3
        elif Semscore == 14:
            standardized_Semscore = 4
        elif 15 <= Semscore <= 16:
            standardized_Semscore = 5
        elif 17 <= Semscore <= 19:
            standardized_Semscore = Semscore - 11
        elif 20 <= Semscore <= 21:
            standardized_Semscore = 9
        elif 22 <= Semscore <= 24:
            standardized_Semscore = Semscore - 12
        elif 25 <= Semscore <= 26:
            standardized_Semscore = 13
        elif 27 <= Semscore <= 31:
            standardized_Semscore = Semscore - 13
        else:
            standardized_Semscore = 19

    if chrono_age == 16.5:
        if 0 <= Semscore <= 10:
            standardized_Semscore = 1
        elif 11 <= Semscore <= 12:
            standardized_Semscore = 2
        elif 13 <= Semscore <= 14:
            standardized_Semscore = 3
        elif 15 <= Semscore <= 18:
            standardized_Semscore = Semscore - 11
        elif 19 <= Semscore <= 20:
            standardized_Semscore = 8
        elif 21 <= Semscore <= 24:
            standardized_Semscore = Semscore - 12
        elif 25 <= Semscore <= 26:
            standardized_Semscore = 13
        elif 27 <= Semscore <= 31:
            standardized_Semscore = Semscore - 13
        else:
            standardized_Semscore = 19

    standardized_scores.append(standardized_Semscore)
    QIverbal.append(standardized_Semscore)
    QIcv.append(standardized_Semscore)


def find_standardized_Ariscore():
    if chrono_age == 6:
        if 0 <= Ariscore <= 6:
            standardized_Ariscore = Ariscore + 3
        elif Ariscore == 7:
            standardized_Ariscore = Ariscore + 4
        elif Ariscore == 8:
            standardized_Ariscore = Ariscore + 5
        elif Ariscore == 9:
            standardized_Ariscore = Ariscore + 6
        elif 10 <= Ariscore <= 11:
            standardized_Ariscore = Ariscore + 7
        else:
            standardized_Ariscore = 19

    if chrono_age == 6.5:
        if 0 <= Ariscore <= 6:
            standardized_Ariscore = Ariscore + 2
        elif 7 <= Ariscore <= 9:
            standardized_Ariscore = Ariscore + 3
        elif Ariscore == 10:
            standardized_Ariscore = Ariscore + 4
        elif 11 <= Ariscore <= 13:
            standardized_Ariscore = Ariscore + 5
        else:
            standardized_Ariscore = 19

    if chrono_age == 7:
        if 0 <= Ariscore <= 1:
            standardized_Ariscore = Ariscore + 1
        elif 2 <= Ariscore <= 3:
            standardized_Ariscore = 3
        elif 4 <= Ariscore <= 8:
            standardized_Ariscore = Ariscore
        elif Ariscore == 9:
            standardized_Ariscore = Ariscore + 1
        elif Ariscore == 10:
            standardized_Ariscore = Ariscore + 2
        elif 11 <= Ariscore <= 12:
            standardized_Ariscore = Ariscore + 4
        elif Ariscore == 13:
            standardized_Ariscore = Ariscore + 5
        else:
            standardized_Ariscore = 19

    if chrono_age == 7.5:
        if 0 <= Ariscore <= 2:
            standardized_Ariscore = 1
        elif Ariscore == 3:
            standardized_Ariscore = Ariscore - 1
        elif 4 <= Ariscore <= 5:
            standardized_Ariscore = 3
        elif Ariscore == 6:
            standardized_Ariscore = Ariscore - 2
        elif Ariscore == 7:
            standardized_Ariscore = Ariscore - 1
        elif 8 <= Ariscore <= 10:
            standardized_Ariscore = Ariscore
        elif 11 <= Ariscore <= 12:
            standardized_Ariscore = Ariscore + 1
        elif 16 <= Ariscore <= 16:
            standardized_Ariscore = Ariscore + 2
        else:
            standardized_Ariscore = 19

    if chrono_age == 8:
        if 0 <= Ariscore <= 2:
            standardized_Ariscore = 1
        elif 3 <= Ariscore <= 4:
            standardized_Ariscore = 2
        elif 5 <= Ariscore <= 11:
            standardized_Ariscore = Ariscore - 2
        elif 12 <= Ariscore <= 14:
            standardized_Ariscore = Ariscore - 1
        elif Ariscore == 15:
            standardized_Ariscore = Ariscore
        elif 16 <= Ariscore <= 17:
            standardized_Ariscore = Ariscore + 1
        else:
            standardized_Ariscore = 19

    if chrono_age == 8.5:
        if 0 <= Ariscore <= 3:
            standardized_Ariscore = 1
        elif 4 <= Ariscore <= 5:
            standardized_Ariscore = 2
        elif 6 <= Ariscore <= 7:
            standardized_Ariscore = Ariscore - 3
        elif 8 <= Ariscore <= 12:
            standardized_Ariscore = Ariscore - 2
        elif 13 <= Ariscore <= 19:
            standardized_Ariscore = Ariscore - 1
        else:
            standardized_Ariscore = 19

    if chrono_age == 9:
        if 0 <= Ariscore <= 3:
            standardized_Ariscore = 1
        elif 4 <= Ariscore <= 5:
            standardized_Ariscore = 2
        elif 6 <= Ariscore <= 7:
            standardized_Ariscore = Ariscore - 3
        elif 8 <= Ariscore <= 9:
            standardized_Ariscore = Ariscore - 2
        elif 10 <= Ariscore <= 11:
            standardized_Ariscore = 8
        elif 12 <= Ariscore <= 13:
            standardized_Ariscore = Ariscore - 3
        elif 14 <= Ariscore <= 17:
            standardized_Ariscore = Ariscore - 2
        elif 18 <= Ariscore <= 19:
            standardized_Ariscore = Ariscore - 1
        else:
            standardized_Ariscore = 19

    if chrono_age == 9.5:
        if 0 <= Ariscore <= 4:
            standardized_Ariscore = 1
        elif 5 <= Ariscore <= 14:
            standardized_Ariscore = Ariscore - 3
        elif 15 <= Ariscore <= 18:
            standardized_Ariscore = Ariscore - 2
        elif Ariscore == 19:
            standardized_Ariscore = Ariscore - 1
        else:
            standardized_Ariscore = 19

    if chrono_age == 10:
        if 0 <= Ariscore <= 4:
            standardized_Ariscore = 1
        elif 5 <= Ariscore <= 14:
            standardized_Ariscore = Ariscore - 3
        elif 15 <= Ariscore <= 18:
            standardized_Ariscore = Ariscore - 2
        elif Ariscore == 19:
            standardized_Ariscore = Ariscore - 1
        else:
            standardized_Ariscore = 19

    if chrono_age == 10.5:
        if 0 <= Ariscore <= 5:
            standardized_Ariscore = 1
        elif 6 <= Ariscore <= 8:
            standardized_Ariscore = Ariscore - 4
        elif 9 <= Ariscore <= 20:
            standardized_Ariscore = Ariscore - 3
        elif 21 <= Ariscore <= 22:
            standardized_Ariscore = 18
        else:
            standardized_Ariscore = 19

    if chrono_age == 11:
        if 0 <= Ariscore <= 5:
            standardized_Ariscore = 1
        elif 6 <= Ariscore <= 9:
            standardized_Ariscore = Ariscore - 4
        elif 10 <= Ariscore <= 11:
            standardized_Ariscore = Ariscore - 3
        elif 12 <= Ariscore <= 13:
            standardized_Ariscore = 9
        elif 14 <= Ariscore <= 15:
            standardized_Ariscore = Ariscore - 4
        elif 16 <= Ariscore <= 19:
            standardized_Ariscore = Ariscore - 3
        elif 20 <= Ariscore <= 21:
            standardized_Ariscore = 17
        elif 21 <= Ariscore <= 22:
            standardized_Ariscore = 18
        else:
            standardized_Ariscore = 19

    if chrono_age == 11.5:
        if 0 <= Ariscore <= 5:
            standardized_Ariscore = 1
        elif 6 <= Ariscore <= 17:
            standardized_Ariscore = Ariscore - 4
        elif Ariscore == 18:
            standardized_Ariscore = Ariscore - 3
        elif 19 <= Ariscore <= 20:
            standardized_Ariscore = 16
        elif Ariscore == 21:
            standardized_Ariscore = Ariscore - 4
        elif 22 <= Ariscore <= 23:
            standardized_Ariscore = 18
        else:
            standardized_Ariscore = 19

    if chrono_age == 12:
        if 0 <= Ariscore <= 6:
            standardized_Ariscore = 1
        elif 7 <= Ariscore <= 8:
            standardized_Ariscore = Ariscore - 5
        elif 9 <= Ariscore <= 21:
            standardized_Ariscore = Ariscore - 4
        elif 22 <= Ariscore <= 23:
            standardized_Ariscore = 18
        else:
            standardized_Ariscore = 19

    if chrono_age == 12.5:
        if 0 <= Ariscore <= 6:
            standardized_Ariscore = 1
        elif 7 <= Ariscore <= 14:
            standardized_Ariscore = Ariscore - 5
        elif 15 <= Ariscore <= 18:
            standardized_Ariscore = Ariscore - 4
        elif 19 <= Ariscore <= 20:
            standardized_Ariscore = 15
        elif 21 <= Ariscore <= 23:
            standardized_Ariscore = Ariscore - 5
        else:
            standardized_Ariscore = 19

    if chrono_age == 13:
        if 0 <= Ariscore <= 7:
            standardized_Ariscore = 1
        elif 8 <= Ariscore <= 11:
            standardized_Ariscore = Ariscore - 6
        elif Ariscore == 12:
            standardized_Ariscore = Ariscore - 5
        elif 13 <= Ariscore <= 14:
            standardized_Ariscore = 8
        elif 15 <= Ariscore <= 17:
            standardized_Ariscore = Ariscore - 6
        elif 18 <= Ariscore <= 22:
            standardized_Ariscore = Ariscore - 5
        elif 23 <= Ariscore <= 24:
            standardized_Ariscore = 18
        else:
            standardized_Ariscore = 19

    if chrono_age == 13.5:
        if 0 <= Ariscore <= 7:
            standardized_Ariscore = 1
        elif 8 <= Ariscore <= 11:
            standardized_Ariscore = Ariscore - 6
        elif Ariscore == 12:
            standardized_Ariscore = Ariscore - 5
        elif 13 <= Ariscore <= 14:
            standardized_Ariscore = 8
        elif 15 <= Ariscore <= 24:
            standardized_Ariscore = Ariscore - 6
        else:
            standardized_Ariscore = 19

    if chrono_age == 14:
        if 0 <= Ariscore <= 7:
            standardized_Ariscore = 1
        elif 8 <= Ariscore <= 11:
            standardized_Ariscore = Ariscore - 6
        elif Ariscore == 12:
            standardized_Ariscore = Ariscore - 5
        elif 13 <= Ariscore <= 14:
            standardized_Ariscore = 8
        elif 15 <= Ariscore <= 17:
            standardized_Ariscore = Ariscore - 6
        elif 18 <= Ariscore <= 19:
            standardized_Ariscore = 12
        elif 20 <= Ariscore <= 25:
            standardized_Ariscore = Ariscore - 7
        else:
            standardized_Ariscore = 19

    if chrono_age == 14.5:
        if 0 <= Ariscore <= 7:
            standardized_Ariscore = 1
        elif 8 <= Ariscore <= 11:
            standardized_Ariscore = Ariscore - 6
        elif Ariscore == 12:
            standardized_Ariscore = Ariscore - 5
        elif 13 <= Ariscore <= 14:
            standardized_Ariscore = 8
        elif 15 <= Ariscore <= 17:
            standardized_Ariscore = Ariscore - 6
        elif 18 <= Ariscore <= 19:
            standardized_Ariscore = 12
        elif 20 <= Ariscore <= 22:
            standardized_Ariscore = Ariscore - 7
        elif 23 <= Ariscore <= 24:
            standardized_Ariscore = 16
        elif 25 <= Ariscore <= 26:
            standardized_Ariscore = Ariscore - 8
        else:
            standardized_Ariscore = 19

    if chrono_age == 15:
        if 0 <= Ariscore <= 7:
            standardized_Ariscore = 1
        elif 8 <= Ariscore <= 11:
            standardized_Ariscore = Ariscore - 6
        elif Ariscore == 12:
            standardized_Ariscore = Ariscore - 5
        elif 13 <= Ariscore <= 14:
            standardized_Ariscore = 8
        elif Ariscore == 15:
            standardized_Ariscore = Ariscore - 6
        elif 16 <= Ariscore <= 17:
            standardized_Ariscore = 10
        elif 18 <= Ariscore <= 21:
            standardized_Ariscore = Ariscore - 7
        elif 22 <= Ariscore <= 23:
            standardized_Ariscore = 15
        elif 24 <= Ariscore <= 26:
            standardized_Ariscore = Ariscore - 8
        else:
            standardized_Ariscore = 19

    if chrono_age == 15.5:
        if 0 <= Ariscore <= 7:
            standardized_Ariscore = 1
        elif 8 <= Ariscore <= 14:
            standardized_Ariscore = Ariscore - 6
        elif 15 <= Ariscore <= 16:
            standardized_Ariscore = 9
        elif 17 <= Ariscore <= 18:
            standardized_Ariscore = Ariscore - 7
        elif 19 <= Ariscore <= 20:
            standardized_Ariscore = 12
        elif 21 <= Ariscore <= 26:
            standardized_Ariscore = Ariscore - 8
        else:
            standardized_Ariscore = 19

    if chrono_age == 16:
        if 0 <= Ariscore <= 7:
            standardized_Ariscore = 1
        elif 8 <= Ariscore <= 12:
            standardized_Ariscore = Ariscore - 6
        elif 13 <= Ariscore <= 14:
            standardized_Ariscore = 7
        elif 15 <= Ariscore <= 16:
            standardized_Ariscore = 8
        elif 17 <= Ariscore <= 24:
            standardized_Ariscore = Ariscore - 8
        elif 25 <= Ariscore <= 26:
            standardized_Ariscore = 17
        elif Ariscore == 27:
            standardized_Ariscore = Ariscore - 9
        else:
            standardized_Ariscore = 19

    if chrono_age == 16.5:
        if 0 <= Ariscore <= 8:
            standardized_Ariscore = 1
        elif 9 <= Ariscore <= 14:
            standardized_Ariscore = Ariscore - 7
        elif 15 <= Ariscore <= 16:
            standardized_Ariscore = 8
        elif 17 <= Ariscore <= 24:
            standardized_Ariscore = Ariscore - 8
        elif 25 <= Ariscore <= 26:
            standardized_Ariscore = 17
        elif Ariscore == 27:
            standardized_Ariscore = Ariscore - 9
        else:
            standardized_Ariscore = 19

    standardized_scores.append(standardized_Ariscore)
    QIverbal.append(standardized_Ariscore)


def find_standardized_Vocscore():
    if chrono_age == 6:
        if 0 <= Vocscore <= 6:
            standardized_Vocscore = Vocscore + 2
        elif 7 <= Vocscore <= 8:
            standardized_Vocscore = 9
        elif 9 <= Vocscore <= 10:
            standardized_Vocscore = 10
        elif 11 <= Vocscore <= 18:
            standardized_Vocscore = Vocscore
        else:
            standardized_Vocscore = 19

    if chrono_age == 6.5:
        if 0 <= Vocscore <= 2:
            standardized_Vocscore = Vocscore + 1
        elif 3 <= Vocscore <= 4:
            standardized_Vocscore = Vocscore + 2
        elif 5 <= Vocscore <= 6:
            standardized_Vocscore = 7
        elif Vocscore == 7:
            standardized_Vocscore = Vocscore + 1
        elif 8 <= Vocscore <= 9:
            standardized_Vocscore = 9
        elif Vocscore == 10:
            standardized_Vocscore = Vocscore
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 11
        elif 13 <= Vocscore <= 14:
            standardized_Vocscore = Vocscore - 1
        elif 15 <= Vocscore <= 16:
            standardized_Vocscore = 14
        elif 17 <= Vocscore <= 20:
            standardized_Vocscore = Vocscore - 2
        else:
            standardized_Vocscore = 19

    if chrono_age == 7:
        if 0 <= Vocscore <= 5:
            standardized_Vocscore = Vocscore + 1
        elif 6 <= Vocscore <= 7:
            standardized_Vocscore = 7
        elif 8 <= Vocscore <= 9:
            standardized_Vocscore = 8
        elif 10 <= Vocscore <= 11:
            standardized_Vocscore = 9
        elif 12 <= Vocscore <= 14:
            standardized_Vocscore = Vocscore - 2
        elif 15 <= Vocscore <= 16:
            standardized_Vocscore = 13
        elif 17 <= Vocscore <= 18:
            standardized_Vocscore = 14
        elif Vocscore == 19:
            standardized_Vocscore = Vocscore - 4
        elif 20 <= Vocscore <= 21:
            standardized_Vocscore = Vocscore - 3
        else:
            standardized_Vocscore = 19

    if chrono_age == 7.5:
        if 0 <= Vocscore <= 1:
            standardized_Vocscore = 1
        elif 2 <= Vocscore <= 5:
            standardized_Vocscore = Vocscore
        elif 6 <= Vocscore <= 7:
            standardized_Vocscore = 6
        elif 8 <= Vocscore <= 9:
            standardized_Vocscore = 7
        elif 10 <= Vocscore <= 11:
            standardized_Vocscore = 8
        elif Vocscore == 12:
            standardized_Vocscore = Vocscore - 3
        elif 13 <= Vocscore <= 14:
            standardized_Vocscore = 10
        elif Vocscore == 15:
            standardized_Vocscore = Vocscore - 4
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 12
        elif 18 <= Vocscore <= 21:
            standardized_Vocscore = Vocscore - 5
        elif 22 <= Vocscore <= 23:
            standardized_Vocscore = 17
        elif Vocscore == 24:
            standardized_Vocscore = Vocscore - 6
        else:
            standardized_Vocscore = 19

    if chrono_age == 8:
        if 0 <= Vocscore <= 1:
            standardized_Vocscore = 1
        elif 2 <= Vocscore <= 3:
            standardized_Vocscore = 2
        elif Vocscore == 4:
            standardized_Vocscore = Vocscore - 1
        elif 5 <= Vocscore <= 6:
            standardized_Vocscore = 4
        elif 7 <= Vocscore <= 9:
            standardized_Vocscore = 5
        elif Vocscore == 10:
            standardized_Vocscore = 6
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 7
        elif Vocscore == 13:
            standardized_Vocscore = Vocscore - 5
        elif 14 <= Vocscore <= 15:
            standardized_Vocscore = 9
        elif Vocscore == 16:
            standardized_Vocscore = Vocscore - 6
        elif 17 <= Vocscore <= 18:
            standardized_Vocscore = 11
        elif 19 <= Vocscore <= 25:
            standardized_Vocscore = Vocscore - 7
        else:
            standardized_Vocscore = 19

    if chrono_age == 8.5:
        if 0 <= Vocscore <= 3:
            standardized_Vocscore = 1
        elif Vocscore == 4:
            standardized_Vocscore = 2
        elif 5 <= Vocscore <= 6:
            standardized_Vocscore = 3
        elif 7 <= Vocscore <= 8:
            standardized_Vocscore = 4
        elif 9 <= Vocscore <= 10:
            standardized_Vocscore = 5
        elif Vocscore == 11:
            standardized_Vocscore = 6
        elif 12 <= Vocscore <= 13:
            standardized_Vocscore = 7
        elif Vocscore == 14:
            standardized_Vocscore = 8
        elif 15 <= Vocscore <= 16:
            standardized_Vocscore = 9
        elif Vocscore == 17:
            standardized_Vocscore = 10
        elif 18 <= Vocscore <= 19:
            standardized_Vocscore = 11
        elif Vocscore == 20:
            standardized_Vocscore = 12
        elif 21 <= Vocscore <= 22:
            standardized_Vocscore = 13
        elif 23 <= Vocscore <= 26:
            standardized_Vocscore = Vocscore - 9
        elif 27 <= Vocscore <= 28:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 9:
        if 0 <= Vocscore <= 3:
            standardized_Vocscore = 1
        elif 4 <= Vocscore <= 6:
            standardized_Vocscore = 2
        elif 7 <= Vocscore <= 8:
            standardized_Vocscore = 3
        elif 9 <= Vocscore <= 10:
            standardized_Vocscore = Vocscore - 5
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 6
        elif 13 <= Vocscore <= 14:
            standardized_Vocscore = 7
        elif Vocscore == 15:
            standardized_Vocscore = 8
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 9
        elif 18 <= Vocscore <= 19:
            standardized_Vocscore = 10
        elif 20 <= Vocscore <= 21:
            standardized_Vocscore = Vocscore - 9
        elif 22 <= Vocscore <= 23:
            standardized_Vocscore = 13
        elif 24 <= Vocscore <= 26:
            standardized_Vocscore = Vocscore - 10
        elif 27 <= Vocscore <= 28:
            standardized_Vocscore = 17
        elif Vocscore == 29:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 9.5:
        if 0 <= Vocscore <= 5:
            standardized_Vocscore = 1
        elif Vocscore == 6:
            standardized_Vocscore = 2
        elif 7 <= Vocscore <= 8:
            standardized_Vocscore = 3
        elif Vocscore == 9:
            standardized_Vocscore = 4
        elif 10 <= Vocscore <= 11:
            standardized_Vocscore = 5
        elif 12 <= Vocscore <= 13:
            standardized_Vocscore = 6
        elif Vocscore == 14:
            standardized_Vocscore = 7
        elif Vocscore == 15:
            standardized_Vocscore = 8
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 9
        elif 18 <= Vocscore <= 19:
            standardized_Vocscore = 10
        elif Vocscore <= 20:
            standardized_Vocscore = 11
        elif 21 <= Vocscore <= 22:
            standardized_Vocscore = 12
        elif 23 <= Vocscore <= 24:
            standardized_Vocscore = 13
        elif Vocscore == 25:
            standardized_Vocscore = 14
        elif 26 <= Vocscore <= 27:
            standardized_Vocscore = 15
        elif 28 <= Vocscore <= 29:
            standardized_Vocscore = 16
        elif 30 <= Vocscore <= 32:
            standardized_Vocscore = 17
        elif 33 <= Vocscore <= 34:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 10:
        if 0 <= Vocscore <= 5:
            standardized_Vocscore = 1
        elif 6 <= Vocscore <= 7:
            standardized_Vocscore = 2
        elif 8 <= Vocscore <= 9:
            standardized_Vocscore = 3
        elif 10 <= Vocscore <= 11:
            standardized_Vocscore = 4
        elif 12 <= Vocscore <= 13:
            standardized_Vocscore = Vocscore - 7
        elif 14 <= Vocscore <= 15:
            standardized_Vocscore = 7
        elif Vocscore == 16:
            standardized_Vocscore = 8
        elif 17 <= Vocscore <= 18:
            standardized_Vocscore = 9
        elif 19 <= Vocscore <= 20:
            standardized_Vocscore = 10
        elif Vocscore == 21:
            standardized_Vocscore = 11
        elif 22 <= Vocscore <= 23:
            standardized_Vocscore = 12
        elif 24 <= Vocscore <= 25:
            standardized_Vocscore = 13
        elif 26 <= Vocscore <= 27:
            standardized_Vocscore = 14
        elif 28 <= Vocscore <= 29:
            standardized_Vocscore = 15
        elif 30 <= Vocscore <= 31:
            standardized_Vocscore = 16
        elif 32 <= Vocscore <= 33:
            standardized_Vocscore = 17
        elif 34 <= Vocscore <= 35:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 10.5:
        if 0 <= Vocscore <= 5:
            standardized_Vocscore = 1
        elif 6 <= Vocscore <= 8:
            standardized_Vocscore = 2
        elif 9 <= Vocscore <= 10:
            standardized_Vocscore = 3
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 4
        elif 13 <= Vocscore <= 14:
            standardized_Vocscore = Vocscore - 8
        elif 15 <= Vocscore <= 16:
            standardized_Vocscore = 7
        elif 17 <= Vocscore <= 18:
            standardized_Vocscore = 8
        elif Vocscore == 19:
            standardized_Vocscore = 9
        elif 20 <= Vocscore <= 21:
            standardized_Vocscore = 10
        elif 22 <= Vocscore <= 23:
            standardized_Vocscore = 11
        elif 24 <= Vocscore <= 25:
            standardized_Vocscore = 12
        elif 26 <= Vocscore <= 27:
            standardized_Vocscore = 13
        elif 28 <= Vocscore <= 30:
            standardized_Vocscore = 14
        elif 31 <= Vocscore <= 32:
            standardized_Vocscore = 15
        elif 33 <= Vocscore <= 34:
            standardized_Vocscore = 16
        elif 35 <= Vocscore <= 36:
            standardized_Vocscore = 17
        elif Vocscore == 37:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 11:
        if 0 <= Vocscore <= 6:
            standardized_Vocscore = 1
        elif 7 <= Vocscore <= 8:
            standardized_Vocscore = 2
        elif 9 <= Vocscore <= 10:
            standardized_Vocscore = 3
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 4
        elif 13 <= Vocscore <= 14:
            standardized_Vocscore = 5
        elif Vocscore == 15:
            standardized_Vocscore = 6
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 7
        elif 18 <= Vocscore <= 19:
            standardized_Vocscore = 8
        elif 20 <= Vocscore <= 21:
            standardized_Vocscore = 9
        elif 22 <= Vocscore <= 23:
            standardized_Vocscore = 10
        elif 24 <= Vocscore <= 25:
            standardized_Vocscore = 11
        elif 26 <= Vocscore <= 27:
            standardized_Vocscore = 12
        elif 28 <= Vocscore <= 29:
            standardized_Vocscore = 13
        elif 30 <= Vocscore <= 31:
            standardized_Vocscore = 14
        elif 32 <= Vocscore <= 33:
            standardized_Vocscore = 15
        elif 34 <= Vocscore <= 35:
            standardized_Vocscore = 16
        elif Vocscore == 36:
            standardized_Vocscore = 17
        elif Vocscore == 37:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 11.5:
        if 0 <= Vocscore <= 7:
            standardized_Vocscore = 1
        elif 8 <= Vocscore <= 10:
            standardized_Vocscore = 2
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 3
        elif Vocscore == 13:
            standardized_Vocscore = 4
        elif 14 <= Vocscore <= 15:
            standardized_Vocscore = 5
        elif Vocscore == 16:
            standardized_Vocscore = 6
        elif 17 <= Vocscore <= 18:
            standardized_Vocscore = 7
        elif 19 <= Vocscore <= 20:
            standardized_Vocscore = 8
        elif 21 <= Vocscore <= 22:
            standardized_Vocscore = 9
        elif 23 <= Vocscore <= 24:
            standardized_Vocscore = 10
        elif 25 <= Vocscore <= 26:
            standardized_Vocscore = 11
        elif 27 <= Vocscore <= 29:
            standardized_Vocscore = 12
        elif 30 <= Vocscore <= 31:
            standardized_Vocscore = 13
        elif 32 <= Vocscore <= 33:
            standardized_Vocscore = 14
        elif 34 <= Vocscore <= 35:
            standardized_Vocscore = 15
        elif 36 <= Vocscore <= 38:
            standardized_Vocscore = 16
        elif 39 <= Vocscore <= 41:
            standardized_Vocscore = 17
        elif 42 <= Vocscore <= 43:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 12:
        if 0 <= Vocscore <= 8:
            standardized_Vocscore = 1
        elif 9 <= Vocscore <= 10:
            standardized_Vocscore = 2
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 3
        elif 13 <= Vocscore <= 14:
            standardized_Vocscore = 4
        elif Vocscore == 15:
            standardized_Vocscore = 5
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 6
        elif Vocscore == 18:
            standardized_Vocscore = 7
        elif 19 <= Vocscore <= 21:
            standardized_Vocscore = 8
        elif 22 <= Vocscore <= 24:
            standardized_Vocscore = 9
        elif 25 <= Vocscore <= 26:
            standardized_Vocscore = 10
        elif 27 <= Vocscore <= 28:
            standardized_Vocscore = 11
        elif 29 <= Vocscore <= 30:
            standardized_Vocscore = 12
        elif 31 <= Vocscore <= 32:
            standardized_Vocscore = 13
        elif 33 <= Vocscore <= 34:
            standardized_Vocscore = 14
        elif 35 <= Vocscore <= 37:
            standardized_Vocscore = 15
        elif 38 <= Vocscore <= 40:
            standardized_Vocscore = 16
        elif 41 <= Vocscore <= 42:
            standardized_Vocscore = 17
        elif 43 <= Vocscore <= 44:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 12.5:
        if 0 <= Vocscore <= 9:
            standardized_Vocscore = 1
        elif 10 <= Vocscore <= 11:
            standardized_Vocscore = 2
        elif 12 <= Vocscore <= 13:
            standardized_Vocscore = 3
        elif Vocscore == 14:
            standardized_Vocscore = 4
        elif Vocscore == 15:
            standardized_Vocscore = 5
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 6
        elif 18 <= Vocscore <= 20:
            standardized_Vocscore = 7
        elif 21 <= Vocscore <= 23:
            standardized_Vocscore = 8
        elif 24 <= Vocscore <= 25:
            standardized_Vocscore = 9
        elif 26 <= Vocscore <= 28:
            standardized_Vocscore = 10
        elif 29 <= Vocscore <= 30:
            standardized_Vocscore = 11
        elif 31 <= Vocscore <= 32:
            standardized_Vocscore = 12
        elif 33 <= Vocscore <= 35:
            standardized_Vocscore = 13
        elif 36 <= Vocscore <= 38:
            standardized_Vocscore = 14
        elif 39 <= Vocscore <= 41:
            standardized_Vocscore = 15
        elif 42 <= Vocscore <= 43:
            standardized_Vocscore = 16
        elif 44 <= Vocscore <= 45:
            standardized_Vocscore = Vocscore - 27
        else:
            standardized_Vocscore = 19

    if chrono_age == 13:
        if 0 <= Vocscore <= 10:
            standardized_Vocscore = 1
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 2
        elif 13 <= Vocscore <= 14:
            standardized_Vocscore = 3
        elif 15 <= Vocscore <= 16:
            standardized_Vocscore = 4
        elif 17 <= Vocscore <= 19:
            standardized_Vocscore = 5
        elif 20 <= Vocscore <= 21:
            standardized_Vocscore = 6
        elif 22 <= Vocscore <= 23:
            standardized_Vocscore = 7
        elif 24 <= Vocscore <= 26:
            standardized_Vocscore = 8
        elif 27 <= Vocscore <= 28:
            standardized_Vocscore = 9
        elif 29 <= Vocscore <= 30:
            standardized_Vocscore = 10
        elif 31 <= Vocscore <= 32:
            standardized_Vocscore = 11
        elif 33 <= Vocscore <= 35:
            standardized_Vocscore = 12
        elif 36 <= Vocscore <= 38:
            standardized_Vocscore = 13
        elif 39 <= Vocscore <= 40:
            standardized_Vocscore = 14
        elif 41 <= Vocscore <= 42:
            standardized_Vocscore = 15
        elif 43 <= Vocscore <= 44:
            standardized_Vocscore = 16
        elif 45 <= Vocscore <= 46:
            standardized_Vocscore = Vocscore - 28
        else:
            standardized_Vocscore = 19

    if chrono_age == 13.5:
        if 0 <= Vocscore <= 10:
            standardized_Vocscore = 1
        elif 11 <= Vocscore <= 12:
            standardized_Vocscore = 2
        elif 13 <= Vocscore <= 15:
            standardized_Vocscore = 3
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 4
        elif 18 <= Vocscore <= 20:
            standardized_Vocscore = 5
        elif 21 <= Vocscore <= 22:
            standardized_Vocscore = 6
        elif 23 <= Vocscore <= 24:
            standardized_Vocscore = 7
        elif 25 <= Vocscore <= 27:
            standardized_Vocscore = 8
        elif 28 <= Vocscore <= 29:
            standardized_Vocscore = 9
        elif 30 <= Vocscore <= 32:
            standardized_Vocscore = 10
        elif 33 <= Vocscore <= 34:
            standardized_Vocscore = 11
        elif 35 <= Vocscore <= 36:
            standardized_Vocscore = 12
        elif 37 <= Vocscore <= 38:
            standardized_Vocscore = 13
        elif 39 <= Vocscore <= 40:
            standardized_Vocscore = 14
        elif 41 <= Vocscore <= 42:
            standardized_Vocscore = 15
        elif 43 <= Vocscore <= 44:
            standardized_Vocscore = 16
        elif 45 <= Vocscore <= 46:
            standardized_Vocscore = Vocscore - 28
        else:
            standardized_Vocscore = 19

    if chrono_age == 14:
        if 0 <= Vocscore <= 13:
            standardized_Vocscore = 1
        elif 14 <= Vocscore <= 15:
            standardized_Vocscore = 2
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 3
        elif 18 <= Vocscore <= 19:
            standardized_Vocscore = 4
        elif 20 <= Vocscore <= 21:
            standardized_Vocscore = 5
        elif 22 <= Vocscore <= 23:
            standardized_Vocscore = 6
        elif 24 <= Vocscore <= 25:
            standardized_Vocscore = 7
        elif 26 <= Vocscore <= 27:
            standardized_Vocscore = 8
        elif 28 <= Vocscore <= 31:
            standardized_Vocscore = 9
        elif 32 <= Vocscore <= 33:
            standardized_Vocscore = 10
        elif 34 <= Vocscore <= 35:
            standardized_Vocscore = 11
        elif 36 <= Vocscore <= 37:
            standardized_Vocscore = 12
        elif 38 <= Vocscore <= 39:
            standardized_Vocscore = 13
        elif Vocscore == 40:
            standardized_Vocscore = 14
        elif 41 <= Vocscore <= 42:
            standardized_Vocscore = 15
        elif 43 <= Vocscore <= 44:
            standardized_Vocscore = 16
        elif 45 <= Vocscore <= 46:
            standardized_Vocscore = 17
        elif Vocscore == 47:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 14.5:
        if 0 <= Vocscore <= 13:
            standardized_Vocscore = 1
        elif 14 <= Vocscore <= 15:
            standardized_Vocscore = 2
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 3
        elif 18 <= Vocscore <= 19:
            standardized_Vocscore = 4
        elif 20 <= Vocscore <= 21:
            standardized_Vocscore = 5
        elif 22 <= Vocscore <= 24:
            standardized_Vocscore = 6
        elif 25 <= Vocscore <= 26:
            standardized_Vocscore = 7
        elif 27 <= Vocscore <= 29:
            standardized_Vocscore = 8
        elif 30 <= Vocscore <= 32:
            standardized_Vocscore = 9
        elif 33 <= Vocscore <= 34:
            standardized_Vocscore = 10
        elif 35 <= Vocscore <= 37:
            standardized_Vocscore = 11
        elif 38 <= Vocscore <= 39:
            standardized_Vocscore = 12
        elif 40 <= Vocscore <= 41:
            standardized_Vocscore = 13
        elif 42 <= Vocscore <= 43:
            standardized_Vocscore = 14
        elif 44 <= Vocscore <= 45:
            standardized_Vocscore = 15
        elif 46 <= Vocscore <= 47:
            standardized_Vocscore = 16
        elif 48 <= Vocscore <= 49:
            standardized_Vocscore = 17
        elif 50 <= Vocscore <= 52:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 15:
        if 0 <= Vocscore <= 13:
            standardized_Vocscore = 1
        elif 14 <= Vocscore <= 15:
            standardized_Vocscore = 2
        elif 16 <= Vocscore <= 17:
            standardized_Vocscore = 3
        elif 18 <= Vocscore <= 19:
            standardized_Vocscore = 4
        elif 20 <= Vocscore <= 22:
            standardized_Vocscore = 5
        elif 23 <= Vocscore <= 24:
            standardized_Vocscore = 6
        elif 25 <= Vocscore <= 27:
            standardized_Vocscore = 7
        elif 28 <= Vocscore <= 30:
            standardized_Vocscore = 8
        elif 31 <= Vocscore <= 33:
            standardized_Vocscore = 9
        elif 34 <= Vocscore <= 36:
            standardized_Vocscore = 10
        elif 37 <= Vocscore <= 38:
            standardized_Vocscore = 11
        elif 39 <= Vocscore <= 41:
            standardized_Vocscore = 12
        elif 42 <= Vocscore <= 43:
            standardized_Vocscore = 13
        elif Vocscore == 44:
            standardized_Vocscore = 14
        elif 45 <= Vocscore <= 46:
            standardized_Vocscore = 15
        elif 47 <= Vocscore <= 49:
            standardized_Vocscore = 16
        elif 50 <= Vocscore <= 51:
            standardized_Vocscore = 17
        elif 52 <= Vocscore <= 53:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 15.5:
        if 0 <= Vocscore <= 14:
            standardized_Vocscore = 1
        elif 15 <= Vocscore <= 16:
            standardized_Vocscore = 2
        elif 17 <= Vocscore <= 18:
            standardized_Vocscore = 3
        elif 19 <= Vocscore <= 21:
            standardized_Vocscore = 4
        elif 22 <= Vocscore <= 24:
            standardized_Vocscore = 5
        elif 25 <= Vocscore <= 27:
            standardized_Vocscore = 6
        elif 28 <= Vocscore <= 30:
            standardized_Vocscore = 7
        elif 31 <= Vocscore <= 33:
            standardized_Vocscore = 8
        elif 34 <= Vocscore <= 35:
            standardized_Vocscore = 9
        elif 36 <= Vocscore <= 38:
            standardized_Vocscore = 10
        elif 39 <= Vocscore <= 40:
            standardized_Vocscore = 11
        elif 41 <= Vocscore <= 43:
            standardized_Vocscore = 12
        elif 44 <= Vocscore <= 45:
            standardized_Vocscore = 13
        elif 46 <= Vocscore <= 47:
            standardized_Vocscore = 14
        elif 48 <= Vocscore <= 49:
            standardized_Vocscore = 15
        elif 50 <= Vocscore <= 51:
            standardized_Vocscore = 16
        elif 52 <= Vocscore <= 53:
            standardized_Vocscore = 17
        elif Vocscore == 54:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 16:
        if 0 <= Vocscore <= 16:
            standardized_Vocscore = 1
        elif 17 <= Vocscore <= 19:
            standardized_Vocscore = 2
        elif 20 <= Vocscore <= 23:
            standardized_Vocscore = 3
        elif 24 <= Vocscore <= 26:
            standardized_Vocscore = 4
        elif 27 <= Vocscore <= 28:
            standardized_Vocscore = 5
        elif 29 <= Vocscore <= 30:
            standardized_Vocscore = 6
        elif 31 <= Vocscore <= 32:
            standardized_Vocscore = 7
        elif 33 <= Vocscore <= 34:
            standardized_Vocscore = 8
        elif 35 <= Vocscore <= 37:
            standardized_Vocscore = 9
        elif 38 <= Vocscore <= 40:
            standardized_Vocscore = 10
        elif 41 <= Vocscore <= 42:
            standardized_Vocscore = 11
        elif 43 <= Vocscore <= 44:
            standardized_Vocscore = 12
        elif 45 <= Vocscore <= 46:
            standardized_Vocscore = 13
        elif 47 <= Vocscore <= 48:
            standardized_Vocscore = 14
        elif 49 <= Vocscore <= 51:
            standardized_Vocscore = 15
        elif 52 <= Vocscore <= 53:
            standardized_Vocscore = 16
        elif Vocscore == 54:
            standardized_Vocscore = 17
        elif 55 <= Vocscore <= 56:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    if chrono_age == 16.5:
        if 0 <= Vocscore <= 18:
            standardized_Vocscore = 1
        elif 19 <= Vocscore <= 21:
            standardized_Vocscore = 2
        elif 22 <= Vocscore <= 24:
            standardized_Vocscore = 3
        elif 25 <= Vocscore <= 26:
            standardized_Vocscore = 4
        elif 27 <= Vocscore <= 29:
            standardized_Vocscore = 5
        elif 30 <= Vocscore <= 31:
            standardized_Vocscore = 6
        elif Vocscore == 32:
            standardized_Vocscore = 7
        elif 33 <= Vocscore <= 34:
            standardized_Vocscore = 8
        elif 35 <= Vocscore <= 37:
            standardized_Vocscore = 9
        elif 38 <= Vocscore <= 40:
            standardized_Vocscore = 10
        elif 41 <= Vocscore <= 42:
            standardized_Vocscore = 11
        elif 43 <= Vocscore <= 44:
            standardized_Vocscore = 12
        elif 45 <= Vocscore <= 46:
            standardized_Vocscore = 13
        elif 47 <= Vocscore <= 48:
            standardized_Vocscore = 14
        elif 49 <= Vocscore <= 51:
            standardized_Vocscore = 15
        elif 52 <= Vocscore <= 53:
            standardized_Vocscore = 16
        elif 54 <= Vocscore <= 55:
            standardized_Vocscore = 17
        elif 56 <= Vocscore <= 57:
            standardized_Vocscore = 18
        else:
            standardized_Vocscore = 19

    standardized_scores.append(standardized_Vocscore)
    QIverbal.append(standardized_Vocscore)
    QIcv.append(standardized_Vocscore)


def find_standardized_Compscore():
    if chrono_age == 6:
        if 0 <= Compscore <= 1:
            standardized_Compscore = Compscore + 4
        elif 2 <= Compscore <= 5:
            standardized_Compscore = Compscore + 5
        elif Compscore == 6:
            standardized_Compscore = Compscore + 6
        elif Compscore == 7:
            standardized_Compscore = Compscore + 7
        elif 8 <= Compscore <= 10:
            standardized_Compscore = Compscore + 8
        else:
            standardized_Compscore = 19

    if chrono_age == 6.5:
        if Compscore == 0:
            standardized_Compscore = Compscore + 3
        elif 1 <= Compscore <= 2:
            standardized_Compscore = Compscore + 4
        elif 3 <= Compscore <= 7:
            standardized_Compscore = Compscore + 5
        elif 8 <= Compscore <= 12:
            standardized_Compscore = Compscore + 6
        else:
            standardized_Compscore = 19

    if chrono_age == 7:
        if 0 <= Compscore <= 6:
            standardized_Compscore = Compscore + 3
        elif 7 <= Compscore <= 11:
            standardized_Compscore = Compscore + 4
        elif 12 <= Compscore <= 13:
            standardized_Compscore = Compscore + 5
        else:
            standardized_Compscore = 19

    if chrono_age == 7.5:
        if 0 <= Compscore <= 1:
            standardized_Compscore = Compscore + 2
        elif 2 <= Compscore <= 8:
            standardized_Compscore = Compscore + 3
        elif 9 <= Compscore <= 10:
            standardized_Compscore = 12
        elif 11 <= Compscore <= 14:
            standardized_Compscore = Compscore + 2
        elif Compscore == 15:
            standardized_Compscore = Compscore + 3
        else:
            standardized_Compscore = 19

    if chrono_age == 8:
        if 0 <= Compscore <= 5:
            standardized_Compscore = Compscore + 2
        elif 6 <= Compscore <= 7:
            standardized_Compscore = 8
        elif 8 <= Compscore <= 14:
            standardized_Compscore = Compscore + 1
        elif 15 <= Compscore <= 16:
            standardized_Compscore = Compscore + 2
        else:
            standardized_Compscore = 19

    if chrono_age == 8.5:
        if 0 <= Compscore <= 7:
            standardized_Compscore = Compscore + 1
        elif 8 <= Compscore <= 9:
            standardized_Compscore = 9
        elif 10 <= Compscore <= 15:
            standardized_Compscore = Compscore
        elif 16 <= Compscore <= 17:
            standardized_Compscore = Compscore + 1
        else:
            standardized_Compscore = 19

    if chrono_age == 9:
        if 0 <= Compscore <= 1:
            standardized_Compscore = 1
        elif 2 <= Compscore <= 6:
            standardized_Compscore = Compscore
        elif 7 <= Compscore <= 8:
            standardized_Compscore = 8
        elif 9 <= Compscore <= 13:
            standardized_Compscore = Compscore - 1
        elif 14 <= Compscore <= 18:
            standardized_Compscore = Compscore
        else:
            standardized_Compscore = 19

    if chrono_age == 9.5:
        if 0 <= Compscore <= 1:
            standardized_Compscore = 1
        elif 2 <= Compscore <= 4:
            standardized_Compscore = Compscore
        elif 5 <= Compscore <= 6:
            standardized_Compscore = 5
        elif 7 <= Compscore <= 13:
            standardized_Compscore = Compscore - 1
        elif 14 <= Compscore <= 15:
            standardized_Compscore = 13
        elif 16 <= Compscore <= 17:
            standardized_Compscore = Compscore - 2
        elif 18 <= Compscore <= 19:
            standardized_Compscore = 16
        elif 20 <= Compscore <= 21:
            standardized_Compscore = Compscore - 3
        else:
            standardized_Compscore = 19

    if chrono_age == 10:
        if 0 <= Compscore <= 1:
            standardized_Compscore = 1
        elif 2 <= Compscore <= 4:
            standardized_Compscore = Compscore
        elif 5 <= Compscore <= 6:
            standardized_Compscore = 5
        elif 7 <= Compscore <= 8:
            standardized_Compscore = 6
        elif 9 <= Compscore <= 10:
            standardized_Compscore = Compscore - 2
        elif 11 <= Compscore <= 12:
            standardized_Compscore = 9
        elif 13 <= Compscore <= 16:
            standardized_Compscore = Compscore - 3
        elif 17 <= Compscore <= 18:
            standardized_Compscore = 14
        elif 19 <= Compscore <= 22:
            standardized_Compscore = Compscore - 4
        else:
            standardized_Compscore = 19

    if chrono_age == 10.5:
        if 0 <= Compscore <= 2:
            standardized_Compscore = 1
        elif 3 <= Compscore <= 5:
            standardized_Compscore = Compscore - 1
        elif 6 <= Compscore <= 8:
            standardized_Compscore = 5
        elif 9 <= Compscore <= 14:
            standardized_Compscore = Compscore - 3
        elif 15 <= Compscore <= 16:
            standardized_Compscore = 12
        elif Compscore == 17:
            standardized_Compscore = 13
        elif 18 <= Compscore <= 19:
            standardized_Compscore = 14
        elif 20 <= Compscore <= 21:
            standardized_Compscore = 15
        elif 22 <= Compscore <= 24:
            standardized_Compscore = Compscore - 6
        else:
            standardized_Compscore = 19

    if chrono_age == 11:
        if 0 <= Compscore <= 2:
            standardized_Compscore = 1
        elif 3 <= Compscore <= 4:
            standardized_Compscore = 2
        elif Compscore == 5:
            standardized_Compscore = 3
        elif 6 <= Compscore <= 7:
            standardized_Compscore = 4
        elif 8 <= Compscore <= 9:
            standardized_Compscore = 5
        elif 10 <= Compscore <= 12:
            standardized_Compscore = Compscore - 4
        elif 13 <= Compscore <= 14:
            standardized_Compscore = 9
        elif 15 <= Compscore <= 18:
            standardized_Compscore = Compscore - 5
        elif 19 <= Compscore <= 21:
            standardized_Compscore = 14
        elif 22 <= Compscore <= 25:
            standardized_Compscore = Compscore - 7
        else:
            standardized_Compscore = 19

    if chrono_age == 11.5:
        if 0 <= Compscore <= 4:
            standardized_Compscore = 1
        elif 5 <= Compscore <= 6:
            standardized_Compscore = Compscore - 3
        elif 7 <= Compscore <= 8:
            standardized_Compscore = 4
        elif 9 <= Compscore <= 12:
            standardized_Compscore = Compscore - 4
        elif 15 <= Compscore <= 16:
            standardized_Compscore = Compscore - 5
        elif 17 <= Compscore <= 18:
            standardized_Compscore = 12
        elif Compscore == 19:
            standardized_Compscore = 13
        elif 20 <= Compscore <= 21:
            standardized_Compscore = 14
        elif 22 <= Compscore <= 23:
            standardized_Compscore = 15
        elif 24 <= Compscore <= 26:
            standardized_Compscore = Compscore - 8
        else:
            standardized_Compscore = 19

    if chrono_age == 12:
        if 0 <= Compscore <= 4:
            standardized_Compscore = 1
        elif 5 <= Compscore <= 6:
            standardized_Compscore = 2
        elif 7 <= Compscore <= 11:
            standardized_Compscore = Compscore - 4
        elif 12 <= Compscore <= 13:
            standardized_Compscore = 8
        elif 14 <= Compscore <= 15:
            standardized_Compscore = 9
        elif 16 <= Compscore <= 19:
            standardized_Compscore = Compscore - 6
        elif 20 <= Compscore <= 21:
            standardized_Compscore = 14
        elif 22 <= Compscore <= 23:
            standardized_Compscore = 15
        elif Compscore == 24:
            standardized_Compscore = 16
        elif 25 <= Compscore <= 26:
            standardized_Compscore = 17
        elif Compscore == 27:
            standardized_Compscore = 18
        else:
            standardized_Compscore = 19

    if chrono_age == 12.5:
        if 0 <= Compscore <= 5:
            standardized_Compscore = 1
        elif 6 <= Compscore <= 7:
            standardized_Compscore = 2
        elif 8 <= Compscore <= 12:
            standardized_Compscore = Compscore - 5
        elif 13 <= Compscore <= 14:
            standardized_Compscore = 8
        elif 15 <= Compscore <= 16:
            standardized_Compscore = 9
        elif 17 <= Compscore <= 19:
            standardized_Compscore = Compscore - 7
        elif 20 <= Compscore <= 21:
            standardized_Compscore = 13
        elif Compscore == 22:
            standardized_Compscore = 14
        elif 23 <= Compscore <= 24:
            standardized_Compscore = 15
        elif 25 <= Compscore <= 26:
            standardized_Compscore = 16
        elif 27 <= Compscore <= 28:
            standardized_Compscore = Compscore - 10
        else:
            standardized_Compscore = 19

    if chrono_age == 13:
        if 0 <= Compscore <= 6:
            standardized_Compscore = 1
        elif 7 <= Compscore <= 8:
            standardized_Compscore = 2
        elif 9 <= Compscore <= 10:
            standardized_Compscore = 3
        elif 11 <= Compscore <= 14:
            standardized_Compscore = Compscore - 7
        elif 15 <= Compscore <= 16:
            standardized_Compscore = 8
        elif 17 <= Compscore <= 18:
            standardized_Compscore = 9
        elif 19 <= Compscore <= 22:
            standardized_Compscore = Compscore - 9
        elif 23 <= Compscore <= 24:
            standardized_Compscore = 14
        elif Compscore == 25:
            standardized_Compscore = 15
        elif 26 <= Compscore <= 27:
            standardized_Compscore = 16
        elif 28 <= Compscore <= 29:
            standardized_Compscore = Compscore - 11
        else:
            standardized_Compscore = 19

    if chrono_age == 13.5:
        if 0 <= Compscore <= 7:
            standardized_Compscore = 1
        elif 8 <= Compscore <= 10:
            standardized_Compscore = 2
        elif Compscore == 11:
            standardized_Compscore = 3
        elif 12 <= Compscore <= 13:
            standardized_Compscore = Compscore - 7
        elif 14 <= Compscore <= 15:
            standardized_Compscore = 7
        elif 16 <= Compscore <= 17:
            standardized_Compscore = 8
        elif 18 <= Compscore <= 19:
            standardized_Compscore = Compscore - 9
        elif 20 <= Compscore <= 21:
            standardized_Compscore = 11
        elif Compscore == 22:
            standardized_Compscore = 12
        elif 23 <= Compscore <= 24:
            standardized_Compscore = 13
        elif 25 <= Compscore <= 29:
            standardized_Compscore = Compscore - 11
        else:
            standardized_Compscore = 19

    if chrono_age == 14:
        if 0 <= Compscore <= 8:
            standardized_Compscore = 1
        elif 9 <= Compscore <= 10:
            standardized_Compscore = 2
        elif 11 <= Compscore <= 14:
            standardized_Compscore = Compscore - 8
        elif 15 <= Compscore <= 16:
            standardized_Compscore = 7
        elif 17 <= Compscore <= 18:
            standardized_Compscore = 8
        elif 19 <= Compscore <= 20:
            standardized_Compscore = 9
        elif 21 <= Compscore <= 29:
            standardized_Compscore = Compscore - 11
        else:
            standardized_Compscore = 19

    if chrono_age == 14.5:
        if 0 <= Compscore <= 9:
            standardized_Compscore = 1
        elif 10 <= Compscore <= 13:
            standardized_Compscore = Compscore - 8
        elif 14 <= Compscore <= 15:
            standardized_Compscore = 6
        elif 16 <= Compscore <= 17:
            standardized_Compscore = 7
        elif Compscore == 18:
            standardized_Compscore = 8
        elif 19 <= Compscore <= 20:
            standardized_Compscore = 9
        elif 21 <= Compscore <= 22:
            standardized_Compscore = Compscore - 11
        elif 23 <= Compscore <= 24:
            standardized_Compscore = 12
        elif 25 <= Compscore <= 28:
            standardized_Compscore = Compscore - 12
        elif 29 <= Compscore <= 30:
            standardized_Compscore = 17
        elif Compscore == 31:
            standardized_Compscore = 18
        else:
            standardized_Compscore = 19

    if chrono_age == 15:
        if 0 <= Compscore <= 9:
            standardized_Compscore = 1
        elif 10 <= Compscore <= 11:
            standardized_Compscore = 2
        elif 12 <= Compscore <= 14:
            standardized_Compscore = Compscore - 9
        elif 15 <= Compscore <= 16:
            standardized_Compscore = 6
        elif Compscore == 17:
            standardized_Compscore = 7
        elif Compscore == 18:
            standardized_Compscore = 8
        elif 19 <= Compscore <= 20:
            standardized_Compscore = 9
        elif 21 <= Compscore <= 22:
            standardized_Compscore = Compscore - 11
        elif 23 <= Compscore <= 24:
            standardized_Compscore = Compscore - 12
        elif 25 <= Compscore <= 26:
            standardized_Compscore = 13
        elif 27 <= Compscore <= 29:
            standardized_Compscore = Compscore - 13
        elif 30 <= Compscore <= 31:
            standardized_Compscore = 17
        elif Compscore == 32:
            standardized_Compscore = 18
        else:
            standardized_Compscore = 19

    if chrono_age == 15.5:
        if 0 <= Compscore <= 10:
            standardized_Compscore = 1
        elif 13 <= Compscore <= 13:
            standardized_Compscore = Compscore - 9
        elif 14 <= Compscore <= 15:
            standardized_Compscore = 5
        elif 16 <= Compscore <= 17:
            standardized_Compscore = 6
        elif Compscore == 18:
            standardized_Compscore = 7
        elif Compscore == 19:
            standardized_Compscore = 8
        elif 20 <= Compscore <= 21:
            standardized_Compscore = 9
        elif 22 <= Compscore <= 23:
            standardized_Compscore = 10
        elif 24 <= Compscore <= 25:
            standardized_Compscore = Compscore - 13
        elif 28 <= Compscore <= 29:
            standardized_Compscore = Compscore - 14
        elif 30 <= Compscore <= 31:
            standardized_Compscore = 16
        elif Compscore == 32:
            standardized_Compscore = 17
        elif Compscore == 33:
            standardized_Compscore = 18
        else:
            standardized_Compscore = 19

    if chrono_age == 16:
        if 0 <= Compscore <= 10:
            standardized_Compscore = 1
        elif 11 <= Compscore <= 12:
            standardized_Compscore = 2
        elif 13 <= Compscore <= 14:
            standardized_Compscore = Compscore - 10
        elif 15 <= Compscore <= 17:
            standardized_Compscore = 5
        elif Compscore == 18:
            standardized_Compscore = 6
        elif 19 <= Compscore <= 20:
            standardized_Compscore = 7
        elif Compscore == 21:
            standardized_Compscore = 8
        elif 22 <= Compscore <= 23:
            standardized_Compscore = 9
        elif 24 <= Compscore <= 26:
            standardized_Compscore = Compscore - 14
        elif 27 <= Compscore <= 28:
            standardized_Compscore = 13
        elif 29 <= Compscore <= 33:
            standardized_Compscore = Compscore - 15
        else:
            standardized_Compscore = 19

    if chrono_age == 16.5:
        if 0 <= Compscore <= 11:
            standardized_Compscore = 1
        elif 12 <= Compscore <= 14:
            standardized_Compscore = Compscore - 10
        elif 15 <= Compscore <= 17:
            standardized_Compscore = 5
        elif Compscore == 18:
            standardized_Compscore = 6
        elif 19 <= Compscore <= 20:
            standardized_Compscore = 7
        elif Compscore == 21:
            standardized_Compscore = 8
        elif 22 <= Compscore <= 23:
            standardized_Compscore = 9
        elif 24 <= Compscore <= 26:
            standardized_Compscore = Compscore - 14
        elif 27 <= Compscore <= 28:
            standardized_Compscore = 13
        elif 29 <= Compscore <= 31:
            standardized_Compscore = Compscore - 15
        elif 32 <= Compscore <= 33:
            standardized_Compscore = 17
        elif Compscore == 34:
            standardized_Compscore = 18
        else:
            standardized_Compscore = 19

    standardized_scores.append(standardized_Compscore)
    QIverbal.append(standardized_Compscore)
    QIcv.append(standardized_Compscore)


def find_standardized_MDscore():
    if chrono_age == 6:
        if 0 <= MDscore <= 10:
            standardized_MDscore = MDscore + 1
        elif MDscore == 11:
            standardized_MDscore = MDscore + 2
        elif 12 <= MDscore <= 15:
            standardized_MDscore = MDscore + 3
        else:
            standardized_MDscore = 19

    if chrono_age == 6.5:
        if 0 <= MDscore <= 1:
            standardized_MDscore = 1
        elif 2 <= MDscore <= 7:
            standardized_MDscore = MDscore
        elif 8 <= MDscore <= 11:
            standardized_MDscore = MDscore + 1
        elif 12 <= MDscore <= 16:
            standardized_MDscore = MDscore + 2
        else:
            standardized_MDscore = 19

    if chrono_age == 7:
        if 0 <= MDscore <= 2:
            standardized_MDscore = 1
        elif 3 <= MDscore <= 4:
            standardized_MDscore = 2
        elif 5 <= MDscore <= 6:
            standardized_MDscore = MDscore - 2
        elif MDscore == 7:
            standardized_MDscore = MDscore - 1
        elif 8 <= MDscore <= 11:
            standardized_MDscore = MDscore
        elif 12 <= MDscore <= 15:
            standardized_MDscore = MDscore + 1
        elif MDscore == 16:
            standardized_MDscore = MDscore + 2
        else:
            standardized_MDscore = 19

    if chrono_age == 7.5:
        if 0 <= MDscore <= 3:
            standardized_MDscore = 1
        elif 4 <= MDscore <= 6:
            standardized_MDscore = MDscore - 2
        elif 7 <= MDscore <= 8:
            standardized_MDscore = MDscore - 1
        elif 9 <= MDscore <= 18:
            standardized_MDscore = MDscore
        else:
            standardized_MDscore = 19

    if chrono_age == 8:
        if 0 <= MDscore <= 3:
            standardized_MDscore = 1
        elif 4 <= MDscore <= 9:
            standardized_MDscore = MDscore - 2
        elif 10 <= MDscore <= 17:
            standardized_MDscore = MDscore - 1
        elif MDscore == 18:
            standardized_MDscore = MDscore
        else:
            standardized_MDscore = 19

    if chrono_age == 8.5:
        if 0 <= MDscore <= 4:
            standardized_MDscore = 1
        elif 5 <= MDscore <= 6:
            standardized_MDscore = MDscore - 3
        elif 7 <= MDscore <= 9:
            standardized_MDscore = MDscore - 2
        elif 10 <= MDscore <= 19:
            standardized_MDscore = MDscore - 1
        else:
            standardized_MDscore = 19

    if chrono_age == 8.5:
        if 0 <= MDscore <= 4:
            standardized_MDscore = 1
        elif 5 <= MDscore <= 6:
            standardized_MDscore = MDscore - 3
        elif 7 <= MDscore <= 9:
            standardized_MDscore = MDscore - 2
        elif 10 <= MDscore <= 19:
            standardized_MDscore = MDscore - 1
        else:
            standardized_MDscore = 19

    if chrono_age == 9:
        if 0 <= MDscore <= 4:
            standardized_MDscore = 1
        elif 5 <= MDscore <= 7:
            standardized_MDscore = MDscore - 3
        elif 8 <= MDscore <= 11:
            standardized_MDscore = MDscore - 2
        elif 12 <= MDscore <= 18:
            standardized_MDscore = MDscore - 1
        elif 19 <= MDscore <= 20:
            standardized_MDscore = 18
        else:
            standardized_MDscore = 19

    if chrono_age == 9.5:
        if 0 <= MDscore <= 4:
            standardized_MDscore = 1
        elif 5 <= MDscore <= 8:
            standardized_MDscore = MDscore - 3
        elif 9 <= MDscore <= 13:
            standardized_MDscore = MDscore - 2
        elif 14 <= MDscore <= 18:
            standardized_MDscore = MDscore - 1
        elif 19 <= MDscore <= 20:
            standardized_MDscore = 18
        else:
            standardized_MDscore = 19

    if chrono_age == 10:
        if 0 <= MDscore <= 4:
            standardized_MDscore = 1
        elif 5 <= MDscore <= 8:
            standardized_MDscore = MDscore - 3
        elif 9 <= MDscore <= 13:
            standardized_MDscore = MDscore - 2
        elif 14 <= MDscore <= 18:
            standardized_MDscore = MDscore - 1
        elif 19 <= MDscore <= 20:
            standardized_MDscore = 18
        else:
            standardized_MDscore = 19

    if chrono_age == 10.5:
        if 0 <= MDscore <= 4:
            standardized_MDscore = 1
        elif 5 <= MDscore <= 9:
            standardized_MDscore = MDscore - 3
        elif 10 <= MDscore <= 20:
            standardized_MDscore = MDscore - 2
        else:
            standardized_MDscore = 19

    if chrono_age == 11:
        if 0 <= MDscore <= 5:
            standardized_MDscore = 1
        elif 6 <= MDscore <= 7:
            standardized_MDscore = MDscore - 4
        elif 8 <= MDscore <= 21:
            standardized_MDscore = MDscore - 3
        else:
            standardized_MDscore = 19

    if chrono_age == 11.5:
        if 0 <= MDscore <= 5:
            standardized_MDscore = 1
        elif 6 <= MDscore <= 8:
            standardized_MDscore = MDscore - 4
        elif 9 <= MDscore <= 21:
            standardized_MDscore = MDscore - 3
        else:
            standardized_MDscore = 19

    if chrono_age == 12:
        if 0 <= MDscore <= 5:
            standardized_MDscore = 1
        elif 6 <= MDscore <= 8:
            standardized_MDscore = MDscore - 4
        elif 9 <= MDscore <= 12:
            standardized_MDscore = MDscore - 3
        elif 13 <= MDscore <= 14:
            standardized_MDscore = 10
        elif 15 <= MDscore <= 22:
            standardized_MDscore = MDscore - 4
        else:
            standardized_MDscore = 19

    if chrono_age == 12.5:
        if 0 <= MDscore <= 5:
            standardized_MDscore = 1
        elif 6 <= MDscore <= 9:
            standardized_MDscore = MDscore - 4
        elif 10 <= MDscore <= 12:
            standardized_MDscore = MDscore - 3
        elif 13 <= MDscore <= 14:
            standardized_MDscore = 10
        elif 15 <= MDscore <= 22:
            standardized_MDscore = MDscore - 4
        else:
            standardized_MDscore = 19

    if chrono_age == 13:
        if 0 <= MDscore <= 5:
            standardized_MDscore = 1
        elif 6 <= MDscore <= 22:
            standardized_MDscore = MDscore - 4
        else:
            standardized_MDscore = 19

    if chrono_age == 13.5:
        if 0 <= MDscore <= 6:
            standardized_MDscore = 1
        elif 7 <= MDscore <= 8:
            standardized_MDscore = MDscore - 5
        elif 9 <= MDscore <= 16:
            standardized_MDscore = MDscore - 4
        elif 17 <= MDscore <= 18:
            standardized_MDscore = 13
        elif 19 <= MDscore <= 23:
            standardized_MDscore = MDscore - 5
        else:
            standardized_MDscore = 19

    if chrono_age == 14:
        if 0 <= MDscore <= 6:
            standardized_MDscore = 1
        elif 7 <= MDscore <= 10:
            standardized_MDscore = MDscore - 5
        elif 11 <= MDscore <= 13:
            standardized_MDscore = MDscore - 4
        elif 14 <= MDscore <= 15:
            standardized_MDscore = 10
        elif 16 <= MDscore <= 23:
            standardized_MDscore = MDscore - 5
        else:
            standardized_MDscore = 19

    if chrono_age == 14.5:
        if 0 <= MDscore <= 6:
            standardized_MDscore = 1
        elif 7 <= MDscore <= 19:
            standardized_MDscore = MDscore - 5
        elif 20 <= MDscore <= 21:
            standardized_MDscore = 15
        elif 22 <= MDscore <= 24:
            standardized_MDscore = MDscore - 6
        else:
            standardized_MDscore = 19

    if chrono_age == 15:
        if 0 <= MDscore <= 6:
            standardized_MDscore = 1
        elif 7 <= MDscore <= 18:
            standardized_MDscore = MDscore - 5
        elif 19 <= MDscore <= 20:
            standardized_MDscore = 14
        elif 21 <= MDscore <= 24:
            standardized_MDscore = MDscore - 6
        else:
            standardized_MDscore = 19

    if chrono_age == 15.5:
        if 0 <= MDscore <= 6:
            standardized_MDscore = 1
        elif 7 <= MDscore <= 16:
            standardized_MDscore = MDscore - 5
        elif 17 <= MDscore <= 18:
            standardized_MDscore = 12
        elif MDscore == 19:
            standardized_MDscore = 13
        elif 20 <= MDscore <= 21:
            standardized_MDscore = 14
        elif 22 <= MDscore <= 25:
            standardized_MDscore = MDscore - 7
        else:
            standardized_MDscore = 19

    if chrono_age == 16:
        if 0 <= MDscore <= 6:
            standardized_MDscore = 1
        elif 7 <= MDscore <= 13:
            standardized_MDscore = MDscore - 5
        elif 14 <= MDscore <= 15:
            standardized_MDscore = 9
        elif 16 <= MDscore <= 18:
            standardized_MDscore = MDscore - 6
        elif 19 <= MDscore <= 20:
            standardized_MDscore = 13
        elif 21 <= MDscore <= 23:
            standardized_MDscore = MDscore - 7
        elif 24 <= MDscore <= 25:
            standardized_MDscore = 17
        elif MDscore == 26:
            standardized_MDscore = 18
        else:
            standardized_MDscore = 19

    if chrono_age == 16.5:
        if 0 <= MDscore <= 7:
            standardized_MDscore = 1
        elif 8 <= MDscore <= 18:
            standardized_MDscore = MDscore - 6
        elif 19 <= MDscore <= 20:
            standardized_MDscore = 13
        elif 21 <= MDscore <= 22:
            standardized_MDscore = MDscore - 7
        elif 23 <= MDscore <= 24:
            standardized_MDscore = 16
        elif 25 <= MDscore <= 26:
            standardized_MDscore = MDscore - 8
        else:
            standardized_MDscore = 19

    standardized_scores.append(standardized_MDscore)


def find_standardized_Codscore():
    if chrono_age == 6:
        if 0 <= Codscore <= 7:
            standardized_Codscore = 1
        elif 8 <= Codscore <= 9:
            standardized_Codscore = 2
        elif 10 <= Codscore <= 12:
            standardized_Codscore = 3
        elif 13 <= Codscore <= 17:
            standardized_Codscore = 4
        elif 18 <= Codscore <= 21:
            standardized_Codscore = 5
        elif 22 <= Codscore <= 23:
            standardized_Codscore = 6
        elif 24 <= Codscore <= 26:
            standardized_Codscore = 7
        elif 27 <= Codscore <= 28:
            standardized_Codscore = 8
        elif 29 <= Codscore <= 33:
            standardized_Codscore = 9
        elif 34 <= Codscore <= 36:
            standardized_Codscore = 10
        elif 37 <= Codscore <= 41:
            standardized_Codscore = 11
        elif 42 <= Codscore <= 46:
            standardized_Codscore = 12
        elif 47 <= Codscore <= 50:
            standardized_Codscore = 13
        elif 51 <= Codscore <= 54:
            standardized_Codscore = 14
        elif 55 <= Codscore <= 58:
            standardized_Codscore = 15
        elif 59 <= Codscore <= 60:
            standardized_Codscore = 16
        elif 61 <= Codscore <= 62:
            standardized_Codscore = 17
        elif Codscore == 63:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 6.5:
        if 0 <= Codscore <= 7:
            standardized_Codscore = 1
        elif 8 <= Codscore <= 9:
            standardized_Codscore = 2
        elif 10 <= Codscore <= 13:
            standardized_Codscore = 3
        elif 14 <= Codscore <= 18:
            standardized_Codscore = 4
        elif 19 <= Codscore <= 22:
            standardized_Codscore = 5
        elif 23 <= Codscore <= 25:
            standardized_Codscore = 6
        elif 26 <= Codscore <= 28:
            standardized_Codscore = 7
        elif 29 <= Codscore <= 33:
            standardized_Codscore = 8
        elif 34 <= Codscore <= 36:
            standardized_Codscore = 9
        elif 37 <= Codscore <= 40:
            standardized_Codscore = 10
        elif 41 <= Codscore <= 45:
            standardized_Codscore = 11
        elif 46 <= Codscore <= 50:
            standardized_Codscore = 12
        elif 51 <= Codscore <= 54:
            standardized_Codscore = 13
        elif 55 <= Codscore <= 58:
            standardized_Codscore = 14
        elif 59 <= Codscore <= 60:
            standardized_Codscore = 15
        elif 61 <= Codscore <= 62:
            standardized_Codscore = 16
        elif Codscore == 63:
            standardized_Codscore = 17
        elif Codscore == 64:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 7:
        if 0 <= Codscore <= 12:
            standardized_Codscore = 1
        elif 13 <= Codscore <= 17:
            standardized_Codscore = 2
        elif 18 <= Codscore <= 22:
            standardized_Codscore = 3
        elif 23 <= Codscore <= 24:
            standardized_Codscore = 4
        elif 25 <= Codscore <= 26:
            standardized_Codscore = 5
        elif 27 <= Codscore <= 31:
            standardized_Codscore = 6
        elif 32 <= Codscore <= 33:
            standardized_Codscore = 7
        elif 34 <= Codscore <= 36:
            standardized_Codscore = 8
        elif 37 <= Codscore <= 40:
            standardized_Codscore = 9
        elif 41 <= Codscore <= 44:
            standardized_Codscore = 10
        elif 45 <= Codscore <= 50:
            standardized_Codscore = 11
        elif 51 <= Codscore <= 55:
            standardized_Codscore = 12
        elif 56 <= Codscore <= 58:
            standardized_Codscore = 13
        elif 59 <= Codscore <= 60:
            standardized_Codscore = 14
        elif 61 <= Codscore <= 62:
            standardized_Codscore = 15
        elif Codscore == 63:
            standardized_Codscore = 16
        elif Codscore == 64:
            standardized_Codscore = 17
        else:
            standardized_Codscore = 18

    if chrono_age == 7.5:
        if 0 <= Codscore <= 16:
            standardized_Codscore = 1
        elif 17 <= Codscore <= 19:
            standardized_Codscore = 2
        elif 20 <= Codscore <= 22:
            standardized_Codscore = 3
        elif 23 <= Codscore <= 24:
            standardized_Codscore = 4
        elif 25 <= Codscore <= 26:
            standardized_Codscore = 5
        elif 27 <= Codscore <= 31:
            standardized_Codscore = 6
        elif 32 <= Codscore <= 33:
            standardized_Codscore = 7
        elif 34 <= Codscore <= 36:
            standardized_Codscore = 8
        elif 37 <= Codscore <= 41:
            standardized_Codscore = 9
        elif 42 <= Codscore <= 45:
            standardized_Codscore = 10
        elif 46 <= Codscore <= 51:
            standardized_Codscore = 11
        elif 52 <= Codscore <= 55:
            standardized_Codscore = 12
        elif 56 <= Codscore <= 59:
            standardized_Codscore = 13
        elif Codscore == 60:
            standardized_Codscore = 14
        elif 61 <= Codscore <= 62:
            standardized_Codscore = 15
        elif Codscore == 63:
            standardized_Codscore = 16
        elif Codscore == 64:
            standardized_Codscore = 17
        else:
            standardized_Codscore = 18

    if chrono_age == 8:
        if 0 <= Codscore <= 10:
            standardized_Codscore = 1
        elif 11 <= Codscore <= 14:
            standardized_Codscore = 2
        elif 15 <= Codscore <= 18:
            standardized_Codscore = 3
        elif 19 <= Codscore <= 22:
            standardized_Codscore = 4
        elif 23 <= Codscore <= 24:
            standardized_Codscore = 5
        elif 25 <= Codscore <= 27:
            standardized_Codscore = 6
        elif 28 <= Codscore <= 29:
            standardized_Codscore = 7
        elif Codscore == 30:
            standardized_Codscore = 8
        elif 31 <= Codscore <= 33:
            standardized_Codscore = 9
        elif 34 <= Codscore <= 35:
            standardized_Codscore = 10
        elif 36 <= Codscore <= 37:
            standardized_Codscore = 11
        elif 38 <= Codscore <= 40:
            standardized_Codscore = 12
        elif 41 <= Codscore <= 43:
            standardized_Codscore = 13
        elif 44 <= Codscore <= 45:
            standardized_Codscore = 14
        elif 46 <= Codscore <= 48:
            standardized_Codscore = 15
        elif Codscore == 49:
            standardized_Codscore = 16
        elif 50 <= Codscore <= 51:
            standardized_Codscore = 17
        elif 52 <= Codscore <= 53:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 8.5:
        if 0 <= Codscore <= 11:
            standardized_Codscore = 1
        elif 12 <= Codscore <= 16:
            standardized_Codscore = 2
        elif 17 <= Codscore <= 21:
            standardized_Codscore = 3
        elif 22 <= Codscore <= 23:
            standardized_Codscore = 4
        elif 24 <= Codscore <= 26:
            standardized_Codscore = 5
        elif 27 <= Codscore <= 28:
            standardized_Codscore = 6
        elif 29 <= Codscore <= 30:
            standardized_Codscore = 7
        elif 31 <= Codscore <= 32:
            standardized_Codscore = 8
        elif 33 <= Codscore <= 35:
            standardized_Codscore = 9
        elif 36 <= Codscore <= 37:
            standardized_Codscore = 10
        elif 38 <= Codscore <= 40:
            standardized_Codscore = 11
        elif 41 <= Codscore <= 44:
            standardized_Codscore = 12
        elif 45 <= Codscore <= 46:
            standardized_Codscore = 13
        elif 47 <= Codscore <= 49:
            standardized_Codscore = 14
        elif 50 <= Codscore <= 51:
            standardized_Codscore = 15
        elif 52 <= Codscore <= 55:
            standardized_Codscore = 16
        elif 56 <= Codscore <= 57:
            standardized_Codscore = 17
        elif 58 <= Codscore <= 59:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 9:
        if 0 <= Codscore <= 12:
            standardized_Codscore = 1
        elif 13 <= Codscore <= 16:
            standardized_Codscore = 2
        elif 17 <= Codscore <= 21:
            standardized_Codscore = 3
        elif 22 <= Codscore <= 25:
            standardized_Codscore = 4
        elif 26 <= Codscore <= 28:
            standardized_Codscore = 5
        elif 29 <= Codscore <= 30:
            standardized_Codscore = 6
        elif 31 <= Codscore <= 32:
            standardized_Codscore = 7
        elif 33 <= Codscore <= 35:
            standardized_Codscore = 8
        elif 36 <= Codscore <= 37:
            standardized_Codscore = 9
        elif 38 <= Codscore <= 40:
            standardized_Codscore = 10
        elif 41 <= Codscore <= 44:
            standardized_Codscore = 11
        elif 45 <= Codscore <= 46:
            standardized_Codscore = 12
        elif 47 <= Codscore <= 48:
            standardized_Codscore = 13
        elif 49 <= Codscore <= 51:
            standardized_Codscore = 14
        elif 52 <= Codscore <= 53:
            standardized_Codscore = 15
        elif 54 <= Codscore <= 56:
            standardized_Codscore = 16
        elif 57 <= Codscore <= 58:
            standardized_Codscore = 17
        elif 59 <= Codscore <= 60:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 9.5:
        if 0 <= Codscore <= 14:
            standardized_Codscore = 1
        elif 15 <= Codscore <= 18:
            standardized_Codscore = 2
        elif 19 <= Codscore <= 22:
            standardized_Codscore = 3
        elif 23 <= Codscore <= 26:
            standardized_Codscore = 4
        elif 27 <= Codscore <= 28:
            standardized_Codscore = 5
        elif 29 <= Codscore <= 30:
            standardized_Codscore = 6
        elif 31 <= Codscore <= 33:
            standardized_Codscore = 7
        elif 34 <= Codscore <= 37:
            standardized_Codscore = 8
        elif 38 <= Codscore <= 39:
            standardized_Codscore = 9
        elif 40 <= Codscore <= 43:
            standardized_Codscore = 10
        elif 44 <= Codscore <= 46:
            standardized_Codscore = 11
        elif 47 <= Codscore <= 49:
            standardized_Codscore = 12
        elif 50 <= Codscore <= 52:
            standardized_Codscore = 13
        elif 53 <= Codscore <= 55:
            standardized_Codscore = 14
        elif 56 <= Codscore <= 57:
            standardized_Codscore = 15
        elif Codscore == 58:
            standardized_Codscore = 16
        elif Codscore <= 59:
            standardized_Codscore = 17
        elif Codscore <= 60:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 10:
        if 0 <= Codscore <= 14:
            standardized_Codscore = 1
        elif 15 <= Codscore <= 18:
            standardized_Codscore = 2
        elif 19 <= Codscore <= 22:
            standardized_Codscore = 3
        elif 23 <= Codscore <= 26:
            standardized_Codscore = 4
        elif 27 <= Codscore <= 29:
            standardized_Codscore = 5
        elif 30 <= Codscore <= 31:
            standardized_Codscore = 6
        elif 32 <= Codscore <= 35:
            standardized_Codscore = 7
        elif 36 <= Codscore <= 38:
            standardized_Codscore = 8
        elif 39 <= Codscore <= 42:
            standardized_Codscore = 9
        elif 43 <= Codscore <= 45:
            standardized_Codscore = 10
        elif 46 <= Codscore <= 48:
            standardized_Codscore = 11
        elif 49 <= Codscore <= 51:
            standardized_Codscore = 12
        elif 52 <= Codscore <= 54:
            standardized_Codscore = 13
        elif 55 <= Codscore <= 56:
            standardized_Codscore = 14
        elif 57 <= Codscore <= 58:
            standardized_Codscore = 15
        elif Codscore == 59:
            standardized_Codscore = 16
        elif Codscore <= 60:
            standardized_Codscore = 17
        elif 61 <= Codscore <= 62:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 10.5:
        if 0 <= Codscore <= 17:
            standardized_Codscore = 1
        elif 18 <= Codscore <= 22:
            standardized_Codscore = 2
        elif 23 <= Codscore <= 25:
            standardized_Codscore = 3
        elif 26 <= Codscore <= 28:
            standardized_Codscore = 4
        elif 29 <= Codscore <= 31:
            standardized_Codscore = 5
        elif 32 <= Codscore <= 34:
            standardized_Codscore = 6
        elif 33 <= Codscore <= 37:
            standardized_Codscore = 7
        elif 38 <= Codscore <= 41:
            standardized_Codscore = 8
        elif 42 <= Codscore <= 44:
            standardized_Codscore = 9
        elif 45 <= Codscore <= 47:
            standardized_Codscore = 10
        elif 48 <= Codscore <= 50:
            standardized_Codscore = 11
        elif 51 <= Codscore <= 53:
            standardized_Codscore = 12
        elif 54 <= Codscore <= 56:
            standardized_Codscore = 13
        elif 57 <= Codscore <= 58:
            standardized_Codscore = 14
        elif 59 <= Codscore <= 60:
            standardized_Codscore = 15
        elif 61 <= Codscore <= 62:
            standardized_Codscore = 16
        elif 63 <= Codscore <= 64:
            standardized_Codscore = 17
        elif 65 <= Codscore <= 66:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 11:
        if 0 <= Codscore <= 17:
            standardized_Codscore = 1
        elif 18 <= Codscore <= 22:
            standardized_Codscore = 2
        elif 23 <= Codscore <= 27:
            standardized_Codscore = 3
        elif 28 <= Codscore <= 31:
            standardized_Codscore = 4
        elif 32 <= Codscore <= 33:
            standardized_Codscore = 5
        elif 34 <= Codscore <= 36:
            standardized_Codscore = 6
        elif 37 <= Codscore <= 39:
            standardized_Codscore = 7
        elif 40 <= Codscore <= 44:
            standardized_Codscore = 8
        elif 45 <= Codscore <= 46:
            standardized_Codscore = 9
        elif 47 <= Codscore <= 48:
            standardized_Codscore = 10
        elif 49 <= Codscore <= 50:
            standardized_Codscore = 11
        elif 51 <= Codscore <= 55:
            standardized_Codscore = 12
        elif 56 <= Codscore <= 57:
            standardized_Codscore = 13
        elif 58 <= Codscore <= 60:
            standardized_Codscore = 14
        elif 61 <= Codscore <= 62:
            standardized_Codscore = 15
        elif 63 <= Codscore <= 64:
            standardized_Codscore = 16
        elif Codscore == 65:
            standardized_Codscore = 17
        elif 66 <= Codscore <= 67:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 11.5:
        if 0 <= Codscore <= 20:
            standardized_Codscore = 1
        elif 21 <= Codscore <= 25:
            standardized_Codscore = 2
        elif 26 <= Codscore <= 28:
            standardized_Codscore = 3
        elif 29 <= Codscore <= 32:
            standardized_Codscore = 4
        elif 33 <= Codscore <= 35:
            standardized_Codscore = 5
        elif 36 <= Codscore <= 38:
            standardized_Codscore = 6
        elif 39 <= Codscore <= 42:
            standardized_Codscore = 7
        elif 43 <= Codscore <= 45:
            standardized_Codscore = 8
        elif 46 <= Codscore <= 48:
            standardized_Codscore = 9
        elif 49 <= Codscore <= 50:
            standardized_Codscore = 10
        elif 51 <= Codscore <= 55:
            standardized_Codscore = 11
        elif 56 <= Codscore <= 57:
            standardized_Codscore = 12
        elif 58 <= Codscore <= 59:
            standardized_Codscore = 13
        elif 60 <= Codscore <= 62:
            standardized_Codscore = 14
        elif 63 <= Codscore <= 64:
            standardized_Codscore = 15
        elif 65 <= Codscore <= 66:
            standardized_Codscore = 16
        elif Codscore == 67:
            standardized_Codscore = 17
        elif 68 <= Codscore <= 69:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 12:
        if 0 <= Codscore <= 21:
            standardized_Codscore = 1
        elif 22 <= Codscore <= 25:
            standardized_Codscore = 2
        elif 26 <= Codscore <= 29:
            standardized_Codscore = 3
        elif 30 <= Codscore <= 33:
            standardized_Codscore = 4
        elif 34 <= Codscore <= 36:
            standardized_Codscore = 5
        elif 37 <= Codscore <= 39:
            standardized_Codscore = 6
        elif 40 <= Codscore <= 44:
            standardized_Codscore = 7
        elif 45 <= Codscore <= 47:
            standardized_Codscore = 8
        elif 48 <= Codscore <= 50:
            standardized_Codscore = 9
        elif 51 <= Codscore <= 54:
            standardized_Codscore = 10
        elif 55 <= Codscore <= 56:
            standardized_Codscore = 11
        elif 57 <= Codscore <= 58:
            standardized_Codscore = 12
        elif 59 <= Codscore <= 61:
            standardized_Codscore = 13
        elif 62 <= Codscore <= 63:
            standardized_Codscore = 14
        elif 64 <= Codscore <= 66:
            standardized_Codscore = 15
        elif Codscore == 67:
            standardized_Codscore = 16
        elif 68 <= Codscore <= 69:
            standardized_Codscore = 17
        elif 70 <= Codscore <= 71:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 12.5:
        if 0 <= Codscore <= 24:
            standardized_Codscore = 1
        elif 25 <= Codscore <= 28:
            standardized_Codscore = 2
        elif 29 <= Codscore <= 31:
            standardized_Codscore = 3
        elif 32 <= Codscore <= 35:
            standardized_Codscore = 4
        elif 36 <= Codscore <= 38:
            standardized_Codscore = 5
        elif 39 <= Codscore <= 41:
            standardized_Codscore = 6
        elif 42 <= Codscore <= 45:
            standardized_Codscore = 7
        elif 46 <= Codscore <= 49:
            standardized_Codscore = 8
        elif 50 <= Codscore <= 53:
            standardized_Codscore = 9
        elif 54 <= Codscore <= 56:
            standardized_Codscore = 10
        elif 57 <= Codscore <= 59:
            standardized_Codscore = 11
        elif 60 <= Codscore <= 63:
            standardized_Codscore = 12
        elif 64 <= Codscore <= 66:
            standardized_Codscore = 13
        elif 67 <= Codscore <= 70:
            standardized_Codscore = 14
        elif 71 <= Codscore <= 74:
            standardized_Codscore = 15
        elif 75 <= Codscore <= 78:
            standardized_Codscore = 16
        elif 79 <= Codscore <= 80:
            standardized_Codscore = 17
        elif 81 <= Codscore <= 82:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 13:
        if 0 <= Codscore <= 25:
            standardized_Codscore = 1
        elif 26 <= Codscore <= 29:
            standardized_Codscore = 2
        elif 30 <= Codscore <= 33:
            standardized_Codscore = 3
        elif 34 <= Codscore <= 37:
            standardized_Codscore = 4
        elif 38 <= Codscore <= 39:
            standardized_Codscore = 5
        elif 40 <= Codscore <= 43:
            standardized_Codscore = 6
        elif 44 <= Codscore <= 47:
            standardized_Codscore = 7
        elif 48 <= Codscore <= 52:
            standardized_Codscore = 8
        elif 53 <= Codscore <= 56:
            standardized_Codscore = 9
        elif 57 <= Codscore <= 60:
            standardized_Codscore = 10
        elif 61 <= Codscore <= 63:
            standardized_Codscore = 11
        elif 64 <= Codscore <= 69:
            standardized_Codscore = 12
        elif 70 <= Codscore <= 74:
            standardized_Codscore = 13
        elif 75 <= Codscore <= 76:
            standardized_Codscore = 14
        elif 77 <= Codscore <= 78:
            standardized_Codscore = 15
        elif Codscore == 79:
            standardized_Codscore = 16
        elif Codscore == 80:
            standardized_Codscore = 17
        elif 81 <= Codscore <= 82:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 13.5:
        if 0 <= Codscore <= 28:
            standardized_Codscore = 1
        elif 29 <= Codscore <= 34:
            standardized_Codscore = 2
        elif 35 <= Codscore <= 37:
            standardized_Codscore = 3
        elif 38 <= Codscore <= 39:
            standardized_Codscore = 4
        elif 40 <= Codscore <= 44:
            standardized_Codscore = 5
        elif 45 <= Codscore <= 47:
            standardized_Codscore = 6
        elif 48 <= Codscore <= 52:
            standardized_Codscore = 7
        elif 53 <= Codscore <= 55:
            standardized_Codscore = 8
        elif 56 <= Codscore <= 60:
            standardized_Codscore = 9
        elif 61 <= Codscore <= 63:
            standardized_Codscore = 10
        elif 64 <= Codscore <= 67:
            standardized_Codscore = 11
        elif 68 <= Codscore <= 72:
            standardized_Codscore = 12
        elif 73 <= Codscore <= 75:
            standardized_Codscore = 13
        elif 76 <= Codscore <= 77:
            standardized_Codscore = 14
        elif 78 <= Codscore <= 80:
            standardized_Codscore = 15
        elif 81 <= Codscore <= 83:
            standardized_Codscore = 16
        elif 84 <= Codscore <= 86:
            standardized_Codscore = 17
        elif 87 <= Codscore <= 90:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 14:
        if 0 <= Codscore <= 29:
            standardized_Codscore = 1
        elif 30 <= Codscore <= 35:
            standardized_Codscore = 2
        elif 36 <= Codscore <= 40:
            standardized_Codscore = 3
        elif 41 <= Codscore <= 47:
            standardized_Codscore = 4
        elif 48 <= Codscore <= 51:
            standardized_Codscore = 5
        elif 52 <= Codscore <= 53:
            standardized_Codscore = 6
        elif 54 <= Codscore <= 55:
            standardized_Codscore = 7
        elif 56 <= Codscore <= 59:
            standardized_Codscore = 8
        elif 60 <= Codscore <= 63:
            standardized_Codscore = 9
        elif 64 <= Codscore <= 66:
            standardized_Codscore = 10
        elif 67 <= Codscore <= 69:
            standardized_Codscore = 11
        elif 70 <= Codscore <= 73:
            standardized_Codscore = 12
        elif 74 <= Codscore <= 76:
            standardized_Codscore = 13
        elif Codscore == 77:
            standardized_Codscore = 14
        elif 78 <= Codscore <= 83:
            standardized_Codscore = 15
        elif 84 <= Codscore <= 87:
            standardized_Codscore = 16
        elif 88 <= Codscore <= 90:
            standardized_Codscore = 17
        elif 91 <= Codscore <= 92:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 14.5:
        if 0 <= Codscore <= 31:
            standardized_Codscore = 1
        elif 32 <= Codscore <= 37:
            standardized_Codscore = 2
        elif 38 <= Codscore <= 42:
            standardized_Codscore = 3
        elif 43 <= Codscore <= 47:
            standardized_Codscore = 4
        elif 48 <= Codscore <= 51:
            standardized_Codscore = 5
        elif 52 <= Codscore <= 54:
            standardized_Codscore = 6
        elif 55 <= Codscore <= 56:
            standardized_Codscore = 7
        elif 57 <= Codscore <= 60:
            standardized_Codscore = 8
        elif 61 <= Codscore <= 64:
            standardized_Codscore = 9
        elif 65 <= Codscore <= 67:
            standardized_Codscore = 10
        elif 68 <= Codscore <= 69:
            standardized_Codscore = 11
        elif 70 <= Codscore <= 73:
            standardized_Codscore = 12
        elif 74 <= Codscore <= 77:
            standardized_Codscore = 13
        elif 78 <= Codscore <= 79:
            standardized_Codscore = 14
        elif 80 <= Codscore <= 84:
            standardized_Codscore = 15
        elif 85 <= Codscore <= 87:
            standardized_Codscore = 16
        elif 88 <= Codscore <= 90:
            standardized_Codscore = 17
        elif 91 <= Codscore <= 92:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 15:
        if 0 <= Codscore <= 32:
            standardized_Codscore = 1
        elif 32 <= Codscore <= 37:
            standardized_Codscore = 2
        elif 38 <= Codscore <= 42:
            standardized_Codscore = 3
        elif 43 <= Codscore <= 47:
            standardized_Codscore = 4
        elif 48 <= Codscore <= 51:
            standardized_Codscore = 5
        elif 52 <= Codscore <= 54:
            standardized_Codscore = 6
        elif 55 <= Codscore <= 57:
            standardized_Codscore = 7
        elif 58 <= Codscore <= 61:
            standardized_Codscore = 8
        elif 62 <= Codscore <= 64:
            standardized_Codscore = 9
        elif 65 <= Codscore <= 68:
            standardized_Codscore = 10
        elif 69 <= Codscore <= 70:
            standardized_Codscore = 11
        elif 71 <= Codscore <= 74:
            standardized_Codscore = 12
        elif 75 <= Codscore <= 78:
            standardized_Codscore = 13
        elif 79 <= Codscore <= 80:
            standardized_Codscore = 14
        elif 81 <= Codscore <= 84:
            standardized_Codscore = 15
        elif 85 <= Codscore <= 87:
            standardized_Codscore = 16
        elif 88 <= Codscore <= 90:
            standardized_Codscore = 17
        elif 91 <= Codscore <= 92:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 15.5:
        if 0 <= Codscore <= 33:
            standardized_Codscore = 1
        elif 34 <= Codscore <= 37:
            standardized_Codscore = 2
        elif 38 <= Codscore <= 42:
            standardized_Codscore = 3
        elif 43 <= Codscore <= 47:
            standardized_Codscore = 4
        elif 48 <= Codscore <= 51:
            standardized_Codscore = 5
        elif 52 <= Codscore <= 55:
            standardized_Codscore = 6
        elif 56 <= Codscore <= 57:
            standardized_Codscore = 7
        elif 58 <= Codscore <= 62:
            standardized_Codscore = 8
        elif 63 <= Codscore <= 66:
            standardized_Codscore = 9
        elif 67 <= Codscore <= 69:
            standardized_Codscore = 10
        elif 70 <= Codscore <= 72:
            standardized_Codscore = 11
        elif 73 <= Codscore <= 77:
            standardized_Codscore = 12
        elif 78 <= Codscore <= 80:
            standardized_Codscore = 13
        elif 81 <= Codscore <= 83:
            standardized_Codscore = 14
        elif 84 <= Codscore <= 86:
            standardized_Codscore = 15
        elif 87 <= Codscore <= 88:
            standardized_Codscore = 16
        elif 89 <= Codscore <= 90:
            standardized_Codscore = 17
        elif 91 <= Codscore <= 93:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 16:
        if 0 <= Codscore <= 34:
            standardized_Codscore = 1
        elif 35 <= Codscore <= 37:
            standardized_Codscore = 2
        elif 38 <= Codscore <= 43:
            standardized_Codscore = 3
        elif 43 <= Codscore <= 48:
            standardized_Codscore = 4
        elif 49 <= Codscore <= 53:
            standardized_Codscore = 5
        elif 54 <= Codscore <= 56:
            standardized_Codscore = 6
        elif 57 <= Codscore <= 59:
            standardized_Codscore = 7
        elif 60 <= Codscore <= 63:
            standardized_Codscore = 8
        elif 64 <= Codscore <= 67:
            standardized_Codscore = 9
        elif 68 <= Codscore <= 71:
            standardized_Codscore = 10
        elif 72 <= Codscore <= 74:
            standardized_Codscore = 11
        elif 75 <= Codscore <= 78:
            standardized_Codscore = 12
        elif 79 <= Codscore <= 82:
            standardized_Codscore = 13
        elif 83 <= Codscore <= 85:
            standardized_Codscore = 14
        elif 86 <= Codscore <= 87:
            standardized_Codscore = 15
        elif 88 <= Codscore <= 90:
            standardized_Codscore = 16
        elif 91 <= Codscore <= 92:
            standardized_Codscore = 17
        elif 93 <= Codscore <= 94:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    if chrono_age == 16.5:
        if 0 <= Codscore <= 36:
            standardized_Codscore = 1
        elif 37 <= Codscore <= 39:
            standardized_Codscore = 2
        elif 40 <= Codscore <= 44:
            standardized_Codscore = 3
        elif 45 <= Codscore <= 48:
            standardized_Codscore = 4
        elif 49 <= Codscore <= 53:
            standardized_Codscore = 5
        elif 54 <= Codscore <= 56:
            standardized_Codscore = 6
        elif 57 <= Codscore <= 60:
            standardized_Codscore = 7
        elif 61 <= Codscore <= 64:
            standardized_Codscore = 8
        elif 65 <= Codscore <= 68:
            standardized_Codscore = 9
        elif 69 <= Codscore <= 71:
            standardized_Codscore = 10
        elif 72 <= Codscore <= 75:
            standardized_Codscore = 11
        elif 76 <= Codscore <= 79:
            standardized_Codscore = 12
        elif 80 <= Codscore <= 83:
            standardized_Codscore = 13
        elif 84 <= Codscore <= 85:
            standardized_Codscore = 14
        elif 86 <= Codscore <= 89:
            standardized_Codscore = 15
        elif 90 <= Codscore <= 91:
            standardized_Codscore = 16
        elif 92 <= Codscore <= 93:
            standardized_Codscore = 17
        elif 94 <= Codscore <= 96:
            standardized_Codscore = 18
        else:
            standardized_Codscore = 19

    standardized_scores.append(standardized_Codscore)
    QIrealizacao.append(standardized_Codscore)
    QIvp.append(standardized_Codscore)


def find_standardized_DGscore():
    if chrono_age == 6:
        if 0 <= DGscore <= 3:
            standardized_DGscore = DGscore + 4
        elif 4 <= DGscore <= 5:
            standardized_DGscore = 8
        elif 6 <= DGscore <= 8:
            standardized_DGscore = 9
        elif DGscore == 9:
            standardized_DGscore = 10
        elif 10 <= DGscore <= 11:
            standardized_DGscore = 11
        elif 12 <= DGscore <= 13:
            standardized_DGscore = 12
        elif 14 <= DGscore <= 15:
            standardized_DGscore = 13
        elif 16 <= DGscore <= 17:
            standardized_DGscore = 14
        elif 18 <= DGscore <= 19:
            standardized_DGscore = 15
        elif 20 <= DGscore <= 21:
            standardized_DGscore = DGscore - 4
        elif 22 <= DGscore <= 23:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 6.5:
        if 0 <= DGscore <= 3:
            standardized_DGscore = DGscore + 3
        elif 4 <= DGscore <= 5:
            standardized_DGscore = 7
        elif 6 <= DGscore <= 7:
            standardized_DGscore = 8
        elif 8 <= DGscore <= 9:
            standardized_DGscore = 9
        elif 10 <= DGscore <= 11:
            standardized_DGscore = 10
        elif 12 <= DGscore <= 14:
            standardized_DGscore = 11
        elif 15 <= DGscore <= 17:
            standardized_DGscore = 12
        elif 18 <= DGscore <= 19:
            standardized_DGscore = 13
        elif DGscore == 20:
            standardized_DGscore = 14
        elif 21 <= DGscore <= 23:
            standardized_DGscore = 15
        elif 24 <= DGscore <= 27:
            standardized_DGscore = 16
        elif 28 <= DGscore <= 30:
            standardized_DGscore = 17
        elif 31 <= DGscore <= 32:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 7:
        if 0 <= DGscore <= 3:
            standardized_DGscore = DGscore + 1
        elif 4 <= DGscore <= 5:
            standardized_DGscore = 5
        elif 6 <= DGscore <= 7:
            standardized_DGscore = DGscore
        elif 8 <= DGscore <= 10:
            standardized_DGscore = 8
        elif 11 <= DGscore <= 13:
            standardized_DGscore = 9
        elif 14 <= DGscore <= 16:
            standardized_DGscore = 10
        elif 17 <= DGscore <= 18:
            standardized_DGscore = 11
        elif 19 <= DGscore <= 20:
            standardized_DGscore = 12
        elif DGscore == 21:
            standardized_DGscore = 13
        elif 22 <= DGscore <= 23:
            standardized_DGscore = 14
        elif 24 <= DGscore <= 25:
            standardized_DGscore = 15
        elif 26 <= DGscore <= 30:
            standardized_DGscore = 16
        elif 31 <= DGscore <= 32:
            standardized_DGscore = 17
        elif 33 <= DGscore <= 34:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 7.5:
        if 0 <= DGscore <= 2:
            standardized_DGscore = DGscore + 1
        elif 3 <= DGscore <= 4:
            standardized_DGscore = 4
        elif DGscore == 5:
            standardized_DGscore = DGscore
        elif 6 <= DGscore <= 7:
            standardized_DGscore = 6
        elif 8 <= DGscore <= 9:
            standardized_DGscore = 7
        elif 10 <= DGscore <= 12:
            standardized_DGscore = 8
        elif 13 <= DGscore <= 15:
            standardized_DGscore = 9
        elif 16 <= DGscore <= 18:
            standardized_DGscore = 10
        elif 19 <= DGscore <= 20:
            standardized_DGscore = 11
        elif 21 <= DGscore <= 22:
            standardized_DGscore = 12
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 13
        elif 26 <= DGscore <= 28:
            standardized_DGscore = 14
        elif 29 <= DGscore <= 31:
            standardized_DGscore = 15
        elif DGscore == 32:
            standardized_DGscore = 16
        elif 33 <= DGscore <= 34:
            standardized_DGscore = 17
        elif 35 <= DGscore <= 37:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 8:
        if 0 <= DGscore <= 1:
            standardized_DGscore = 1
        elif 2 <= DGscore <= 3:
            standardized_DGscore = DGscore
        elif 4 <= DGscore <= 5:
            standardized_DGscore = 4
        elif 6 <= DGscore <= 7:
            standardized_DGscore = 5
        elif 8 <= DGscore <= 9:
            standardized_DGscore = 6
        elif 10 <= DGscore <= 11:
            standardized_DGscore = 7
        elif 11 <= DGscore <= 14:
            standardized_DGscore = 8
        elif 15 <= DGscore <= 17:
            standardized_DGscore = 9
        elif 18 <= DGscore <= 20:
            standardized_DGscore = 10
        elif 21 <= DGscore <= 22:
            standardized_DGscore = 11
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 12
        elif 26 <= DGscore <= 28:
            standardized_DGscore = 13
        elif 29 <= DGscore <= 30:
            standardized_DGscore = 14
        elif 31 <= DGscore <= 32:
            standardized_DGscore = 15
        elif 33 <= DGscore <= 34:
            standardized_DGscore = 16
        elif 35 <= DGscore <= 36:
            standardized_DGscore = 17
        elif 37 <= DGscore <= 38:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 8.5:
        if 0 <= DGscore <= 1:
            standardized_DGscore = 1
        elif DGscore == 2:
            standardized_DGscore = 2
        elif 3 <= DGscore <= 4:
            standardized_DGscore = 3
        elif 5 <= DGscore <= 6:
            standardized_DGscore = 4
        elif 7 <= DGscore <= 9:
            standardized_DGscore = 5
        elif DGscore == 10:
            standardized_DGscore = 6
        elif 11 <= DGscore <= 13:
            standardized_DGscore = 7
        elif 14 <= DGscore <= 16:
            standardized_DGscore = 8
        elif 17 <= DGscore <= 18:
            standardized_DGscore = 9
        elif 19 <= DGscore <= 20:
            standardized_DGscore = 10
        elif 21 <= DGscore <= 23:
            standardized_DGscore = 11
        elif 24 <= DGscore <= 26:
            standardized_DGscore = 12
        elif 27 <= DGscore <= 29:
            standardized_DGscore = 13
        elif 30 <= DGscore <= 32:
            standardized_DGscore = 14
        elif DGscore == 33:
            standardized_DGscore = 15
        elif 34 <= DGscore <= 35:
            standardized_DGscore = 16
        elif DGscore == 36:
            standardized_DGscore = 17
        elif 37 <= DGscore <= 39:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 9:
        if 0 <= DGscore <= 1:
            standardized_DGscore = 1
        elif DGscore == 2:
            standardized_DGscore = 2
        elif 3 <= DGscore <= 4:
            standardized_DGscore = 3
        elif 5 <= DGscore <= 7:
            standardized_DGscore = 4
        elif 8 <= DGscore <= 9:
            standardized_DGscore = 5
        elif 10 <= DGscore <= 11:
            standardized_DGscore = 6
        elif 12 <= DGscore <= 14:
            standardized_DGscore = 7
        elif 15 <= DGscore <= 17:
            standardized_DGscore = 8
        elif 18 <= DGscore <= 19:
            standardized_DGscore = 9
        elif 20 <= DGscore <= 21:
            standardized_DGscore = 10
        elif 22 <= DGscore <= 23:
            standardized_DGscore = 11
        elif 24 <= DGscore <= 26:
            standardized_DGscore = 12
        elif 27 <= DGscore <= 31:
            standardized_DGscore = 13
        elif DGscore == 32:
            standardized_DGscore = 14
        elif 33 <= DGscore <= 34:
            standardized_DGscore = 15
        elif 35 <= DGscore <= 36:
            standardized_DGscore = 16
        elif 37 <= DGscore <= 38:
            standardized_DGscore = 17
        elif 39 <= DGscore <= 40:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 9.5:
        if 0 <= DGscore <= 2:
            standardized_DGscore = 1
        elif DGscore == 3:
            standardized_DGscore = 2
        elif 4 <= DGscore <= 5:
            standardized_DGscore = 3
        elif 6 <= DGscore <= 9:
            standardized_DGscore = 4
        elif 10 <= DGscore <= 11:
            standardized_DGscore = 5
        elif 12 <= DGscore <= 13:
            standardized_DGscore = 6
        elif 14 <= DGscore <= 16:
            standardized_DGscore = 7
        elif 17 <= DGscore <= 19:
            standardized_DGscore = 8
        elif 20 <= DGscore <= 21:
            standardized_DGscore = 9
        elif 22 <= DGscore <= 24:
            standardized_DGscore = 10
        elif 25 <= DGscore <= 27:
            standardized_DGscore = 11
        elif 28 <= DGscore <= 30:
            standardized_DGscore = 12
        elif 31 <= DGscore <= 32:
            standardized_DGscore = 13
        elif 33 <= DGscore <= 35:
            standardized_DGscore = 14
        elif 36 <= DGscore <= 38:
            standardized_DGscore = 15
        elif DGscore == 39:
            standardized_DGscore = 16
        elif 40 <= DGscore <= 41:
            standardized_DGscore = 17
        elif DGscore == 42:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 10:
        if 0 <= DGscore <= 4:
            standardized_DGscore = 1
        elif 5 <= DGscore <= 8:
            standardized_DGscore = 2
        elif 9 <= DGscore <= 11:
            standardized_DGscore = 3
        elif DGscore == 12:
            standardized_DGscore = 4
        elif 13 <= DGscore <= 14:
            standardized_DGscore = 5
        elif 15 <= DGscore <= 17:
            standardized_DGscore = 6
        elif 18 <= DGscore <= 19:
            standardized_DGscore = 7
        elif 20 <= DGscore <= 21:
            standardized_DGscore = 8
        elif 22 <= DGscore <= 24:
            standardized_DGscore = 9
        elif 25 <= DGscore <= 26:
            standardized_DGscore = 10
        elif 27 <= DGscore <= 28:
            standardized_DGscore = 11
        elif 29 <= DGscore <= 31:
            standardized_DGscore = 12
        elif 32 <= DGscore <= 35:
            standardized_DGscore = 13
        elif 36 <= DGscore <= 37:
            standardized_DGscore = 14
        elif 38 <= DGscore <= 39:
            standardized_DGscore = 15
        elif 40 <= DGscore <= 41:
            standardized_DGscore = 16
        elif 42 <= DGscore <= 43:
            standardized_DGscore = 17
        elif 44 <= DGscore <= 45:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 10.5:
        if 0 <= DGscore <= 5:
            standardized_DGscore = 1
        elif 6 <= DGscore <= 8:
            standardized_DGscore = 2
        elif 9 <= DGscore <= 11:
            standardized_DGscore = 3
        elif DGscore == 12:
            standardized_DGscore = 4
        elif 13 <= DGscore <= 14:
            standardized_DGscore = 5
        elif 15 <= DGscore <= 17:
            standardized_DGscore = 6
        elif 18 <= DGscore <= 19:
            standardized_DGscore = 7
        elif 20 <= DGscore <= 22:
            standardized_DGscore = 8
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 9
        elif 26 <= DGscore <= 27:
            standardized_DGscore = 10
        elif 28 <= DGscore <= 30:
            standardized_DGscore = 11
        elif 31 <= DGscore <= 33:
            standardized_DGscore = 12
        elif 34 <= DGscore <= 37:
            standardized_DGscore = 13
        elif 38 <= DGscore <= 39:
            standardized_DGscore = 14
        elif 40 <= DGscore <= 42:
            standardized_DGscore = 15
        elif DGscore == 43:
            standardized_DGscore = 16
        elif DGscore == 44:
            standardized_DGscore = 17
        elif 45 <= DGscore <= 46:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 11:
        if 0 <= DGscore <= 5:
            standardized_DGscore = 1
        elif 6 <= DGscore <= 8:
            standardized_DGscore = 2
        elif 9 <= DGscore <= 11:
            standardized_DGscore = 3
        elif DGscore == 12:
            standardized_DGscore = 4
        elif 13 <= DGscore <= 15:
            standardized_DGscore = 5
        elif 16 <= DGscore <= 17:
            standardized_DGscore = 6
        elif 18 <= DGscore <= 21:
            standardized_DGscore = 7
        elif 22 <= DGscore <= 24:
            standardized_DGscore = 8
        elif 25 <= DGscore <= 26:
            standardized_DGscore = 9
        elif 27 <= DGscore <= 28:
            standardized_DGscore = 10
        elif 29 <= DGscore <= 31:
            standardized_DGscore = 11
        elif 32 <= DGscore <= 36:
            standardized_DGscore = 12
        elif 37 <= DGscore <= 38:
            standardized_DGscore = 13
        elif 39 <= DGscore <= 41:
            standardized_DGscore = 14
        elif 42 <= DGscore <= 43:
            standardized_DGscore = 15
        elif 44 <= DGscore <= 45:
            standardized_DGscore = 16
        elif 46 <= DGscore <= 47:
            standardized_DGscore = 17
        elif 48 <= DGscore <= 49:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 11.5:
        if 0 <= DGscore <= 6:
            standardized_DGscore = 1
        elif 7 <= DGscore <= 8:
            standardized_DGscore = 2
        elif 9 <= DGscore <= 11:
            standardized_DGscore = 3
        elif 12 <= DGscore <= 13:
            standardized_DGscore = 4
        elif 14 <= DGscore <= 16:
            standardized_DGscore = 5
        elif 17 <= DGscore <= 18:
            standardized_DGscore = 6
        elif 19 <= DGscore <= 22:
            standardized_DGscore = 7
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 8
        elif 26 <= DGscore <= 27:
            standardized_DGscore = 9
        elif 28 <= DGscore <= 30:
            standardized_DGscore = 10
        elif 31 <= DGscore <= 34:
            standardized_DGscore = 11
        elif 35 <= DGscore <= 37:
            standardized_DGscore = 12
        elif 38 <= DGscore <= 41:
            standardized_DGscore = 13
        elif 42 <= DGscore <= 43:
            standardized_DGscore = 14
        elif 44 <= DGscore <= 45:
            standardized_DGscore = 15
        elif 46 <= DGscore <= 48:
            standardized_DGscore = 16
        elif 49 <= DGscore <= 50:
            standardized_DGscore = 17
        elif 51 <= DGscore <= 52:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 12:
        if 0 <= DGscore <= 6:
            standardized_DGscore = 1
        elif 7 <= DGscore <= 8:
            standardized_DGscore = 2
        elif 9 <= DGscore <= 11:
            standardized_DGscore = 3
        elif 12 <= DGscore <= 14:
            standardized_DGscore = 4
        elif 15 <= DGscore <= 16:
            standardized_DGscore = 5
        elif 17 <= DGscore <= 21:
            standardized_DGscore = 6
        elif 22 <= DGscore <= 24:
            standardized_DGscore = 7
        elif 25 <= DGscore <= 27:
            standardized_DGscore = 8
        elif 28 <= DGscore <= 30:
            standardized_DGscore = 9
        elif 31 <= DGscore <= 33:
            standardized_DGscore = 10
        elif 34 <= DGscore <= 36:
            standardized_DGscore = 11
        elif 37 <= DGscore <= 39:
            standardized_DGscore = 12
        elif 40 <= DGscore <= 42:
            standardized_DGscore = 13
        elif 43 <= DGscore <= 44:
            standardized_DGscore = 14
        elif 45 <= DGscore <= 46:
            standardized_DGscore = 15
        elif 47 <= DGscore <= 48:
            standardized_DGscore = 16
        elif 49 <= DGscore <= 50:
            standardized_DGscore = 17
        elif 51 <= DGscore <= 52:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 12.5:
        if 0 <= DGscore <= 7:
            standardized_DGscore = 1
        elif 8 <= DGscore <= 9:
            standardized_DGscore = 2
        elif 10 <= DGscore <= 11:
            standardized_DGscore = 3
        elif 12 <= DGscore <= 14:
            standardized_DGscore = 4
        elif 15 <= DGscore <= 19:
            standardized_DGscore = 5
        elif 20 <= DGscore <= 22:
            standardized_DGscore = 6
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 7
        elif 26 <= DGscore <= 27:
            standardized_DGscore = 8
        elif 28 <= DGscore <= 30:
            standardized_DGscore = 9
        elif 31 <= DGscore <= 34:
            standardized_DGscore = 10
        elif 35 <= DGscore <= 37:
            standardized_DGscore = 11
        elif 38 <= DGscore <= 41:
            standardized_DGscore = 12
        elif 42 <= DGscore <= 43:
            standardized_DGscore = 13
        elif 44 <= DGscore <= 47:
            standardized_DGscore = 14
        elif 48 <= DGscore <= 50:
            standardized_DGscore = 15
        elif 51 <= DGscore <= 42:
            standardized_DGscore = 16
        elif DGscore == 53:
            standardized_DGscore = 17
        elif 54 <= DGscore <= 55:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 13:
        if 0 <= DGscore <= 7:
            standardized_DGscore = 1
        elif 8 <= DGscore <= 9:
            standardized_DGscore = 2
        elif 10 <= DGscore <= 12:
            standardized_DGscore = 3
        elif 12 <= DGscore <= 15:
            standardized_DGscore = 4
        elif 16 <= DGscore <= 20:
            standardized_DGscore = 5
        elif 21 <= DGscore <= 22:
            standardized_DGscore = 6
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 7
        elif 26 <= DGscore <= 28:
            standardized_DGscore = 8
        elif 29 <= DGscore <= 32:
            standardized_DGscore = 9
        elif 33 <= DGscore <= 35:
            standardized_DGscore = 10
        elif 36 <= DGscore <= 39:
            standardized_DGscore = 11
        elif 40 <= DGscore <= 42:
            standardized_DGscore = 12
        elif 43 <= DGscore <= 45:
            standardized_DGscore = 13
        elif 46 <= DGscore <= 47:
            standardized_DGscore = 14
        elif 48 <= DGscore <= 50:
            standardized_DGscore = 15
        elif 51 <= DGscore <= 52:
            standardized_DGscore = 16
        elif 53 <= DGscore <= 54:
            standardized_DGscore = 17
        elif 55 <= DGscore <= 56:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 13.5:
        if 0 <= DGscore <= 8:
            standardized_DGscore = 1
        elif 9 <= DGscore <= 12:
            standardized_DGscore = 2
        elif 13 <= DGscore <= 15:
            standardized_DGscore = 3
        elif 16 <= DGscore <= 18:
            standardized_DGscore = 4
        elif 19 <= DGscore <= 21:
            standardized_DGscore = 5
        elif 22 <= DGscore <= 24:
            standardized_DGscore = 6
        elif 25 <= DGscore <= 27:
            standardized_DGscore = 7
        elif 28 <= DGscore <= 30:
            standardized_DGscore = 8
        elif 31 <= DGscore <= 34:
            standardized_DGscore = 9
        elif 35 <= DGscore <= 36:
            standardized_DGscore = 10
        elif 37 <= DGscore <= 40:
            standardized_DGscore = 11
        elif 41 <= DGscore <= 43:
            standardized_DGscore = 12
        elif 44 <= DGscore <= 45:
            standardized_DGscore = 13
        elif 46 <= DGscore <= 47:
            standardized_DGscore = 14
        elif 48 <= DGscore <= 50:
            standardized_DGscore = 15
        elif 51 <= DGscore <= 52:
            standardized_DGscore = 16
        elif 53 <= DGscore <= 54:
            standardized_DGscore = 17
        elif 55 <= DGscore <= 56:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 14:
        if 0 <= DGscore <= 9:
            standardized_DGscore = 1
        elif 10 <= DGscore <= 12:
            standardized_DGscore = 2
        elif 13 <= DGscore <= 16:
            standardized_DGscore = 3
        elif 17 <= DGscore <= 19:
            standardized_DGscore = 4
        elif 20 <= DGscore <= 22:
            standardized_DGscore = 5
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 6
        elif 26 <= DGscore <= 28:
            standardized_DGscore = 7
        elif 29 <= DGscore <= 31:
            standardized_DGscore = 8
        elif 32 <= DGscore <= 34:
            standardized_DGscore = 9
        elif 35 <= DGscore <= 38:
            standardized_DGscore = 10
        elif 39 <= DGscore <= 41:
            standardized_DGscore = 11
        elif 42 <= DGscore <= 43:
            standardized_DGscore = 12
        elif 44 <= DGscore <= 45:
            standardized_DGscore = 13
        elif 46 <= DGscore <= 47:
            standardized_DGscore = 14
        elif 48 <= DGscore <= 50:
            standardized_DGscore = 15
        elif 51 <= DGscore <= 52:
            standardized_DGscore = 16
        elif 53 <= DGscore <= 54:
            standardized_DGscore = 17
        elif 55 <= DGscore <= 56:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 14.5:
        if 0 <= DGscore <= 10:
            standardized_DGscore = 1
        elif 11 <= DGscore <= 13:
            standardized_DGscore = 2
        elif 14 <= DGscore <= 16:
            standardized_DGscore = 3
        elif 17 <= DGscore <= 19:
            standardized_DGscore = 4
        elif 20 <= DGscore <= 22:
            standardized_DGscore = 5
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 6
        elif 26 <= DGscore <= 28:
            standardized_DGscore = 7
        elif 29 <= DGscore <= 31:
            standardized_DGscore = 8
        elif 32 <= DGscore <= 34:
            standardized_DGscore = 9
        elif 35 <= DGscore <= 38:
            standardized_DGscore = 10
        elif 39 <= DGscore <= 41:
            standardized_DGscore = 11
        elif 42 <= DGscore <= 43:
            standardized_DGscore = 12
        elif 44 <= DGscore <= 45:
            standardized_DGscore = 13
        elif 46 <= DGscore <= 47:
            standardized_DGscore = 14
        elif 48 <= DGscore <= 50:
            standardized_DGscore = 15
        elif 51 <= DGscore <= 52:
            standardized_DGscore = 16
        elif 53 <= DGscore <= 54:
            standardized_DGscore = 17
        elif 55 <= DGscore <= 56:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 15:
        if 0 <= DGscore <= 10:
            standardized_DGscore = 1
        elif 11 <= DGscore <= 13:
            standardized_DGscore = 2
        elif 14 <= DGscore <= 16:
            standardized_DGscore = 3
        elif 17 <= DGscore <= 19:
            standardized_DGscore = 4
        elif 20 <= DGscore <= 22:
            standardized_DGscore = 5
        elif 23 <= DGscore <= 25:
            standardized_DGscore = 6
        elif 26 <= DGscore <= 28:
            standardized_DGscore = 7
        elif 29 <= DGscore <= 31:
            standardized_DGscore = 8
        elif 32 <= DGscore <= 34:
            standardized_DGscore = 9
        elif 35 <= DGscore <= 38:
            standardized_DGscore = 10
        elif 39 <= DGscore <= 41:
            standardized_DGscore = 11
        elif 42 <= DGscore <= 43:
            standardized_DGscore = 12
        elif 44 <= DGscore <= 45:
            standardized_DGscore = 13
        elif 46 <= DGscore <= 47:
            standardized_DGscore = 14
        elif 48 <= DGscore <= 50:
            standardized_DGscore = 15
        elif 51 <= DGscore <= 52:
            standardized_DGscore = 16
        elif 53 <= DGscore <= 54:
            standardized_DGscore = 17
        elif 55 <= DGscore <= 56:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 15.5:
        if 0 <= DGscore <= 11:
            standardized_DGscore = 1
        elif 12 <= DGscore <= 13:
            standardized_DGscore = 2
        elif 14 <= DGscore <= 16:
            standardized_DGscore = 3
        elif 17 <= DGscore <= 20:
            standardized_DGscore = 4
        elif 21 <= DGscore <= 23:
            standardized_DGscore = 5
        elif 24 <= DGscore <= 25:
            standardized_DGscore = 6
        elif 26 <= DGscore <= 29:
            standardized_DGscore = 7
        elif 30 <= DGscore <= 32:
            standardized_DGscore = 8
        elif 33 <= DGscore <= 35:
            standardized_DGscore = 9
        elif 36 <= DGscore <= 38:
            standardized_DGscore = 10
        elif 39 <= DGscore <= 41:
            standardized_DGscore = 11
        elif 42 <= DGscore <= 44:
            standardized_DGscore = 12
        elif 45 <= DGscore <= 47:
            standardized_DGscore = 13
        elif 48 <= DGscore <= 49:
            standardized_DGscore = 14
        elif 50 <= DGscore <= 52:
            standardized_DGscore = 15
        elif 53 <= DGscore <= 54:
            standardized_DGscore = 16
        elif DGscore == 55:
            standardized_DGscore = 17
        elif 56 <= DGscore <= 57:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 16:
        if 0 <= DGscore <= 12:
            standardized_DGscore = 1
        elif 13 <= DGscore <= 16:
            standardized_DGscore = 2
        elif 17 <= DGscore <= 20:
            standardized_DGscore = 3
        elif 21 <= DGscore <= 23:
            standardized_DGscore = 4
        elif 24 <= DGscore <= 25:
            standardized_DGscore = 5
        elif DGscore == 26:
            standardized_DGscore = 6
        elif 27 <= DGscore <= 30:
            standardized_DGscore = 7
        elif 31 <= DGscore <= 34:
            standardized_DGscore = 8
        elif 35 <= DGscore <= 37:
            standardized_DGscore = 9
        elif 38 <= DGscore <= 41:
            standardized_DGscore = 10
        elif 42 <= DGscore <= 44:
            standardized_DGscore = 11
        elif 45 <= DGscore <= 46:
            standardized_DGscore = 12
        elif 47 <= DGscore <= 48:
            standardized_DGscore = 13
        elif 49 <= DGscore <= 51:
            standardized_DGscore = 14
        elif 52 <= DGscore <= 53:
            standardized_DGscore = 15
        elif 54 <= DGscore <= 55:
            standardized_DGscore = 16
        elif 56 <= DGscore <= 57:
            standardized_DGscore = 17
        elif 58 <= DGscore <= 59:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19

    if chrono_age == 16.5:
        if 0 <= DGscore <= 14:
            standardized_DGscore = 1
        elif 15 <= DGscore <= 17:
            standardized_DGscore = 2
        elif 18 <= DGscore <= 20:
            standardized_DGscore = 3
        elif 21 <= DGscore <= 23:
            standardized_DGscore = 4
        elif 24 <= DGscore <= 26:
            standardized_DGscore = 5
        elif 27 <= DGscore <= 28:
            standardized_DGscore = 6
        elif 29 <= DGscore <= 32:
            standardized_DGscore = 7
        elif 33 <= DGscore <= 35:
            standardized_DGscore = 8
        elif 36 <= DGscore <= 38:
            standardized_DGscore = 9
        elif 39 <= DGscore <= 41:
            standardized_DGscore = 10
        elif 42 <= DGscore <= 44:
            standardized_DGscore = 11
        elif 45 <= DGscore <= 47:
            standardized_DGscore = 12
        elif 48 <= DGscore <= 49:
            standardized_DGscore = 13
        elif 50 <= DGscore <= 51:
            standardized_DGscore = 14
        elif 52 <= DGscore <= 53:
            standardized_DGscore = 15
        elif 54 <= DGscore <= 55:
            standardized_DGscore = 16
        elif 56 <= DGscore <= 58:
            standardized_DGscore = 17
        elif 59 <= DGscore <= 60:
            standardized_DGscore = 18
        else:
            standardized_DGscore = 19
    standardized_scores.append(standardized_DGscore)
    QIrealizacao.append(standardized_DGscore)
    QIop.append(standardized_DGscore)


def find_standardized_Cubscore():
    if chrono_age == 6:
        if 0 <= Cubscore <= 4:
            standardized_Cubscore = Cubscore + 2
        elif 5 <= Cubscore <= 6:
            standardized_Cubscore = 7
        elif 7 <= Cubscore <= 9:
            standardized_Cubscore = 8
        elif 10 <= Cubscore <= 12:
            standardized_Cubscore = 9
        elif 13 <= Cubscore <= 15:
            standardized_Cubscore = 10
        elif 16 <= Cubscore <= 19:
            standardized_Cubscore = 11
        elif 20 <= Cubscore <= 24:
            standardized_Cubscore = 12
        elif 25 <= Cubscore <= 27:
            standardized_Cubscore = 13
        elif 28 <= Cubscore <= 31:
            standardized_Cubscore = 14
        elif 32 <= Cubscore <= 34:
            standardized_Cubscore = 15
        elif 35 <= Cubscore <= 38:
            standardized_Cubscore = 16
        elif 39 <= Cubscore <= 40:
            standardized_Cubscore = 17
        elif 41 <= Cubscore <= 42:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 6.5:
        if 0 <= Cubscore <= 4:
            standardized_Cubscore = Cubscore + 2
        elif 5 <= Cubscore <= 6:
            standardized_Cubscore = 7
        elif 7 <= Cubscore <= 10:
            standardized_Cubscore = 8
        elif 11 <= Cubscore <= 15:
            standardized_Cubscore = 9
        elif 16 <= Cubscore <= 18:
            standardized_Cubscore = 10
        elif 19 <= Cubscore <= 22:
            standardized_Cubscore = 11
        elif 23 <= Cubscore <= 27:
            standardized_Cubscore = 12
        elif 28 <= Cubscore <= 31:
            standardized_Cubscore = 13
        elif 32 <= Cubscore <= 33:
            standardized_Cubscore = 14
        elif 34 <= Cubscore <= 38:
            standardized_Cubscore = 15
        elif 39 <= Cubscore <= 43:
            standardized_Cubscore = 16
        elif 44 <= Cubscore <= 46:
            standardized_Cubscore = 17
        elif 47 <= Cubscore <= 49:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 7:
        if 0 <= Cubscore <= 2:
            standardized_Cubscore = Cubscore + 2
        elif 3 <= Cubscore <= 4:
            standardized_Cubscore = 5
        elif Cubscore == 5:
            standardized_Cubscore = 6
        elif 6 <= Cubscore <= 10:
            standardized_Cubscore = 7
        elif 11 <= Cubscore <= 15:
            standardized_Cubscore = 8
        elif 16 <= Cubscore <= 18:
            standardized_Cubscore = 9
        elif 19 <= Cubscore <= 21:
            standardized_Cubscore = 10
        elif 22 <= Cubscore <= 26:
            standardized_Cubscore = 11
        elif 27 <= Cubscore <= 30:
            standardized_Cubscore = 12
        elif 31 <= Cubscore <= 32:
            standardized_Cubscore = 13
        elif 33 <= Cubscore <= 35:
            standardized_Cubscore = 14
        elif 36 <= Cubscore <= 41:
            standardized_Cubscore = 15
        elif 42 <= Cubscore <= 46:
            standardized_Cubscore = 16
        elif 47 <= Cubscore <= 49:
            standardized_Cubscore = 17
        elif 50 <= Cubscore <= 51:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 7.5:
        if 0 <= Cubscore <= 2:
            standardized_Cubscore = Cubscore + 1
        elif 3 <= Cubscore <= 4:
            standardized_Cubscore = 4
        elif Cubscore == 5:
            standardized_Cubscore = 5
        elif 6 <= Cubscore <= 9:
            standardized_Cubscore = 6
        elif 10 <= Cubscore <= 13:
            standardized_Cubscore = 7
        elif 14 <= Cubscore <= 17:
            standardized_Cubscore = 8
        elif 18 <= Cubscore <= 20:
            standardized_Cubscore = 9
        elif 21 <= Cubscore <= 25:
            standardized_Cubscore = 10
        elif 26 <= Cubscore <= 29:
            standardized_Cubscore = 11
        elif 30 <= Cubscore <= 33:
            standardized_Cubscore = 12
        elif 34 <= Cubscore <= 38:
            standardized_Cubscore = 13
        elif 39 <= Cubscore <= 42:
            standardized_Cubscore = 14
        elif 43 <= Cubscore <= 46:
            standardized_Cubscore = 15
        elif 47 <= Cubscore <= 49:
            standardized_Cubscore = 16
        elif 50 <= Cubscore <= 53:
            standardized_Cubscore = 17
        elif 54 <= Cubscore <= 57:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 8:
        if 0 <= Cubscore <= 1:
            standardized_Cubscore = 1
        elif 2 <= Cubscore <= 3:
            standardized_Cubscore = 2
        elif Cubscore == 4:
            standardized_Cubscore = 3
        elif Cubscore == 5:
            standardized_Cubscore = 4
        elif 6 <= Cubscore <= 8:
            standardized_Cubscore = 5
        elif 9 <= Cubscore <= 13:
            standardized_Cubscore = 6
        elif 14 <= Cubscore <= 16:
            standardized_Cubscore = 7
        elif 17 <= Cubscore <= 19:
            standardized_Cubscore = 8
        elif 20 <= Cubscore <= 24:
            standardized_Cubscore = 9
        elif 25 <= Cubscore <= 29:
            standardized_Cubscore = 10
        elif 30 <= Cubscore <= 33:
            standardized_Cubscore = 11
        elif 34 <= Cubscore <= 37:
            standardized_Cubscore = 12
        elif 38 <= Cubscore <= 41:
            standardized_Cubscore = 13
        elif 42 <= Cubscore <= 45:
            standardized_Cubscore = 14
        elif 46 <= Cubscore <= 48:
            standardized_Cubscore = 15
        elif 49 <= Cubscore <= 52:
            standardized_Cubscore = 16
        elif 53 <= Cubscore <= 56:
            standardized_Cubscore = 17
        elif 57 <= Cubscore <= 58:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 8.5:
        if 0 <= Cubscore <= 1:
            standardized_Cubscore = 1
        elif 2 <= Cubscore <= 3:
            standardized_Cubscore = 2
        elif 4 <= Cubscore <= 5:
            standardized_Cubscore = 3
        elif 6 <= Cubscore <= 8:
            standardized_Cubscore = 4
        elif 9 <= Cubscore <= 11:
            standardized_Cubscore = 5
        elif 12 <= Cubscore <= 15:
            standardized_Cubscore = 6
        elif 16 <= Cubscore <= 19:
            standardized_Cubscore = 7
        elif 20 <= Cubscore <= 22:
            standardized_Cubscore = 8
        elif 23 <= Cubscore <= 26:
            standardized_Cubscore = 9
        elif 27 <= Cubscore <= 31:
            standardized_Cubscore = 10
        elif 32 <= Cubscore <= 35:
            standardized_Cubscore = 11
        elif 36 <= Cubscore <= 39:
            standardized_Cubscore = 12
        elif 40 <= Cubscore <= 43:
            standardized_Cubscore = 13
        elif 44 <= Cubscore <= 47:
            standardized_Cubscore = 14
        elif 48 <= Cubscore <= 52:
            standardized_Cubscore = 15
        elif 53 <= Cubscore <= 54:
            standardized_Cubscore = 16
        elif 55 <= Cubscore <= 57:
            standardized_Cubscore = 17
        elif 58 <= Cubscore <= 59:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 9:
        if 0 <= Cubscore <= 2:
            standardized_Cubscore = 1
        elif 3 <= Cubscore <= 5:
            standardized_Cubscore = 2
        elif 6 <= Cubscore <= 10:
            standardized_Cubscore = 3
        elif 11 <= Cubscore <= 13:
            standardized_Cubscore = 4
        elif 14 <= Cubscore <= 17:
            standardized_Cubscore = 5
        elif 18 <= Cubscore <= 19:
            standardized_Cubscore = 6
        elif 20 <= Cubscore <= 21:
            standardized_Cubscore = 7
        elif 22 <= Cubscore <= 25:
            standardized_Cubscore = 8
        elif 26 <= Cubscore <= 29:
            standardized_Cubscore = 9
        elif 30 <= Cubscore <= 33:
            standardized_Cubscore = 10
        elif 34 <= Cubscore <= 38:
            standardized_Cubscore = 11
        elif 39 <= Cubscore <= 40:
            standardized_Cubscore = 12
        elif 41 <= Cubscore <= 44:
            standardized_Cubscore = 13
        elif 45 <= Cubscore <= 50:
            standardized_Cubscore = 14
        elif 51 <= Cubscore <= 53:
            standardized_Cubscore = 15
        elif 54 <= Cubscore <= 56:
            standardized_Cubscore = 16
        elif 57 <= Cubscore <= 58:
            standardized_Cubscore = 17
        elif 59 <= Cubscore <= 60:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 9.5:
        if 0 <= Cubscore <= 3:
            standardized_Cubscore = 1
        elif 4 <= Cubscore <= 6:
            standardized_Cubscore = 2
        elif 7 <= Cubscore <= 11:
            standardized_Cubscore = 3
        elif 12 <= Cubscore <= 16:
            standardized_Cubscore = 4
        elif 17 <= Cubscore <= 19:
            standardized_Cubscore = 5
        elif 20 <= Cubscore <= 22:
            standardized_Cubscore = 6
        elif 23 <= Cubscore <= 25:
            standardized_Cubscore = 7
        elif 26 <= Cubscore <= 29:
            standardized_Cubscore = 8
        elif 30 <= Cubscore <= 32:
            standardized_Cubscore = 9
        elif 33 <= Cubscore <= 36:
            standardized_Cubscore = 10
        elif 37 <= Cubscore <= 39:
            standardized_Cubscore = 11
        elif 40 <= Cubscore <= 42:
            standardized_Cubscore = 12
        elif 43 <= Cubscore <= 45:
            standardized_Cubscore = 13
        elif 46 <= Cubscore <= 50:
            standardized_Cubscore = 14
        elif 51 <= Cubscore <= 53:
            standardized_Cubscore = 15
        elif 54 <= Cubscore <= 56:
            standardized_Cubscore = 16
        elif 57 <= Cubscore <= 58:
            standardized_Cubscore = 17
        elif 59 <= Cubscore <= 60:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 10:
        if 0 <= Cubscore <= 5:
            standardized_Cubscore = 1
        elif 6 <= Cubscore <= 10:
            standardized_Cubscore = 2
        elif 11 <= Cubscore <= 13:
            standardized_Cubscore = 3
        elif 14 <= Cubscore <= 17:
            standardized_Cubscore = 4
        elif 18 <= Cubscore <= 19:
            standardized_Cubscore = 5
        elif 20 <= Cubscore <= 22:
            standardized_Cubscore = 6
        elif 23 <= Cubscore <= 28:
            standardized_Cubscore = 7
        elif 29 <= Cubscore <= 32:
            standardized_Cubscore = 8
        elif 33 <= Cubscore <= 34:
            standardized_Cubscore = 9
        elif 35 <= Cubscore <= 37:
            standardized_Cubscore = 10
        elif 38 <= Cubscore <= 41:
            standardized_Cubscore = 11
        elif 42 <= Cubscore <= 43:
            standardized_Cubscore = 12
        elif 44 <= Cubscore <= 45:
            standardized_Cubscore = 13
        elif 46 <= Cubscore <= 50:
            standardized_Cubscore = 14
        elif 51 <= Cubscore <= 53:
            standardized_Cubscore = 15
        elif 54 <= Cubscore <= 56:
            standardized_Cubscore = 16
        elif 57 <= Cubscore <= 59:
            standardized_Cubscore = 17
        elif Cubscore == 60:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 10.5:
        if 0 <= Cubscore <= 6:
            standardized_Cubscore = 1
        elif 7 <= Cubscore <= 10:
            standardized_Cubscore = 2
        elif 11 <= Cubscore <= 13:
            standardized_Cubscore = 3
        elif 14 <= Cubscore <= 17:
            standardized_Cubscore = 4
        elif 18 <= Cubscore <= 19:
            standardized_Cubscore = 5
        elif 20 <= Cubscore <= 24:
            standardized_Cubscore = 6
        elif 25 <= Cubscore <= 28:
            standardized_Cubscore = 7
        elif 29 <= Cubscore <= 33:
            standardized_Cubscore = 8
        elif 34 <= Cubscore <= 36:
            standardized_Cubscore = 9
        elif 37 <= Cubscore <= 39:
            standardized_Cubscore = 10
        elif 40 <= Cubscore <= 43:
            standardized_Cubscore = 11
        elif 44 <= Cubscore <= 46:
            standardized_Cubscore = 12
        elif 47 <= Cubscore <= 50:
            standardized_Cubscore = 13
        elif 51 <= Cubscore <= 52:
            standardized_Cubscore = 14
        elif 53 <= Cubscore <= 56:
            standardized_Cubscore = 15
        elif 57 <= Cubscore <= 59:
            standardized_Cubscore = 16
        elif Cubscore == 60:
            standardized_Cubscore = 17
        elif 61 <= Cubscore <= 62:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 11:
        if 0 <= Cubscore <= 6:
            standardized_Cubscore = 1
        elif 7 <= Cubscore <= 10:
            standardized_Cubscore = 2
        elif 11 <= Cubscore <= 13:
            standardized_Cubscore = 3
        elif 14 <= Cubscore <= 17:
            standardized_Cubscore = 4
        elif 18 <= Cubscore <= 19:
            standardized_Cubscore = 5
        elif 20 <= Cubscore <= 24:
            standardized_Cubscore = 6
        elif 25 <= Cubscore <= 28:
            standardized_Cubscore = 7
        elif 29 <= Cubscore <= 34:
            standardized_Cubscore = 8
        elif 35 <= Cubscore <= 38:
            standardized_Cubscore = 9
        elif 39 <= Cubscore <= 42:
            standardized_Cubscore = 10
        elif 43 <= Cubscore <= 46:
            standardized_Cubscore = 11
        elif 47 <= Cubscore <= 50:
            standardized_Cubscore = 12
        elif 51 <= Cubscore <= 52:
            standardized_Cubscore = 13
        elif 53 <= Cubscore <= 56:
            standardized_Cubscore = 14
        elif 57 <= Cubscore <= 59:
            standardized_Cubscore = 15
        elif Cubscore == 60:
            standardized_Cubscore = 16
        elif Cubscore == 61:
            standardized_Cubscore = 17
        elif 62 <= Cubscore <= 63:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 11.5:
        if 0 <= Cubscore <= 7:
            standardized_Cubscore = 1
        elif 8 <= Cubscore <= 10:
            standardized_Cubscore = 2
        elif 11 <= Cubscore <= 15:
            standardized_Cubscore = 3
        elif 16 <= Cubscore <= 20:
            standardized_Cubscore = 4
        elif 21 <= Cubscore <= 24:
            standardized_Cubscore = 5
        elif 25 <= Cubscore <= 29:
            standardized_Cubscore = 6
        elif 30 <= Cubscore <= 33:
            standardized_Cubscore = 7
        elif 34 <= Cubscore <= 38:
            standardized_Cubscore = 8
        elif 39 <= Cubscore <= 41:
            standardized_Cubscore = 9
        elif 42 <= Cubscore <= 45:
            standardized_Cubscore = 10
        elif 46 <= Cubscore <= 49:
            standardized_Cubscore = 11
        elif 50 <= Cubscore <= 52:
            standardized_Cubscore = 12
        elif 53 <= Cubscore <= 55:
            standardized_Cubscore = 13
        elif 56 <= Cubscore <= 57:
            standardized_Cubscore = 14
        elif 58 <= Cubscore <= 60:
            standardized_Cubscore = 15
        elif 61 <= Cubscore <= 62:
            standardized_Cubscore = 16
        elif Cubscore == 63:
            standardized_Cubscore = 17
        elif Cubscore == 64:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 12:
        if 0 <= Cubscore <= 8:
            standardized_Cubscore = 1
        elif 9 <= Cubscore <= 12:
            standardized_Cubscore = 2
        elif 13 <= Cubscore <= 16:
            standardized_Cubscore = 3
        elif 17 <= Cubscore <= 20:
            standardized_Cubscore = 4
        elif 21 <= Cubscore <= 24:
            standardized_Cubscore = 5
        elif 25 <= Cubscore <= 30:
            standardized_Cubscore = 6
        elif 31 <= Cubscore <= 35:
            standardized_Cubscore = 7
        elif 36 <= Cubscore <= 39:
            standardized_Cubscore = 8
        elif 40 <= Cubscore <= 43:
            standardized_Cubscore = 9
        elif 44 <= Cubscore <= 47:
            standardized_Cubscore = 10
        elif 48 <= Cubscore <= 50:
            standardized_Cubscore = 11
        elif 51 <= Cubscore <= 54:
            standardized_Cubscore = 12
        elif 55 <= Cubscore <= 56:
            standardized_Cubscore = 13
        elif 57 <= Cubscore <= 58:
            standardized_Cubscore = 14
        elif 59 <= Cubscore <= 60:
            standardized_Cubscore = 15
        elif 61 <= Cubscore <= 63:
            standardized_Cubscore = 16
        elif Cubscore == 64:
            standardized_Cubscore = 17
        elif Cubscore == 65:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 12.5:
        if 0 <= Cubscore <= 12:
            standardized_Cubscore = 1
        elif 13 <= Cubscore <= 17:
            standardized_Cubscore = 2
        elif 18 <= Cubscore <= 22:
            standardized_Cubscore = 3
        elif 23 <= Cubscore <= 26:
            standardized_Cubscore = 4
        elif 27 <= Cubscore <= 30:
            standardized_Cubscore = 5
        elif 31 <= Cubscore <= 32:
            standardized_Cubscore = 6
        elif 33 <= Cubscore <= 38:
            standardized_Cubscore = 7
        elif 39 <= Cubscore <= 41:
            standardized_Cubscore = 8
        elif 42 <= Cubscore <= 45:
            standardized_Cubscore = 9
        elif 46 <= Cubscore <= 48:
            standardized_Cubscore = 10
        elif 49 <= Cubscore <= 52:
            standardized_Cubscore = 11
        elif 53 <= Cubscore <= 55:
            standardized_Cubscore = 12
        elif 56 <= Cubscore <= 58:
            standardized_Cubscore = 13
        elif 59 <= Cubscore <= 60:
            standardized_Cubscore = 14
        elif 61 <= Cubscore <= 63:
            standardized_Cubscore = 15
        elif Cubscore == 64:
            standardized_Cubscore = 16
        elif Cubscore == 65:
            standardized_Cubscore = 17
        elif Cubscore == 66:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 13:
        if 0 <= Cubscore <= 14:
            standardized_Cubscore = 1
        elif 15 <= Cubscore <= 19:
            standardized_Cubscore = 2
        elif 20 <= Cubscore <= 24:
            standardized_Cubscore = 3
        elif 25 <= Cubscore <= 29:
            standardized_Cubscore = 4
        elif 30 <= Cubscore <= 32:
            standardized_Cubscore = 5
        elif 33 <= Cubscore <= 37:
            standardized_Cubscore = 6
        elif 38 <= Cubscore <= 40:
            standardized_Cubscore = 7
        elif 41 <= Cubscore <= 43:
            standardized_Cubscore = 8
        elif 44 <= Cubscore <= 47:
            standardized_Cubscore = 9
        elif 48 <= Cubscore <= 50:
            standardized_Cubscore = 10
        elif 51 <= Cubscore <= 55:
            standardized_Cubscore = 11
        elif 56 <= Cubscore <= 57:
            standardized_Cubscore = 12
        elif 58 <= Cubscore <= 59:
            standardized_Cubscore = 13
        elif 60 <= Cubscore <= 61:
            standardized_Cubscore = 14
        elif 62 <= Cubscore <= 63:
            standardized_Cubscore = 15
        elif 64 <= Cubscore <= 65:
            standardized_Cubscore = 16
        elif Cubscore == 66:
            standardized_Cubscore = 17
        elif Cubscore == 67:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 13.5:
        if 0 <= Cubscore <= 16:
            standardized_Cubscore = 1
        elif 17 <= Cubscore <= 21:
            standardized_Cubscore = 2
        elif 22 <= Cubscore <= 25:
            standardized_Cubscore = 3
        elif 26 <= Cubscore <= 29:
            standardized_Cubscore = 4
        elif 30 <= Cubscore <= 32:
            standardized_Cubscore = 5
        elif 33 <= Cubscore <= 37:
            standardized_Cubscore = 6
        elif 38 <= Cubscore <= 41:
            standardized_Cubscore = 7
        elif 42 <= Cubscore <= 45:
            standardized_Cubscore = 8
        elif 46 <= Cubscore <= 48:
            standardized_Cubscore = 9
        elif 49 <= Cubscore <= 51:
            standardized_Cubscore = 10
        elif 52 <= Cubscore <= 55:
            standardized_Cubscore = 11
        elif 56 <= Cubscore <= 58:
            standardized_Cubscore = 12
        elif 59 <= Cubscore <= 60:
            standardized_Cubscore = 13
        elif 61 <= Cubscore <= 62:
            standardized_Cubscore = 14
        elif 63 <= Cubscore <= 64:
            standardized_Cubscore = 15
        elif 65 <= Cubscore <= 66:
            standardized_Cubscore = 16
        elif Cubscore == 67:
            standardized_Cubscore = 17
        elif Cubscore == 68:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 14:
        if 0 <= Cubscore <= 18:
            standardized_Cubscore = 1
        elif 19 <= Cubscore <= 22:
            standardized_Cubscore = 2
        elif 23 <= Cubscore <= 26:
            standardized_Cubscore = 3
        elif 27 <= Cubscore <= 29:
            standardized_Cubscore = 4
        elif 30 <= Cubscore <= 32:
            standardized_Cubscore = 5
        elif 33 <= Cubscore <= 37:
            standardized_Cubscore = 6
        elif 38 <= Cubscore <= 42:
            standardized_Cubscore = 7
        elif 43 <= Cubscore <= 46:
            standardized_Cubscore = 8
        elif 47 <= Cubscore <= 50:
            standardized_Cubscore = 9
        elif 51 <= Cubscore <= 53:
            standardized_Cubscore = 10
        elif 54 <= Cubscore <= 56:
            standardized_Cubscore = 11
        elif 57 <= Cubscore <= 59:
            standardized_Cubscore = 12
        elif 60 <= Cubscore <= 61:
            standardized_Cubscore = 13
        elif 62 <= Cubscore <= 63:
            standardized_Cubscore = 14
        elif 64 <= Cubscore <= 65:
            standardized_Cubscore = 15
        elif Cubscore == 66:
            standardized_Cubscore = 16
        elif Cubscore == 67:
            standardized_Cubscore = 17
        elif Cubscore == 68:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 14.5:
        if 0 <= Cubscore <= 19:
            standardized_Cubscore = 1
        elif 20 <= Cubscore <= 23:
            standardized_Cubscore = 2
        elif 24 <= Cubscore <= 28:
            standardized_Cubscore = 3
        elif 29 <= Cubscore <= 32:
            standardized_Cubscore = 4
        elif 33 <= Cubscore <= 36:
            standardized_Cubscore = 5
        elif 37 <= Cubscore <= 40:
            standardized_Cubscore = 6
        elif 41 <= Cubscore <= 44:
            standardized_Cubscore = 7
        elif 45 <= Cubscore <= 48:
            standardized_Cubscore = 8
        elif 49 <= Cubscore <= 51:
            standardized_Cubscore = 9
        elif 52 <= Cubscore <= 54:
            standardized_Cubscore = 10
        elif 55 <= Cubscore <= 57:
            standardized_Cubscore = 11
        elif 58 <= Cubscore <= 59:
            standardized_Cubscore = 12
        elif 60 <= Cubscore <= 61:
            standardized_Cubscore = 13
        elif 62 <= Cubscore <= 63:
            standardized_Cubscore = 14
        elif 64 <= Cubscore <= 65:
            standardized_Cubscore = 15
        elif Cubscore == 66:
            standardized_Cubscore = 16
        elif Cubscore == 67:
            standardized_Cubscore = 17
        elif Cubscore == 68:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 15:
        if 0 <= Cubscore <= 19:
            standardized_Cubscore = 1
        elif 20 <= Cubscore <= 23:
            standardized_Cubscore = 2
        elif 24 <= Cubscore <= 28:
            standardized_Cubscore = 3
        elif 29 <= Cubscore <= 32:
            standardized_Cubscore = 4
        elif 33 <= Cubscore <= 37:
            standardized_Cubscore = 5
        elif 38 <= Cubscore <= 42:
            standardized_Cubscore = 6
        elif 43 <= Cubscore <= 46:
            standardized_Cubscore = 7
        elif 47 <= Cubscore <= 50:
            standardized_Cubscore = 8
        elif 51 <= Cubscore <= 53:
            standardized_Cubscore = 9
        elif 54 <= Cubscore <= 56:
            standardized_Cubscore = 10
        elif 57 <= Cubscore <= 58:
            standardized_Cubscore = 11
        elif 59 <= Cubscore <= 60:
            standardized_Cubscore = 12
        elif 61 <= Cubscore <= 62:
            standardized_Cubscore = 13
        elif 63 <= Cubscore <= 64:
            standardized_Cubscore = 14
        elif Cubscore == 65:
            standardized_Cubscore = 15
        elif Cubscore == 66:
            standardized_Cubscore = 16
        elif Cubscore == 67:
            standardized_Cubscore = 17
        elif Cubscore == 68:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 15.5:
        if 0 <= Cubscore <= 21:
            standardized_Cubscore = 1
        elif 22 <= Cubscore <= 26:
            standardized_Cubscore = 2
        elif 27 <= Cubscore <= 31:
            standardized_Cubscore = 3
        elif 32 <= Cubscore <= 36:
            standardized_Cubscore = 4
        elif 37 <= Cubscore <= 39:
            standardized_Cubscore = 5
        elif 40 <= Cubscore <= 42:
            standardized_Cubscore = 6
        elif 43 <= Cubscore <= 46:
            standardized_Cubscore = 7
        elif 47 <= Cubscore <= 50:
            standardized_Cubscore = 8
        elif 51 <= Cubscore <= 53:
            standardized_Cubscore = 9
        elif 54 <= Cubscore <= 56:
            standardized_Cubscore = 10
        elif 57 <= Cubscore <= 58:
            standardized_Cubscore = 11
        elif 59 <= Cubscore <= 60:
            standardized_Cubscore = 12
        elif 61 <= Cubscore <= 62:
            standardized_Cubscore = 13
        elif 63 <= Cubscore <= 64:
            standardized_Cubscore = 14
        elif Cubscore == 65:
            standardized_Cubscore = 15
        elif Cubscore == 66:
            standardized_Cubscore = 16
        elif Cubscore == 67:
            standardized_Cubscore = 17
        elif Cubscore == 68:
            standardized_Cubscore = 18
        else:
            standardized_Cubscore = 19

    if chrono_age == 16:
        if 0 <= Cubscore <= 23:
            standardized_Cubscore = 1
        elif 24 <= Cubscore <= 28:
            standardized_Cubscore = 2
        elif 29 <= Cubscore <= 32:
            standardized_Cubscore = 3
        elif 33 <= Cubscore <= 37:
            standardized_Cubscore = 4
        elif 38 <= Cubscore <= 40:
            standardized_Cubscore = 5
        elif 41 <= Cubscore <= 42:
            standardized_Cubscore = 6
        elif 43 <= Cubscore <= 47:
            standardized_Cubscore = 7
        elif 48 <= Cubscore <= 51:
            standardized_Cubscore = 8
        elif 52 <= Cubscore <= 54:
            standardized_Cubscore = 9
        elif 55 <= Cubscore <= 56:
            standardized_Cubscore = 10
        elif 57 <= Cubscore <= 58:
            standardized_Cubscore = 11
        elif 59 <= Cubscore <= 60:
            standardized_Cubscore = 12
        elif 61 <= Cubscore <= 62:
            standardized_Cubscore = 13
        elif 63 <= Cubscore <= 64:
            standardized_Cubscore = 14
        elif 65 <= Cubscore <= 66:
            standardized_Cubscore = 15
        elif Cubscore == 67:
            standardized_Cubscore = 16
        elif Cubscore == 68:
            standardized_Cubscore = 17
        else:
            standardized_Cubscore = 18

    if chrono_age == 16.5:
        if 0 <= Cubscore <= 26:
            standardized_Cubscore = 1
        elif 27 <= Cubscore <= 30:
            standardized_Cubscore = 2
        elif 31 <= Cubscore <= 34:
            standardized_Cubscore = 3
        elif 35 <= Cubscore <= 38:
            standardized_Cubscore = 4
        elif 39 <= Cubscore <= 40:
            standardized_Cubscore = 5
        elif 41 <= Cubscore <= 43:
            standardized_Cubscore = 6
        elif 44 <= Cubscore <= 47:
            standardized_Cubscore = 7
        elif 48 <= Cubscore <= 51:
            standardized_Cubscore = 8
        elif 52 <= Cubscore <= 54:
            standardized_Cubscore = 9
        elif 55 <= Cubscore <= 56:
            standardized_Cubscore = 10
        elif 57 <= Cubscore <= 59:
            standardized_Cubscore = 11
        elif 60 <= Cubscore <= 61:
            standardized_Cubscore = 12
        elif 62 <= Cubscore <= 63:
            standardized_Cubscore = 13
        elif Cubscore == 64:
            standardized_Cubscore = 14
        elif 65 <= Cubscore <= 66:
            standardized_Cubscore = 15
        elif Cubscore == 67:
            standardized_Cubscore = 16
        elif Cubscore == 68:
            standardized_Cubscore = 17
        else:
            standardized_Cubscore = 18
    standardized_scores.append(standardized_Cubscore)
    QIrealizacao.append(standardized_Cubscore)
    QIop.append(standardized_Cubscore)


def find_standardized_COscore():
    if chrono_age == 6:
        if 0 <= COscore <= 2:
            standardized_COscore = COscore + 1
        elif 3 <= COscore <= 4:
            standardized_COscore = 4
        elif 5 <= COscore <= 6:
            standardized_COscore = 5
        elif COscore == 7:
            standardized_COscore = 6
        elif 8 <= COscore <= 9:
            standardized_COscore = 7
        elif 10 <= COscore <= 11:
            standardized_COscore = 8
        elif 12 <= COscore <= 14:
            standardized_COscore = 9
        elif 15 <= COscore <= 16:
            standardized_COscore = 10
        elif 17 <= COscore <= 19:
            standardized_COscore = 11
        elif 20 <= COscore <= 22:
            standardized_COscore = 12
        elif 23 <= COscore <= 24:
            standardized_COscore = 13
        elif COscore == 25:
            standardized_COscore = 14
        elif 26 <= COscore <= 28:
            standardized_COscore = 15
        elif 29 <= COscore <= 30:
            standardized_COscore = 16
        elif COscore == 31:
            standardized_COscore = 17
        elif 32 <= COscore <= 33:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 6.5:
        if 0 <= COscore <= 2:
            standardized_COscore = COscore + 1
        elif 3 <= COscore <= 4:
            standardized_COscore = 4
        elif 5 <= COscore <= 6:
            standardized_COscore = 5
        elif 7 <= COscore <= 8:
            standardized_COscore = 6
        elif 9 <= COscore <= 10:
            standardized_COscore = 7
        elif 11 <= COscore <= 12:
            standardized_COscore = 8
        elif 13 <= COscore <= 15:
            standardized_COscore = 9
        elif 16 <= COscore <= 18:
            standardized_COscore = 10
        elif 19 <= COscore <= 21:
            standardized_COscore = 11
        elif 22 <= COscore <= 23:
            standardized_COscore = 12
        elif 24 <= COscore <= 25:
            standardized_COscore = 13
        elif 26 <= COscore <= 27:
            standardized_COscore = 14
        elif 28 <= COscore <= 29:
            standardized_COscore = 15
        elif COscore == 30:
            standardized_COscore = 16
        elif COscore == 31:
            standardized_COscore = 17
        elif 32 <= COscore <= 33:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 7:
        if 0 <= COscore <= 1:
            standardized_COscore = COscore + 1
        elif 2 <= COscore <= 3:
            standardized_COscore = 3
        elif 4 <= COscore <= 6:
            standardized_COscore = 4
        elif 7 <= COscore <= 8:
            standardized_COscore = 5
        elif 9 <= COscore <= 10:
            standardized_COscore = 6
        elif 11 <= COscore <= 12:
            standardized_COscore = 7
        elif 13 <= COscore <= 14:
            standardized_COscore = 8
        elif 15 <= COscore <= 17:
            standardized_COscore = 9
        elif 18 <= COscore <= 20:
            standardized_COscore = 10
        elif 21 <= COscore <= 22:
            standardized_COscore = 11
        elif 23 <= COscore <= 25:
            standardized_COscore = 12
        elif 26 <= COscore <= 27:
            standardized_COscore = 13
        elif COscore == 28:
            standardized_COscore = 14
        elif COscore == 29:
            standardized_COscore = 15
        elif COscore == 30:
            standardized_COscore = 16
        elif COscore == 31:
            standardized_COscore = 17
        elif 32 <= COscore <= 33:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 7.5:
        if 0 <= COscore <= 1:
            standardized_COscore = 1
        elif COscore == 2:
            standardized_COscore = 2
        elif 3 <= COscore <= 5:
            standardized_COscore = 3
        elif COscore == 6:
            standardized_COscore = 4
        elif 7 <= COscore <= 8:
            standardized_COscore = 5
        elif 9 <= COscore <= 10:
            standardized_COscore = 6
        elif 11 <= COscore <= 13:
            standardized_COscore = 7
        elif 14 <= COscore <= 16:
            standardized_COscore = 8
        elif 17 <= COscore <= 19:
            standardized_COscore = 9
        elif 20 <= COscore <= 21:
            standardized_COscore = 10
        elif 22 <= COscore <= 23:
            standardized_COscore = 11
        elif 24 <= COscore <= 26:
            standardized_COscore = 12
        elif 27 <= COscore <= 28:
            standardized_COscore = 13
        elif COscore == 29:
            standardized_COscore = 14
        elif 30 <= COscore <= 31:
            standardized_COscore = 15
        elif COscore == 32:
            standardized_COscore = 16
        elif 33 <= COscore <= 34:
            standardized_COscore = 17
        elif 35 <= COscore <= 36:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 8:
        if 0 <= COscore <= 2:
            standardized_COscore = 1
        elif 3 <= COscore <= 4:
            standardized_COscore = 2
        elif COscore == 5:
            standardized_COscore = 3
        elif 6 <= COscore <= 7:
            standardized_COscore = 4
        elif 8 <= COscore <= 9:
            standardized_COscore = 5
        elif 10 <= COscore <= 11:
            standardized_COscore = 6
        elif 12 <= COscore <= 14:
            standardized_COscore = 7
        elif 15 <= COscore <= 18:
            standardized_COscore = 8
        elif 19 <= COscore <= 20:
            standardized_COscore = 9
        elif 21 <= COscore <= 23:
            standardized_COscore = 10
        elif 24 <= COscore <= 25:
            standardized_COscore = 11
        elif 26 <= COscore <= 27:
            standardized_COscore = 12
        elif 28 <= COscore <= 29:
            standardized_COscore = 13
        elif COscore == 30:
            standardized_COscore = 14
        elif COscore == 31:
            standardized_COscore = 15
        elif 32 <= COscore <= 33:
            standardized_COscore = 16
        elif 34 <= COscore <= 35:
            standardized_COscore = 17
        elif 36 <= COscore <= 37:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 8.5:
        if 0 <= COscore <= 3:
            standardized_COscore = 1
        elif 4 <= COscore <= 5:
            standardized_COscore = 2
        elif COscore == 6:
            standardized_COscore = 3
        elif 7 <= COscore <= 8:
            standardized_COscore = 4
        elif 9 <= COscore <= 11:
            standardized_COscore = 5
        elif 12 <= COscore <= 13:
            standardized_COscore = 6
        elif 14 <= COscore <= 16:
            standardized_COscore = 7
        elif 17 <= COscore <= 20:
            standardized_COscore = 8
        elif 21 <= COscore <= 22:
            standardized_COscore = 9
        elif 23 <= COscore <= 24:
            standardized_COscore = 10
        elif 25 <= COscore <= 27:
            standardized_COscore = 11
        elif 28 <= COscore <= 29:
            standardized_COscore = 12
        elif COscore == 30:
            standardized_COscore = 13
        elif COscore == 31:
            standardized_COscore = 14
        elif COscore == 32:
            standardized_COscore = 15
        elif COscore == 33:
            standardized_COscore = 16
        elif 34 <= COscore <= 35:
            standardized_COscore = 17
        elif 36 <= COscore <= 37:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 9:
        if 0 <= COscore <= 5:
            standardized_COscore = 1
        elif 6 <= COscore <= 8:
            standardized_COscore = 2
        elif 9 <= COscore <= 10:
            standardized_COscore = 3
        elif 11 <= COscore <= 12:
            standardized_COscore = 4
        elif COscore == 13:
            standardized_COscore = 5
        elif 14 <= COscore <= 15:
            standardized_COscore = 6
        elif 16 <= COscore <= 19:
            standardized_COscore = 7
        elif 20 <= COscore <= 21:
            standardized_COscore = 8
        elif 22 <= COscore <= 23:
            standardized_COscore = 9
        elif 24 <= COscore <= 26:
            standardized_COscore = 10
        elif 27 <= COscore <= 28:
            standardized_COscore = 11
        elif 29 <= COscore <= 30:
            standardized_COscore = 12
        elif COscore == 31:
            standardized_COscore = 13
        elif COscore == 32:
            standardized_COscore = 14
        elif COscore == 33:
            standardized_COscore = 15
        elif COscore == 34:
            standardized_COscore = 16
        elif COscore == 35:
            standardized_COscore = 17
        elif 36 <= COscore <= 37:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 9.5:
        if 0 <= COscore <= 6:
            standardized_COscore = 1
        elif 7 <= COscore <= 9:
            standardized_COscore = 2
        elif 10 <= COscore <= 11:
            standardized_COscore = 3
        elif 12 <= COscore <= 13:
            standardized_COscore = 4
        elif 14 <= COscore <= 15:
            standardized_COscore = 5
        elif 16 <= COscore <= 18:
            standardized_COscore = 6
        elif 19 <= COscore <= 20:
            standardized_COscore = 7
        elif 21 <= COscore <= 22:
            standardized_COscore = 8
        elif 23 <= COscore <= 25:
            standardized_COscore = 9
        elif 26 <= COscore <= 28:
            standardized_COscore = 10
        elif COscore == 29:
            standardized_COscore = 11
        elif COscore == 30:
            standardized_COscore = 12
        elif 31 <= COscore <= 32:
            standardized_COscore = 13
        elif COscore == 33:
            standardized_COscore = 14
        elif 34 <= COscore <= 35:
            standardized_COscore = 15
        elif COscore == 36:
            standardized_COscore = 16
        elif COscore == 37:
            standardized_COscore = 17
        elif COscore == 38:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 10:
        if 0 <= COscore <= 8:
            standardized_COscore = 1
        elif 9 <= COscore <= 10:
            standardized_COscore = 2
        elif 11 <= COscore <= 13:
            standardized_COscore = 3
        elif 14 <= COscore <= 16:
            standardized_COscore = 4
        elif 17 <= COscore <= 18:
            standardized_COscore = 5
        elif 19 <= COscore <= 20:
            standardized_COscore = 6
        elif 21 <= COscore <= 22:
            standardized_COscore = 7
        elif 23 <= COscore <= 24:
            standardized_COscore = 8
        elif 25 <= COscore <= 27:
            standardized_COscore = 9
        elif 28 <= COscore <= 29:
            standardized_COscore = 10
        elif COscore == 30:
            standardized_COscore = 11
        elif COscore == 31:
            standardized_COscore = 12
        elif 32 <= COscore <= 33:
            standardized_COscore = 13
        elif COscore == 34:
            standardized_COscore = 14
        elif 35 <= COscore <= 36:
            standardized_COscore = 15
        elif COscore == 37:
            standardized_COscore = 16
        elif COscore == 38:
            standardized_COscore = 17
        elif COscore == 39:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 10.5:
        if 0 <= COscore <= 8:
            standardized_COscore = 1
        elif 9 <= COscore <= 10:
            standardized_COscore = 2
        elif 11 <= COscore <= 13:
            standardized_COscore = 3
        elif 14 <= COscore <= 16:
            standardized_COscore = 4
        elif 17 <= COscore <= 18:
            standardized_COscore = 5
        elif 19 <= COscore <= 21:
            standardized_COscore = 6
        elif COscore == 22:
            standardized_COscore = 7
        elif 23 <= COscore <= 24:
            standardized_COscore = 8
        elif 25 <= COscore <= 27:
            standardized_COscore = 9
        elif 28 <= COscore <= 29:
            standardized_COscore = 10
        elif COscore == 30:
            standardized_COscore = 11
        elif 31 <= COscore <= 32:
            standardized_COscore = 12
        elif COscore == 33:
            standardized_COscore = 13
        elif 34 <= COscore <= 35:
            standardized_COscore = 14
        elif 36 <= COscore <= 37:
            standardized_COscore = 15
        elif COscore == 38:
            standardized_COscore = 16
        elif COscore == 39:
            standardized_COscore = 17
        elif COscore == 40:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 11:
        if 0 <= COscore <= 8:
            standardized_COscore = 1
        elif 9 <= COscore <= 11:
            standardized_COscore = 2
        elif 12 <= COscore <= 13:
            standardized_COscore = 3
        elif 14 <= COscore <= 16:
            standardized_COscore = 4
        elif 17 <= COscore <= 18:
            standardized_COscore = 5
        elif 19 <= COscore <= 21:
            standardized_COscore = 6
        elif 22 <= COscore <= 23:
            standardized_COscore = 7
        elif 24 <= COscore <= 25:
            standardized_COscore = 8
        elif 26 <= COscore <= 27:
            standardized_COscore = 9
        elif 28 <= COscore <= 29:
            standardized_COscore = 10
        elif 30 <= COscore <= 31:
            standardized_COscore = 11
        elif COscore == 32:
            standardized_COscore = 12
        elif 33 <= COscore <= 34:
            standardized_COscore = 13
        elif COscore == 35:
            standardized_COscore = 14
        elif 36 <= COscore <= 37:
            standardized_COscore = 15
        elif COscore == 38:
            standardized_COscore = 16
        elif COscore == 39:
            standardized_COscore = 17
        elif 40 <= COscore <= 41:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 11.5:
        if 0 <= COscore <= 9:
            standardized_COscore = 1
        elif 10 <= COscore <= 13:
            standardized_COscore = 2
        elif 14 <= COscore <= 15:
            standardized_COscore = 3
        elif 16 <= COscore <= 17:
            standardized_COscore = 4
        elif 18 <= COscore <= 20:
            standardized_COscore = 5
        elif 21 <= COscore <= 22:
            standardized_COscore = 6
        elif 23 <= COscore <= 24:
            standardized_COscore = 7
        elif 25 <= COscore <= 26:
            standardized_COscore = 8
        elif 27 <= COscore <= 28:
            standardized_COscore = 9
        elif 29 <= COscore <= 30:
            standardized_COscore = 10
        elif COscore == 31:
            standardized_COscore = 11
        elif 32 <= COscore <= 33:
            standardized_COscore = 12
        elif 34 <= COscore <= 35:
            standardized_COscore = 13
        elif COscore == 36:
            standardized_COscore = 14
        elif 37 <= COscore <= 38:
            standardized_COscore = 15
        elif COscore == 39:
            standardized_COscore = 16
        elif COscore == 40:
            standardized_COscore = 17
        elif COscore == 41:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 12:
        if 0 <= COscore <= 9:
            standardized_COscore = 1
        elif 10 <= COscore <= 13:
            standardized_COscore = 2
        elif 14 <= COscore <= 16:
            standardized_COscore = 3
        elif 17 <= COscore <= 18:
            standardized_COscore = 4
        elif 19 <= COscore <= 21:
            standardized_COscore = 5
        elif 22 <= COscore <= 23:
            standardized_COscore = 6
        elif 24 <= COscore <= 25:
            standardized_COscore = 7
        elif 26 <= COscore <= 28:
            standardized_COscore = 8
        elif 29 <= COscore <= 30:
            standardized_COscore = 9
        elif 31 <= COscore <= 32:
            standardized_COscore = 10
        elif COscore == 33:
            standardized_COscore = 11
        elif COscore == 34:
            standardized_COscore = 12
        elif COscore == 35:
            standardized_COscore = 13
        elif COscore == 36:
            standardized_COscore = 14
        elif 37 <= COscore <= 38:
            standardized_COscore = 15
        elif COscore == 39:
            standardized_COscore = 16
        elif COscore == 40:
            standardized_COscore = 17
        elif COscore == 41:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 12.5:
        if 0 <= COscore <= 11:
            standardized_COscore = 1
        elif 12 <= COscore <= 14:
            standardized_COscore = 2
        elif 15 <= COscore <= 17:
            standardized_COscore = 3
        elif 18 <= COscore <= 19:
            standardized_COscore = 4
        elif 20 <= COscore <= 22:
            standardized_COscore = 5
        elif 23 <= COscore <= 24:
            standardized_COscore = 6
        elif 25 <= COscore <= 26:
            standardized_COscore = 7
        elif 27 <= COscore <= 28:
            standardized_COscore = 8
        elif 29 <= COscore <= 30:
            standardized_COscore = 9
        elif 31 <= COscore <= 32:
            standardized_COscore = 10
        elif COscore == 33:
            standardized_COscore = 11
        elif 34 <= COscore <= 35:
            standardized_COscore = 12
        elif COscore == 36:
            standardized_COscore = 13
        elif COscore == 37:
            standardized_COscore = 14
        elif 38 <= COscore <= 39:
            standardized_COscore = 15
        elif COscore == 40:
            standardized_COscore = 16
        elif COscore == 41:
            standardized_COscore = 17
        elif COscore == 42:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 13:
        if 0 <= COscore <= 13:
            standardized_COscore = 1
        elif 14 <= COscore <= 16:
            standardized_COscore = 2
        elif 17 <= COscore <= 18:
            standardized_COscore = 3
        elif 19 <= COscore <= 20:
            standardized_COscore = 4
        elif 21 <= COscore <= 22:
            standardized_COscore = 5
        elif 23 <= COscore <= 24:
            standardized_COscore = 6
        elif 25 <= COscore <= 26:
            standardized_COscore = 7
        elif 27 <= COscore <= 28:
            standardized_COscore = 8
        elif 29 <= COscore <= 31:
            standardized_COscore = 9
        elif 32 <= COscore <= 33:
            standardized_COscore = 10
        elif COscore == 34:
            standardized_COscore = 11
        elif COscore == 35:
            standardized_COscore = 12
        elif COscore == 36:
            standardized_COscore = 13
        elif 37 <= COscore <= 38:
            standardized_COscore = 14
        elif COscore == 39:
            standardized_COscore = 15
        elif COscore == 40:
            standardized_COscore = 16
        elif 41 <= COscore <= 42:
            standardized_COscore = 17
        elif COscore == 43:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 13.5:
        if 0 <= COscore <= 14:
            standardized_COscore = 1
        elif 15 <= COscore <= 16:
            standardized_COscore = 2
        elif 17 <= COscore <= 18:
            standardized_COscore = 3
        elif 19 <= COscore <= 21:
            standardized_COscore = 4
        elif 22 <= COscore <= 23:
            standardized_COscore = 5
        elif 24 <= COscore <= 25:
            standardized_COscore = 6
        elif 26 <= COscore <= 27:
            standardized_COscore = 7
        elif 28 <= COscore <= 29:
            standardized_COscore = 8
        elif 30 <= COscore <= 31:
            standardized_COscore = 9
        elif 32 <= COscore <= 33:
            standardized_COscore = 10
        elif COscore == 34:
            standardized_COscore = 11
        elif COscore == 35:
            standardized_COscore = 12
        elif 36 <= COscore <= 37:
            standardized_COscore = 13
        elif COscore == 38:
            standardized_COscore = 14
        elif COscore == 39:
            standardized_COscore = 15
        elif COscore == 40:
            standardized_COscore = 16
        elif 41 <= COscore <= 42:
            standardized_COscore = 17
        elif COscore == 43:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 14:
        if 0 <= COscore <= 15:
            standardized_COscore = 1
        elif 16 <= COscore <= 18:
            standardized_COscore = 2
        elif 19 <= COscore <= 20:
            standardized_COscore = 3
        elif 21 <= COscore <= 22:
            standardized_COscore = 4
        elif 23 <= COscore <= 25:
            standardized_COscore = 5
        elif COscore == 26:
            standardized_COscore = 6
        elif 27 <= COscore <= 28:
            standardized_COscore = 7
        elif COscore == 29:
            standardized_COscore = 8
        elif 30 <= COscore <= 31:
            standardized_COscore = 9
        elif 32 <= COscore <= 33:
            standardized_COscore = 10
        elif 34 <= COscore <= 35:
            standardized_COscore = 11
        elif COscore == 36:
            standardized_COscore = 12
        elif COscore == 37:
            standardized_COscore = 13
        elif COscore == 38:
            standardized_COscore = 14
        elif 39 <= COscore <= 40:
            standardized_COscore = 15
        elif COscore == 41:
            standardized_COscore = 16
        elif COscore == 42:
            standardized_COscore = 17
        elif COscore == 43:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 14.5:
        if 0 <= COscore <= 16:
            standardized_COscore = 1
        elif 17 <= COscore <= 18:
            standardized_COscore = 2
        elif 19 <= COscore <= 20:
            standardized_COscore = 3
        elif 21 <= COscore <= 22:
            standardized_COscore = 4
        elif 23 <= COscore <= 25:
            standardized_COscore = 5
        elif COscore == 26:
            standardized_COscore = 6
        elif 27 <= COscore <= 28:
            standardized_COscore = 7
        elif COscore == 29:
            standardized_COscore = 8
        elif 30 <= COscore <= 31:
            standardized_COscore = 9
        elif 32 <= COscore <= 33:
            standardized_COscore = 10
        elif 34 <= COscore <= 35:
            standardized_COscore = 11
        elif COscore == 36:
            standardized_COscore = 12
        elif COscore == 37:
            standardized_COscore = 13
        elif COscore == 38:
            standardized_COscore = 14
        elif 39 <= COscore <= 40:
            standardized_COscore = 15
        elif COscore == 41:
            standardized_COscore = 16
        elif COscore == 42:
            standardized_COscore = 17
        elif COscore == 43:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 15:
        if 0 <= COscore <= 16:
            standardized_COscore = 1
        elif 17 <= COscore <= 18:
            standardized_COscore = 2
        elif 19 <= COscore <= 20:
            standardized_COscore = 3
        elif 21 <= COscore <= 22:
            standardized_COscore = 4
        elif 23 <= COscore <= 25:
            standardized_COscore = 5
        elif 26 <= COscore <= 27:
            standardized_COscore = 6
        elif COscore == 28:
            standardized_COscore = 7
        elif 29 <= COscore <= 30:
            standardized_COscore = 8
        elif 31 <= COscore <= 32:
            standardized_COscore = 9
        elif COscore == 33:
            standardized_COscore = 10
        elif 34 <= COscore <= 35:
            standardized_COscore = 11
        elif COscore == 36:
            standardized_COscore = 12
        elif COscore == 37:
            standardized_COscore = 13
        elif 38 <= COscore <= 39:
            standardized_COscore = 14
        elif COscore == 40:
            standardized_COscore = 15
        elif COscore == 41:
            standardized_COscore = 16
        elif COscore == 42:
            standardized_COscore = 17
        elif COscore == 43:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 15.5:
        if 0 <= COscore <= 17:
            standardized_COscore = 1
        elif 18 <= COscore <= 19:
            standardized_COscore = 2
        elif 20 <= COscore <= 21:
            standardized_COscore = 3
        elif COscore == 22:
            standardized_COscore = 4
        elif 23 <= COscore <= 25:
            standardized_COscore = 5
        elif 26 <= COscore <= 27:
            standardized_COscore = 6
        elif COscore == 28:
            standardized_COscore = 7
        elif 29 <= COscore <= 30:
            standardized_COscore = 8
        elif 31 <= COscore <= 32:
            standardized_COscore = 9
        elif COscore == 33:
            standardized_COscore = 10
        elif 34 <= COscore <= 35:
            standardized_COscore = 11
        elif COscore == 36:
            standardized_COscore = 12
        elif COscore == 37:
            standardized_COscore = 13
        elif 38 <= COscore <= 39:
            standardized_COscore = 14
        elif COscore == 40:
            standardized_COscore = 15
        elif COscore == 41:
            standardized_COscore = 16
        elif COscore == 42:
            standardized_COscore = 17
        elif COscore == 43:
            standardized_COscore = 18
        else:
            standardized_COscore = 19

    if chrono_age == 16:
        if 0 <= COscore <= 17:
            standardized_COscore = 1
        elif 18 <= COscore <= 19:
            standardized_COscore = 2
        elif 20 <= COscore <= 21:
            standardized_COscore = 3
        elif 22 <= COscore <= 23:
            standardized_COscore = 4
        elif 24 <= COscore <= 25:
            standardized_COscore = 5
        elif 26 <= COscore <= 27:
            standardized_COscore = 6
        elif 28 <= COscore <= 29:
            standardized_COscore = 7
        elif 30 <= COscore <= 31:
            standardized_COscore = 8
        elif COscore == 32:
            standardized_COscore = 9
        elif 33 <= COscore <= 34:
            standardized_COscore = 10
        elif COscore == 35:
            standardized_COscore = 11
        elif COscore == 36:
            standardized_COscore = 12
        elif 37 <= COscore <= 38:
            standardized_COscore = 13
        elif COscore == 39:
            standardized_COscore = 14
        elif 40 <= COscore <= 41:
            standardized_COscore = 15
        elif COscore == 42:
            standardized_COscore = 16
        elif COscore == 43:
            standardized_COscore = 17
        else:
            standardized_COscore = 18

    if chrono_age == 16.5:
        if 0 <= COscore <= 18:
            standardized_COscore = 1
        elif 19 <= COscore <= 20:
            standardized_COscore = 2
        elif 21 <= COscore <= 22:
            standardized_COscore = 3
        elif 23 <= COscore <= 24:
            standardized_COscore = 4
        elif 25 <= COscore <= 26:
            standardized_COscore = 5
        elif COscore == 27:
            standardized_COscore = 6
        elif 28 <= COscore <= 29:
            standardized_COscore = 7
        elif 30 <= COscore <= 31:
            standardized_COscore = 8
        elif COscore == 32:
            standardized_COscore = 9
        elif 33 <= COscore <= 34:
            standardized_COscore = 10
        elif COscore == 35:
            standardized_COscore = 11
        elif COscore == 36:
            standardized_COscore = 12
        elif 37 <= COscore <= 38:
            standardized_COscore = 13
        elif COscore == 39:
            standardized_COscore = 14
        elif 40 <= COscore <= 41:
            standardized_COscore = 15
        elif COscore == 42:
            standardized_COscore = 16
        elif COscore == 43:
            standardized_COscore = 17
        else:
            standardized_COscore = 18
    standardized_scores.append(standardized_COscore)
    QIrealizacao.append(standardized_COscore)
    QIop.append(standardized_COscore)


def find_standardized_PSscore():
    if chrono_age == 6:
        if PSscore == 0:
            standardized_PSscore = PSscore + 4
        elif 1 <= PSscore <= 2:
            standardized_PSscore = 5
        elif 3 <= PSscore <= 4:
            standardized_PSscore = 6
        elif 5 <= PSscore <= 7:
            standardized_PSscore = 7
        elif 8 <= PSscore <= 11:
            standardized_PSscore = 8
        elif 12 <= PSscore <= 13:
            standardized_PSscore = 9
        elif 13 <= PSscore <= 15:
            standardized_PSscore = 10
        elif 16 <= PSscore <= 17:
            standardized_PSscore = 11
        elif 18 <= PSscore <= 20:
            standardized_PSscore = 12
        elif 21 <= PSscore <= 22:
            standardized_PSscore = 13
        elif 23 <= PSscore <= 25:
            standardized_PSscore = 14
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 15
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 16
        elif 30 <= PSscore <= 32:
            standardized_PSscore = 17
        elif 33 <= PSscore <= 34:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 6.5:
        if PSscore == 0:
            standardized_PSscore = PSscore + 3
        elif 1 <= PSscore <= 2:
            standardized_PSscore = 4
        elif 3 <= PSscore <= 4:
            standardized_PSscore = 5
        elif 5 <= PSscore <= 7:
            standardized_PSscore = 6
        elif 8 <= PSscore <= 10:
            standardized_PSscore = 7
        elif 11 <= PSscore <= 13:
            standardized_PSscore = 8
        elif 14 <= PSscore <= 16:
            standardized_PSscore = 9
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 10
        elif 19 <= PSscore <= 20:
            standardized_PSscore = 11
        elif 21 <= PSscore <= 24:
            standardized_PSscore = 12
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 13
        elif 27 <= PSscore <= 28:
            standardized_PSscore = 14
        elif 29 <= PSscore <= 30:
            standardized_PSscore = 15
        elif 31 <= PSscore <= 32:
            standardized_PSscore = 16
        elif 33 <= PSscore <= 35:
            standardized_PSscore = 17
        elif 36 <= PSscore <= 39:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 7:
        if PSscore == 0:
            standardized_PSscore = 1
        elif 1 <= PSscore <= 3:
            standardized_PSscore = 2
        elif 4 <= PSscore <= 6:
            standardized_PSscore = 2
        elif 7 <= PSscore <= 10:
            standardized_PSscore = 3
        elif 11 <= PSscore <= 12:
            standardized_PSscore = 5
        elif PSscore == 13:
            standardized_PSscore = 6
        elif 14 <= PSscore <= 15:
            standardized_PSscore = 7
        elif 16 <= PSscore <= 17:
            standardized_PSscore = 8
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 9
        elif 20 <= PSscore <= 22:
            standardized_PSscore = 10
        elif 23 <= PSscore <= 24:
            standardized_PSscore = 11
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 12
        elif 27 <= PSscore <= 28:
            standardized_PSscore = 13
        elif PSscore == 29:
            standardized_PSscore = 14
        elif 30 <= PSscore <= 31:
            standardized_PSscore = 15
        elif 32 <= PSscore <= 35:
            standardized_PSscore = 16
        elif 36 <= PSscore <= 39:
            standardized_PSscore = 17
        elif 40 <= PSscore <= 42:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 7.5:
        if 0 <= PSscore <= 2:
            standardized_PSscore = 1
        elif 3 <= PSscore <= 4:
            standardized_PSscore = 2
        elif 5 <= PSscore <= 7:
            standardized_PSscore = 2
        elif 8 <= PSscore <= 10:
            standardized_PSscore = 3
        elif 11 <= PSscore <= 12:
            standardized_PSscore = 5
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 6
        elif PSscore == 15:
            standardized_PSscore = 7
        elif 16 <= PSscore <= 17:
            standardized_PSscore = 8
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 9
        elif 20 <= PSscore <= 23:
            standardized_PSscore = 10
        elif PSscore == 24:
            standardized_PSscore = 11
        elif 25 <= PSscore <= 27:
            standardized_PSscore = 12
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 13
        elif PSscore == 30:
            standardized_PSscore = 14
        elif 31 <= PSscore <= 32:
            standardized_PSscore = 15
        elif 33 <= PSscore <= 36:
            standardized_PSscore = 16
        elif 37 <= PSscore <= 39:
            standardized_PSscore = 17
        elif 40 <= PSscore <= 43:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 8:
        if 0 <= PSscore <= 2:
            standardized_PSscore = PSscore + 1
        elif 3 <= PSscore <= 4:
            standardized_PSscore = 4
        elif 5 <= PSscore <= 6:
            standardized_PSscore = 5
        elif 7 <= PSscore <= 8:
            standardized_PSscore = 6
        elif 9 <= PSscore <= 10:
            standardized_PSscore = 7
        elif 11 <= PSscore <= 12:
            standardized_PSscore = 8
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 9
        elif 15 <= PSscore <= 16:
            standardized_PSscore = 10
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 11
        elif PSscore == 19:
            standardized_PSscore = 12
        elif PSscore == 20:
            standardized_PSscore = 13
        elif 21 <= PSscore <= 22:
            standardized_PSscore = 14
        elif 23 <= PSscore <= 24:
            standardized_PSscore = 15
        elif PSscore == 25:
            standardized_PSscore = 16
        elif PSscore == 26:
            standardized_PSscore = 17
        elif PSscore == 27:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 8.5:
        if PSscore == 0:
            standardized_PSscore = 1
        elif 1 <= PSscore <= 2:
            standardized_PSscore = 2
        elif PSscore == 3:
            standardized_PSscore = 3
        elif 4 <= PSscore <= 5:
            standardized_PSscore = 4
        elif 6 <= PSscore <= 8:
            standardized_PSscore = 5
        elif 9 <= PSscore <= 10:
            standardized_PSscore = 6
        elif 11 <= PSscore <= 12:
            standardized_PSscore = 7
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 8
        elif PSscore == 15:
            standardized_PSscore = 9
        elif 16 <= PSscore <= 18:
            standardized_PSscore = 10
        elif PSscore == 19:
            standardized_PSscore = 11
        elif PSscore == 20:
            standardized_PSscore = 12
        elif 21 <= PSscore <= 22:
            standardized_PSscore = 13
        elif PSscore == 23:
            standardized_PSscore = 14
        elif 24 <= PSscore <= 25:
            standardized_PSscore = 15
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 16
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 17
        elif PSscore == 30:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 9:
        if 0 <= PSscore <= 4:
            standardized_PSscore = 1
        elif 5 <= PSscore <= 6:
            standardized_PSscore = 2
        elif 7 <= PSscore <= 8:
            standardized_PSscore = 3
        elif PSscore == 9:
            standardized_PSscore = 4
        elif 10 <= PSscore <= 11:
            standardized_PSscore = 5
        elif PSscore == 12:
            standardized_PSscore = 6
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 7
        elif 15 <= PSscore <= 16:
            standardized_PSscore = 8
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 9
        elif PSscore == 19:
            standardized_PSscore = 10
        elif PSscore == 20:
            standardized_PSscore = 11
        elif PSscore == 21:
            standardized_PSscore = 12
        elif PSscore == 22:
            standardized_PSscore = 13
        elif 23 <= PSscore <= 24:
            standardized_PSscore = 14
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 15
        elif 27 <= PSscore <= 28:
            standardized_PSscore = 16
        elif PSscore == 29:
            standardized_PSscore = 17
        elif PSscore == 30:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 9.5:
        if 0 <= PSscore <= 5:
            standardized_PSscore = 1
        elif 6 <= PSscore <= 7:
            standardized_PSscore = 2
        elif PSscore == 8:
            standardized_PSscore = 3
        elif PSscore == 9:
            standardized_PSscore = 4
        elif 10 <= PSscore <= 11:
            standardized_PSscore = 5
        elif 12 <= PSscore <= 13:
            standardized_PSscore = 6
        elif 14 <= PSscore <= 15:
            standardized_PSscore = 7
        elif 16 <= PSscore <= 17:
            standardized_PSscore = 8
        elif PSscore == 18:
            standardized_PSscore = 9
        elif PSscore == 19:
            standardized_PSscore = 10
        elif 20 <= PSscore <= 21:
            standardized_PSscore = 11
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 12
        elif PSscore == 24:
            standardized_PSscore = 13
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 14
        elif 27 <= PSscore <= 28:
            standardized_PSscore = 15
        elif PSscore == 29:
            standardized_PSscore = 16
        elif PSscore == 30:
            standardized_PSscore = 17
        elif PSscore == 31:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 10:
        if 0 <= PSscore <= 7:
            standardized_PSscore = 1
        elif PSscore == 8:
            standardized_PSscore = 2
        elif PSscore == 9:
            standardized_PSscore = 3
        elif PSscore == 10:
            standardized_PSscore = 4
        elif 11 <= PSscore <= 12:
            standardized_PSscore = 5
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 6
        elif 15 <= PSscore <= 16:
            standardized_PSscore = 7
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 8
        elif 19 <= PSscore <= 20:
            standardized_PSscore = 9
        elif PSscore == 21:
            standardized_PSscore = 10
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 11
        elif PSscore == 24:
            standardized_PSscore = 12
        elif PSscore == 25:
            standardized_PSscore = 13
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 14
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 15
        elif PSscore == 30:
            standardized_PSscore = 16
        elif PSscore == 31:
            standardized_PSscore = 17
        elif PSscore == 32:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 10.5:
        if 0 <= PSscore <= 7:
            standardized_PSscore = 1
        elif 8 <= PSscore <= 9:
            standardized_PSscore = 2
        elif PSscore == 10:
            standardized_PSscore = 3
        elif 11 <= PSscore <= 12:
            standardized_PSscore = 4
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 5
        elif 15 <= PSscore <= 16:
            standardized_PSscore = 6
        elif PSscore == 17:
            standardized_PSscore = 7
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 8
        elif PSscore == 20:
            standardized_PSscore = 9
        elif 21 <= PSscore <= 23:
            standardized_PSscore = 10
        elif PSscore == 24:
            standardized_PSscore = 11
        elif PSscore == 25:
            standardized_PSscore = 12
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 13
        elif PSscore == 28:
            standardized_PSscore = 14
        elif 29 <= PSscore <= 30:
            standardized_PSscore = 15
        elif PSscore == 31:
            standardized_PSscore = 16
        elif PSscore == 32:
            standardized_PSscore = 17
        elif PSscore == 33:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 11:
        if 0 <= PSscore <= 8:
            standardized_PSscore = 1
        elif 9 <= PSscore <= 10:
            standardized_PSscore = 2
        elif 11 <= PSscore <= 12:
            standardized_PSscore = 3
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 4
        elif 15 <= PSscore <= 16:
            standardized_PSscore = 5
        elif PSscore == 17:
            standardized_PSscore = 6
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 7
        elif 20 <= PSscore <= 21:
            standardized_PSscore = 8
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 9
        elif PSscore == 24:
            standardized_PSscore = 10
        elif PSscore == 25:
            standardized_PSscore = 11
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 12
        elif PSscore == 28:
            standardized_PSscore = 13
        elif PSscore == 29:
            standardized_PSscore = 14
        elif 30 <= PSscore <= 31:
            standardized_PSscore = 15
        elif PSscore == 32:
            standardized_PSscore = 16
        elif PSscore == 33:
            standardized_PSscore = 17
        elif PSscore == 34:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 11.5:
        if 0 <= PSscore <= 8:
            standardized_PSscore = 1
        elif 9 <= PSscore <= 10:
            standardized_PSscore = 2
        elif 11 <= PSscore <= 12:
            standardized_PSscore = 3
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 4
        elif 15 <= PSscore <= 16:
            standardized_PSscore = 5
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 6
        elif PSscore == 19:
            standardized_PSscore = 7
        elif 20 <= PSscore <= 21:
            standardized_PSscore = 8
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 9
        elif PSscore == 24:
            standardized_PSscore = 10
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 11
        elif PSscore == 27:
            standardized_PSscore = 12
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 13
        elif 30 <= PSscore <= 31:
            standardized_PSscore = 14
        elif PSscore == 32:
            standardized_PSscore = 15
        elif PSscore == 33:
            standardized_PSscore = 16
        elif 34 <= PSscore <= 35:
            standardized_PSscore = 17
        elif 36 <= PSscore <= 37:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 12:
        if 0 <= PSscore <= 9:
            standardized_PSscore = 1
        elif 10 <= PSscore <= 11:
            standardized_PSscore = 2
        elif 12 <= PSscore <= 13:
            standardized_PSscore = 3
        elif 14 <= PSscore <= 15:
            standardized_PSscore = 4
        elif 16 <= PSscore <= 17:
            standardized_PSscore = 5
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 6
        elif PSscore == 20:
            standardized_PSscore = 7
        elif 21 <= PSscore <= 21:
            standardized_PSscore = 8
        elif PSscore == 23:
            standardized_PSscore = 9
        elif 24 <= PSscore <= 25:
            standardized_PSscore = 10
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 11
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 12
        elif PSscore == 30:
            standardized_PSscore = 13
        elif 31 <= PSscore <= 32:
            standardized_PSscore = 14
        elif PSscore == 33:
            standardized_PSscore = 15
        elif 34 <= PSscore <= 35:
            standardized_PSscore = 16
        elif 36 <= PSscore <= 37:
            standardized_PSscore = 17
        elif PSscore == 38:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 12.5:
        if 0 <= PSscore <= 9:
            standardized_PSscore = 1
        elif 10 <= PSscore <= 11:
            standardized_PSscore = 2
        elif 12 <= PSscore <= 13:
            standardized_PSscore = 3
        elif 14 <= PSscore <= 15:
            standardized_PSscore = 4
        elif 16 <= PSscore <= 17:
            standardized_PSscore = 5
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 6
        elif 20 <= PSscore <= 21:
            standardized_PSscore = 7
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 8
        elif PSscore == 24:
            standardized_PSscore = 9
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 10
        elif 27 <= PSscore <= 28:
            standardized_PSscore = 11
        elif 29 <= PSscore <= 30:
            standardized_PSscore = 12
        elif 31 <= PSscore <= 32:
            standardized_PSscore = 13
        elif PSscore == 33:
            standardized_PSscore = 14
        elif 34 <= PSscore <= 35:
            standardized_PSscore = 15
        elif PSscore == 36:
            standardized_PSscore = 16
        elif 37 <= PSscore <= 38:
            standardized_PSscore = 17
        elif PSscore == 39:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 13:
        if 0 <= PSscore <= 11:
            standardized_PSscore = 1
        elif 12 <= PSscore <= 13:
            standardized_PSscore = 2
        elif PSscore == 14:
            standardized_PSscore = 3
        elif 15 <= PSscore <= 16:
            standardized_PSscore = 4
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 5
        elif 19 <= PSscore <= 20:
            standardized_PSscore = 6
        elif 21 <= PSscore <= 22:
            standardized_PSscore = 7
        elif 23 <= PSscore <= 24:
            standardized_PSscore = 8
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 9
        elif 27 <= PSscore <= 28:
            standardized_PSscore = 10
        elif 29 <= PSscore <= 30:
            standardized_PSscore = 11
        elif PSscore == 31:
            standardized_PSscore = 12
        elif 32 <= PSscore <= 33:
            standardized_PSscore = 13
        elif PSscore == 34:
            standardized_PSscore = 14
        elif PSscore == 35:
            standardized_PSscore = 15
        elif 36 <= PSscore <= 37:
            standardized_PSscore = 16
        elif 38 <= PSscore <= 39:
            standardized_PSscore = 17
        elif PSscore == 40:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 13.5:
        if 0 <= PSscore <= 12:
            standardized_PSscore = 1
        elif 13 <= PSscore <= 14:
            standardized_PSscore = 2
        elif PSscore == 15:
            standardized_PSscore = 3
        elif 16 <= PSscore <= 17:
            standardized_PSscore = 4
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 5
        elif 20 <= PSscore <= 21:
            standardized_PSscore = 6
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 7
        elif 24 <= PSscore <= 25:
            standardized_PSscore = 8
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 9
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 10
        elif 30 <= PSscore <= 31:
            standardized_PSscore = 11
        elif PSscore == 32:
            standardized_PSscore = 12
        elif 33 <= PSscore <= 34:
            standardized_PSscore = 13
        elif PSscore == 35:
            standardized_PSscore = 14
        elif 36 <= PSscore <= 37:
            standardized_PSscore = 15
        elif PSscore == 38:
            standardized_PSscore = 16
        elif PSscore == 39:
            standardized_PSscore = 17
        elif PSscore == 40:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 14:
        if 0 <= PSscore <= 13:
            standardized_PSscore = 1
        elif 14 <= PSscore <= 15:
            standardized_PSscore = 2
        elif 16 <= PSscore <= 17:
            standardized_PSscore = 3
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 4
        elif 20 <= PSscore <= 21:
            standardized_PSscore = 5
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 6
        elif 24 <= PSscore <= 25:
            standardized_PSscore = 7
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 8
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 9
        elif PSscore == 30:
            standardized_PSscore = 10
        elif PSscore == 31:
            standardized_PSscore = 11
        elif 32 <= PSscore <= 32:
            standardized_PSscore = 12
        elif PSscore == 34:
            standardized_PSscore = 13
        elif 35 <= PSscore <= 36:
            standardized_PSscore = 14
        elif 37 <= PSscore <= 38:
            standardized_PSscore = 15
        elif PSscore == 39:
            standardized_PSscore = 16
        elif PSscore == 40:
            standardized_PSscore = 17
        elif PSscore == 41:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 14.5:
        if 0 <= PSscore <= 14:
            standardized_PSscore = 1
        elif 15 <= PSscore <= 17:
            standardized_PSscore = 2
        elif PSscore == 18:
            standardized_PSscore = 3
        elif 19 <= PSscore <= 20:
            standardized_PSscore = 4
        elif 21 <= PSscore <= 22:
            standardized_PSscore = 5
        elif PSscore == 23:
            standardized_PSscore = 6
        elif 24 <= PSscore <= 25:
            standardized_PSscore = 7
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 8
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 9
        elif PSscore == 30:
            standardized_PSscore = 10
        elif 31 <= PSscore <= 32:
            standardized_PSscore = 11
        elif PSscore == 33:
            standardized_PSscore = 12
        elif 34 <= PSscore <= 35:
            standardized_PSscore = 13
        elif PSscore == 36:
            standardized_PSscore = 14
        elif 37 <= PSscore <= 38:
            standardized_PSscore = 15
        elif PSscore == 39:
            standardized_PSscore = 16
        elif PSscore == 40:
            standardized_PSscore = 17
        elif PSscore == 41:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 15:
        if 0 <= PSscore <= 16:
            standardized_PSscore = 1
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 2
        elif 19 <= PSscore <= 20:
            standardized_PSscore = 3
        elif PSscore == 21:
            standardized_PSscore = 4
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 5
        elif PSscore == 24:
            standardized_PSscore = 6
        elif PSscore == 25:
            standardized_PSscore = 7
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 8
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 9
        elif PSscore == 30:
            standardized_PSscore = 10
        elif 31 <= PSscore <= 32:
            standardized_PSscore = 11
        elif PSscore == 33:
            standardized_PSscore = 12
        elif 34 <= PSscore <= 35:
            standardized_PSscore = 13
        elif PSscore == 36:
            standardized_PSscore = 14
        elif 37 <= PSscore <= 38:
            standardized_PSscore = 15
        elif PSscore == 39:
            standardized_PSscore = 16
        elif PSscore == 40:
            standardized_PSscore = 17
        elif PSscore == 41:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 15.5:
        if 0 <= PSscore <= 16:
            standardized_PSscore = 1
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 2
        elif 19 <= PSscore <= 20:
            standardized_PSscore = 3
        elif PSscore == 21:
            standardized_PSscore = 4
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 5
        elif PSscore == 24:
            standardized_PSscore = 6
        elif PSscore == 25:
            standardized_PSscore = 7
        elif 26 <= PSscore <= 27:
            standardized_PSscore = 8
        elif 28 <= PSscore <= 29:
            standardized_PSscore = 9
        elif 30 <= PSscore <= 31:
            standardized_PSscore = 10
        elif PSscore == 32:
            standardized_PSscore = 11
        elif 33 <= PSscore <= 34:
            standardized_PSscore = 12
        elif 35 <= PSscore <= 36:
            standardized_PSscore = 13
        elif 37 <= PSscore <= 38:
            standardized_PSscore = 14
        elif PSscore == 39:
            standardized_PSscore = 15
        elif 40 <= PSscore <= 41:
            standardized_PSscore = 16
        elif PSscore == 42:
            standardized_PSscore = 17
        elif PSscore == 43:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 16:
        if 0 <= PSscore <= 16:
            standardized_PSscore = 1
        elif 17 <= PSscore <= 18:
            standardized_PSscore = 2
        elif 19 <= PSscore <= 20:
            standardized_PSscore = 3
        elif PSscore == 21:
            standardized_PSscore = 4
        elif 22 <= PSscore <= 23:
            standardized_PSscore = 5
        elif PSscore == 24:
            standardized_PSscore = 6
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 7
        elif 27 <= PSscore <= 29:
            standardized_PSscore = 8
        elif 30 <= PSscore <= 31:
            standardized_PSscore = 9
        elif PSscore == 32:
            standardized_PSscore = 10
        elif 33 <= PSscore <= 34:
            standardized_PSscore = 11
        elif 35 <= PSscore <= 36:
            standardized_PSscore = 12
        elif PSscore == 37:
            standardized_PSscore = 13
        elif 38 <= PSscore <= 39:
            standardized_PSscore = 14
        elif PSscore == 40:
            standardized_PSscore = 15
        elif PSscore == 41:
            standardized_PSscore = 16
        elif PSscore == 42:
            standardized_PSscore = 17
        elif PSscore == 43:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    if chrono_age == 16.5:
        if 0 <= PSscore <= 17:
            standardized_PSscore = 1
        elif 18 <= PSscore <= 19:
            standardized_PSscore = 2
        elif PSscore == 20:
            standardized_PSscore = 3
        elif 21 <= PSscore <= 22:
            standardized_PSscore = 4
        elif PSscore == 23:
            standardized_PSscore = 5
        elif PSscore == 24:
            standardized_PSscore = 6
        elif 25 <= PSscore <= 26:
            standardized_PSscore = 7
        elif 27 <= PSscore <= 29:
            standardized_PSscore = 8
        elif 30 <= PSscore <= 31:
            standardized_PSscore = 9
        elif PSscore == 32:
            standardized_PSscore = 10
        elif 33 <= PSscore <= 34:
            standardized_PSscore = 11
        elif 35 <= PSscore <= 36:
            standardized_PSscore = 12
        elif 37 <= PSscore <= 38:
            standardized_PSscore = 13
        elif PSscore == 39:
            standardized_PSscore = 14
        elif PSscore == 40:
            standardized_PSscore = 15
        elif 41 <= PSscore <= 42:
            standardized_PSscore = 16
        elif PSscore == 43:
            standardized_PSscore = 17
        elif PSscore == 44:
            standardized_PSscore = 18
        else:
            standardized_PSscore = 19

    standardized_scores.append(standardized_PSscore)
    QIvp.append(standardized_PSscore)


def find_standardized_Labscore():
    if chrono_age == 6:
        if 0 <= Labscore <= 2:
            standardized_Labscore = Labscore + 1
        elif 3 <= Labscore <= 4:
            standardized_Labscore = 4
        elif 5 <= Labscore <= 8:
            standardized_Labscore = Labscore
        elif 9 <= Labscore <= 10:
            standardized_Labscore = 9
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 10
        elif 13 <= Labscore <= 14:
            standardized_Labscore = Labscore + 1
        elif 15 <= Labscore <= 16:
            standardized_Labscore = 13
        elif 17 <= Labscore <= 18:
            standardized_Labscore = 14
        elif 19 <= Labscore <= 22:
            standardized_Labscore = Labscore - 4
        else:
            standardized_Labscore = 19

    if chrono_age == 6.5:
        if 0 <= Labscore <= 1:
            standardized_Labscore = 1
        elif Labscore == 2:
            standardized_Labscore = 2
        elif 3 <= Labscore <= 4:
            standardized_Labscore = 3
        elif 5 <= Labscore <= 10:
            standardized_Labscore = Labscore - 1
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 10
        elif Labscore == 13:
            standardized_Labscore = 11
        elif 14 <= Labscore <= 15:
            standardized_Labscore = 12
        elif 16 <= Labscore <= 17:
            standardized_Labscore = 13
        elif 18 <= Labscore <= 19:
            standardized_Labscore = 14
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 15
        elif 22 <= Labscore <= 24:
            standardized_Labscore = Labscore - 6
        else:
            standardized_Labscore = 19

    if chrono_age == 7:
        if 0 <= Labscore <= 3:
            standardized_Labscore = 1
        elif 4 <= Labscore <= 6:
            standardized_Labscore = Labscore - 2
        elif Labscore == 7:
            standardized_Labscore = Labscore - 1
        elif 8 <= Labscore <= 9:
            standardized_Labscore = 7
        elif Labscore == 10:
            standardized_Labscore == 8
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 9
        elif Labscore == 13:
            standardized_Labscore = 10
        elif 14 <= Labscore <= 15:
            standardized_Labscore = 11
        elif 16 <= Labscore <= 17:
            standardized_Labscore = 12
        elif Labscore == 18:
            standardized_Labscore = 13
        elif 19 <= Labscore <= 20:
            standardized_Labscore = 14
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 15
        elif 23 <= Labscore <= 25:
            standardized_Labscore = Labscore - 7
        else:
            standardized_Labscore = 19

    if chrono_age == 7.5:
        if 0 <= Labscore <= 3:
            standardized_Labscore = 1
        elif 4 <= Labscore <= 8:
            standardized_Labscore = Labscore - 2
        elif 9 <= Labscore <= 10:
            standardized_Labscore = 7
        elif Labscore == 11:
            standardized_Labscore = 8
        elif 12 <= Labscore <= 13:
            standardized_Labscore = 9
        elif 14 <= Labscore <= 15:
            standardized_Labscore = 10
        elif 16 <= Labscore <= 17:
            standardized_Labscore = 11
        elif Labscore == 18:
            standardized_Labscore = 12
        elif 19 <= Labscore <= 20:
            standardized_Labscore = 13
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 14
        elif 23 <= Labscore <= 24:
            standardized_Labscore = 15
        elif 25 <= Labscore <= 26:
            standardized_Labscore = Labscore - 9
        else:
            standardized_Labscore = 19

    if chrono_age == 8:
        if 0 <= Labscore <= 4:
            standardized_Labscore = 1
        elif 5 <= Labscore <= 6:
            standardized_Labscore = Labscore - 2
        elif 7 <= Labscore <= 8:
            standardized_Labscore = 4
        elif 9 <= Labscore <= 10:
            standardized_Labscore = Labscore - 4
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 7
        elif Labscore == 13:
            standardized_Labscore = 8
        elif 14 <= Labscore <= 15:
            standardized_Labscore = 9
        elif 16 <= Labscore <= 17:
            standardized_Labscore = 10
        elif Labscore == 18:
            standardized_Labscore = 11
        elif 19 <= Labscore <= 20:
            standardized_Labscore = 12
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 13
        elif 23 <= Labscore <= 28:
            standardized_Labscore = Labscore - 9

    if chrono_age == 8.5:
        if 0 <= Labscore <= 5:
            standardized_Labscore = 1
        elif 6 <= Labscore <= 10:
            standardized_Labscore = Labscore - 4
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 7
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 8
        elif Labscore == 15:
            standardized_Labscore = 9
        elif 16 <= Labscore <= 17:
            standardized_Labscore = 10
        elif 18 <= Labscore <= 19:
            standardized_Labscore = 11
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 12
        elif 22 <= Labscore <= 23:
            standardized_Labscore = 13
        elif 24 <= Labscore <= 25:
            standardized_Labscore = Labscore - 10
        elif 26 <= Labscore <= 28:
            standardized_Labscore = Labscore - 9

    if chrono_age == 9:
        if 0 <= Labscore <= 5:
            standardized_Labscore = 1
        elif 6 <= Labscore <= 8:
            standardized_Labscore = Labscore - 4
        elif 9 <= Labscore <= 10:
            standardized_Labscore = 5
        elif 11 <= Labscore <= 12:
            standardized_Labscore = Labscore - 5
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 8
        elif 15 <= Labscore <= 16:
            standardized_Labscore = 9
        elif 17 <= Labscore <= 18:
            standardized_Labscore = 10
        elif 19 <= Labscore <= 20:
            standardized_Labscore = 11
        elif Labscore == 21:
            standardized_Labscore = 12
        elif 22 <= Labscore <= 23:
            standardized_Labscore = 13
        elif 24 <= Labscore <= 26:
            standardized_Labscore = Labscore - 10
        elif 27 <= Labscore <= 28:
            standardized_Labscore = Labscore - 9

    if chrono_age == 9.5:
        if 0 <= Labscore <= 6:
            standardized_Labscore = 1
        elif 7 <= Labscore <= 10:
            standardized_Labscore = Labscore - 5
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 6
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 7
        elif 15 <= Labscore <= 16:
            standardized_Labscore = 8
        elif Labscore == 17:
            standardized_Labscore = 9
        elif 18 <= Labscore <= 19:
            standardized_Labscore = 10
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 11
        elif 22 <= Labscore <= 26:
            standardized_Labscore = Labscore - 10
        elif 27 <= Labscore <= 28:
            standardized_Labscore = Labscore - 9

    if chrono_age == 10:
        if 0 <= Labscore <= 6:
            standardized_Labscore = 1
        elif 7 <= Labscore <= 8:
            standardized_Labscore = Labscore - 5
        elif 9 <= Labscore <= 10:
            standardized_Labscore = 4
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 5
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 6
        elif Labscore == 15:
            standardized_Labscore = 7
        elif 16 <= Labscore <= 17:
            stndardized_Labscore = 8
        elif 18 <= Labscore <= 19:
            standardized_Labscore = 9
        elif 20 <= Labscore <= 21:
            standardized_Labscore = Labscore - 10
        elif 22 <= Labscore <= 23:
            standardized_Labscore = 12
        elif 24 <= Labscore <= 26:
            standardized_Labscore = Labscore - 11
        elif Labscore == 27:
            standardized_Labscore = Labscore - 10
        else:
            standardized_Labscore = 19

    if chrono_age == 10.5:
        if 0 <= Labscore <= 6:
            standardized_Labscore = 1
        elif 7 <= Labscore <= 8:
            standardized_Labscore = Labscore - 5
        elif 9 <= Labscore <= 10:
            standardized_Labscore = 4
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 5
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 6
        elif Labscore == 15:
            standardized_Labscore = 7
        elif 16 <= Labscore <= 17:
            stndardized_Labscore = 8
        elif 18 <= Labscore <= 19:
            standardized_Labscore = 9
        elif Labscore == 20:
            standardized_Labscore = Labscore - 10
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 11
        elif 23 <= Labscore <= 27:
            standardized_Labscore = Labscore - 11
        else:
            standardized_Labscore = 18

    if chrono_age == 11:
        if 0 <= Labscore <= 6:
            standardized_Labscore = 1
        elif 7 <= Labscore <= 8:
            standardized_Labscore = Labscore - 5
        elif 9 <= Labscore <= 10:
            standardized_Labscore = 4
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 5
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 6
        elif Labscore == 15:
            standardized_Labscore = 7
        elif 16 <= Labscore <= 17:
            stndardized_Labscore = 8
        elif 18 <= Labscore <= 19:
            standardized_Labscore = 9
        elif Labscore == 20:
            standardized_Labscore = Labscore - 10
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 11
        elif Labscore == 23:
            standardized_Labscore = 12
        elif 24 <= Labscore <= 25:
            standardized_Labscore = 13
        elif 26 <= Labscore <= 28:
            standardized_Labscore = Labscore - 11

    if chrono_age == 11.5:
        if 0 <= Labscore <= 7:
            standardized_Labscore = 1
        elif 8 <= Labscore <= 9:
            standardized_Labscore = Labscore - 6
        elif 10 <= Labscore <= 11:
            standardized_Labscore = 4
        elif Labscore == 12:
            standardized_Labscore = 5
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 6
        elif 15 <= Labscore <= 16:
            standardized_Labscore = 7
        elif 16 <= Labscore <= 17:
            stndardized_Labscore = 8
        elif Labscore == 19:
            standardized_Labscore = 9
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 10
        elif Labscore == 22:
            standardized_Labscore = 11
        elif 23 <= Labscore <= 24:
            standardized_Labscore = 12
        elif 25 <= Labscore <= 26:
            standardized_Labscore = Labscore - 12
        elif 27 <= Labscore <= 28:
            standardized_Labscore = Labscore - 11

    if chrono_age == 12:
        if 0 <= Labscore <= 8:
            standardized_Labscore = 1
        elif 9 <= Labscore <= 10:
            standardized_Labscore = 2
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 3
        elif Labscore == 13:
            standardized_Labscore = 4
        elif Labscore == 14:
            standardized_Labscore = 5
        elif Labscore == 15:
            standardized_Labscore = 6
        elif 16 <= Labscore <= 17:
            standardized_Labscore = 7
        elif Labscore == 18:
            stndardized_Labscore = 8
        elif 19 <= Labscore <= 20:
            standardized_Labscore = 9
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 10
        elif 23 <= Labscore <= 27:
            standardized_Labscore = Labscore - 12
        elif Labscore == 28:
            standardized_Labscore = Labscore - 11

    if chrono_age == 12.5:
        if 0 <= Labscore <= 8:
            standardized_Labscore = 1
        elif 9 <= Labscore <= 10:
            standardized_Labscore = 2
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 3
        elif Labscore == 13:
            standardized_Labscore = 4
        elif Labscore == 14:
            standardized_Labscore = 5
        elif Labscore == 15:
            standardized_Labscore = 6
        elif 16 <= Labscore <= 17:
            standardized_Labscore = 7
        elif Labscore == 18:
            stndardized_Labscore = 8
        elif 19 <= Labscore <= 20:
            standardized_Labscore = 9
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 10
        elif 23 <= Labscore <= 28:
            standardized_Labscore = Labscore - 12

    if chrono_age == 13:
        if 0 <= Labscore <= 9:
            standardized_Labscore = 1
        elif 10 <= Labscore <= 11:
            standardized_Labscore = 2
        elif 12 <= Labscore <= 15:
            standardized_Labscore = Labscore - 9
        elif 16 <= Labscore <= 17:
            standardized_Labscore = 7
        elif Labscore == 18:
            stndardized_Labscore = 8
        elif 19 <= Labscore <= 20:
            standardized_Labscore = 9
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 10
        elif 23 <= Labscore <= 28:
            standardized_Labscore = Labscore - 12

    if chrono_age == 13.5:
        if 0 <= Labscore <= 9:
            standardized_Labscore = 1
        elif 10 <= Labscore <= 11:
            standardized_Labscore = 2
        elif Labscore == 12:
            standardized_Labscore = 3
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 4
        elif 15 <= Labscore <= 16:
            standardized_Labscore = Labscore - 10
        elif 17 <= Labscore <= 18:
            standardized_Labscore = 7
        elif Labscore == 19:
            stndardized_Labscore = 8
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 9
        elif 22 <= Labscore <= 28:
            standardized_Labscore = Labscore - 12

    if chrono_age == 14:
        if 0 <= Labscore <= 10:
            standardized_Labscore = 1
        elif 11 <= Labscore <= 12:
            standardized_Labscore = 2
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 3
        elif 15 <= Labscore <= 16:
            standardized_Labscore = 4
        elif 17 <= Labscore <= 20:
            standardized_Labscore = Labscore - 12
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 9
        elif 23 <= Labscore <= 26:
            standardized_Labscore = Labscore - 13
        elif 27 <= Labscore <= 28:
            standardized_Labscore = Labscore - 12

    if chrono_age == 14.5:
        if 0 <= Labscore <= 11:
            standardized_Labscore = 1
        elif 12 <= Labscore <= 13:
            standardized_Labscore = 2
        elif Labscore == 14:
            standardized_Labscore = 3
        elif 15 <= Labscore <= 16:
            standardized_Labscore = 4
        elif 17 <= Labscore <= 20:
            standardized_Labscore = Labscore - 12
        elif 21 <= Labscore <= 22:
            standardized_Labscore = 9
        elif 23 <= Labscore <= 26:
            standardized_Labscore = Labscore - 13
        elif 27 <= Labscore <= 28:
            standardized_Labscore = Labscore - 12

    if chrono_age == 15:
        if 0 <= Labscore <= 11:
            standardized_Labscore = 1
        elif 12 <= Labscore <= 13:
            standardized_Labscore = 2
        elif Labscore == 14:
            standardized_Labscore = 3
        elif 15 <= Labscore <= 16:
            standardized_Labscore = 4
        elif 17 <= Labscore <= 19:
            standardized_Labscore = Labscore - 12
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 8
        elif Labscore == 22:
            standardized_Labscore = 9
        elif 23 <= Labscore <= 24:
            standardized_Labscore = 10
        elif Labscore == 25:
            standardized_Labscore = 11
        elif Labscore == 26:
            standardized_Labscore = 13
        elif 27 <= Labscore <= 28:
            standardized_Labscore = Labscore - 12

    if chrono_age == 15.5:
        if 0 <= Labscore <= 12:
            standardized_Labscore = 1
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 2
        elif 15 <= Labscore <= 19:
            standardized_Labscore = Labscore - 12
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 8
        elif Labscore == 22:
            standardized_Labscore = 9
        elif 23 <= Labscore <= 24:
            standardized_Labscore = 10
        elif Labscore == 25:
            standardized_Labscore = 11
        elif Labscore == 26:
            standardized_Labscore = 13
        elif 27 <= Labscore <= 28:
            standardized_Labscore = Labscore - 12

    if chrono_age == 16:
        if 0 <= Labscore <= 12:
            standardized_Labscore = 1
        elif 13 <= Labscore <= 14:
            standardized_Labscore = 2
        elif 15 <= Labscore <= 19:
            standardized_Labscore = Labscore - 12
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 8
        elif 22 <= Labscore <= 23:
            standardized_Labscore = 9
        elif 24 <= Labscore <= 25:
            standardized_Labscore = Labscore - 14
        elif Labscore == 26:
            standardized_Labscore = 13
        elif 27 <= Labscore <= 28:
            standardized_Labscore = Labscore - 12

    if chrono_age == 16.5:
        if 0 <= Labscore <= 13:
            standardized_Labscore = 1
        elif 14 <= Labscore <= 16:
            standardized_Labscore = Labscore - 12
        elif 17 <= Labscore <= 18:
            standardized_Labscore = 5
        elif Labscore == 19:
            standardized_Labscore = Labscore - 13
        elif 20 <= Labscore <= 21:
            standardized_Labscore = 7
        elif 22 <= Labscore <= 25:
            standardized_Labscore = Labscore - 14
        elif 26 <= Labscore <= 27:
            standardized_Labscore = Labscore - 13
        elif Labscore == 28:
            standardized_Labscore = Labscore - 12

    standardized_scores.append(standardized_Labscore)


def find_QIscore():
    total_verbal = sum(QIverbal)
    total_realizacao = sum(QIrealizacao)
    total_cv = sum(QIcv)
    total_op = sum(QIop)
    total_vp = sum(QIvp)


    def find_QIverbal():
        if total_verbal == 5:
            QI_verbal = 46
        elif 6 <= total_verbal <= 7:
            QI_verbal = 47
        elif 8 <= total_verbal <= 14:
            QI_verbal = total_verbal + 40
        elif 15 <= total_verbal <= 25:
            QI_verbal = total_verbal + 41
        elif 26 <= total_verbal <= 30:
            QI_verbal = total_verbal + 40
        elif 31 <= total_verbal <= 32:
            QI_verbal = total_verbal + 41
        elif 33 <= total_verbal <= 34:
            QI_verbal = total_verbal + 42
        elif total_verbal == 35:
            QI_verbal = 78
        elif 36 <= total_verbal <= 38:
            QI_verbal = total_verbal + 44
        elif total_verbal == 39:
            QI_verbal = 84
        elif 40 <= total_verbal <= 41:
            QI_verbal = total_verbal + 46
        elif total_verbal == 42:
            QI_verbal = 89
        elif 43 <= total_verbal <= 46:
            QI_verbal = total_verbal + 48
        elif total_verbal == 48:
            QI_verbal = 97
        elif 49 <= total_verbal <= 52:
            QI_verbal = total_verbal + 50
        elif 53 <= total_verbal <= 55:
            QI_verbal = total_verbal + 51
        elif 56 <= total_verbal <= 61:
            QI_verbal = total_verbal + 52
        elif 62 <= total_verbal <= 65:
            QI_verbal = total_verbal + 53
        elif 66 <= total_verbal <= 68:
            QI_verbal = total_verbal + 54
        elif 69 <= total_verbal <= 72:
            QI_verbal = total_verbal + 55
        elif 73 <= total_verbal <= 75:
            QI_verbal = total_verbal + 56
        elif total_verbal == 76:
            QI_verbal = 133
        elif total_verbal == 77:
            QI_verbal = 135
        elif 78 <= total_verbal <= 80:
            QI_verbal = total_verbal + 59
        elif 81 <= total_verbal <= 95:
            QI_verbal = total_verbal + 60

        print("QI verbal = " + str(QI_verbal))

    def find_QIrealizacao():
        if 5 <= total_realizacao <= 29:
            QI_realizacao = total_realizacao + 41
        elif 30 <= total_realizacao <= 38:
            QI_realizacao = total_realizacao + 42
        elif total_realizacao == 39:
            QI_realizacao = 82
        elif total_realizacao == 40:
            QI_realizacao = 84
        elif 41 <= total_realizacao <= 42:
            QI_realizacao = total_realizacao + 45
        elif 43 <= total_realizacao <= 44:
            QI_realizacao = total_realizacao + 46
        elif 45 <= total_realizacao <= 46:
            QI_realizacao = total_realizacao + 47
        elif 47 <= total_realizacao <= 48:
            QI_realizacao = total_realizacao + 48
        elif 49 <= total_realizacao <= 50:
            QI_realizacao = total_realizacao + 49
        elif 51 <= total_realizacao <= 53:
            QI_realizacao = total_realizacao + 50
        elif 54 <= total_realizacao <= 55:
            QI_realizacao = total_realizacao + 51
        elif 56 <= total_realizacao <= 57:
            QI_realizacao = total_realizacao + 52
        elif 58 <= total_realizacao <= 60:
            QI_realizacao = total_realizacao + 53
        elif total_realizacao == 61:
            QI_realizacao = 115
        elif 62 <= total_realizacao <= 64:
            QI_realizacao = total_realizacao + 55
        elif total_realizacao == 65:
            QI_realizacao = total_realizacao + 56
        elif 66 <= total_realizacao <= 68:
            QI_realizacao = total_realizacao + 57
        elif total_realizacao == 69:
            QI_realizacao = total_realizacao + 58
        elif total_realizacao == 70:
            QI_realizacao = total_realizacao + 60
        elif 71 <= total_realizacao <= 72:
            QI_realizacao = total_realizacao + 61
        elif 73 <= total_realizacao <= 92:
            QI_realizacao = total_realizacao + 62
        elif 93 <= total_realizacao <= 95:
            QI_realizacao = 155

        print("QI realizacao = " + str(QI_realizacao))




    def find_QIescala_completa(total_ec = total_verbal + total_realizacao):

        if 10 <= total_ec <= 17:
            QI_escala_completa = total_ec + 30
        elif 18 <= total_ec <= 19:
            QI_escala_completa = 47
        elif 20 <= total_ec <= 21:
            QI_escala_completa = 48
        elif 22 <= total_ec <= 24:
            QI_escala_completa = total_ec + 27
        elif 25 <= total_ec <= 26:
            QI_escala_completa = total_ec + 26
        elif 27 <= total_ec <= 28:
            QI_escala_completa = total_ec + 25
        elif 29 <= total_ec <= 30:
            QI_escala_completa = total_ec + 24
        elif 31 <= total_ec <= 32:
            QI_escala_completa = 54
        elif 33 <= total_ec <= 35:
            QI_escala_completa = 55
        elif 36 <= total_ec <= 38:
            QI_escala_completa = 56
        elif 39 <= total_ec <= 41:
            QI_escala_completa = 57
        elif total_ec == 42:
            QI_escala_completa = 58
        elif 43 <= total_ec <= 46:
            QI_escala_completa = total_ec + 15
        elif 47 <= total_ec <= 48:
            QI_escala_completa = total_ec + 14
        elif 49 <= total_ec <= 50:
            QI_escala_completa = 62
        elif 51 <= total_ec <= 53:
            QI_escala_completa = 63
        elif 54 <= total_ec <= 56:
            QI_escala_completa = 64
        elif 57 <= total_ec <= 58:
            QI_escala_completa = 65
        elif 59 <= total_ec <= 60:
            QI_escala_completa = 66
        elif 61 <= total_ec <= 62:
            QI_escala_completa = 67
        elif 63 <= total_ec <= 64:
            QI_escala_completa = 68
        elif 65 <= total_ec <= 66:
            QI_escala_completa = 69
        elif 67 <= total_ec <= 71:
            QI_escala_completa = total_ec + 4
        elif 72 <= total_ec <= 74:
            QI_escala_completa = total_ec + 3
        elif 75 <= total_ec <= 77:
            QI_escala_completa = total_ec + 2
        elif 78 <= total_ec <= 84:
            QI_escala_completa = total_ec + 1
        elif 85 <= total_ec <= 90:
            QI_escala_completa = total_ec
        elif 91 <= total_ec <= 101:
            QI_escala_completa = total_ec - 1
        elif 102 <= total_ec <= 104:
            QI_escala_completa = total_ec - 2
        elif 105 <= total_ec <= 108:
            QI_escala_completa = total_ec - 3
        elif 109 <= total_ec <= 114:
            QI_escala_completa = total_ec - 4
        elif 115 <= total_ec <= 119:
            QI_escala_completa = total_ec - 5
        elif 120 <= total_ec <= 123:
            QI_escala_completa = total_ec - 6
        elif 124 <= total_ec <= 127:
            QI_escala_completa = total_ec - 7
        elif 128 <= total_ec <= 133:
            QI_escala_completa = total_ec - 8
        elif 134 <= total_ec <= 141:
            QI_escala_completa = total_ec - 9
        elif 142 <= total_ec <= 150:
            QI_escala_completa = total_ec - 8
        elif 151 <= total_ec <= 152:
            QI_escala_completa = total_ec - 9
        elif 153 <= total_ec <= 154:
            QI_escala_completa = total_ec - 10
        elif 155 <= total_ec <= 158:
            QI_escala_completa = total_ec - 11
        elif 159 <= total_ec <= 160:
            QI_escala_completa = total_ec - 12
        elif 161 <= total_ec <= 163:
            QI_escala_completa = total_ec - 13
        elif 164 <= total_ec <= 166:
            QI_escala_completa = total_ec - 14
        elif 167 <= total_ec <= 169:
            QI_escala_completa = total_ec - 15
        elif 170 <= total_ec <= 171:
            QI_escala_completa = total_ec - 16
        elif 172 <= total_ec <= 173:
            QI_escala_completa = total_ec - 17
        elif 174 <= total_ec <= 175:
            QI_escala_completa = total_ec - 18
        elif 176 <= total_ec <= 177:
            QI_escala_completa = total_ec = 19
        elif 178 <= total_ec <= 179:
            QI_escala_completa = total_ec - 20
        elif total_ec == 180:
            QI_escala_completa = 159
        elif 181 <= total_ec <= 190:
            QI_escala_completa = 160

        print("QI Escala Completa = " + str(QI_escala_completa))

    def find_QI_compreensao_verbal ():
        if 4 <= total_cv <= 16:
            QI_compreensao_verbal = total_cv + 44
        elif 17 <= total_cv <= 20:
            QI_compreensao_verbal = total_cv + 45
        elif total_cv == 21:
            QI_compreensao_verbal = 68
        elif 22 <= total_cv <= 24:
            QI_compreensao_verbal = total_cv + 48
        elif 25 <= total_cv <= 29:
            n = 49
            for i in range (25, 30):
                x = i + n
                n = n + 1
                if i == total_cv:
                    QI_compreensao_verbal = x
        elif 30 <= total_cv <= 32:
            n = 53
            for i in range (30, 33):
                x = i + n
                n = n + 1
                if i == total_cv:
                    QI_compreensao_verbal = x
        elif 33 <= total_cv <= 36:
            n = 55
            for i in range(33, 37):
                x = i + n
                n = n + 1
                if i == total_cv:
                    QI_compreensao_verbal = x
        elif 37 <= total_cv <= 39:
            n = 58
            for i in range (37, 40):
                x = i + n
                n = n + 1
                if i == total_cv:
                    QI_compreensao_verbal = x
        elif total_cv == 40:
            QI_compreensao_verbal = 100
        elif 41 <= total_cv <= 42:
            QI_compreensao_verbal = total_verbal + 61
        elif 43 <= total_cv <= 44:
            QI_compreensao_verbal = total_verbal + 62
        elif 45 <= total_cv <= 48:
            QI_compreensao_verbal = total_cv + 63
        elif 49 <= total_cv <= 50:
            QI_compreensao_verbal = total_cv + 64
        elif total_cv == 51:
            QI_compreensao_verbal = 116
        elif 52 <= total_cv <= 53:
            QI_compreensao_verbal = total_cv + 66
        elif 54 <= total_cv <= 55:
            QI_compreensao_verbal = total_cv + 67
        elif 56 <= total_cv <= 58:
            QI_compreensao_verbal = total_cv + 68
        elif 59 <= total_cv <= 60:
            QI_compreensao_verbal = total_cv + 69
        elif 61 <= total_cv <= 62:
            QI_compreensao_verbal = total_cv + 70
        elif 63 <= total_cv <= 66:
            n = 71
            for i in range (63, 67):
                x = i + n
                n = n + 1
                if i == total_cv:
                    QI_compreensao_verbal = x
        elif 67 <= total_cv <= 76:
            QI_compreensao_verbal = total_cv + 74
        print("QI Compreensao Verbal = " + str(QI_compreensao_verbal))

    def find_QI_organizacao_perceptiva():
        if 4 <= total_op <= 18:
            QI_organizacao_perceptiva = total_op + 46
        elif total_op == 19:
            QI_organizacao_perceptiva = 66
        elif 20 <= total_op <= 22:
            QI_organizacao_perceptiva = total_op + 48
        elif 23 <= total_op <= 26:
            QI_organizacao_perceptiva = total_op + 49
        elif 27 <= total_op <= 28:
            QI_organizacao_perceptiva = total_op + 50
        elif total_op == 29:
            QI_organizacao_perceptiva = 81
        elif 30 <= total_op <= 31:
            QI_organizacao_perceptiva = total_op + 53
        elif total_op == 32:
            QI_organizacao_perceptiva = 86
        elif 33 <= total_op <= 34:
            QI_organizacao_perceptiva = total_op + 55
        elif total_op == 35:
            QI_organizacao_perceptiva = 91
        elif 36 <= total_op <= 37:
            QI_organizacao_perceptiva = total_op + 57
        elif 38 <= total_op <= 40:
            n = 58
            for i in range(38, 41):
                x = i + n
                n = n + 1
                if i == total_op:
                    QI_organizacao_perceptiva = x
        elif total_op == 41:
            QI_organizacao_perceptiva = 101
        elif 42 <= total_op <= 43:
            QI_organizacao_perceptiva = total_op + 61
        elif 44 <= total_op <= 45:
            QI_organizacao_perceptiva = 62
        elif 46 <= total_op <= 48:
            n = 63
            for i in range (46, 49):
                x = i + n
                n = n + 1
                if i == total_op:
                    QI_organizacao_perceptiva = x
        elif total_op == 49:
            QI_organizacao_perceptiva = 114
        elif 50 <= total_op <= 52:
            QI_organizacao_perceptiva = total_op + 66
        elif total_op == 53:
            QI_organizacao_perceptiva = 120
        elif 54 <= total_op <= 57:
            n = 69
            for i in range (54, 58):
                x = i + n
                n = n + 1
                if i == total_op:
                    QI_organizacao_perceptiva = x
        elif total_op == 58:
            QI_organizacao_perceptiva = 132
        elif 59 <= total_op <= 61:
            QI_organizacao_perceptiva = total_op + 75
        elif 62 <= total_op <= 63:
            QI_organizacao_perceptiva = total_op + 76
        elif 64 <= total_op <= 67:
            QI_organizacao_perceptiva = total_op + 77
        elif 68 <= total_op <= 73:
            QI_organizacao_perceptiva = total_op + 76
        elif 74 <= total_op <= 76:
            QI_organizacao_perceptiva = 150

        print("QI Organizacao Perceptiva = " + str(QI_organizacao_perceptiva))

    def find_QI_velocidade_processamento():
        if 2 <= total_vp <= 3:
            QI_velocidade_processamento = total_vp + 48
        elif 4 <= total_vp <= 5:
            QI_velocidade_processamento = total_vp + 49
        elif total_vp == 6:
            QI_velocidade_processamento = 57
        elif 7 <= total_vp <= 10:
            n = 52
            for i in range (7, 11):
                x = i + n
                n = n + 3
                if i == total_vp:
                    QI_velocidade_processamento = x
        elif total_vp == 11:
            QI_velocidade_processamento = 74
        elif total_vp == 12:
            QI_velocidade_processamento = 77
        elif total_vp == 13:
            QI_velocidade_processamento = 81
        elif total_vp == 14:
            QI_velocidade_processamento = 84
        elif 15 <= total_vp <= 18:
            n = 71
            for i in range (15, 19):
                x = i + n
                n = n + 2
                if i == total_vp:
                    QI_velocidade_processamento = x
        elif 19 <= total_vp <= 24:
            n = 78
            for i in range (19, 25):
                x = i + n
                n = n + 2
                if i == total_vp:
                    QI_velocidade_processamento = x
        elif total_vp == 25:
            QI_velocidade_processamento = 114
        elif total_vp == 26:
            QI_velocidade_processamento = 117
        elif 27 <= total_vp <= 33:
            n = 92
            for i in range (27, 34):
                x = i + n
                n = n + 2
                if i == total_vp:
                    QI_velocidade_processamento = x
        elif total_vp == 34:
            QI_velocidade_processamento = 141
        elif total_vp == 35:
            QI_velocidade_processamento = 145
        elif total_vp == 36:
            QI_velocidade_processamento = 147
        elif total_vp == 37:
            QI_velocidade_processamento = 149
        elif total_vp == 38:
            QI_velocidade_processamento = 150
        print("QI Velocidade Processamento = " + str(QI_velocidade_processamento))





    find_QIverbal()
    find_QIrealizacao()
    find_QIescala_completa()
    find_QI_compreensao_verbal()
    find_QI_organizacao_perceptiva()
    find_QI_velocidade_processamento()





find_standardized_Infscore()
find_standardized_Semscore()
find_standardized_Ariscore()
find_standardized_Vocscore()
find_standardized_Compscore()
find_standardized_MDscore()
find_standardized_CGscore()
find_standardized_Codscore()
find_standardized_DGscore()
find_standardized_Cubscore()
find_standardized_COscore()
find_standardized_PSscore()
find_standardized_Labscore()

print(standardized_scores)

find_QIscore()
