
from .modelos.datos_carrera import caja
from .modelos.academia import caja_academia
from .modelos.carreras import caja_carrera
from .modelos.ramas import caja_ramas
from .modelos.ramas_optativa import caja_optativa
from . import models

def visualiza_datos_carreras(q):
            user=[]
            user_f=[]
            df= models.consulta(q)
            print()
            i=0
            c,f= df.shape
            k=0
            while(i <c):
                 k=0
                 while(k<f):
                    # print(df.iloc[i,k], end=" ")
                    k+=1
                 user=caja(user_f,df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],int(df.iloc[i,3]),int(df.iloc[i,4]),int(df.iloc[i,5]),int(df.iloc[i,6]),int(df.iloc[i,7]))
                 
                 i+=1
            return user
def visualiza_academia(q):
            user=[]
            user_f=[]
            df= models.consulta(q)
            print()
            i=0
            c,f= df.shape
            k=0
            while(i <c):
                 k=0
                 while(k<f):
                    k+=1
                 user= caja_academia(user_f,int(df.iloc[i,0]),df.iloc[i,1],int(df.iloc[i,2]))
                 
                 i+=1
            return user

def visualiza_carrera(q):
       user=[]
       user_f=[]
       df= models.consulta(q)
       print()
       i=0
       k=0
       c,f=df.shape
       while(i <c):
        k=0
        while(k<f):
            k+=1
        user= caja_carrera(user_f,df.iloc[i,0],df.iloc[i,1],int(df.iloc[i,2]),
                               int(df.iloc[i,3]),int(df.iloc[i,4]),int(df.iloc[i,5]),int(df.iloc[i,6]))
          #   print(user)
        i+=1
       return user

def visualiza_ramas(q):
       user=[]
       user_f=[]
       df= models.consulta(q)
       print()
       i=0
       k=0
       c,f=df.shape
       while(i <c):
        k=0
        while(k<f):
            k+=1
        user= caja_ramas(user_f,int(df.iloc[i,0]),df.iloc[i,1],df.iloc[i,2],int(df.iloc[i,3]))
          #   print(user)
        i+=1
       return user
def visualiza_optativa(q):
       user=[]
       user_f=[]
       df= models.consulta(q)
       print()
       i=0
       k=0
       c,f=df.shape
       while(i <c):
        k=0
        while(k<f):
            k+=1
        user= caja_optativa(user_f,int(df.iloc[i,0]),df.iloc[i,1],int(df.iloc[i,2]))
          #   print(user)
        i+=1
       return user