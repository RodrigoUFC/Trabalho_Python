import shelve
import os

def validaCpf(cpf, d1=0, d2=0, i=0):
    if len(cpf) == 11:
        while i < 10:
            d1, d2, i = (d1 + (int(cpf[i]) * (11 - i - 1))) % 11 if i < 9 else d1, (
                       d2 + (int(cpf[i]) * (11 - i))) % 11, i + 1
        return (int(cpf[9]) == (11 - d1 if d1 > 1 else 0)) and (int(cpf[10]) == (11 - d2 if d2 > 1 else 0))
    else:
        return False

def salvar(dic_funcionarios):
    s=shelve.open('./funcionarios/funcionario'+'1'+'.db')
    try:
        s['dados']=dic_funcionarios
    finally:
        s.close()

def carregaDados():
    dados={}
    if len(os.listdir('./funcionarios')) > 0:
        s = shelve.open('./funcionarios/funcionario' + '1' + '.db')
        try:
            dados = s['dados']
        finally:
            s.close()
    return dados
def cadastro(dic_funcionarios):
    print(" Digite o nome do funcionário: ")
    nome = input(" >>> ")
    print(" Digite o CPF do funcionário: ")
    cpf = input(" >>> ")
    while not validaCpf(cpf):
        print(" CPF invalido! Digite o CPF do funcionário: ")
        cpf = input(" >>> ")

    print(" Digite o número correspondente ao sexo do funcionario: 0 - MASCULINO / 1 - FEMININO")
    sexo = int(input(" >>> "))
    print(" Digite a data de nascimento do funcionario: (dia)  ->  (mes)  ->  (ano) ")
    dataN = []
    for i in range(3):
        dataN.append(int(input(" >>> ")))
    print(" Digite o número correspondente ao cargo do funcionario: 0 - Pedreiro / 1 - Engenheiro / 2 - Tecnico Administrativo")
    cargo = int(input(" >>> "))
    print(" Digite o valor do salario do funcionario: ")
    salario = float(input(" >>> "))
    print(" Digite a data de contratação do funcionário: ")
    dataC = []
    for i in range(3):
        dataC.append(int(input(" >>> ")))
        dic_funcionarios = {'Nome': nome, 'CPF': cpf, 'sexo': sexo, 'DataNascimento': dataN, 'Cargo': cargo, 'Salario': salario, 'DataContratação': dataC}
    print("Cadastro realizado com sucesso !")
    return(dic_funcionarios)


def consulta(dic_funcionarios):
    print(" Digite o CPF referente ao funcionário a ser consultado: ")
    cpf = input(" >>> ")
    if cpf in dic_funcionarios.values():
        print(" Dados do funcionario")
        print(" Nome:")
        print(dic_funcionarios['Nome'])
        print(" Cpf:")
        print(dic_funcionarios['CPF'])
        print(" Sexo:")
        if dic_funcionarios['sexo'] == 0:
            print("Masculino")
        if dic_funcionarios['sexo'] == 1:
            print("Feminino")
        print(" Data de nascimento:")
        print("%d/%d/%d" %(dic_funcionarios['DataNascimento'][0],dic_funcionarios['DataNascimento'][1],dic_funcionarios['DataNascimento'][2]))
        print(" Cargo: ")
        if dic_funcionarios['Cargo'] == 0:
            print("Pedreiro")
        if dic_funcionarios['Cargo'] == 1:
            print("Engenheiro")
        if dic_funcionarios['Cargo'] == 2:
            print("Tecnico Administrativo")
        print(" Valor do salario: ")
        print(dic_funcionarios['Salario'])
        print(" Data de contracao: ")
        print("%d/%d/%d" %(dic_funcionarios['DataContratação'][0],dic_funcionarios['DataContratação'][1],dic_funcionarios['DataContratação'][2]))
    else:
        print(" Funcionário não encontrado! ")

