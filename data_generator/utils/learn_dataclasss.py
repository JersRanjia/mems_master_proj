from dataclasses import dataclass, field


@dataclass
class Test:
    nom: str
    vrai_nom: str = field(init=False)

    def __post_init__(self):
        self.vrai_nom = self.nom.upper()


class TestChild(Test):
    def __init__(self) -> None:
        super().__init__("adala")


if __name__ == '__main__':
    print(TestChild())
