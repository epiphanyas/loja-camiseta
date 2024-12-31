class Camiseta:
    def __init__(self, nome, tamanho, preco, estoque):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} - Tamanho: {self.tamanho} - Preço: R${self.preco:.2f} - Estoque: {self.estoque}"
    
class Loja:
    def __init__(self):
        self.camisetas = []

    def adicionar_camiseta(self, camiseta):
        self.camisetas.append(camiseta)

    def listar_camisetas(self):
        if not self.camisetas:
            print("Nenhuma camiseta disponível.")
            return
        for camiseta in self.camisetas:
            print(camiseta)

    def comprar_camiseta(self, nome, quantidade):
        for camiseta in self.camisetas:
            if camiseta.nome == nome:
                if camiseta.estoque >= quantidade:
                    camiseta.estoque -= quantidade
                    print(f"Compra realizada: {quantidade} camiseta(s) de {camiseta.nome}.")
                    return
                else:
                    print("Estoque insuficiente.")
                    return
        print("Camiseta não encontrada.")

def main():
    loja = Loja()

    while True:
        print("\nBem-vindo à loja de camisetas!")
        print("1. Adicionar camiseta")
        print("2. Listar camisetas")
        print("3. Comprar camiseta")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome da camiseta: ")
            tamanho = input("Tamanho (P, M, G): ")
            preco = float(input("Preço: R$"))
            estoque = int(input("Quantidade em estoque: "))
            camiseta = Camiseta(nome, tamanho, preco, estoque)
            loja.adicionar_camiseta(camiseta)
            print("Camiseta adicionada com sucesso!")

        elif opcao == '2':
            print("\nCamisetas disponíveis:")
            loja.listar_camisetas()

        elif opcao == '3':
            nome = input("Nome da camiseta que deseja comprar: ")
            quantidade = int(input("Quantidade: "))
            loja.comprar_camiseta(nome, quantidade)

        elif opcao == '4':
            print("Saindo da loja. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()