print('*** Decoradores en Python ***')

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la funcion saludar')
        resultado = funcion(*args, **kwargs) # llamamos a nuestra funcion
        print('Despues de llamar la funcion saludar')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Carlos')