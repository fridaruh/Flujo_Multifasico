# import module
import streamlit as st
 
# Title
st.title("Proyecto Flujo Maltifasico")
st.text('Por: Daniela Camacho')

st.header('Yacimiento')
st.text('Ingresa los datos del yacimiento para realizar su clasificación:') 
st.text('')
st.text_input('Nombre del yacimiento')
st.text('')

col1, col2 = st.columns(2)

with col1:
    st.text('Composición(%mol)')
    H2S = st.text_input('H2S')
    CO2 = st.text_input('CO2')
    N2 = st.text_input('N2')
    C1 = st.text_input('C1')
    C2 = st.text_input('C2')
    C3 = st.text_input('C3')
    iC4 = st.text_input('iC4')
    nC4= st.text_input('nC4')
    iC5 = st.text_input('iC5')
    nC5 = st.text_input('nC5')
    C6 = st.text_input('C6')
    C7 = st.text_input('C7+')

    Total = H2S + CO2 + N2 + C1 + C2 + C3 + iC4 + nC4 + iC5 + nC5 + C6 + C7

    st.info('Total: ' + str(Total))
    st.text('')
    st.text('Resultado de procesamiento:')
    if Total == '':
        st.error('Ingrese los datos')
    elif float(Total) == 1:
        st.success('Datos correctos')
    else: 
        st.error('El total debe ser 1')

with col2:
    st.text('')
    st.text('')
    p_C7 = st.text_input('p C7+')
    pm_c7 = st.text_input('PM C7+')
    C2_C6 = st.text_input('C2 - C6')
    p_mprom = st.text_input('P mprom')
    pi = st.text_input('Pi (Kg/cm2)')
    ty = st.text_input('Ty (°C)')
    prof = st.text_input('Prof (mbnm)')
    pb_pr = st.text_input('Pb/Pr (kg/cm2)')
    bob = st.text_input('Bob (m3/m3)/zn@Pb')
    rsb = st.text_input('Rsb (m3/m3)/ (porc cond max)')
    rga = st.text_input('RGA (m3/m3)')
    po_ce = st.text_input('po @ ce (gr/cm3)')
    api = st.text_input('°API')

    
## Variables pre-calculadas ##

#Tabla de componentes a comparar
#inicializando las variables
gas_seco_eval = 0
gas_humedo_eval = 0
gas_y_condensado_eval = 0
aceite_cercano_al_punto_eval = 0
aceite_volatil_eval = 0
aceite_negro_eval = 0

##Variables CO2

Gas_seco_co2=0.10
Gas_húmedo_co2=1.41
Gas_y_condensado_co2=2.37
Aceite_cercano_al_punto_critico_co2=1.3
Aceite_volatil_co2=0.93
Aceite_negro_co2=0.02

###Evaluacion CO2
CO2_list = [Gas_seco_co2,Gas_húmedo_co2,Gas_y_condensado_co2,Aceite_cercano_al_punto_critico_co2,Aceite_volatil_co2,Aceite_negro_co2]

CO2_comparaciones=[]
for co2 in CO2_list:
    valor = abs(float(CO2) - float(co2)) 
    CO2_comparaciones.append(valor)

resultado_CO2_val = CO2_comparaciones.index(min(CO2_comparaciones))

if resultado_CO2_val == 0:
   gas_seco_eval= gas_seco_eval + 1
elif resultado_CO2_val == 1:
    gas_humedo_eval =+ 1
elif resultado_CO2_val == 2:
    gas_y_condensado_eval =+ 1
elif resultado_CO2_val == 3:
    aceite_cercano_al_punto_eval =+ 1
elif resultado_CO2_val == 4:
    aceite_volatil_eval =+ 1
else:
    aceite_negro_eval =+1

#### Variables N2

Gas_seco_N2=2.07
Gas_húmedo_N2=0.25
Gas_y_condensado_N2=0.31
Aceite_cercano_al_punto_critico_N2=0.56
Aceite_volatil_N2=0.21
Aceite_negro_N2=0.34

##### Evaluación N2

N2_list = [Gas_seco_N2, Gas_húmedo_N2, Gas_y_condensado_N2, Aceite_cercano_al_punto_critico_N2, Aceite_volatil_N2, Aceite_negro_N2]

N2_comparaciones = []
for n2 in N2_list:
    valor = abs(float(N2) - float(n2)) 
    N2_comparaciones.append(valor)

resultado_N2_val =N2_comparaciones.index(min(N2_comparaciones))

if resultado_N2_val == 0:
    gas_seco_eval = gas_seco_eval + 1
elif resultado_N2_val == 1:
    gas_humedo_eval = gas_humedo_eval + 1
elif resultado_N2_val == 2:
    gas_y_condensado_eval = gas_y_condensado_eval + 1
elif resultado_N2_val == 3:
    aceite_cercano_al_punto_eval = aceite_cercano_al_punto_eval + 1
elif resultado_N2_val == 4:
    aceite_volatil_eval = aceite_volatil_eval + 1
else:
    aceite_negro_eval = aceite_negro_eval +1

###### Variables C1

