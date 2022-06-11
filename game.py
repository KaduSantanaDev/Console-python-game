from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade = int(input('Informe o nivel de dificuldade desejado (1 ,2 ,3 ,4): '))
    calc = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operacao: ')
    calc.mostrar_operacao()

    resultado = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Voce tem {pontos} ponto(s)')

    continuar = int(input('Deseja continuar no jogo (1 - sim, o - nao): '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou com {pontos} ponto(s)')

if __name__ == '__main__':
    main()
