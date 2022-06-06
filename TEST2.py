import pandas as pd

datos = {
    'Nombre' : [1,2,2,3,5,5,5,5,6]
}

df = pd.DataFrame(datos)

print(df.apply(lambda x : x['Nombre'] == 1 , axis=1))
