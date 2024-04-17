class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.disciplinas = []
        self.salas = []

    def __str__(self):
        return f"Curso: {self.nome} ({self.codigo})"


class Disciplina:
    def __init__(self, nome, codigo, professor):
        self.nome = nome
        self.codigo = codigo
        self.professor = professor

    def __str__(self):
        return f"Disciplina: {self.nome} ({self.codigo}) - Professor: {self.professor.nome}"


class Endereco:
    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return f"Endereço: {self.rua}, {self.cidade}, {self.estado} - CEP: {self.cep}"


class Professor:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Professor: {self.nome} ({self.matricula})"

class Aluno:
    def __init__(self, nome, matricula, curso, endereco):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.endereco = endereco

    def __str__(self):
        return f"Aluno: {self.nome} ({self.matricula}) - Curso: {self.curso.nome}"

class Sala:
    def __init__(self, numero, predio, capacidade):
        self.numero = numero
        self.predio = predio
        self.capacidade = capacidade

    def __str__(self):
        return f"Sala: {self.numero}, {self.predio} - Capacidade: {self.capacidade}"

endereco1 = Endereco("Rua A", "Serra Talhada", "Pernambuco", "56900-000")

curso1 = Curso("Sistemas de Informação", "SI014")

aluno1 = Aluno("Fred Mercy", "2023001", curso1, endereco1)

professor1 = Professor("Nick Hope", "P123")

disciplina1 = Disciplina("Programação I", "PROG101", professor1)

curso1.disciplinas.append(disciplina1)

sala1 = Sala("12", "Bloco 2", 50)

curso1.salas.append(sala1)

print(aluno1)
print(professor1)
print(disciplina1)
print(curso1)
print(sala1)
print(endereco1)
