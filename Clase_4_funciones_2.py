agenda_tel={'juan perez':{'telefono':{'tel1´':83013040,'tel2':88259646},'email':'jperez@gmail'},'carlos rojas':{'telefono':87001030, 'email':'crojas@gmail.com'}, 'ana marin':{'telefono':910003,'email':'ana@gmail.com'}}

def agenda_update(nombre,telefono,email):
    agenda_tel.update({'nombre':nombre,'telefono':telefono, 'email':email})
    #print(agenda_tel)

agenda_update('Carmen Alfaro',853524,'calfaro@gmail.com')
print(agenda_tel)




