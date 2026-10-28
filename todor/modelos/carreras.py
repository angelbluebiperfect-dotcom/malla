
def caja_carrera(user_unido,CLAVE,CARRERA,PLAN_N,NUM_CREDITOS,SUM_HORAS_TEORIA,SUM_HORAS_PRACTICA,NUM_SEMESTRES):

 user={
     'CLAVE':CLAVE,
     'CARRERA':CARRERA,
     'PLAN_N': PLAN_N,
     'NUM_CREDITOS':NUM_CREDITOS,
     'SUM_HORAS_TEORIA':SUM_HORAS_TEORIA,
     'SUM_HORAS_PRACTICA':SUM_HORAS_PRACTICA,
     'NUM_SEMESTRES':NUM_SEMESTRES

     }    
 user_unido.append(user)
     # Reemplaza tu bucle 'for' por este:
#  for clave, valor in user.items():
#         print(f"{clave}: {valor}")
 return user_unido