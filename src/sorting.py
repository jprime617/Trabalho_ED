from datetime import datetime
from src.data_structs import Team, Match
from src.sorting import merge_sort, bubble_sort
from src.main import matches

def bubble_sort(arr, key=lambda x: x):
    """
    Algoritmo de ordenação Bubble Sort (O(n²)).
    Ordena a lista 'arr' em ordem crescente, comparando e trocando elementos adjacentes.
    Recebe um parâmetro 'key' para ordenar com base em um atributo específico do elemento.
    """
    n = len(arr)
    for i in range(n):
        # A maior elemento "borbulha" para o final
        for j in range(0, n - i - 1):
            # Compara usando a função key
            if key(arr[j]) > key(arr[j+1]):
                # Troca os elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr, key=lambda x: x):
    """
    Algoritmo de ordenação Merge Sort (O(n log n) e Estável).
    Divide a lista em sublistas, ordena recursivamente e mescla.
    Recebe um parâmetro 'key' para ordenar com base em um atributo específico do elemento.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]  # Parte esquerda
        R = arr[mid:]  # Parte direita
        
        # Ordena recursivamente
        merge_sort(L, key)
        merge_sort(R, key)
        
        i = j = k = 0
        # Mescla as partes ordenadas
        while i < len(L) and j < len(R):
            # Compara usando a função key
            if key(L[i]) < key(R[j]):  # Note a mudança de R[i] para R[j]
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        # Adiciona elementos restantes da esquerda
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        # Adiciona elementos restantes da direita
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def calculate_team_scores(matches):
    """
    Processa uma lista de partidas e calcula o score total de cada time.
    Vitória: 3 pontos | Empate: 1 ponto | Derrota: 0 pontos.
    Retorna um dicionário {team_name: Team_object}.
    """
    teams = {}
    
    for match in matches:
        # Garante que os objetos Team existam no dicionário
        if match.home_team.name not in teams:
            teams[match.home_team.name] = Team(match.home_team.name, score=0)
        if match.away_team.name not in teams:
            teams[match.away_team.name] = Team(match.away_team.name, score=0)
            
        # Regras de Pontuação
        if match.home_score > match.away_score:
            # Time da casa vence
            teams[match.home_team.name].score += 3
        else:
            if match.home_score < match.away_score:
            # Time visitante vence
                teams[match.away_team.name].score += 3
            else:
            # Empate
                teams[match.home_team.name].score += 1
                teams[match.away_team.name].score += 1

    return list(teams.values())

def generate_top_rankings(teams_list, algorithm_name='Merge Sort'):
    """
    Ordena a lista de times e gera o Top 10 mais pontuados e Top 10 menos pontuados.
    """
    # Cria uma cópia para evitar modificar a lista original
    teams_sorted = list(teams_list)

    # 1. Ordenação para o Top 10 MAIS pontuados (Ordem Decrescente)
    # Primeiro, ordena em ordem crescente
    if algorithm_name == 'Merge Sort':
        merge_sort(teams_sorted, key=lambda team: team.score)
    else: # Bubble Sort
        bubble_sort(teams_sorted, key=lambda team: team.score)
    
    # Inverte para ter o maior score no início (Top 10)
    top_10_most = teams_sorted[::-1][:10]
    
    # 2. Top 10 MENOS pontuados (já está no início da lista crescente)
    top_10_least = teams_sorted[:10]

    print(f"\n🏆 **Top 10 MAIS Pontuados** (Algoritmo: {algorithm_name}) 🏆")
    print("-------------------------------------------------")
    for i, team in enumerate(top_10_most):
        print(f"#{i+1}: {team.name} - {team.score} pontos")
    
    print(f"\n⬇️ **Top 10 MENOS Pontuados** (Algoritmo: {algorithm_name}) ⬇️")
    print("-------------------------------------------------")
    for i, team in enumerate(top_10_least):
        print(f"#{i+1}: {team.name} - {team.score} pontos")



