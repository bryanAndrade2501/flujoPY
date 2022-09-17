# Clase representa un grafo dirigido representandolo
# En una matriz de adyacencia 
class Graph:

    def __init__(self, graph):
        self.graph = graph  # grafo residual
        self. ROW = len(graph)
        

    '''Devuelve true si hay un camino desde el origen 's' al sumidero 't' 
    en el grafo residual. También rellena parent[] para almacenar la ruta  '''

    def BFS(self, s, t, parent):

        # Marca el nodo origen como visitado y lo pone en cola
        visited = [False]*(self.ROW)

        # Crea una cola para la busqueda en anchura
        queue = []

        # Marca el nodo de origen como visitado y lo pone en cola
        queue.append(s)
        visited[s] = True

         # Bucle BFS estadar
        while queue:

            # Desencola un vertice de la cola y lo almacena en u
            u = queue.pop(0)

            # Obtener todos los vértices adyacentes del vértice retirado u 
            # Si un adyacente no ha sido visitado, entonces marcarlo como visitado
            # visitado y ponerlo en cola
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                      # Si encontramos una conexión con el nodo de la cola,
                    #  entonces ya no tiene sentido el BFS
                    #Sólo tenemos que establecer su padre y podemos devolver true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        # No se llega al sumidero t entonces 
        # Se devuelve falso
        return False
            
    
    # Devuelve el flujo máximo de s a t en el gráfico dado
    def FordFulkerson(self, source, sink):

        # Este array se rellena con BFS y para almacenar la ruta
        parent = [-1]*(self.ROW)

        max_flow = 0 # No hay flujo inicialmente

        # Aumentar el flujo mientras haya camino desde el origen al sumidero
        while self.BFS(source, sink, parent) :

            # Encuentra la mínima capacidad residual de las aristas a lo 
            #largo del camino llenado por BFS. O podemos decir encontrar
            #el máximo flujo a través del camino encontrado.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Añadir el flujo del camino al flujo global
            max_flow +=  path_flow

            # Actualizar las capacidades residuales de las aristas
            # y las aristas inversas a lo largo del camino
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

 


graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0; sink = 5
 
print ("Flujo maximo posible %d " % g.FordFulkerson(source, sink))


