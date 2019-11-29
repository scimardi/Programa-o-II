from peewee import *
import os

arq = 'pokemon.db'

db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Tipo(BaseModel):
    nome = CharField()
    fraqueza = CharField()

    def __str__(self):
        return self.nome + " possui fraqueza de " + self.fraqueza

class Ataque(BaseModel):
    nome = CharField()
    dano = IntegerField()
    tipo = ForeignKeyField(Tipo)

    def __str__(self):
        return self.nome + " possui o dano de " + str(self.dano) + " e tipo " + str(self.tipo)

class Evolucao(BaseModel):
    nome = CharField()
    bonus_atk = IntegerField()
    bonus_def = IntegerField()

    def __str__(self):
        return self.nome + " evolui o ataque em " + str(self.bonus_atk) + " e a defesa em " + str(self.bonus_def)

class Pokemon(BaseModel):
    nome = CharField()
    tipos = ManyToManyField(Tipo)
    ataques = ManyToManyField(Ataque)
    poder_atk = IntegerField()
    poder_def = IntegerField()
    evolucao = ForeignKeyField(Evolucao)

    def __str__(self):
        tipos_str = []
        for i in self.tipos:
            tipos_str.append(i)

        ataques_str = []
        for i in self.ataques:
            ataques_str.append(i)

        return self.nome + " de tipos " + str(tipos_str) +  " possui os ataques " + str(ataques_str) + " de poder de ataque " + str(self.poder_atk) + " e poder de defesa " + str(self.poder_def) + " de evolução " + str(self.evolucao)

class Pokebola(BaseModel):
    tipo = CharField()
    pokemon = CharField()

    def __str__(self):
        return "Pokebola de tipo " + self.tipo + " possui " + self.pokemon

class Recompensa(BaseModel):
    nome = CharField()
    bonus = CharField()

    def __str__(self):
        return self.nome + " dá o bônus de " + self.bonus

class Inventario(BaseModel):
    pokebolas = ManyToManyField(Pokebola)
    recompensas = ManyToManyField(Recompensa)

    def __str__(self):
        poke = []
        for i in self.pokebolas:
            poke.append(i)

        rec = []
        for i in self.recompensas:
            rec.append(i)

        return " " + str(poke) + " pokebolas e " + str(rec) + " recompensas."
        
class Treinador(BaseModel):
    nome = CharField()
    inventario = ForeignKeyField(Inventario)
    pokemons_amigos = ManyToManyField(Pokemon)

    def __str__(self):
        pokem = []
        for i in self.pokemons_amigos:
            pokem.append(i)
        return "O treinador " + self.nome + " cujo inventário possui " + str(self.inventario) + str(pokem)


class Ginasio(BaseModel):
    lider = ForeignKeyField(Treinador)
    recompensa = ForeignKeyField(Recompensa)

    def __str__(self):
        return str(self.lider) + ", líder do Ginásio, dará " + str(self.recompensa)

class Medico(BaseModel):
    nome = CharField()
    local_trab = CharField()
    pokemon = ForeignKeyField(Pokemon)

    def __str__(self):
        return self.nome + " localizado em " + self.local_trab + " curou o Pokémon " + str(self.pokemon)


if __name__ == "__main__":
    
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Tipo, Ataque, Evolucao, Pokemon, Pokemon.tipos.get_through_model(), Pokemon.ataques.get_through_model(), Pokebola, 
        Recompensa, Inventario, Inventario.pokebolas.get_through_model(), Inventario.recompensas.get_through_model(), Treinador, Treinador.pokemons_amigos.get_through_model(),
        Ginasio, Medico])

    except OperationalError as e:
        print(e)

    tipo1 = Tipo.create(nome = "fogo", fraqueza = "água")
    tipo2 = Tipo.create(nome = "dragão", fraqueza = "fada")
    tipo3 = Tipo.create(nome = "elétrico", fraqueza = "terra")
    tipo4 = Tipo.create(nome = "normal", fraqueza = "lutador")

    ataque1 = Ataque.create(nome = "saliva flamejante", dano = 20, tipo = tipo1)
    ataque2 = Ataque.create(nome = "asas do dragão", dano = 15, tipo = tipo2)
    ataque3 = Ataque.create(nome = "choque do trovão", dano = 20, tipo = tipo3) 
    ataque4 = Ataque.create(nome = "chutar", dano = 15, tipo = tipo4)

    evolucao1 = Evolucao.create(nome = "Charizard", bonus_atk = 15 , bonus_def = 10)
    evolucao2 = Evolucao.create(nome = "Raichu", bonus_atk = 15, bonus_def = 10)

    charmander = Pokemon.create(nome = "Charmander", poder_atk = 30, poder_def = 10, evolucao = evolucao1)
    pikachu = Pokemon.create(nome = "Pikachu", poder_atk = 30, poder_def = 10, evolucao = evolucao2)

    charmander.tipos.add([tipo1,tipo2])
    charmander.ataques.add([ataque1, ataque2])

    pikachu.tipos.add([tipo3,tipo4])
    pikachu.ataques.add([ataque3, ataque4])

    pokeball = Pokebola.create(tipo = "Poke Ball" , pokemon = "Charmander")
    greatball = Pokebola.create(tipo = "Great Ball" , pokemon = "Squirtle")
    ultraball = Pokebola.create(tipo = "Ultra Ball" , pokemon = "Pikachu")
    dreamball = Pokebola.create(tipo = "Dream Ball", pokemon = "Jigglypuff")

    recompensa1 = Recompensa.create(nome = "Insígnia de Fogo", bonus = "entrar no estádio de eletricidade")
    recompensa2 = Recompensa.create(nome = "Insígnia de Eletricidade", bonus = "entrar no estádio de água")
    recompensa3 = Recompensa.create(nome = "Insígnia de Água", bonus = "entrar no estádio dos sonhos")
    recompensa4 = Recompensa.create(nome = "Insígnia dos Sonhos", bonus = "entrar no estádio venenoso")

    inventario1 = Inventario.create()
    inventario2 = Inventario.create()

    inventario1.pokebolas.add([pokeball, greatball])
    inventario2.pokebolas.add([ultraball, dreamball])

    inventario1.recompensas.add([recompensa1,recompensa2])
    inventario2.recompensas.add([recompensa3,recompensa4])

    blaze = Treinador.create(nome = "Blaze", inventario = inventario1)
    ash = Treinador.create(nome = "Ash", inventario = inventario2)

    blaze.pokemons_amigos.add([charmander])
    ash.pokemons_amigos.add([pikachu])

    ginasio1 = Ginasio.create(lider = blaze, recompensa = recompensa1)
    ginasio2 = Ginasio.create(lider = ash, recompensa = recompensa2)

    medico1 = Medico.create(nome = "Mistya", local_trab = "rota 1", pokemon = charmander)
    medico2 = Medico.create(nome = "Brookyu", local_trab = "rota 2", pokemon = pikachu)

    print(blaze)