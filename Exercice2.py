
from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True, order=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not (0 <= self.note <= 10):
            raise ValueError(f"Note invalide : {self.note}. Doit être entre 0 et 10.")
        if self.annee < 1800 or self.annee > 2100:
            raise ValueError(f"Année invalide : {self.annee}.")

    def est_classique(self) -> bool:
        return self.annee < 2000

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    @staticmethod
    def from_json(json_str: str) -> "Film":
        data = json.loads(json_str)
        return Film(**data)

    def promo(self, note_reduite: float) -> "Film":
        return replace(self, note=note_reduite)


if __name__ == "__main__":
    f1 = Film("Le Fabuleux Destin d'Amélie Poulain", "Jean-Pierre Jeunet", 2001, 8.3)
    f2 = f1.promo(7.5)
    json_str = f2.to_json()
    f3 = Film.from_json(json_str)
    favoris = [f1, f2, f3]
    favoris_sorted = sorted(favoris, key=lambda x: x.note)
    for f in favoris_sorted:
        print(f.titre, f.note, f.est_classique())
