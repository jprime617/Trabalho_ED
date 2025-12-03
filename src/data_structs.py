# src/data_structs.py

from datetime import datetime

class Team:
    """
    Representa um time ou seleção.
    """
    def __init__(self, name: str, score: int = 0):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Team({self.name}, gols={self.score})"

    def add_goals(self, goals: int):
        """Adiciona gols ao placar do time."""
        self.score += goals

    def total_goals(self) -> int:
        """Retorna o total de gols do time."""
        return self.score


class Match:
    """
    Representa uma partida de futebol.
    """
    def __init__(self, date: str, home_team: Team, away_team: Team,
                 tournament: str, city: str, country: str, neutral: bool):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.home_team = home_team
        self.away_team = away_team
        self.tournament = tournament
        self.city = city
        self.country = country
        self.neutral = neutral

    def __repr__(self):
        return (f"Match({self.date.date()} | "
                f"{self.home_team.name} {self.home_team.score} x "
                f"{self.away_team.score} {self.away_team.name})")

    def total_goals(self) -> int:
        """Retorna o total de gols da partida."""
        return self.home_team.total_goals() + self.away_team.total_goals()

    def to_list(self) -> list:
        """
        Exporta os dados da partida em formato de lista (para CSV).
        """
        return [
            self.date.strftime("%Y-%m-%d"),
            self.home_team.name,
            self.home_team.score,
            self.away_team.name,
            self.away_team.score,
            self.tournament,
            self.city,
            self.country,
            self.neutral
        ]
