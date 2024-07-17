from modelos.restaurante import Restaurante

restaurante_china = Restaurante('china', 'Comida Chinesa')

restaurante_china.receber_avaliacao('Juan', 10)
restaurante_china.receber_avaliacao('Susy', 5)

def main():
    Restaurante.listar_restaurantes()
    
if __name__== '__main__':
    main()