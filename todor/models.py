import sqlite3
import pandas as pd

def ejecuta(): 
 df = pd.read_csv(rf"C:\Users\amjjc\Pictures\NUBE\todo-list\todor\ACADEMIA.csv",encoding="utf-8")
 df1 = pd.read_csv(rf"C:\Users\amjjc\Pictures\NUBE\todo-list\todor\DATA.csv",encoding="utf-8")
 df_ = pd.read_csv(rf"C:\Users\amjjc\Pictures\NUBE\todo-list\todor\CARRERAS.csv",encoding="utf-8")
 df__ = pd.read_csv(rf"C:\Users\amjjc\Pictures\NUBE\todo-list\todor\DATOS_CARRERAS.csv",encoding="utf-8")
 df___= pd.read_csv(rf"C:\Users\amjjc\Pictures\NUBE\todo-list\todor\RAMAS.csv",encoding="utf-8")
 df____=pd.read_csv(rf"C:\Users\amjjc\Pictures\NUBE\todo-list\todor\RAMAS_O.csv",encoding="utf-8")
 
 conn= sqlite3.connect('malla.db')
 c= conn.cursor()

 c.execute("""
     CREATE TABLE IF NOT EXISTS EDIFICIOS(
ID INT PRIMARY KEY NOT NULL,
NOMBRE_EDIFICIO VARCHAR(200),
ENCARGADO_EDIFICO VARCHAR(200)


)
"""
)
 
 c.execute("""
CREATE TABLE IF NOT EXISTS ACADEMIAS(
MATRICULA INT PRIMARY KEY NOT NULL,
ACADEMIA VARCHAR(200)  NOT NULL,
FK_ID INT,
FOREIGN KEY(FK_ID) REFERENCES EDIFICIOS(ID)

)
"""
 )
 c.execute(
    """
 CREATE TABLE IF NOT EXISTS CARRERAS(
CLAVE VARCHAR(20) PRIMARY KEY NOT NULL,
CARRERA VARCHAR(200),
PLAN_N INT,
NUM_CREDITOS INT,
SUM_HORAS_TEORIA INT,
SUM_HORAS_PRACTICA INT,
NUM_SEMESTRES INT)
"""    
 )
 c.execute(
"""
CREATE TABLE IF NOT EXISTS DATOS_CARRERAS(
    CLAVE_ASIGNATURA VARCHAR(7) NOT NULL,
    CLAVE VARCHAR(20) NOT NULL,
    ASIGNATURA VARCHAR(200),
    SEMESTRE INT NOT NULL,
    CREDITOS INT NOT NULL,
    HORAS_T INT NOT NULL,
    HPRAS_P INT NOT NULL,
    MAT_ACADEMIA INT NOT NULL,
    PRIMARY KEY(CLAVE_ASIGNATURA),
    FOREIGN KEY (CLAVE) REFERENCES CARRERAS(CLAVE),
    FOREIGN KEY (MAT_ACADEMIA) REFERENCES ACADEMIAS(MATricula)
)
"""   
 )
 c.execute(
"""
CREATE TABLE IF NOT EXISTS RAMAS(

ID INT PRIMARY KEY NOT NULL,
NOMBRE_RAMA VARCHAR(200) NOT NULL,
CLAVE VARCHAR(20) NOT NULL,
NUM_SEMESTRES INT,
CONSTRAINT FK_CARRERA_CLAVE FOREIGN KEY(CLAVE) REFERENCES CARRERAS(CLAVE)


)
"""  
 )
 c.execute(
"""
CREATE TABLE IF NOT EXISTS RAMAS_OPTATIVAS(
FK INT NOT NULL,
CLAVE_ASIGNATURA VARCHAR(7) NOT NULL,
SEMESTRE_CURSE INT NOT NULL,
PRIMARY KEY(FK,CLAVE_ASIGNATURA),
CONSTRAINT FK_ID FOREIGN KEY(FK) REFERENCES RAMAS(ID),
CONSTRAINT FK__CLAVE_ASIGNATURA FOREIGN KEY(CLAVE_ASIGNATURA) REFERENCES DATOS_CARRERAS(CLAVE_ASIGNATURA)
);

"""    
 )
#  edificios(conn,c,df1)

