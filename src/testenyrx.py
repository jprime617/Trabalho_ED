# src/main.py

import csv
from data_structs import Match, Team


# Função para checar se o dado está faltando
def faltando(valor: str):
    if valor is None:
        return True

    valor = valor.strip()  # remove espaços

    # Valores considerados como "faltantes"
    return valor == "" or valor.lower() in ["na", "n/a", "null", "none", "-"]



def carregar_partidas_csv(caminho_csv: str):
    matches = []               # Lista de partidas
    times_unicos = set()       # Conjunto para contar times sem repetir
    linhas_filtradas = 0       # Contador de linhas descartadas

    with open(caminho_csv, mode="r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)

        for row in leitor:
            try:
                # Verificar campos essenciais
                if (faltando(row["home_team"]) or 
                    faltando(row["away_team"]) or 
                    faltando(row["home_score"]) or 
                    faltando(row["away_score"]) or
                    faltando(row["date"])):

                    print("Linha ignorada (dados faltantes):", row)
                    linhas_filtradas += 1
                    continue

                # Atualizar times únicos
                times_unicos.add(row["home_team"].strip())
                times_unicos.add(row["away_team"].strip())

                # Criar times
                home = Team(row["home_team"], int(row["home_score"]))
                away = Team(row["away_team"], int(row["away_score"]))

                # Criar Match
                match = Match(
                    date=row["date"],
                    home_team=home,
                    away_team=away,
                    tournament=row["tournament"],
                    city=row["city"],
                    country=row["country"],
                    neutral=str(row["neutral"]).lower() == "true"
                )

                matches.append(match)

            except Exception as e:
                print(f"Linha inválida ignorada: {e}\nConteúdo da linha:", row)
                linhas_filtradas += 1

    return matches, times_unicos, linhas_filtradas



if __name__ == "__main__":
    matches, times_unicos, linhas_filtradas = carregar_partidas_csv("data/results.csv")

    print("\n==== RESULTADOS ====")
    print("Total de partidas carregadas:", len(matches))
    print("Total de times únicos:", len(times_unicos))
    print("Total de linhas filtradas:", linhas_filtradas)
    print("====================\n")

    # Exibir algumas partidas
    for m in matches[:50]:
        print(m)
