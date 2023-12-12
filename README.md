# Seminario Sistemas Operativos

## Practica 1: Procesamientos por lotes

<p>
  El programa leera un archivo con el siguiente formato:
  
    b06:bf51:ef0f:7995:d321:4c8b:811c:1e99, Tabby, Jackett, tjackett9@flickr.com, Female, 148.202.30.5 
    
  Como resultado creara un archivo con el siguiente formato:
  
    Jackett : 2822 : 48977 : 61199 : 31125 : 54049 : 19595 : 33052 : 7833 : 94.CA.1E.5
</p>

## Practica 2: Procesamientos por lotes 2

<p>
  El programa recibira la ubicacion de una carpeta
  <li>
    Se creara una copia de todos los archivos y carpetas.
  </li>
  <li>
    Las letras se cambiaran por digitos del 0 al 9.
  </li>
  <li>
    Los digitos se cambiaran por letras mayusculas.
  </li>
</p>

## Practica 3: Algoritmos de planificacion 1

<p>
  Utilizando los procesos definidos en el archivo se simulara los siguientes algoritmos:
  <li>
    Round Robin (lapso)
  </li>
  <li>
    SJF (El mas corto  primero)
  </li>
  <li>
    FIFO (El primero en llegar, el primero en salir)
  </li>
  <li>
    Prioridades (Establece prioridades)
  </li>
</p>

## Practica 4: Algoritmos de planificacion 2
<p>
  Se utiliza la practica 3: algoritmos de planificacion 1 y se agregan las siguientes opciones:
  <ul>
    <li>Se agrega la opcion de agregar procesos</li>
    <ul>
      <li>Nombre de proceso</li>
      <li>Tiempo de duracion</li>
      <li>Prioridad</li>
      <li>Posicion (principio o final)</li>
    </ul>
    <li>Dar la opcion de poder elegir cualquier de los 4 algorimtos </li>
    <ul>
      <li>Round Robin (lapso)</li>
      <li>SJF (El mas corto  primero)</li>
      <li>FIFO (El primero en llegar, el primero en salir)</li>
      <li>Prioridades (Establece prioridades)</li>
    </ul>
  </ul>
</p>

## Practica 5: Administrador de memoria 1
<p>
  Utilizando los procesos definidos en el archivo se simulara los siguientes algoritmos:
  <ul>
    <li>Primer ajuste</li>
    <li>Mejor ajuste</li>
    <li>Peor ajuste</li>
    <li>Siguiente ajuste</li>
  </ul>
</p>

## Practica 6: Hilos
<p>
  Mover dos imagenes al mismo tiempo
  <ul>
    <li>Mover una imagen de izquierda a derecha</li>
    <li>Mover una imagen de arriba hacia abajo</li>
  </ul>
</p>

## Practica 7: Productor - Consumidor 1
<p>
  Se realizo un programa que controle la entrada y salida de un estacionamiento.
  <ul>
    <li>El estacionamiento tiene un tamaño de 12.</li>
    <li>El programa añade un auto con una frecuencia de 0.5, 1 o 2 segundos elegidos de manera aletoria.</li>
    <li>El usuario puede modificar la frecuencia en la que se añaden autos.</li>
    <li>El programa retira un auto con una frecuencia de 0.5, 1 0 2 segundos elegidos de manera aleatoria.</li>
    <li>El usuario puede modificar la frecuencia en la que se retiran autos. </li>
    <li>No se pueden retirar autos si el estacionamiento esta vacio.</li>
    <li>No se pueden añadir autos si el estacionamiento esta lleno.</li>
  </ul>
</p>
