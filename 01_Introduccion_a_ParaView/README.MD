# Introduccion a ParaView

Es esta sección se hace una introducción de lleno a ParaView, explicando su funcionamiento y los ejecutables principlaes del curso que son paraview y ```pvpython```. Se cuenta con el siguiente material:

- [01. Introducción a ParaView](01_Introduccion_a_ParaView.pdf): diaporama guía del video explicativo.
- [01_Introduccion_a_ParaView.ipynb](01_Introduccion_a_ParaView.ipynb): cuaderno de comandos básicos para trabajar esta sección desde ```pvpython```.

## Videos explicativos

- [ParaView | 01a. Introducción a ParaView - Interfaz gráfica de paraview](https://youtu.be/Hx6kPCnk0RI)
- [ParaView | 01b. Introducción a ParaView - Python Shell y pvpython](https://youtu.be/IM88o6Rj2pA)

## Sobre ```pvpython``` y sus comandos

```pvpython``` es la API de ParaView para trabajar con comandos en lenguaje Python desde el *Python Shell* de paraview. Para obtener información sobre un método en especial basta con emplear el comando ```help()```; más información al respecto se puede en contrar en:

* Página de la wiki sobre [Python Scripting](https://www.paraview.org/Wiki/ParaView/Python_Scripting).
* Repositorio de Kitware con documentación de Python para ParaView [aquí](https://kitware.github.io/paraview-docs/latest/python/). El módulo [```paraview.simple```](https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html) es el más usado.
* La [ParaViewGuide-5.8.1.pdf](https://www.paraview.org/files/v5.8/ParaViewGuide-5.8.1.pdf).

La recomendación cuando se quiera programar una rutina pero se desconozcan los comandos es activar la función ***Start Trace*** en el menú *Tools* de la interfaz gráfica paraview, con el cual, al finalizar el proceso se presentará al usuario un ```script.py``` comentado con todos los comandos escritos de las acciones que se realizaron.

### Comandos inconsistentes encontrados en la guía de ParaView (Cap 1)

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