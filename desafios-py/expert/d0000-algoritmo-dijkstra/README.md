# :heavy_check_mark: Desafio 0000: Algoritmo de Dijkstra

## Enunciado:

O programa recebe um grafo (com seus pesos das arestas), o ponto inicial e final da usuária; é retornado o caminho mais curto entre esses pontos.


---

**Entrada**

```
grafo = { "A" : { "D" : 1, "B": 6 },
          "B" : { "D": 2, "E": 2, "C": 5 },
          "C" : { "E": 5 },
          "D" : { "E": 1 },
          "E" : { }
          }

vertice_inicial = "A"
vertice_final = "C"
```

**Saida**

```
caminho mais curto: ["A", "D", "E", "C"]
```
