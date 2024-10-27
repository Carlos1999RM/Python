#### Preguntar cpor las ventas ###
rbm_serie1_vendidos = int(input("¿Cuántos se han vendido?: "))
rbm_serie_plus_vendidos = int(input("¿Cuántos se han vendido?: "))
rbm_todoterreno_vendidos = int(input("¿Cuántos se han vendido?: "))

#### Guardamos los datos en variables ####
precio1 = 20000
precio2 = 35000
precio3 = 60000
comisión1 = 0.03
comisión2 = 0.05
comisión3 = 0.07

#### Cálculamos la cantidad de euros a comisionar ese mes ####
ganancia_rbm_serie_1 = rbm_serie1_vendidos * precio1 * comisión1
ganancia_rbm_serie_plus = rbm_serie_plus_vendidos * precio2 * comisión2
ganancia_todoterreno = rbm_todoterreno_vendidos * precio3 * comisión3

ganancia_total = ganancia_rbm_serie_1 + ganancia_rbm_serie_plus + ganancia_todoterreno

#### Imprimimos la ganacia total ####

print("La cantidad total de euros a comisionar este mes es de: ", ganancia_total, " euros")
