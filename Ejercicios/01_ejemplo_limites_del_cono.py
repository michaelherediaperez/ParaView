cono = Cone()

# Se imprimen los límites que haya en el momento
lim_inicial = cono.GetDataInformation().GetBounds()
print('Los limites iniciales son: {}'.format(lim_inicial))

# Se actualiza el pipeline.
UpdatePipeline()

# Chequeando los límites otra vez:
lim_act = cono.GetDataInformation().GetBounds()
print('Solamente actualizando, los limites del cono son: {}'.format(lim_act))

# Si cambiamos una propiedad, y miramos los límites, no van a cambiar ya que no 
# hemos actualizado el pipeline.
cono.Radius = 1
cono.Height = 1.3
lim_mod_sin_act = cono.GetDataInformation().GetBounds() 
print('Modificando sin actualizar, los limites del cono son:\
     {}'.format(lim_mod_sin_act))

# Ahora si actualizamos.
UpdatePipeline()
lim_mod_con_act = cono.GetDataInformation().GetBounds()
print('Modificados y actualizados, los limites del cono son:\
     {}'.format(lim_mod_con_act))

Show()
Render()