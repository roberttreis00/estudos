class Animal:
    def __init__(self, nu_patas):
        self.nu_patas = nu_patas

    def __str__(self):
        return str([f'{var}={valor}' for var, valor in self.__dict__.items()])


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Cachorro(Mamifero):
    ...


class Gato(Mamifero):
    ...


class Leao(Mamifero):
    ...


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return 'AVE'


class Ornitorrinco(Mamifero, Ave):
    def __int__(self, cor_bico, cor_pelo, nu_patas):
        print(Ornitorrinco.__mro__)
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nu_patas=nu_patas)


# g1 = Gato(2, 'Preto',)
# print(g1.cor_pelo)
g2 = Ornitorrinco(nu_patas=2, cor_pelo='vermelho', cor_bico='azul')

print(g2)
