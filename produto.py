class Produto():
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

class Item():
    def __init__(self,produto,quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Carrinho():
    
    def __init__(self,data,hora,itens):
        self.data = data
        self.hora = hora
        self.itens = itens
   
    def calcula_preco(self):
        preco_total = 0
        for i in self.itens:
            preco_total += i.produto.preco*i.quantidade
        return preco_total


mariajuana = Produto("Mariajuana",500)
coca = Produto("coca",200)
metaafetaamina = Produto("metaafetaamina",600)
cristianocrakudo = Produto("cristianocrakudo",300)

carrinho = Carrinho("24/05","09:15",[Item(metaafetaamina,99999999)])
print(carrinho.calcula_preco())