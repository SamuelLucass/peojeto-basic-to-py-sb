# Calculo de Salário Liquido de um funcionário
n = input("Digite o seu nome: ")
sb = int(input("Digite o seu salário Bruto: "))

td = 0.049

if sb <= 50000:
    td = 0.03
    d = sb * td
    sl = sb - d
    print("Olá, %s tudo bem ?" % n)
    print("O seu salário bruto é %i. O seu desconto é %i e o seu salário liquido é %i" % (sb, d, sl))
    exit()

if sb > 50000:
    td = 0.038
    d = sb * td
    sl = sb - d
    print("Olá, %s tudo bem ?" % n)
    print("O seu salário bruto é %i. O seu desconto é %i e o seu salário liquido é %i" % (sb, d, sl))
    exit()

if sb > 200000:
    d = sb * td
    sl = sb - d
    print("Olá, %s tudo bem ?" % n)
    print("O seu salário bruto é %i. O seu desconto é %i e o seu salário liquido é %i" % (sb, d, sl))
    exit()

