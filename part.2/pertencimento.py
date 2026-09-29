# arquivo: pertencimento.py
def existe (estoque, produto):
    #o operador in devolve True/false
    return produto in estoque
if __name__== "__main__":
    lista = ["mouse", "teclado"]
    if existe (lista, "mouse"):
        print ("ja cadrastado")
    else:
        print("pode comprar")