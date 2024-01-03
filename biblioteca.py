from banco import *
def inseriraluno(nome, telefone,cpf, email, endereco):
    meucursor = banco.cursor()
    inserir = 'INSERT INTO aluno (nome, telefone, cpf, email, endereco) VALUES (%s, %s, %s, %s, %s)'
    data = (nome, telefone, cpf, email, endereco)
    meucursor.execute(inserir, data)
    banco.commit()
def deletaraluno(id_aluno):
    meucursor = banco.cursor()
    deletar = 'DELETE FROM aluno WHERE id_aluno = %s'
    data = (id_aluno,)
    meucursor.execute(deletar,data)
    banco.commit()

def exibiralunos():
    meucursor = banco.cursor()
    exibir = 'SELECT * FROM aluno'
    meucursor.execute(exibir)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)
    banco.commit()

def inserirmodalidade(nomemodali):
    meucursor = banco.cursor()
    inserir = 'INSERT INTO modalidade (id_modal, nomemodali) VALUES (NULL, %s);'
    data = [(nomemodali)]
    meucursor.execute(inserir,data)
    banco.commit()

def deletarmodalidade(id_modal):
    meucursor = banco.cursor()
    deletar = "DELETE FROM modalidade WHERE id_modal = %s"
    data = (id_modal,)
    meucursor.execute(deletar, data)
    banco.commit()

def exibirmodalidades():
    meucursor = banco.cursor()
    exibir = "SELECT * FROM modalidade"
    meucursor.execute(exibir)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)
    banco.commit()

def inserirfuncionario(nome, cpf, departamento, filhos_fun, salario):
    meucursor = banco.cursor()
    inserirfunc = "INSERT INTO funcionario (nome, cpf, departamento, filhos_fun, salario) VALUES (%s, %s, %s, %s, %s)"
    data = (nome, cpf, departamento, filhos_fun, salario)
    meucursor.execute(inserirfunc, data)
    banco.commit()

def deletarfuncionario(id_funcionario):
    meucursor = banco.cursor()
    deletarfunc = "DELETE FROM funcionario WHERE id_funcionario = %s"
    data = (id_funcionario,)
    meucursor.execute(deletarfunc, data)
    banco.commit()

def exibirfuncionarios():
    meucursor = banco.cursor()
    exibirfunc = "SELECT * FROM funcionario"
    meucursor.execute(exibirfunc)
    result = meucursor.fetchall()
    for x in result:
        print(x)
    banco.commit()

def inserirpersonal(cpf, cref, nome, telefone, email):
    meucursor = banco.cursor()
    inserirperso = "INSERT INTO personal (cpf, cref, nome, telefone, email) VALUES (%s, %s, %s, %s, %s)"
    data = (cpf, cref, nome, telefone, email)
    meucursor.execute(inserirperso, data)
    banco.commit()

def deletarpersonal(cref):
    meucursor = banco.cursor()
    deletarperso = "DELETE FROM personal WHERE cref = %s"
    data = (cref,)
    meucursor.execute(deletarperso, data)
    banco.commit()

def exibirpersonals():
    meucursor = banco.cursor()
    exibirperso = "SELECT * FROM personal"
    meucursor.execute(exibirperso)
    result = meucursor.fetchall()
    for x in result:
        print(x)
    banco.commit()

