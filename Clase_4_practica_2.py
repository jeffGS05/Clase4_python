agenda_tel={'juan perez':{'telefono':{'tel1´':83013040,'tel2':88259646},'email':'jperez@gmail'},'carlos rojas':{'telefono':87001030, 'email':'crojas@gmail.com'}, 'ana marin':{'telefono':910003,'email':'ana@gmail.com'}}
agenda_tel.update({'sofia castro':{'telefono':8785512, 'email':'sofiac@gmail.com'}})

for contacto,info in agenda_tel.items():
    print('nombre',contacto, 'telefono',info['telefono'],'correo',info['email'])

for persona in agenda_tel.keys():
    print('nombre:',persona,
    'telefono:',persona,
    'email:', persona)
