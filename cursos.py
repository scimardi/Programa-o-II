from peewee import *
from os import *

arq = "cursos.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db 

class Habilidade(BaseModel):

    nome_hab = CharField()
    ano = IntegerField()

    def __str__(self):
        return  self.nome_hab + " no ano de " + str(self.ano)  

class Curso(BaseModel):
    nome = CharField()
    ch = IntegerField()
    nome = CharField()
    habilidades = ManyToManyField(Habilidade)

    def __str__(self):
        res = "Curso de " + self.nome + " com carga horária de " + str(self.ch) + " na escola " + self.escola

        for i in self.habilidades:
            res+=str(i)
        return res

class CursoRealizado(BaseModel):

    nome_aluno = CharField()
    curso = ForeignKeyField(Curso)

    def __str__(self):
        return "Curso feito por " + self.nome_aluno + ". Os seguintes cursos foram realizados: "+ str(self.curso)

if __name__ == "__main__":

    if path.exists(arq):
        remove(arq)

    try:
        db.connect()
        db.create_tables([Habilidade, Curso, CursoRealizado, Curso.habilidades.get_through_model()])

    except OperationalError as e:
        print(e)

    op_comp = Habilidade.create(nome_hab = "operação de computador", ano = 2018)

    linux = Curso.create(nome = "Introdução ao Linux", ch = 60, escola = "Microlins")
    linux.habilidades.add(op_comp)

    aluno = CursoRealizado.create(nome_aluno = "Vânia", curso = linux)

    print(aluno)
