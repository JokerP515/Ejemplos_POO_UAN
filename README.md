# Ejemplos_POO_UAN
En este repositorio, estarán los ejemplos hechos para los talleres de POO


## Ejemplo de Herencia

Source file name: [ejemplo_herencia.py](/ejemplo_herencia.py)

En este contexto, la clase "Coche" hereda las caracteristicas de la clase "Vehiculo", en esta última clase, hay atributos que pueden aplicar a cualquier vehiculo, como marca, modelo, color, etc. Pero en la clase "Coche", ya hay atributos más especificos como el tipo de combustible que usa y el número de puertas que hay, sin perder las otras caracteristicas que no es necesario definirlas de nuevo sino heredarlas, como marca, modelo y año. Para poder usar la herencia en Python, es necesario usar el método "super()" de esta manera, se puede obtener los atributos que necesitemos de la clase padre.

## Ejemplo de Polimorfismo

Source file name: [ejemplo_polimorfismo.py](/ejemplo_polimorfismo.py)

En este contexto, la clase Animal tiene un método llamado "hacer_sonido" que está presente en sus respectivas clases hijas, al invocar el mismo mensaje en cada clase hija, dará una respuesta distinta Esto se puede comprobar observando el bucle al final del código

## Ejemplo de Herencia y Polimorfismo

Source file name: [ej_herencia_polimorfismo.py](/ej_herencia_polimorfismo.py)

En este contexto, la clase "Persona" es la clase padre, tiene el método saludar incluido con los atributos nombre y edad y sus clase hijas son "Profesor" y "Estudiante" que hereda aquellos atributos junto a definir uno más el cual es el grado del estudiante y la materia del profesor además de implementar polimorfismo para el método "saludar". Esto dará un saludo personalizado a cada clase

