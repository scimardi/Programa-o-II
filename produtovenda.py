from peewee import *
from os import *

arq = "produtos.db"
db = SqliteDatabase(arq)

class BaseModel (Model):
    class Meta:
        database = db 

class Produto (BaseModel):

    nome = CharField()
    preco_custo = FloatField()
    preco_venda = FloatField()

    def __str__(self):
        return  self.nome + " produzido ao custo de " + str(self.preco_custo) + " reais, vendido por " + str(self.preco_venda) + " reais."

class Venda (BaseModel):
    produtos = ManyToManyField(Produto)
    data = DateField()
    qntd = IntegerField()

    def __str__(self):
        res = "Vendido em " + str(self.data) + " totalizando "+ str(self.qntd) + " unidades."

        for i in self.produtos:
            res+=str(i)
        return res

if __name__ == "__main__":

    if path.exists(arq):
        remove(arq)

    try:
        db.connect()
        db.create_tables([Produto, Venda, Venda.produtos.get_through_model()])

    except OperationalError as e:
        print(e)

    caneta = Produto.create(nome = "caneta", preco_custo = 1.25, preco_venda = 2.5)

    brigadeiro = Produto.create(nome = "brigadeiro", preco_custo = 1.0, preco_venda = 2.0)

    venda1 = Venda.create(data = "06-08-2019", qntd = 4)

    venda2 = Venda.create(data = "06-08-2019", qntd = 3)

    vendas = ([venda1,venda2])

    venda1.produtos.add([caneta, brigadeiro])
    venda2.produtos.add(caneta)

    print(vendas)
