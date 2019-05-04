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

#for funciones in lista_funciones():
    #print('resultado:', lista_funciones(x,y))

funcines_dic={'suma':suma,'resta':resta,'multiplicar':multi,'division':divd,'raiz':raiz,'potencia':potencia}

#usando funciones y dic como una calculadora

for f in funcines_dic.values():
    print('resultado=', f(x,y))
