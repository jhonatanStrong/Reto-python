import pandas as pd

class helpers:

    df :object

    #metodo constructor
    def __init__(self, df = None):

        self.df = df

    
    def convertir_df(self,mes = None):

        nwdf =  pd.DataFrame(self.df)
        nwdf.columns = ['d','valor']
        nwdf = nwdf[pd.notnull(nwdf['valor']) ] 
        nwdf[mes] = mes
        nwdf['agno'] = '2023'
        nwdf['fecha'] = pd.to_datetime(nwdf[mes].astype('str')+"/"+nwdf['d'].astype('str')+"/"+nwdf['agno'])
        nwdf = nwdf[['fecha','valor']]
        return nwdf