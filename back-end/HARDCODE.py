import numpy as np


SCHEDULE = """Fase 1:     Revisão bibliográfica referente a avaliação de sistemas de aprendizado de máquina;
Fase 2:     Estudo sobre a ferramenta Weka e seus sistemas de aprendizado de máquina para classificação;
Fase 3:    Estudo do código Java dos classificadores na ferramenta Weka e identificação dos principais parâmetros;
Fase 4:     Implementação de uma classe de otimização de parâmetros utilizando uma busca em grid;
Fase 5:     Realização de experimentos com dados;
Fase 6:     Elaboração do relatório final e escrita de artigos.Revisão bibliográfica referente a avaliação de sistemas de aprendizado de máquina;"""

FINANCES_DESCRIPTION = """Bolsa: 3 x 300,00
Raspberry Pi 3 B: 259,00
Servidor Digital Ocean: 3 x 20,00"""

DISCIPLINES = """Inteligência artificial, Introdução a Machine Learning, Introdução a Ciência de Dados
Algoritmos e Estruturas de Dados, Projeto e Análise de Algoritmos
Introdução ao Desenvolvimento Web, Web Semântica, Redes de Computadores
Internet das Coisas, Sistemas Distribuídos, Programação Paralela, Redes de Computadores"""

SITUACAO_COLORS = np.array(["green", "orange", "red"])
SITUACAO_DESC = np.array(["Projeto aprovado",
    "Aguardando financiamento",
    "Projeto recusado"])

EMPRESAS = np.array(["Raccoon", "Nubank", "Google", "Facebook",
                     "Apple", "Microsoft", "Spofity", "TokenLab"])

ALUNOS = np.array(["Bruno Coelho", "Gabriel Cruz", "Marcus Vinicius Junqueira",
                   "Leticia Lumi"])