def deleta(dic_funcionarios):
    print(" Digite o CPF referente ao funcionário a ser deletado: ")
    cpf = input(" >>> ")
    if cpf in dic_funcionarios['CPF']:
        print(" Dados do funcionario") 
        print(" Nome:")
        print(dic_funcionarios['Nome'])
        print(" Cpf:")
        print(dic_funcionarios['CPF'])
        print(" Sexo: ")
        if dic_funcionarios['sexo'] == 0:
            print("Masculino")
        if dic_funcionarios['sexo'] == 1:
            print("Feminino")
        print(" Data de nascimento:")
        print("%d/%d/%d" % (dic_funcionarios['DataNascimento'][0], dic_funcionarios['DataNascimento'][1],
                            dic_funcionarios['DataNascimento'][2]))
        print(" Cargo: ")
        if dic_funcionarios['Cargo'] == 0:
            print("Pedreiro")
        if dic_funcionarios['Cargo'] == 1:
            print("Engenheiro")
        if dic_funcionarios['Cargo'] == 2:
            print("Tecnico Administrativo")
        print(" Valor do salario: ")
        print(dic_funcionarios['Salario'])
        print(" Data de contracao: ")
        print("%d/%d/%d" % (dic_funcionarios['DataContratação'][0], dic_funcionarios['DataContratação'][1],
                            dic_funcionarios['DataContratação'][2]))
        print(" Deseja realmente excluir esse funcionario: 0 - sim / 1 - nao")
        opcao = int(input(" >>> "))
        if opcao == 0:
            del dic_funcionarios['CPF']
            print(" Os dados do funcionário foram deletados! ")
        else:
            print(" OK! ")
    else:
        print(" Funcionário não encontrado! ")

def atualiza(dic_funcionarios):
    print(" Digite o CPF referente ao funcionário cujo os dados serao atualizados: ")
    cpf = input(" >>> ")
    if cpf in dic_funcionarios['CPF']:
        print(" Digite o nome do funcionário: ")
        nome = input(" >>> ")
        print(" Digite o sexo do funcionario: 0 - MASCULINO / 1 - FEMININO ")
        sexo = int(input(" >>> "))
        print(" Digite a data de nascimento do funcionario: (dia)  ->  (mes)  ->  (ano) ")
        dataN = []
        for i in range(3):
            dataN.append(int(input(" >>> ")))
        print(" Digite o numero correspondente ao cargo do funcionario: 0 - Pedreiro / 1 - Engenheiro / 2 - Tecnico Administrativo")
        cargo = int(input(" >>> "))
        print(" Digite o valor do salario do funcionario: ")
        salario = float(input(" >>>"))
        print(" Digite a data de contratação do funcionario: ")
        dataC = []
        for i in range(3):
            dataC.append(int(input(" >>> ")))
        dic_funcionarios[cpf] = (nome,cpf,sexo,dataN,cargo,salario,dataC)

def pagamento(dic_funcionarios):
    listaEng = ["Engenheiros",0,0]
    listaPed = ["Pedreiros",0,0]
    listaTec = ["Tecnico Administrativo",0,0]
    print(" Digite uma data especifica para o calculo da folha de pagamento: dia/mes/ano ")
    data = []
    for i in range(3):
        data.append(int(input(" >>> ")))
    lista_func = dic_funcionarios.keys()
    for i in range(len(lista_func)):
        dataC = dic_funcionarios[lista_func[i]][6]
        tempo = [0]*3
        for j in range(3):
            tempo[j] = data[j] - dataC[j]
        Coe = [0]*3
        Coe[1] = 12*tempo[2]
        Coe[1] = Coe[1]+tempo[1]
        if tempo[1] < 0:
            Coe[2] = tempo[2]-1
        if tempo[0] < 0:
            Coe[1] = Coe[1]-1
    
        if dic_funcionarios[lista_func[i]][4] == 0:
            listaPed[1] = listaPed[1] + 1
            listaPed[2] = listaPed[2] + dic_funcionarios[lista_func[i]][5]*(1.003**float(Coe[1]))*(1.07**float(Coe[2]))
        if dic_funcionarios[lista_func[i]][4] == 1:
            listaEng[1] = listaEng[1] + 1
            listaEng[2] = listaEng[2] + dic_funcionarios[lista_func[i]][5]*(1.001**float(Coe[1]))*(1.1**float(Coe[2]))
        if dic_funcionarios[lista_func[i]][4] == 2:
            listaTec[1] = listaTec[1] + 1
            listaTec[2] = listaTec[2] + dic_funcionarios[lista_func[i]][5]*(1.002**float(Coe[1]))*(1.08**float(Coe[2]))

    tabela = [[ "Funcao","Quantidade", "Salario total"]]
    tabela.append(listaEng)
    tabela.append(listaPed)
    tabela.append(listaTec)
    print("           Folha de pagamento referente a data %d/%d/%d " %(data[0],data[1],data[2]))
    print(" %23.20s %21.15s %20.15s" %(tabela[0][0],tabela[0][1],tabela[0][2]))
    for i in range(1,len(tabela)):
        print(" %25.30s %15.1d %20.2f" %(tabela[i][0],tabela[i][1],tabela[i][2]))

