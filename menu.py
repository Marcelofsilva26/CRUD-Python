from biblioteca import *

while True:
    opcao = input('Escolha uma das opções: \n'
                  '---------------------\n'
                  'Menu academia\n'
                  '1 - Alunos\n'
                  '2 - Modalidades\n'
                  '3 - Funcionarios\n'
                  '4 - Personal\n'
                  '5 - Sair\n'
                  '-> ')

    print()

    if opcao == '1':
        alunoopcao = input('Escolha um comando:\n'
                            '1 - Inserir um aluno\n'
                            '2 - Deletar um aluno\n'
                            '3 - Exibir os alunos\n'
                            '4 - Voltar ao menu\n'
                            '-> ')
        if alunoopcao == '1':
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            cpf = input('Cpf: ')
            email = input('Email: ')
            endereco = input('Endereço: ')
            inseriraluno(nome, telefone, cpf, email, endereco)
            print('Cadastrado na tabela alunos com sucesso!')

        elif alunoopcao == '2':
            id_aluno = input('Digite o id do aluno que deseja deletar: ')
            deletaraluno(int(id_aluno))
            print('Aluno deletado com sucesso!')

        elif alunoopcao == '3':
            exibiralunos()

    elif opcao == '2':
        modalidadeopcao = input('Escolha um comando:\n'
                                 '1 - Inserir uma modalidade\n'
                                 '2 - Deletar uma modalidade\n'
                                 '3 - Exibir as modalidades\n'
                                 '4 - Voltar ao menu\n'
                                 '-> ')
        if modalidadeopcao == '1':
            nome = input('Nome da modalidade: ')
            inserirmodalidade(nome)
            print('Cadastrado na tabela modalidades com sucesso!')

        elif modalidadeopcao == '2':
            deletemodalidade = input('Digite o id da modalidade que deseja deletar: ')
            deletarmodalidade(int(deletemodalidade))
            print('Modalidade deletada com sucesso!')

        elif modalidadeopcao == '3':
            exibirmodalidades()

    elif opcao == '3':
        funcionarioopcao = input('Escolha um comando:\n'
                                  '1 - Inserir um funcionário\n'
                                  '2 - Deletar um funcionário\n'
                                  '3 - Exibir os funcionários\n'
                                  '4 - Voltar ao menu\n'
                                  '-> ')
        if funcionarioopcao == '1':
            nome = input('Nome do funcionário: ')
            cpf = input('Cpf do funcionário: ')
            depart = input('Em qual departamento ele vai trabalhar: ')
            filhos = int(input("O funcionario tem quantos filhos: "))
            salario = float(input("Qual será o salário do funcionário: "))
            inserirfuncionario(nome, cpf, depart, filhos, salario)
            print('Cadastrado na tabela funcionaroios com sucesso!')

        elif funcionarioopcao == '2':
            deletefuncionario = input('Digite o id do funcionário que deseja deletar: ')
            deletarfuncionario(int(deletefuncionario))
            print('Funcionário deletado com sucesso!')

        elif funcionarioopcao == '3':
            exibirfuncionarios()

    elif opcao == '4':
        personalopcao = input('Escolha um comando:\n'
                               '1 - Inserir um personal\n'
                               '2 - Deletar um personal\n'
                               '3 - Exibir os personals\n'
                               '4 - Voltar ao menu\n'
                               '-> ')
        if personalopcao == '1':
            cpf = input('Cpf do personal: ')
            cref = input('Cref do personal: ')
            nome = input('Nome do personal: ')
            telef = input('Telefone do personal:')
            email = input('Email do personal:')
            inserirpersonal(cpf, cref, nome, telef, email,)
            print('Cadastrado na tabela personals com sucesso!')

        elif personalopcao == '2':
            deletepersonal = input('Digite o cref do personal que deseja deletar: ')
            deletarpersonal(deletepersonal)
            print('Personal deletado com sucesso!')

        elif personalopcao == '3':
            exibirpersonals()

    elif opcao == '5':
        break

