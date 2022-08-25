from typing import Counter


class perfil:
    name=''
    instagram=''
    password=''
    rank=0
    counter=0

    def getrank(self, score):
        self.counter=self.counter+1
        self.rank=(self.rank + score)/self.counter

    def print_info(self):
        print (f'Nombre: {self.name}')
        print (f'Calificacion: {self.rank}')
        print (f'Instagram: {self.instagram}')


def principal_menu():
    print("Ingresa un 1 si deseas registrarte, 2 si deseas iniciar sesión o 3 si deseas salir del programa")

def registro():

    print("Escribe tu nombre de usuario: ")
    persona=perfil()
    persona.name=input ()
    print("Escribe tu password: ")
    persona.password=input()
    print("Escribe como te encuentras en instagram: ")
    persona.instagram=input()
    return persona

def iniciar():
    print("Escribe tu nombre de usuario: ")
    name=input()
    cont=-1
    for obj in base_de_datos_personas:
        cont=cont+1
        if obj.name==name:
            print("Escribe tu password ")
            password=input()
            if obj.password==password:
                print("Acceso concedido")
                menu2(cont)
            else:
                print("Password incorrecto")
        else :
            print("No existe ese nombre de usuario.")

def menu2(num_persona):
    print('Para buscar personas ingresa 1\nPara ver tu perfil ingresa 2\nPara salir ingresa un 3')
    opcion=int(input())
    if opcion==1:
        print('Escribe el nombre de usuario de la persona que quieres ver')
        menu2(num_persona)
    if opcion==2:
        base_de_datos_personas[num_persona].print_info()
        print('Ingresa un 3 para regresar al menu')
        input()
        menu2(num_persona)
    if opcion==3:
        principal_menu

principal_menu()
base_de_datos_personas=[]
persona1=perfil()
persona1.name='Imanol'
persona1.password='qaz'
persona1.instagram='Imanol_lonami'
base_de_datos_personas.append(persona1)
contador_de_personas=1
op=int(input())
while op!=3:
    if op==1:
        base_de_datos_personas.append(registro())
        principal_menu()
        op=int(input())
    if op==2:
        iniciar()
        principal_menu()
        op=int(input())

for obj in base_de_datos_personas:
    print( obj.name)
