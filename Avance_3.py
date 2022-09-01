from typing import Counter


class perfil:
    name=''
    instagram=''
    password=''
    rank=3
    counter=0

    def getrank(self, score):
        self.counter=self.counter+1
        self.rank=(self.rank + score)/self.counter

    def print_info(self):
        print (f'Nombre: {self.name}')
        print (f'Calificacion: {self.rank}')
        print (f'Instagram: {self.instagram}')


def principal_menu():
    print("Ingresa un 1 si deseas registrarte, 2 si deseas iniciar sesion o 3 si deseas salir del programa")

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
                return
            else:
                print("Password incorrecto")
                return
    print("No existe ese nombre de usuario.")

def menu2(num_persona):
    print('Para buscar personas ingresa 1\nPara ver tu perfil ingresa 2\nPara salir ingresa un 3')
    opcion=int(input())
    if opcion==1:
        print('Escribe el nombre de usuario de la persona que quieres ver')
        buscar_persona(input(),num_persona)
        menu2(num_persona)
    if opcion==2:
        base_de_datos_personas[num_persona].print_info()
        print('Ingresa cualquier cosa para regresar al menu')
        input()
        menu2(num_persona)
    if opcion==3:
        return

def buscar_persona(name,num_persona):
    if name==base_de_datos_personas[num_persona].name:
        base_de_datos_personas[num_persona].print_info()
        print('Ingresa cualquier cosa para regresar al menu')
        input()
        return
    cont=-1
    for obj in base_de_datos_personas:
        cont=cont+1
        if obj.name==name:
            obj.print_info()
            print('Deseas calificar a esta persona? Ingresa 1 si sí, cualquier otro numero para salir')
            op=int(input())
            if op==1:
                print('Ingresa una calificacion del 0 al 5')
                grade=int(input())
                if (grade>=0) and (grade<=5):
                    obj.getrank(grade)
                    print('Informacion actualizada')
                    obj.print_info()
                    return
                else:
                    print('La calificacion que ingresaste no es valida, intentalo nuevamente')   
                    buscar_persona(name,num_persona)
            else:
                return
        print('No se encontro ese nombre de usuario')

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