Gas_seco_C1=86.12
Gas_humedo_C1=92.46
Gas_y_condensado_C1=73.19
Aceite_cercano_al_punto_critico_C1=69.44
Aceite_volatil_C1=58.77
Aceite_negro_C1=34.62

##### Evaluación C1

C1_list = [Gas_seco_C1, Gas_humedo_C1, Gas_y_condensado_C1, Aceite_cercano_al_punto_critico_C1, Aceite_volatil_C1, Aceite_negro_C1]

C1_comparaciones = []
for c1 in C1_list:
    valor = abs(float(C1) - float(c1)) 
    C1_comparaciones.append(valor)

resultado_C1_val =C1_comparaciones.index(min(C1_comparaciones))

if resultado_C1_val == 0:
    gas_seco_eval = gas_seco_eval + 1
elif resultado_C1_val == 1:
    gas_humedo_eval = gas_humedo_eval + 1
elif resultado_C1_val == 2:
    gas_y_condensado_eval = gas_y_condensado_eval + 1
elif resultado_C1_val == 3:
    aceite_cercano_al_punto_eval = aceite_cercano_al_punto_eval + 1
elif resultado_C1_val == 4:
    aceite_volatil_eval = aceite_volatil_eval + 1
else:
    aceite_negro_eval = aceite_negro_eval +1



## Después de todas las evaluaciones

evaluaciones = [gas_seco_eval,gas_humedo_eval,gas_y_condensado_eval,aceite_cercano_al_punto_eval,aceite_volatil_eval,aceite_negro_eval ]

resultado_total_val = evaluaciones.index(max(evaluaciones))

if resultado_total_val == 0:
    resultante_tablas = 'Gas seco'
elif resultado_total_val == 1:
    resultante_tablas = 'Gas húmedo'
elif resultado_total_val == 2:
    resultante_tablas = 'Gas y condensado'
elif resultado_total_val == 3:
    resultante_tablas = 'Aceite cercano al punto crítico'
elif resultado_total_val == 4:
    resultante_tablas = 'Aceite volátil'
else:
    resultante_tablas = 'Aceite negro'










Gas_seco_C2=5.91

Gas_húmedo_C2=3.18

Gas_y_condensado_C2=7.8

Aceite_cercano_al_punto_critico_C2=7.88

Aceite_volatil_C2=7.57

Aceite_negro_C2=4.11

Gas_seco_C3=3.58

Gas_húmedo_C3=1.01

Gas_y_condensado_C3=3.55

Aceite_cercano_al_punto_critico_C3=4.26

Aceite_volatil_C3=4.09

Aceite_negro_C3=1.01

Gas_seco_iC4=1.72

Gas_húmedo_iC4=0.28

Gas_y_condensado_iC4=0.71

Aceite_cercano_al_punto_critico_iC4=0.89

Aceite_volatil_iC4=0.91

Aceite_negro_iC4=0.76

Gas_seco_nC4=''

Gas_húmedo_nC4=0.24

Gas_y_condensado_nC4=1.45

Aceite_cercano_al_punto_critico_nC4=2.14

Aceite_volatil_nC4=2.09

Aceite_negro_nC4=0.49

Gas_seco_iC5=0.50

Gas_húmedo_iC5=0.13

Gas_y_condensado_iC5=0.64

Aceite_cercano_al_punto_critico_iC5=0.9

Aceite_volatil_iC5=0.77

Aceite_negro_iC5=0.43

Gas_seco_nC5=''

Gas_húmedo_nC5=0.08

Gas_y_condensado_nC5=0.68

Aceite_cercano_al_punto_critico_nC5=1.13

Aceite_volatil_nC5=1.15

Aceite_negro_nC5=0.21

Aceite_negro_C6=1.61

Gas_seco_C7=''

Gas_húmedo_C7=0.82

Gas_y_condensado_C7=8.21

Aceite_cercano_al_punto_critico_C7=10.04

Aceite_volatil_C7=21.76

Aceite_negro_C7=56.4

#El renglon Total = 100 es la suma de todos los elementos

Gas_seco_MC7=''

Gas_húmedo_MC7=130

Gas_y_condensado_MC7=''

Aceite_cercano_al_punto_critico_MC7=''

Aceite_volatil_MC7=''

Aceite_negro_MC7=''

Gas_seco_PMC7=''

Gas_húmedo_PMC7=0.763

Gas_y_condensado_PMC7=''

Aceite_cercano_al_punto_critico_PMC7=''

Aceite_volatil_PMC7=''

Aceite_negro_PMC7=''

Gas_seco_RGA='' #En Scf/bl

Gas_húmedo_RGA=105000 #En Scf/bl

Gas_y_condensado_RGA=5450 #En Scf/bl

Aceite_cercano_al_punto_critico_RGA=3650 #En Scf/bl

Aceite_volatil_RGA=1490 #En scf/bl

Aceite_negro_RGA=300 #En scf/bl

Gas_seco_RGA='' #En m3/m3

Gas_húmedo_RGA=18700 #En m3/m3

Gas_y_condensado_RGA=970 #En m3/m3

