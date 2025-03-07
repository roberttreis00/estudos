from itertools import combinations

curso1 = {"Ana", "Bruno", "Carlos", "Daniela"}
curso2 = {"Carlos", "Daniela", "Eduardo", "Fernanda"}
curso3 = {"Ana", "Carlos", "Fernanda", "Gabriel"}
curso4 = {"Irineu", 'Carlos', 'Fernanda'}


def itens_unicos(*conjuntos):
    conjunto_unicos = set.union(*conjuntos)
    unica_aparicao = [i for i in conjunto_unicos if sum([i in x for x in conjuntos]) == 1]  # mais reduzido

    # for i in conjunto_unicos:
    #     apareceu = 0
    #     for x in conjuntos:
    #         if i in x:
    #             apareceu += 1
    #
    #     if apareceu == 1:
    #         unica_aparicao.append(i)

    return unica_aparicao


print(f'Os alunos que participaram de todos os cursos são: {curso1 & curso2 & curso3}')
print(f'Os alunos que participaram de pelo menos um cursos são: {curso1 | curso2 | curso3}')
print()
print(f'Os alunos que participaram de apenas um curso são: {itens_unicos(curso1, curso2, curso3)}')

print(itens_unicos(curso1, curso2, curso3, curso4))
