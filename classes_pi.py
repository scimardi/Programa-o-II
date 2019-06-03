class Aluno:
    def __init__(self,nome,matricula,turma):
        self.nome = nome
        self.matricula = matricula

class Professor:
    def __init__(self,nome,matricula_prof,areas_atuacao):
        self.nome = nome
        self.matricula_prof = matricula_prof
        self.areas_atuacao = areas_atuacao

class Pi:
    def __init__(self,titulo,ano,alunos,orientadores):
        self.titulo = titulo
        self.ano = ano
        self.alunos = alunos
        self.orientadores = orientadores

guilherme = Aluno("Guilherme",1,"302 Informatica")
nay = Aluno("Naielly",2,"302 Informatica")
benedito = Aluno("Timoteo",24,"302 Informatica")
desconhecido = Professor("?", 0, "?")
pi_da_gente = Pi("Homies",2019,[guilherme,benedito,nay],[desconhecido])
print(pi_da_gente.orientadores[0].areas_atuacao)