Aceite_cercano_al_punto_critico_RGA=650 #En m3/m3

Aceite_volatil_RGA=263 #En m3/m3

Aceite_negro_RGA=53 #En m3/m3

Gas_seco_RGC=''

Gas_húmedo_RGC=10

Gas_y_condensado_RGC=180

Aceite_cercano_al_punto_critico_RGC=275

Aceite_volatil_RGC=''

Aceite_negro_RGC=''

Gas_seco_API=''

Gas_húmedo_API=57

Gas_y_condensado_API=49

Aceite_cercano_al_punto_critico_API=45

Aceite_volatil_API=38

Aceite_negro_API=24

Gas_seco_Yg=''

Gas_húmedo_Yg=0.61

Gas_y_condensado_Yg=0.7

Aceite_cercano_al_punto_critico_Yg=0.71

Aceite_volatil_Yg=0.7

Aceite_negro_Vg=0.63

Gas_seco_Psat='' #en PSIa

Gas_húmedo_Psat=3430 #en PSIa

Gas_y_condensado_Psat=6500 #en PSIa

Aceite_cercano_al_punto_Psat=7015 #en PSIa

Aceite_volatil_Psat=5420 #en PSIa

Aceite_negro_Psat=2810 #en PSIa

Gas_seco_Psat=''#en kg/cm2

Gas_húmedo_Psat=241 #en kg/cm2

Gas_y_condensado_Psat=461 #en kg/cm2

Aceite_cercano_al_punto_Psat=493 #en kg/cm2

Aceite_volatil_Psat=381 #en kg/cm2

Aceite_negro_Psat=137 #en kg/cm2

Gas_seco_Bgb=''#en bl/bl

Gas_húmedo_Bgb=0.0051 #en bl/bl

Gas_y_condensado_Bgb=0.0039 #en bl/bl

Aceite_cercano_al_punto_Bgb=2.78 #en bl/bl

Aceite_volatil_Bgb=1.73 #en bl/bl

Aceite_negro_Bgb=1.16 #en bl/bl

Gas_seco_Bob=''#en bl/bl

Gas_húmedo_Bob=0.0051 #en bl/bl

Gas_y_condensado_Bob=0.0039 #en bl/bl

Aceite_cercano_al_punto_Bob=2.78 #en bl/bl

Aceite_volatil_Bob=1.73 #en bl/bl

Aceite_negro_Bob=1.16 #en bl/bl

Gas_seco_pb='' #en lb/ft3

Gas_húmedo_pb=9.61 #en lb/ft

Gas_y_condensado_pb=26.7 #en lb/ft3

Aceite_cercano_al_punto_critico_pb=30.7 #en lb/ft3

Aceite_volatil_pb=38.2 #en lb/ft3

Aceite_negro_pb=51.4 #en lb/ft3

gas_seco_pb='' #en gr/cm3

Gas_húmedo_pb=0.15 #en gr/cm3

Gas_y_condensado_pb=0.42 #en gr/cm3

Aceite_cercano_al_punto_critico_pb=0.49 #en gr/cm3

Aceite_volatil_pb=0.61 #en gr/cm3

Aceite_negro_pb=0.82 #en gr/cm3


## McCain

##### Mendez

Mendez_RGA_Aceite_negro=200

Mendez_RGA_Aceite_volatil=200-1000

Mendez_RGA_Gas_y_condensado=587-8905

Mendez_Bo_Aceite_negro= 2

Mendez_Bo_Aceite_volatil=2

Mendez_Bo_Gas_y_condensado=''

Mendez_po_Aceite_negro= 0.85  #0.85/<34.9

Mendez_po_Aceite_volatil=0.75-0.85/49.9-35

Mendez_po_Gas_y_condensado=0.75-0.80/57.1-45

Mendez_C7_Aceite_negro=20

Mendez_C7_Aceite_volatil=12.5-25

Mendez_C7_Gas_y_condensado=3-12.5

Perez_RGA_Aceite_negro=20>150

Perez_RGA_Aceite_volatil=160>600

Perez_RGA_Gas_y_condensado=500>9000

Perez_C1_Aceite_negro=13>34

Perez_C1_Aceite_volatil=38>62

Perez_C1_Gas_y_condensado=62>88

Perez_C2_C6_Aceite_negro=17>34

Perez_C2_C6_Aceite_volatil=11>32

Perez_C2_C6_Gas_y_condensado=10>24

Perez_C7_Aceite_negro=36>48

Perez_C7_Aceite_volatil=12>21

Perez_C7_Gas_y_condensado=0>14

### Conteo de puntos para componentes a comparar

### Conteo de puntos para Méndez

### Conteo de puntos para Pérez

### Conteo de puntos para Cronquist

### Conteo de puntos para León-Alamilla


################ Muestra de resultados

st.header('Resultados de las clasificaciones')

st.text(evaluaciones)

st.text(f'Según Tabla de componentes a comparar: ' + resultante_tablas)

st.text('Según Méndez:')

st.text('Según Pérez:')

st.text('Según Cronquist:')

st.text('Según León-Alamilla:')