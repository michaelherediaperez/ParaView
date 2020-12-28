# Cuadernos

A continuación se presentan una serie de cuadernos de Python ```.ipynb```, los cuales contienen comandos básicos para el uso de ```pvpython``` y el Python Shell.

- [01_Introduccion_a_ParaView.ipynb](01_Introduccion_a_ParaView.ipynb)
- [02_Cargar_los_datos.ipynb](02_Cargar_los_datos.ipynb)
- [03_Entendiendo_los_datos.ipynb](03_Entendiendo_los_datos.ipynb)
- [04a_Visualizacion_de_los_datos.ipynb](04a_Visualizacion_de_los_datos.ipynb)
- [04d_Python_Views.ipynb](04d_Python_Views.ipynb)
- [05_Filtracion_de_los_datos.ipynb](05_Filtracion_de_los_datos.ipynb)
- [06_Seleccion_de_los_datos_Python_Selection.ipynb](06_Seleccion_de_los_datos_Python_Selection.ipynb)
- [08_Guardar_resultados.ipynb](08_Guardar_resultados.ipynb)

## Scripting con Python

El scripting con Python se desarrolla en ParaView a través de diferentes herramientras, las cuales son: Python Shell desde la GUI, ```pvbatch``` y ```pvpython```. Para obtener información sobre un método o comando en especial basta con emplear el comando ```help()```; más información al respecto se puede en contrar en:

- La [ParaViewGuide-5.8.1.pdf](https://www.paraview.org/files/v5.8/ParaViewGuide-5.8.1.pdf).
- El módulo [```paraview.simple```](https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html) el cual es el más usado.

La recomendación cuando se quiera programar una rutina pero se desconozcan los comandos es activar la función ***Start Trace*** en el menú *Tools* de la interfaz gráfica paraview, con el cual, al finalizar el proceso se presentará al usuario un ```script.py``` comentado con todos los comandos escritos de las acciones que se realizaron.

## Comandos inconsistentes encontrados en la guía de ParaView (Cap 1)

Tanto en el cuaderno de comandos como en la presentación se encuentra la explicación y la referencia por la cual la guía de ParaView emplea mal el comando

```
Shrink()
entrada_filtro = GetProperty('Input')
```

lo cual lanza el siguiente error:

```
AttributeError: 'paraview.modules.vtkRemotingServerManager.vtkSMInp' object has no attribute 'Port'
```

Siendo la forma correcta

```
filtro = Shrink()
entrada_filtro = filtro.Input
```

## Comandos inconsistentes encontrados en la guía de ParaView (Cap 5)

Desde la versión 5.7 de ParaView se actualizaron los argumentos de la función ```ResampleWithDataset()```, sin embargo, esta actualización no se muestra en la guia ParaViewGuide-5.8.1, en la cual los argumentos son ```Input = ``` y ```Source = ```

```
ResampleWithDataset(Input = ..., Source = ...)
```

los correctos son ```SourceDataArrays = ``` y ```DestinationMesh = ```, respectivamente

```
ResampleWithDataset(SourceDataArrays = ..., DestinationMesh = ...)
```

## Otros links de interés

- [Árboles de datos](https://es.wikipedia.org/wiki/%C3%81rbol_(inform%C3%A1tica)), concepto visto en el tipo de dato multibloque (El formato VTK).
- Cambio en los argumentos de la función ```ResampleWithDataset()```: [https://blog.kitware.com/paraview-5-7-0-release-notes/](https://blog.kitware.com/paraview-5-7-0-release-notes/).
- Sobre los filtros *Python Calculator* y *Programmable Filter*: [https://www.paraview.org/Wiki/Python_calculator_and_programmable_filter](https://www.paraview.org/Wiki/Python_calculator_and_programmable_filter).
- Información sobre el módulo ```paraview.selection```, [aquí](https://kitware.github.io/paraview-docs/latest/python/paraview.selection.html).
