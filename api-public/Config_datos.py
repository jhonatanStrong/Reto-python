from model.helpers import helpers as h
from model import Valor_fiscal as v 
import pandas  as pd
import json as j
from confg import cfg as c

class Config_datos():


    def funion_datos(self,):
        
        p = v.Valor_fiscal('Jhonatan','12/02/1993',c.RUTA_ARCHIVO,c.NOMBRE_ARCHIVO)
        a = p.load_data()
        df =pd.DataFrame(a)
        na =p.transform_Data(df)
        na['fecha'] = na['fecha'].dt.strftime('%Y-%m-%d')
        nw = na.to_dict()

        jsonData = j.dumps(nw)
        
        return nw

