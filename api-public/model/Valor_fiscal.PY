#from ..confg import cfg
import datetime
from pandas import pandas as pd
from .helpers import helpers as h
import json as j


class Valor_fiscal:

    #inicializacion de la variables
    monto : int
    fecha_monto : datetime
    ruta : str
    archivo : str
    


    #metodo constructor
    def __init__(self, monto = None, fecha_monto = None , ruta = None , archivo = None):
        self.monto = monto
        self.fecha_monto = fecha_monto
        self.archivo = archivo
        self.ruta = ruta
    
    def __str__(self,):

        return f"{self.monto}({self.fecha_monto})"
    
    def load_data(self):
            #self.ruta+str("/")+self.archivo
        df = pd.read_csv(self.ruta+str("/")+self.archivo,delimiter=';')

        return df
    def transform_Data(self,df : object):

        df =pd.DataFrame(df)
        df
        ltdf = list()
        cal2 = pd.DataFrame()

        df.columns =  [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12]

        ltc = df.columns

        for x in range(1,len(ltc),1):
            dfn = df[[0,x]]
            cal = h.helpers(dfn)
            cal1 = cal.convertir_df(mes = x)
            ltdf.append(cal1)
            cal2 = pd.concat([cal2,cal1],ignore_index=True )

        return cal2 





#p = Valor_fiscal("jhonatan","12/02/1993","C:/Users/jhcontreras/Documents/3.PERSONAL THINGS/7.Programacion/1.Estudio Personal/2.python\Reto de Python/api-public/archivo_manuales","UF2023.csv")
#a = p.load_data()
#df =pd.DataFrame(a)
#na =p.transform_Data(df)
##print(na)
#
#na['fecha'] = na['fecha'].dt.strftime('%Y-%m-%d')
##nw = na.to_json()
#
#nw = na.to_dict()
#print(j.dumps(nw))



