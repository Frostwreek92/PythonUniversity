print('*** Manejo de Excepciones ***')

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual 0
        if denominador == 0:
            raise Exception('El denominador es igual a 0')

        resultado = numerador / denominador
        print(f'Resultado de la division: {resultado}')
    except Exception as e:
        print(F'Ocurrio un error: {e}')
    else:
        print('No ocurrio ningun error')
    finally:
        print('Terminamos de procesar la excepcion\n')
    # except ZeroDivisionError:
    #     print('No se puede dividir por 0')
    # except TypeError:
    #     print('Los Operandos deben ser numericos')

# Ejemplo de uso
dividir(10, 2)
dividir(10, 0)
dividir(10, '0')