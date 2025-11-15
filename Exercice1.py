
from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True, order=True)
class Livre:
    titre: str
    auteur: str
    prix: float

    def promo(self, prix_reduit: float) -> "Livre":
        return replace(self, prix=prix_reduit)

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    @staticmethod
    def from_json(json_str: str) -> "Livre":
        data = json.loads(json_str)
        return Livre(**data)


if __name__ == "__main__":
    livre1 = Livre("Python Avancé", "Auteur A", 15.0)
    livre2 = livre1.promo(10.0)
    json_str = livre2.to_json()
    livre3 = Livre.from_json(json_str)
    livres = [livre1, livre2, livre3]
    livres_sorted = sorted(livres, key=lambda x: x.prix)
    for l in livres_sorted:
        print(l.titre, l.prix)
