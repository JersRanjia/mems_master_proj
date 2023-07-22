from data_generator.services import ModelService

from random import randint
from typing import List, Optional

from data_generator.models.models_pgsql.account_analytic_line import AccountAnalyticLine
from data_generator.models.models_pgsql.account_analytic_account import AccountAnalyticAccount
from data_generator.models.models_pgsql.account_account import AccountAccount
from datetime import date

DEPENSE_LABELS = {
    "Pneu": 5566,  # 3 à 5ans
    "Filtre carburant": 5566,  # 2ans
    "Filtre à air": 5566,
    "Filtre à l'huile": 5566,
    "Lubrifiant": 5561
}

DEPENSE_PRICE = {
    "Pneu": [150000, 250000],  # 3 à 5ans
    "Filtre carburant": [95000, 150000],  # 2ans
    "Filtre à air": [95000, 150000],
    "Filtre à l'huile": [95000, 150000],
    "Lubrifiant": [95000, 150000]
}


def rand_price(key_depense):
    min, max = DEPENSE_PRICE[key_depense]
    rand_price_out = randint(min/1000, max/1000) * 1000
    return rand_price_out


def rand_date(date_ref: Optional[date] = None):
    """
        !!! deprecated
        Create date superior to the arg date_ref (+ 2months at list)
    date_ref -- reference date
    :type date_ref: datetime
    :return:
    """
    year = 2023
    if date_ref is None :
        return date(year, 1, randint(1, 31))

    month = randint(date_ref.month + 1, (date_ref.month + 3) - 0 if date_ref.month<10 else 12  )
    # day =
    pass


def rand_months():
    size = randint(0, 4)
    if size == 0:
        return []

    first_element = randint(1, 3)
    out = [first_element]
    for i in range(1, size):
        out.append(out[i-1] + randint(2, 3))

    return out


class AccountAnalyticLineService(ModelService):

    def generate_aal(self, aaa_list: List[AccountAnalyticAccount], aa_list: List[AccountAccount]) -> List[AccountAnalyticLine]:
        """
        à partir des aaa et et aa existant : génère les depense sur les vehicules Local (!=location) tel que :
        => pour chaque vehicule est generée chaque dépense possible, la possibilité du nombre en 1an etant de 0->4 (aléatoirement)

        :param aaa_list: List[AccountAnalyticAccount]
        :param aa_list: list[AccountAccount]
        :return:
        """


        # aaa_list = select(AccountAnalyticAccount)
        aal_list: List[AccountAnalyticLine] = []

        for aaa_elmt in aaa_list:  # vehicles
            if aaa_elmt.code == "Local":
                for depense_label, id_aa in DEPENSE_LABELS.items():
                    months = rand_months()
                    if not months:
                        continue
                    # print(id_aa)
                    acc_acc = next(aa for aa in aa_list if aa.id == id_aa)
                    account_analytic_line_nextrows = [
                        AccountAnalyticLine(
                            name=depense_label,
                            date=date(2023, month, randint(1, 28)),
                            general_account=acc_acc,
                            account=aaa_elmt,
                            amount=rand_price(depense_label)
                        )
                        for month in months
                    ]
                    aal_list.extend(account_analytic_line_nextrows)

            else:  # "Location"
                pass

        return aal_list

