from georunes.petromod.modeler import calculate_p, PetroModeler


class RayleighCryst(PetroModeler):
    def ratio_liq(self, liq_fract):
        if liq_fract == 0:
            liq_fract = 0.01
        ratio_liq = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq.items():
            ratio_liq[index] = liq_fract ** (self.bulk_dist_coeffs[index] - 1)
        ratio_liq = ratio_liq.drop(columns=['D', ])
        return ratio_liq

    def ratio_sol(self, liq_fract):
        return self.ratio_liq(liq_fract) * self.bulk_dist_coeffs

    def ratio_sol_avg(self, liq_fract):
        if liq_fract == 1:
            liq_fract = 0.99
        ratio_sol = self.bulk_dist_coeffs.copy()
        for index, row in ratio_sol.items():
            num = 1 - liq_fract ** (self.bulk_dist_coeffs[index])
            ratio_sol[index] = num / (1 - liq_fract)
        return ratio_sol

    def concentration_sol_avg_el(self, el, liq_fract, initial_c0):
        c_sol_el = initial_c0[el] * self.ratio_sol_avg(liq_fract)[el]
        return c_sol_el

    def get_concentration_func(self, alias):
        if alias == 'LIQ':
            return self.concentration_liq_el
        elif alias == 'SOL_INST':
            return self.concentration_sol_el
        elif alias == 'SOL_AVG':
            return self.concentration_sol_avg_el

    def get_conc_func_aliases(self):
        return {"LIQ": "Liquid", "SOL_INST": "Instantaneous solid", "SOL_AVG": "Accumulated solid"}


class RayleighMelting(PetroModeler):
    def ratio_liq(self, liq_fract):
        if liq_fract == 1:
            liq_fract = 0.99
        ratio_liq = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq.items():
            ratio_liq[index] = (1 / self.bulk_dist_coeffs[index]) * (1 - liq_fract) ** (
                        1 / self.bulk_dist_coeffs[index] - 1)
        return ratio_liq

    def ratio_sol(self, liq_fract):
        return self.ratio_liq(liq_fract) * self.bulk_dist_coeffs

    def ratio_liq_avg(self, liq_fract):
        if liq_fract == 0:
            liq_fract = 0.01
        ratio_liq_avg = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq_avg.items():
            num = 1 - (1 - liq_fract) ** (1 / self.bulk_dist_coeffs[index])
            ratio_liq_avg[index] = num / liq_fract
        return ratio_liq_avg

    def concentration_liq_avg_el(self, el, liq_fract, initial_c0):
        c_liq_el = initial_c0[el] * self.ratio_liq_avg(liq_fract)[el]
        return c_liq_el

    def get_concentration_func(self, alias):
        if alias == 'LIQ_INST':
            return self.concentration_liq_el
        elif alias == 'SOL':
            return self.concentration_sol_el
        elif alias == 'LIQ_AVG':
            return self.concentration_liq_avg_el

    def get_conc_func_aliases(self):
        return {"LIQ_INST": "Instantaneous liquid", "SOL": "Solid residue", "LIQ_AVG": "Accumulated liquid"}


class RayleighMeltingNonModal(RayleighMelting):
    def __init__(self, bulk_dist_coeffs, melt_propotions, part_coeffs):
        RayleighMelting.__init__(self, bulk_dist_coeffs)
        self.p = calculate_p(melt_propotions, part_coeffs)

    def ratio_liq(self, liq_fract):
        ratio_liq = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq.items():
            num = (1 - self.p[index] * liq_fract / self.bulk_dist_coeffs[index]) ** (1 / self.p[index] - 1)
            ratio_liq[index] = num/self.bulk_dist_coeffs[index]
        return ratio_liq

    def ratio_sol(self, liq_fract):
        ratio_sol = self.bulk_dist_coeffs.copy()
        for index, row in ratio_sol.items():
            num = (1 - self.p[index] * liq_fract / self.bulk_dist_coeffs[index]) ** (1 / self.p[index])
            ratio_sol[index] = num/(1-liq_fract)
        return ratio_sol

    def ratio_liq_avg(self, liq_fract):
        ratio_liq_avg = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq_avg.items():
            num = 1 - (1 - self.p[index] * liq_fract / self.bulk_dist_coeffs[index]) ** (1 / self.p[index])
            ratio_liq_avg[index] = num / liq_fract
        return ratio_liq_avg
