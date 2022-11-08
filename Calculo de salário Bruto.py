# Calculo de Salário Liquido de um funcionário
n = input("Digite o seu nome: ")
sb = int(input("Digite o seu salário Bruto: "))

td = 0.049
num1 = 50000
num2 = 200000

if sb <= num1:
    td = 0.03
    d = sb * td
    sl = sb - d
    print("Olá, %s tudo bem ?" % n)
    print("O seu salário bruto é %i. O seu desconto é %i e o seu salário liquido é %i" % (sb, d, sl))
    exit()

if (sb > num1) and (sb < num2):
    td = 0.038
    d = sb * td
    sl = sb - d
    print("Olá, %s tudo bem ?" % n)
    print("O seu salário bruto é %i. O seu desconto é %i e o seu salário liquido é %i" % (sb, d, sl))
    exit()

if sb > num2:
    d = sb * td
    sl = sb - d
    print("Olá, %s tudo bem ?" % n)
    print("O seu salário bruto é %i. O seu desconto é %i e o seu salário liquido é %i" % (sb, d, sl))
    exit()
    