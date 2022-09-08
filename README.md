# Book

Imanol Muñiz Ramirez A01701713

Contexto:
En la matería de pothumanismo, ética y tecnología analizamos un capitulo de la serie Black Mirror, Nosedive, en el cual se muestra un futuro distopico en el que existe un "Ranking system" que consiste en que cada persona califica su interacción con otra asignando un número de estrellas entre 1 y 5 y las personas que más constantemente tuvieran buenas calificaciones podían . A mí punto de vista puede que sea un ejercicio bastate ilustrativo como también agresivo por lo que es interesante recrear este sistema como analisis del comportamiento humano.

De acuerdo a los conocimientos y capacidades que se tienen a este momento y los que se pronostican, claro está que es imposible recrear este sistema, por lo que solo lo utilizaremos como inspiración, por lo que se elaborará un programa donde se puedan guardar perfiles para posteriormente ingresar a uno y calificar los demás en base a los comentarios y redes sociales que se muestran sobre la persona buscada. 

Algoritmo:

1. Elige Sign in o Log in.
2. En Sign ingresa, nombre, redes sociales y crea contraseña.
3. En Log in ingresa nombre y contraseña.
4. Se despliega el menú donde las opciones son Mi perfil, Buscar y Salir.
5. Al elegir mi perfil se mostrará la información del usuario con el se hizo log in y estará únicamente la opción de regresae al menú, paso 4.
6. Al elegir Buscar nos pedirá que ingresemos un nombre de una persona
7. Si no existe el nombre registrado en el programa aparece un aviso de que no se encuentra a ese usuario y te redirige al menú, paso 4.
8. Si existe el nombre registrado en el programa, despliega nombre, redes sociales, comentarios y calificación de este usuario.
9. En el perfil de la persona buscada podemos comentar, calificar o regresar al menú, paso 4.
10. Si elegimos la opción salir podrémos volver a elegir entre log in y sign in.  

Avance 2: Añadí el avance dos donde se empezó el diseño de los menus y funciones asi como la creación de una clase.

Avance 3: Se corrigieron errores varios en todo el código, además se implementó la función de clase que ya teniamos getrank y se concluyeron las funciones buscar_persona y menu2. 

Avance 4: Se corrigió un error en el que los comentarios aparecian en todos los perfiles añadiendo el constructor de la clase, además se añadió la posibilidad de poder agragar una descripción a tu perfil y editar la información del usuario una vez que ya ha sido creada la cuenta, para esto se añadieron estructuras de desición pues había que preguntar al usuario si deseaba o no editar alguna parte de su información. 
