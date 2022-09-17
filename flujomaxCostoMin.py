# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 00:39:57 2022

@author: mate_
"""

from ortools.graph import pywrapgraph
# Entre cada par. Por ejemplo, el arco del nodo 0 al nodo 1 tiene una capacidad de 15 y un costo unitario de 4. 
nodos_iniciales = [ 0, 0,  1, 1,  1,  2, 2,  3, 4]
nodos_finales   = [ 1, 2,  2, 3,  4,  3, 4,  4, 2]
capacidades  = [15, 8, 20, 4, 10, 15, 4, 20, 5]
costos_unitarios  = [ 4, 4,  2, 2,  6,  1, 3,  2, 3]
# Se define una matriz de suministros en cada nodo. 
suministros = [20, 0, 0, -5, -15]
# Se crea una instancia de solucionador SimpleMinCostFlow. 
flujo_costo_minimo = pywrapgraph.SimpleMinCostFlow()
# Se añade cada arco.
for i in range(0, len(nodos_iniciales)):
    flujo_costo_minimo.AddArcWithCapacityAndUnitCost(nodos_iniciales[i], nodos_finales[i],
                                                capacidades[i], costos_unitarios[i])
# Se agregan suministros de nodo. 
for i in range(0, len(suministros)):
    flujo_costo_minimo.SetNodeSupply(i, suministros[i])
    
 # Se encuentra el flujo de costo mínimo entre el nodo 0 y el nodo 4. 
if flujo_costo_minimo.Solve() == flujo_costo_minimo.OPTIMAL:
    print('Costo mínimo:', flujo_costo_minimo.OptimalCost())
    print('')
    print(' Arco   Flujo / Capacidad  Costo')
    for i in range(flujo_costo_minimo.NumArcs()):
        # Cálculo del costo.
        cost = flujo_costo_minimo.Flow(i) * flujo_costo_minimo.UnitCost(i)
        print('%1s -> %1s   %3s  / %3s       %3s' % (
            flujo_costo_minimo.Tail(i),
            flujo_costo_minimo.Head(i),
            flujo_costo_minimo.Flow(i),
            flujo_costo_minimo.Capacity(i),
            cost))
else:
    print('Hubo un problema con la entrada de flujo de costo mínimo.')
    
    
    