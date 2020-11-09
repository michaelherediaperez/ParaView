# Introduccion a ParaView

Es esta sección se hace una introducción de lleno a ParaView, explicando su funcionamiento y los ejecutables principlaes del curso que son *paraview* y ```pvpython```. Se cuenta con el siguiente material:

- [01. Introducción a ParaView](01_Introduccion_a_ParaView.pdf): diaporama guía del video explicativo.
- [01_Introduccion_a_ParaView.ipynb](01_Introduccion_a_ParaView.ipynb): cuaderno de comandos básicos para trabajar esta sección desde ```pvpython```.
- [Video](): video explicativo de introducción a ParaView.

### Sobre ```pvpython``` y sus comandos

```pvpython``` es la API de ParaView para trabajar con comandos en lenguaje Python desde el *Python Shell* de paraview. Para obtener información sobre un método en especial basta con emplear el comando ```help()```; más información al respecto se puede en contrar en:

* Página de la wiki sobre [Python Scripting](https://www.paraview.org/Wiki/ParaView/Python_Scripting).
* Repositorio de Kitware con documentación de Python para ParaView [aquí](https://kitware.github.io/paraview-docs/latest/python/). El módulo [```paraview.simple```](https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html) es el más usado.
* La [ParaViewGuide-5.8.1.pdf](https://www.paraview.org/files/v5.8/ParaViewGuide-5.8.1.pdf).

La recomendación cuando se quiera programar una rutina pero se desconozcan los comandos es activar la función ***Start Trace*** en el menú *Tools* de la interfaz gráfica paraview, con el cual,} al finalizar el proceso se presentará al usuario un ```script.py``` comentado con todos los comandos escritos de las acciones que se realizaron.