def idade(dic_funcionarios):
    print(" Digite uma data especifica para o calculo da idade: dia/mes/ano ")
    data = []
    for i in range(3):
        data.append(int(input(" >>> ")))
    velho = 0
    idadeV = 0
    nome_velho = ("ninguem")
    lista_func = dic_funcionarios.keys()
    for i in range(len(lista_func)):
        dataC = dic_funcionarios[lista_func[i]][3]
        tempo = [0]*3
        for j in range(3):
            tempo[j] = data[j]-dataC[j]
        Coe = [0]*3
        Coe[1] = 12*tempo[2]
        Coe[1] = Coe[1]+tempo[1]
        if tempo[1] < 0:
            Coe[2] = tempo[2]-1
        if tempo[0] < 0:
            Coe[1] = Coe[1]-1
        tempoT = Coe[1]*30 + tempo[0]
        if tempoT > velho:
            velho = tempoT
            idadeV = Coe[2]
            nome_velho = dic_funcionarios[lista_func[i]][0]
    print(" %s e o funcionario mais velho da empreasa, ele tem %d anos de idade. " %(nome_velho,idadeV))

def cresc_fin(dic_funcionarios):
    print(" Digite o cpf referente ao funcionário a ser consultado: ")
    cpf = input(" >>> ")
    print(" Digite uma data especifica para o calculo do crescimento financeiro do funcionario: (dia)  ->  (mes)  ->  (ano) ")
    data = []
    for i in range(3):
        data.append(int(input(" >>> ")))
    if cpf in dic_funcionarios['CPF']:
        dataC = dic_funcionarios['DataContratação']
        tempo=[0]*3
        for j in range(3):
            tempo[j] = data[j] - dataC[j]
        Coe = [0]*3
        Coe[1] = 12*tempo[2]
        Coe[1] = Coe[1] + tempo[1]
        if tempo[1] < 0:
            Coe[2] = tempo[2]-1
        if tempo[0] < 0:
            Coe[1] = Coe[1]-1
            
        if dic_funcionarios['Cargo'] == 0:
            pagamento = dic_funcionarios['Salario']*(1.003**float(Coe[1]))*(1.07**float(Coe[2]))
        if dic_funcionarios['Cargo'] == 1:
            pagamento=dic_funcionarios['Salario']*(1.001**float(Coe[1]))*(1.1**float(Coe[2]))
        if dic_funcionarios['Cargo'] == 2:
            pagamento=dic_funcionarios['Salario']*(1.002**float(Coe[1]))*(1.08**float(Coe[2]))

        rel_pag = (pagamento/dic_funcionarios['Salario'])*100
        print(" O salario do funcionario cresceu %1.2f por cento "  %(rel_pag,))
    else:
        print(" Funcionário não encontrado! ")

