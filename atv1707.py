#Questão 1
def mencao():
    quest = 0
    quant = int(input("Insira a quantidade de questionários você fez:"))
    for _ in range(quant):
        entry3 = float(input(f"digite a nota dos seus {quant} questionários:"))
        quest += entry3
    entry2 = input("Insira a nota de sua provas e projetos separados por espaco:").split()
    p1,p2,proj1,proj2 = map(int,entry2)
    mpp = (p1+2*p2)/3
    mpproj = (proj1+2*proj2)/3
    nf = 0.5*mpp+0.4*mpproj + 0.1* quest

    if 90 <= nf >= 100:
        mencao = "SS"
    elif 70 <= nf < 90:
        mencao = "MS"
    elif 50 <= nf < 70:
        mencao = "MM"
    elif 30 <= nf < 50:
        mencao = "MI"
    elif 0 <= nf < 30:
        mencao = "II"
    else:
        mencao = "Nota inválida"

    print(f"Sua mencao em apc é:",mencao)
#mencao()
#Questão 2
def new_word():
