from abc import abstractmethod, ABC
import pandas as pd


def initial_comp_as_series(list_elements, list_concentrations):
    return pd.Series(list_concentrations, index=list_elements)


def compute_bulk_dist_coeffs(min_props, part_coeffs):
    bulk_dist_coeffs = pd.DataFrame(index=part_coeffs.index)
    df_prop = pd.Series(min_props)
    for index, row in part_coeffs.iterrows():
        res = row * df_prop
        val = res.sum() / 100
        bulk_dist_coeffs.at[index, 'D'] = val
    return bulk_dist_coeffs['D']


def calculate_p(melt_proportions, part_coeffs):
    if sum(melt_proportions.values()) != 1:
        raise Exception("The sum of the melt proportions must be 1.")
    part_coeffs_minerals = part_coeffs.keys()

    # Verify the minerals provided with melt proportions
    missing_minerals = []
    for mineral in melt_proportions:
        if mineral not in part_coeffs_minerals:
            missing_minerals.append(mineral)
    if missing_minerals:
        notification = "Minerals missing in the dataset: " + str(missing_minerals)
        raise Exception(notification)

    p = pd.DataFrame(index=part_coeffs.index)
    for element, row in part_coeffs.iterrows():
        tot = 0
        for mineral, prop in melt_proportions.items():
            tot += row[mineral] * prop
        p.at[element, 'P'] = tot

    return p['P']


class PetroModeler(ABC):
    def __init__(self, bulk_dist_coeffs):
        self.bulk_dist_coeffs = bulk_dist_coeffs

    def set_bulk_dist_coeffs(self, bulk_dist_coeffs):
        self.bulk_dist_coeffs = bulk_dist_coeffs

    def list_elements(self):
        keys = self.bulk_dist_coeffs.index.tolist()
        return keys

    @abstractmethod
    def ratio_liq(self, liq_fract):
        pass

    @abstractmethod
    def ratio_sol(self, liq_fract):
        return self.ratio_liq(liq_fract) * self.bulk_dist_coeffs

    def concentration_liq_el(self, el, liq_fract, initial_c0):
        c_liq_el = initial_c0[el] * self.ratio_liq(liq_fract)[el]
        return c_liq_el

    def concentration_sol_el(self, el, liq_fract, initial_c0):
        c_sol_el = initial_c0[el] * self.ratio_sol(liq_fract)[el]
        return c_sol_el

    def concentration_liq_els(self, list_elements, liq_fract, initial_c0):
        return [self.concentration_liq_el(el, liq_fract, initial_c0) for el in list_elements]

    def concentration_sol_els(self, list_elements, liq_fract, initial_c0):
        return [self.concentration_sol_el(el, liq_fract, initial_c0) for el in list_elements]

    def get_concentration_func(self, alias):
        if alias == 'LIQ':
            return self.concentration_liq_el
        elif alias == 'SOL':
            return self.concentration_sol_el

    def get_conc_func_aliases(self):
        return {"LIQ": "Liquid", "SOL": "Solid", }
