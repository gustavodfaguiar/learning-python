import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print('Posição:', i, ' Valor:', self.valores[i])
    # O(1) - O(2) constante
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
    # O(n)  - Linear
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

if __name__ == "__main__":
    vetor = VetorNaoOrdenado(5)
    vetor.imprime()
    vetor.insere(2)
    vetor.imprime()
    print(vetor.pesquisar(2))
