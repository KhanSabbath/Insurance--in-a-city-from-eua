import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from os import path

#endereço do arquivo    documentos/Estudo/ti_estudo/estatistica/aula1/dados/insurance.xlsx
DIRETORIO_AVO= Path('../Estudo/ti_estudo/estatistica/aula1/').resolve()
ENDERECO_ARQUIVO=path.join(DIRETORIO_AVO,'dados', 'insurance.csv')# Ler arquivo
#variavel df recebe toda os dados
df=pd.read_csv(ENDERECO_ARQUIVO) 
print(df)

#plotagem de graficos
# head of     age   sex   bmi  children smoker   region
#bmi vs freq
super_magro=0
normal=0
sobrepeso=0
obeso=0
muito_obeso=0
for _, row in df.iterrows():       #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html . Se vc olhar a documentação desse método, ele retorna duas coisas, o índice da linha e o conteúdo dela Mas, no seu caso, vc não tá usando o índice pra nada, só o row Daí a IA sugeriu vc colocar uma "variável morta", que seria esse _ Daí a IA sugeriu vc colocar uma "variável morta", que seria esse "_" . Como o método retorna duas coisas mas vc só precisa de uma delas, vc pode fazer isso. uando vc vai pegar o retorno de uma função ou método, se essa coisa retornar algo que vc n precise atribuir a uma variável no seu código, vc pode fazer isso _ = func(bla_bla_bla)  
    bmi=row['bmi']
    if bmi<18.5:
        super_magro += 1
    elif 18.5<= bmi <24.9:
        normal += 1
    elif 24.9 <= bmi < 29.9:
        sobrepeso += 1
    elif 29.9<= bmi <39.9:
        obeso += 1
    else:
        muito_obeso += 1

# Impressão dos resultados
print('os dados são os seguintes')
print(f'super magros:{super_magro}, normal:{normal}, sobrepeso:{sobrepeso}, obeso:{obeso} e muito obeso:{muito_obeso}')

#criar um dicionário de contadores
bmi_count={'Super_magro': super_magro, 'Normal': normal, 'Sobrepeso':sobrepeso, 'Obeso': obeso, 'Muito obeso': muito_obeso} 

#Preparação de dados
categoria=list(bmi_count.keys())
frequencia_abs=list(bmi_count.values())

#Criar gráfico
plt.figure(figsize=(8,5))
plt.bar(categoria, frequencia_abs, color='red')
plt.title('Frequência da categorias do IMC nos EUA')
plt.xlabel('Categoria do IMC')
plt.ylabel('Frequência Absoluta')
#plt.ylim(0, 400) 
plt.grid(axis='y', linestyle='--', alpha=0.7)
#plt.tight_layout()

#showww!
plt.show()

#children vs smoker  - número de filhos tem relação com fumar, estresse
#age vs smoker
#region vs bmi
#region vs smoker