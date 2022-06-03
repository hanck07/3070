import pandas as pd
import numpy as np


data = {
        "UNO": [420,500,800,150],
        "DOS": [1,2,3,6],
}

df = pd.DataFrame(data)


df['Status'] = np.where(df['UNO']>=200,'bien','mal')

print(df)

