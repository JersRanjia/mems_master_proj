from data_generator.services import ModelService

from random import randint
from typing import List

from data_generator.models.models_pgsql.account_analytic_account import AccountAnalyticAccount


class AccountAnalyticAccountService(ModelService):

    @staticmethod
    def rand_numero() -> str:
        # generate the number
        n = randint(1000, 9999)

        # generate trigramme
        first = "T"
        second_nb = -1
        while second_nb in (-1, 8, 24):  # i et y telque 0->a
            second_nb = randint(0, 25)

        third_nb = -1
        while third_nb in (-1, 8, 24):  # i et y telque 0->a
            third_nb = randint(0, 25)

        second = chr(second_nb + 65)
        third = chr(third_nb + 65)

        return f"{str(n)}{first}{second}{third}"

    @staticmethod
    def rand_code_vehic() -> str:
        """
        10% to get Location => 1/10

        :return: Location or Something else
        """

        def_domain = ["Location"] + (["Local"]*9)
        index = randint(0, 9)
        return def_domain[index]

    def gen_aaa_vehicle_model(self, vehic_number=20) -> List[AccountAnalyticAccount]:
        """
        Generate {vehic_number} vehicle

        :return:

        """
        out = [
            AccountAnalyticAccount(
                name=self.rand_numero(),
                code=self.rand_code_vehic()
            )
            for _ in range(vehic_number)
        ]

        return out

