import peewee, os 
db = peewee.SqliteDatabase("teste.db")


class Animal(peewee.Model):
    nomedono = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()
    
    class Meta:
        database = db

    def __str__(self):
        return self.tipo_animal," ",self.raca," do ",self.nomedono

class Consulta(peewee.Model):
    data = peewee.CharField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    meu_ID = peewee.CharField()
    
    
    class Meta:
        database = db
    
    def __str__(self):
        return self.servico," ", self.data," ", self.horario," ", self.confirma, " ", self.meu_ID, " Animal: ",str(self.animal)


if __name__ == "__main__":
    arquivo = "teste.db"
    if os.path.exists(arquivo):
        os.remove(arquivo)
    
    try:
        db.connect()
        db.create_tables([Animal,Consulta])
    
    except peewee.OperationalError as e:
        print("erro",str(e))

