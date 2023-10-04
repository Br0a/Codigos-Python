salario = float(input("Informe o salário: "))#Float é usado para quando se pode digitar números decimais, como 1.5

if salario <= 3000:
    print("Progamador jûnior")
#elif em outras linguagens é o else e if, porém no Python significa então (elif = então)
elif salario> 3000 and salario<=6000:
    print("Progamador pleno")
elif salario> 6000 and salario <= 15000:
    print("progamador Sênior")
else:
    print("Gerente de projetos")
