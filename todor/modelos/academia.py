
def caja_academia(user_unido,MATRICULA,ACADEMIA,FK_ID):

 user={
     'MATRICULA':MATRICULA,
     'ACADEMIA': ACADEMIA,
     'FK_ID': FK_ID
   }    
 user_unido.append(user)
 return user_unido