#  query= "SELECT * FROM EDIFICIOS"
# #  c.execute(query)
# #  rows= c.fetchall()

# #  for i in rows:
# #     print(i)
#  consulta(query,conn)

#  academias(c,df)
#  query= "SELECT * FROM ACADEMIAS"
#  consulta(query,conn)

#  carreras(c,df_)
#  query= "SELECT * FROM CARRERAS"
#  consulta(query,conn)

#  datos_carreras(c,df__)
#  query="SELECT * FROM DATOS_CARRERAS"
#  consulta(query,conn)

#  ramas(c,df___)
#  query="SELECT * FROM RAMAS"
#  consulta(query,conn)

#  ramas_optativa(c,df____)
#  query="SELECT * FROM RAMAS_OPTATIVAS"
#  consulta(query,conn)

 conn.commit()
 conn.close()
def consulta(q):
    conn1=sqlite3.connect('malla.db')
    cn= pd.read_sql_query(q,conn1)
    return cn

def insertar(conn,c,id,e,n):
   try:
    query= "INSERT INTO EDIFICIOS VALUES(?,?,?)"
    c.execute(query,(id,e,n))
   except Exception as e:
      print(f"Error {e}")  
def insertar_academia(c,cod,a,fk):
   try:
    query= "INSERT INTO ACADEMIAS VALUES(?,?,?)"
    c.execute(query,(cod,a,fk))
   except Exception as e:
     print(f" error {e}")
def insertar_carrera(c,clave,carrera,plan_n,num_c,horas_t,horas_p,n_s):
   try:
     query="INSERT INTO CARRERAS VALUES(?,?,?,?,?,?,?)"
     c.execute(query,(clave,carrera,plan_n,num_c,horas_t,horas_p,n_s))  
   except Exception as e:
      print(f"error {e}")
def insertar_datos_carrera(c,clave_A,clave,asignatura,semestre,num_c,horas_t,horas_p,mat):
   try:
     query="INSERT INTO DATOS_CARRERAS VALUES(?,?,?,?,?,?,?,?)"
     c.execute(query,(clave_A,clave,asignatura,semestre,num_c,horas_t,horas_p,mat))  
   except Exception as e:
      print(f"error {e}")

def insertar_ramas(c,id,nr,clave,n_s):
   try:
    query= "INSERT INTO RAMAS VALUES(?,?,?,?)"
    c.execute(query,(id,nr,clave,n_s))
   
   except Exception as e:
      print(f"error {e}")

def insertar_ramas_optativa(c,id,clave,n_s):
   try:
    query= "INSERT INTO RAMAS_OPTATIVAS VALUES(?,?,?)"
    c.execute(query,(id,clave,n_s))
   
   except Exception as e:
      print(f"error {e}")
def edificios(conn,c,df):
   j,f= df.shape
   i=0


   while(i < j):

    
     insertar(conn,c, int(df.iloc[i,0]),df.iloc[i,1],df.iloc[i,2])
     i+=1
def academias(c,df):
   j,f= df.shape
   i=0
   while(i < j):
        insertar_academia(c,int(df.iloc[i,0]),df.iloc[i,1],int(df.iloc[i,2]))
        i+=1
def carreras(c,df):
   j,f= df.shape
   i=0

   while(i<j):
       insertar_carrera(c,df.iloc[i,0],df.iloc[i,1],int(df.iloc[i,2]),int(df.iloc[i,3]),int(df.iloc[i,4]),int(df.iloc[i,5]),int(df.iloc[i,6]))
       i+=1
def datos_carreras(c,df):
      j,f= df.shape
      i=0
   
      while(i<j):
          insertar_datos_carrera(c,df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],int(df.iloc[i,3]),int(df.iloc[i,4]),int(df.iloc[i,5]),int(df.iloc[i,6]),int(df.iloc[i,7]))
          i+=1
def ramas(c,df):
   j,f= df.shape
   i=0
      
   while(i<j):
         insertar_ramas(c,int(df.iloc[i,0]),df.iloc[i,1],df.iloc[i,2],int(df.iloc[i,3]))
         i+=1
def ramas_optativa(c,df):
   j,f= df.shape
   i=0
      
   while(i<j):
         insertar_ramas_optativa(c,int(df.iloc[i,0]),df.iloc[i,1],int(df.iloc[i,2]))
         i+=1
    