def maior_salario(dic_funcionarios):
    salario = 0
    cpf = ("ninguem")
    print(" Digite uma data para conferir o funcionário de maior salário: (dia)  ->  (mes)  ->  (ano) ")
    data = []
    for i in range(3):
        data.append(int(input(" >>> ")))
    lista_func = dic_funcionarios.keys()
    for i in range(len(lista_func)):
        dataC = dic_funcionarios[lista_func[i][6]]
        tempo = [0]*3
        for j in range(3):
            tempo[j] = data[j]-dataC[j]
        Coe = [0]*3
        Coe[1] = 12*tempo[2]
        Coe[1] = Coe[1]+tempo[1]
        if tempo[1] < 0:
            Coe[2] = tempo[2]-1
        if tempo[0] < 0:
            Coe[1] = Coe[1]-1
    
        if dic_funcionarios[lista_func[i]][4] == 0:
            salarioF = dic_funcionarios[lista_func[i]][5]*(1.003**float(Coe[1]))*(1.07**float(Coe[2]))
        if dic_funcionarios[lista_func[i]][4] == 1:
            salarioF = dic_funcionarios[lista_func[i]][5]*(1.001**float(Coe[1]))*(1.1**float(Coe[2]))
        if dic_funcionarios[lista_func[i]][4] == 2:
            salarioF = dic_funcionarios[lista_func[i]][5]*(1.002**float(Coe[1]))*(1.08**float(Coe[2]))
        if salarioF > salario:
            cpf=lista_func[i]
    print(" Dados do funcionario com maior salario") 
    print(" Nome:")
    print(dic_funcionarios[cpf][0])
    print(" Cpf:")
    print(dic_funcionarios[cpf][1])
    print(" Sexo:")
    if dic_funcionarios[cpf][2] == 0:
        print("Masculino")
    if dic_funcionarios[cpf][2] == 1:
        print("Feminino")
    print(" Data de nascimento:")
    print("%d/%d/%d" %(dic_funcionarios[cpf][3][0],dic_funcionarios[cpf][3][1],dic_funcionarios[cpf][3][2]))
    print(" Cargo:")
    if dic_funcionarios[cpf][4] == 0:
        print("Pedreiro")
    if dic_funcionarios[cpf][4] == 1:
        print("Engenheiro")
    if dic_funcionarios[cpf][4] == 2:
        print("Tecnico Administrativo")
    print(" Valor do salario:")
    print(dic_funcionarios[cpf][5])
    print(" Data de contracao:")
    print("%d/%d/%d" %(dic_funcionarios[cpf][6][0],dic_funcionarios[cpf][6][1],dic_funcionarios[cpf][6][2]))

def media_salario(dic_funcionarios):
    salarios = 0
    funcio = 0
    print(" Digite uma data especifica para calcular a média dos salarios dos funcionarios: (dia)  ->  (mes)  ->  (ano) ")
    data = []
    for i in range(3):
        data.append(int(input(" >>> ")))
    lista_func = dic_funcionarios.keys()
    for i in range(len(lista_func)):
        dataC = dic_funcionarios[lista_func[i]][6]
        tempo = [0]*3
        for j in range(3):
            tempo[j] = data[j]-dataC[j]
        Coe = [0]*3
        Coe[1] = 12*tempo[2]
        Coe[1] = Coe[1]+tempo[1]
        if tempo[1] < 0:
            Coe[2] = tempo[2]-1
        if tempo[0] < 0:
            Coe[1] = Coe[1]-1
            
        if dic_funcionarios[lista_func[i]][4] == 0:
            funcio = funcio + 1
            salarios = salarios + dic_funcionarios[lista_func[i]][5]*(1.003**float(Coe[1]))*(1.07**float(Coe[2]))
        if dic_funcionarios[lista_func[i]][4] == 1:
            funcio = funcio + 1
            salarios = salarios + dic_funcionarios[lista_func[i]][5]*(1.001**float(Coe[1]))*(1.1**float(Coe[2]))
        if dic_funcionarios[lista_func[i]][4] == 2:
            funcio = funcio + 1
            salarios = salarios + dic_funcionarios[lista_func[i]][5]*(1.002**float(Coe[1]))*(1.08**float(Coe[2]))
    mediaS = salarios/funcio

    lista_func = dic_funcionarios.keys()
    for i in range(len(lista_func)):
        salarioF = 0
        dataC = dic_funcionarios[lista_func[i]][6]
        tempo = [0]*3
        for j in range(3):
            tempo[j] = data[j]-dataC[j]
        Coe = [0]*3
        Coe[1] = 12*tempo[2]
        Coe[1] = Coe[1]+tempo[1]
        if tempo[1] < 0:
            Coe[2] = tempo[2]-1
        if tempo[0] < 0:
            Coe[1] = Coe[1]-1

        if dic_funcionarios[lista_func[i]][4] == 0:
            salarioF = dic_funcionarios[lista_func[i]][5]*(1.003**float(Coe[1]))*(1.07**float(Coe[2]))
        if dic_funcionarios[lista_func[i]][4] == 1:
            salarioF = dic_funcionarios[lista_func[i]][5]*(1.001**float(Coe[1]))*(1.1**float(Coe[2]))
        if dic_funcionarios[lista_func[i]][4] == 2:
            salarioF = dic_funcionarios[lista_func[i]][5]*(1.002**float(Coe[1]))*(1.08**float(Coe[2]))
        if salarioF > mediaS:
            print(" O funcionario %s portador do cpf %s recebe %f" %(dic_funcionarios[lista_func[i]][0],dic_funcionarios[lista_func[i]][1],salarioF))

