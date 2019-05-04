# Opciones de Diccionarios

# Opcion 1

midic={'llave1' :'valor1', 'llave2': 'valor2'}

# Opcion 2

otro_dic= dict(llave1='valor1', llave2='clave2')

print(midic['llave1'])

## Funciones
def mi_primer_funcion(a,b):
    return a+b
mi_primer_funcion(8,9)

#### funcion lambda is the fast way to execute code without full funtion

vari=lambda a:a+1
vari(10)
## Colection of lambda funcion
suma=lambda x,y: x+y
resta=lambda x,y: x-y
multi=lambda x,y: x*y
divd=lambda x,y: x/y
import math
potencia=lambda x,y: math.pow(x,y)
raiz=lambda x,y: math.pow(x,1/y)

lista_funciones=[suma,resta,multi,divd,raiz,potencia]

x=8
y=5

for funciones in lista_funciones():
    resultado=lista_funciones(x,y)

funcines_dic={'suma':suma,'resta':resta,'multiplicar':multi,'division':divd,'raiz':raiz,'potencia':potencia}

print(funcines_dic.items())

