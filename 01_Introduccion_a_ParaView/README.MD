# Introduccion a ParaView

Es esta sección se hace una introducción de lleno a ParaView, explicando su funcionamiento y los ejecutables principlaes del curso que son paraview y ```pvpython```. Se cuenta con el siguiente material:

- [01. Introducción a ParaView](01_Introduccion_a_ParaView.pdf): diaporama guía del video explicativo.
- [01_Introduccion_a_ParaView.ipynb](01_Introduccion_a_ParaView.ipynb): cuaderno de comandos básicos para trabajar esta sección desde ```pvpython```.

## Videos explicativos

- [ParaView | 01a. Introducción a ParaView - Interfaz gráfica de paraview](https://youtu.be/Hx6kPCnk0RI)
- [ParaView | 01b. Introducción a ParaView - Python Shell](https://youtu.be/IM88o6Rj2pA)
- [ParaView | 01c. ¿Python Shell, pvpython y pvbatch? Explicando la diferencia](https://youtu.be/qzdUFue56PE)

## Scripting con Python

El scripting con Python se desarrolla en ParaView a través de diferentes herramientras, las cuales son: Python Shell desde la GUI, ```pvbatch``` y ```pvpython```. Para obtener información sobre un método o comando en especial basta con emplear el comando ```help()```; más información al respecto se puede en contrar en:

- La [ParaViewGuide-5.8.1.pdf](https://www.paraview.org/files/v5.8/ParaViewGuide-5.8.1.pdf).
- El módulo [```paraview.simple```](https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html) el cual es el más usado.

La recomendación cuando se quiera programar una rutina pero se desconozcan los comandos es activar la función ***Start Trace*** en el menú *Tools* de la interfaz gráfica paraview, con el cual, al finalizar el proceso se presentará al usuario un ```script.py``` comentado con todos los comandos escritos de las acciones que se realizaron.

**En la sección [09. Python con ParaView](...\09_Python_con_ParaView) se explicará con mucho mayor bagaje el scripting con Python.** Por el momento, se trabajará por el Python Shell y los comandos de ```pvpython```.

## Comandos inconsistentes encontrados en la guía de ParaView (Cap 1)

Tanto en el cuaderno de comandos como en el diaporama se encuentra la explicación y la referencia por la cual la guía de ParaView emplea mal el comando

```
Shrink()
entrada_filtro = GetProperty('Input')
```

lo cual lanza el sigueinte error:

```
AttributeError: 'paraview.modules.vtkRemotingServerManager.vtkSMInp' object has no attribute 'Port'
```

Siendo la forma correcta

```
filtro = Shrink()
entrada_filtro = filtro.Input
```