def relatorio(dic_funcionarios):
    listaPe = []
    listaEn = []
    listaTe = []
    lista_func = dic_funcionarios.keys()
    for i in range(len(lista_func)):
        if dic_funcionarios[lista_func[i]][4] == 0:
            listaPe.append(dic_funcionarios[lista_func[i]][5])
        if dic_funcionarios[lista_func[i]][4] == 1:
            listaEn.append(dic_funcionarios[lista_func[i]][5])
        if dic_funcionarios[lista_func[i]][4] == 2:
            listaTe.append(dic_funcionarios[lista_func[i]][5])
    listaPe.sort()
    listaEn.sort()
    listaTe.sort()
    listaPed = []
    listaEng = []
    listaTec = []
    for i in range(len(listaPe)-1,-1,-1):
        listaPed.append(listaPe[i])
    for i in range(len(listaEn)-1,-1,-1):
        listaEng.append(listaEn[i])
    for i in range(len(listaTe)-1,-1,-1):
        listaTec.append(listaTe[i])
        
    lista_func = dic_funcionarios.keys()
    print("\n")
    print(" Lista dos funcionarios no cargo de Pedreiro: ")
    for i in range(len(listaPed)):
        for j in range(len(lista_func)):
            if dic_funcionarios[lista_func[j]][4] == 0:
                if dic_funcionarios[lista_func[j]][5] == listaPed[i]:
                    print(dic_funcionarios[lista_func[j]][0])
    print("\n")                
    print(" Lista dos funcionarios no cargo de Engenheiro: ")
    for i in range(len(listaEng)):
        for j in range(len(lista_func)):
            if dic_funcionarios[lista_func[j]][4] == 1:
                if dic_funcionarios[lista_func[j]][5] == listaEng[i]:
                    print(dic_funcionarios[lista_func[j]][0])
    print("\n")
    print(" Lista dos funcionarios no cargo de Tecnico administrativo: ")
    for i in range(len(listaTec)):
        for j in range(len(lista_func)):
            if dic_funcionarios[lista_func[j]][4] == 2:
                if dic_funcionarios[lista_func[j]][5] == listaTec[i]:
                    print(dic_funcionarios[lista_func[j]][0])
                








dic_funcionarios = carregaDados()
menu = 30
while menu != 11:
    print("\n     \033[4;34mBem-vindo à Plataforma Virtual da PythonEngenharia!\033[m")
    print("\n     \033[1;34mNosso MENU irá lhe auxiliar da melhor maneira possível:\033[m")
    print("  \033[;36m 0 - Salvar dados em um arquivo\033[m")
    print("  \033[;36m 1 - Cadastrar um funcionario\033[m")
    print("  \033[;36m 2 - Consultar os dados de um funcionario\033[m")
    print("  \033[;36m 3 - Excluir um funcionario\033[m")
    print("  \033[;36m 4 - Atualizar dados cadastrais de um funcionario\033[m")
    print("  \033[;36m 5 - Calculo da folha de pagamento\033[m")
    print("  \033[;36m 6 - Ver funcionario com maior idade da empresa\033[m")
    print("  \033[;36m 7 - Calculo do crescimento financeiro do funcionario\033[m")
    print("  \033[;36m 8 - Ver os dados do funcionario com maior salario da empresa\033[m")
    print("  \033[;36m 9 - Retornar funcionarios com salario acima da media\033[m")
    print("  \033[;36m 10 - Relatorio de funcionarios\033[m")
    print("  \033[;36m 11 - Sair do programa\033[m")
    print("\n     \033[1;34mDigite o número referente a sua opção:\033[m ")
    menu = int(input(" >>> "))
    if menu == 0:
        salvar(dic_funcionarios)
    if menu == 1:
        dic_funcionarios.update(cadastro(dic_funcionarios))
    if menu == 2:
        consulta(dic_funcionarios)
    if menu == 3:
        deleta(dic_funcionarios)
    if menu == 4:
        atualiza(dic_funcionarios)
    if menu == 5:
        pagamento(dic_funcionarios)
    if menu == 6:
        idade(dic_funcionarios)
    if menu == 7:
        cresc_fin(dic_funcionarios)
    if menu == 8:
        maior_salario(dic_funcionarios)
    if menu == 9:
        media_salario(dic_funcionarios)
    if menu == 10:
        relatorio(dic_funcionarios)
    if menu == 12:
        print(dic_funcionarios)
        
        
        
    
        
    
