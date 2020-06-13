.. Tkinter con Python3 documentation master file, created by
   sphinx-quickstart on Sat Jun 13 13:10:09 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tkinter con Python3
===================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Introducción
================================================================================

Python es un lenguaje de programación muy potente que se caracteriza por incluir un montón de módulos en su instalación estándar. Uno de estos módulos es ``tkinter`` que permite la construcción de interfaces gráficas de usuario.

Este módulo incluye no solo muchos controles como botones o cajas de texto sino también dos **gestores de geometría** que permiten incluir elementos en una ventana y permitir a estos algoritmos el redibujado de controles cuando una ventana cambia de tamaño.

Sin embargo su uso puede ser relativamente complicado, especialmente al principio. En este documento se explica como trabajar con el gestor de geometría llamado ``grid``, el más flexible pero también el más complejo de usar de los dos.

Primer programa
================================================================================

Todo programa ``tkinter`` se caracteriza por

* Instancia un objeto de la clase ``Tk`` **una y solo una vez** . Este objeto es la "ventana principal" del programa.

* Debemos siempre llamar al método ``mainloop`` de este objeto. Este método tomará el control y se ejecutará hasta que cerremos la ventana (de hecho ejecuta el bucle de gestión de eventos de ``tkinter``) 

Un primer programa mínimo sería así:

.. literalinclude:: src/programa1.py
   :language: python

Y mostraría esto:

.. figure:: ./img/programa1.png
    :scale: 60%
    :align: center
    :figclass: align-center

    Programa mínimo en tkinter


Añadiendo controles
================================================================================

En ``tkinter`` el proceso de construcción del GUI está basado en objetos pero la mecánica general es que **creamos objetos y en dicha creación indicamos qué objeto va a ser el padre o contenedor.** Este proceso es bastante distinto del de Java donde lo que se hace es crear un objeto contenedor, luego un control y luego llamar hace algo como ``contenedor.add(control)`` 

Así, por ejemplo, podemos añadir un botón a nuestra ventana usando un programa como el siguiente:


.. literalinclude:: src/programa2.py
   :language: python

Que mostraría esto:

.. figure:: ./img/programa2.png
    :align: center
    :figclass: align-center

    Un botón en tkinter

El gestor de geometría ``grid`` 
================================================================================

En el programa anterior ya podemos ver que al usar ``grid`` debemos indicar la fila y la columna en la que se ubica el botón. Así, en el programa anterior hemos creado un botón y le hemos ordenador que se integre en la rejilla del contenedor padre (en este caso la ventana raíz) en la posición (0,0)

Es importante observar las diferencias de ``tkinter`` con respecto a otros lenguajes, como por ejemplo en Java. En Java se crea un contenedor, al contenedor se le asigna una geometría y luego se llama al método ``add`` del contenedor. Sin embargo, en ``tkinter`` el hijo "ordena indirectamente al padre" que se cree una rejilla. Recordamos también que en ``tkinter`` al crear un control se debe indicar en esa creación quien es el control padre o contenedor.

En un grid hay algunas consideraciones importantes:

* **Cuantas filas y columnas va a tener el grid**. Esta cantidad no se indica "a priori" sino que a medida que vayamos construyendo elementos podemos ir indicando nuevas coordenadas.

* **Cuantas filas y columnas va a ocupar un control** . Un control puede ocupar más espacio y no limitarse solo a "una celda de la tabla".

* **Qué peso va a tener cada fila y cada columna** . Si una ventana se redimensiona y se hace más grande o más pequeña podemos decidir como repartir proporcionalmente el espacio sobrante. Esto no es obligatorio de hacer pero ayuda a conseguir diseños bastante flexibles que se adaptan automáticamente a distintas resoluciones.


Veamos estos puntos uno por uno.


Filas y columnas de un grid
--------------------------------------------------------------------------------

Supongamos que queremos crear un interfaz como este:

.. figure:: ./img/programa3-1.png
    :align: center
    :figclass: align-center

    Una matriz de botones


Un posible programa podría ser este. Como se puede ver, se pueden usar los parámetros ``row`` y ``column`` para indicar la posición en la que debe ubicarse un control:

.. literalinclude:: src/programa3.py
   :language: python

Este programa parece tener un aspecto razonable. Pero veamos lo que ocurre si agrandamos la ventana:

.. figure:: ./img/programa3-2.png
    :align: center
    :figclass: align-center

    Desaprovechamiento del espacio

Como vemos, al agrandar la ventana *los botones no se agrandan.* No solo se desperdicia espacio sino que también el aspecto del interfaz es poco profesional. Sin embargo este programa nos ha permitido ilustrar como funciona el posicionamiento de controles dentro de filas y columnas.







Anchura y altura de un control
--------------------------------------------------------------------------------






Peso de una fila o columna
--------------------------------------------------------------------------------







Indices y tablas
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`