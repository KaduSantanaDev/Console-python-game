from random import randint

class Calcular:
    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self) -> int:
        return self.__dificuldade

    @property
    def valor1(self) -> int:
        return self.__valor1

    @property
    def valor2(self) -> int:
        return self.__valor2

    @property
    def operacao(self) -> int:
        return self.__operacao

    @property
    def resultado(self) -> int:
        return self.__resultado

    @property
    def _gerar_valor(self) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        elif self.operacao == 3:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'


    def checar_resultado(self, resp: int) -> bool:
        certo = False

        if self.resultado == resp:
            print('Resposta correta')
            certo = True
        else:
            print('Resposta incorreta')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')

    def __str__(self) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Desconhecido'

        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nTipo: {op}' \
