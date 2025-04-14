import time
import sys

sys.setrecursionlimit(10000) 

def distEdit(p1, p2):
    l = len(p1)
    c = len(p2)

    matriz = [[0 for _ in range(c + 1)] for _ in range(l + 1)]
    iteracoes = 0

    for i in range(l + 1):
        matriz[i][0] = i

    for j in range(c + 1):
        matriz[0][j] = j

    for i in range(1, l + 1):
        for j in range(1, c + 1):
            iteracoes += 1
            if p1[i - 1] == p2[j - 1]:
                custoex = 0
            else:
                custoex = 1
            matriz[i][j] = min(
                matriz[i - 1][j] + 1,          # remoção
                matriz[i][j - 1] + 1,          # inserção
                matriz[i - 1][j - 1] + custoex # substituição
            )

    return matriz[l][c], iteracoes


def distancia_edicao_memo(s1, s2):
    memo = {}
    iteracoes = {"count": 0}

    def resolver(i, j):
        iteracoes["count"] += 1

        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s1):
            resultado = len(s2) - j
        elif j == len(s2):
            resultado = len(s1) - i
        elif s1[i] == s2[j]:
            resultado = resolver(i + 1, j + 1)
        else:
            inserir = 1 + resolver(i, j + 1)
            remover = 1 + resolver(i + 1, j)
            substituir = 1 + resolver(i + 1, j + 1)
            resultado = min(inserir, remover, substituir)

        memo[(i, j)] = resultado
        return resultado

    distancia = resolver(0, 0)
    return distancia, iteracoes["count"]



s1 = "Casablanca"
s2 = "Portentoso"

s1_1 = "Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to simplify the build processes in the Jakarta Turbine project. There were several projects, each with their own Ant build files, that were all slightly different. JARs were checked into CVS. We wanted a standard way to build the projects, a clear definition of what the project consisted of, an easy way to publish project information and a way to share JARs across several projects. The result is a tool that can now be used for building and managing any Java-based project. We hope that we have created something that will make the day-to-day work of Java developers easier and generally help with the comprehension of any Java-based project.";

s2_1 = (
    "This post is not about deep learning. But it could be might as well. This is the power of "
    "kernels. They are universally applicable in any machine learning algorithm. Why you might "
    "ask? I am going to try to answer this question in this article. "
    "Go to the profile of Marin Vlastelica Pogančić "
    "Marin Vlastelica Pogančić Jun"
)

s1_3 = 'Luana'
s2_3 = 'Freitas'

inicio = time.time()
resultados_dist_edit = distEdit(s1_1, s2_1)
fim = time.time()
print('distEdit: iteracoes {}, distancia {} e tempo {}'.format(resultados_dist_edit[1], resultados_dist_edit[0], fim - inicio))
      
inicio = time.time()
resultados_distancia_edicoes = distancia_edicao_memo(s1_1, s2_1)
fim = time.time()
print('distancia_edicao: iteracoes {}, distancia {} e tempo {}'.format(resultados_distancia_edicoes[1], resultados_distancia_edicoes[0], fim - inicio))
