def caja_optativa(user_unido, FK,CLAVE_ASIGNATURA,SEMESTRE_CURSE):

 user={
  
     'FK':FK,
     'CLAVE_ASIGNATURA': CLAVE_ASIGNATURA,
     'SEMESTRE_CURSE': SEMESTRE_CURSE,
   
   }    
 user_unido.append(user)
 return user_unido