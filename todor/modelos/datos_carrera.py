
def caja(user_unido,CLAVE_ASIGNATURA,CLAVE,ASIGNATURA,SEMESTRE,CREDITOS,HORAS_T,HORAS_P,MAT_ACADEMIA):

 user={
     'CLAVE_ASIGNATURA':CLAVE_ASIGNATURA,
     'CLAVE': CLAVE,
     'ASIGNATURA': ASIGNATURA,
     'SEMESTRE':SEMESTRE,
     'CREDITOS':CREDITOS,
     'HORAS_T': HORAS_T,
     'HORAS_P':HORAS_P,
     'MAT_ACADEMIA':MAT_ACADEMIA




     }    
 user_unido.append(user)
     # Reemplaza tu bucle 'for' por este:
 for clave, valor in user.items():
        print(f"{clave}: {valor}")
 return user_unido


