class Consulta:
    
    def __init__(self,cliente,animal,finalidade,horario_marcado,horario_executado):
        self.cliente = cliente
        self.animal = animal
        self.finalidade = finalidade
        self.horario_marcado = horario_marcado
        self.horario_executado = horario_executado

class Animal:
    
    def __init__(self,nome,especie,dat_nasc):
        self.nome = nome
        self.especie = especie
        self.dat_nasc = dat_nasc

class Produto:

    def __init__(self,codigo,preco,quantidade_estoque,nome_produto):
        self.codigo = codigo
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.nome_produto = nome_produto

class Cliente:

    def __init__(self,email,senha,telefone):
        self.email = email
        self.senha = senha
        self.telefone = telefone
