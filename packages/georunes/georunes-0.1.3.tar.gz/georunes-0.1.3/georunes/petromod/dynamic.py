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


class DynamicMelting(PetroModeler):
    def __init__(self, bulk_dist_coeffs, melt_propotions, part_coeffs, phi):
        PetroModeler.__init__(self, bulk_dist_coeffs)
        self.p = calculate_p(melt_propotions, part_coeffs)
        self.phi = phi

    def get_x(self, liq_fract):
        return (liq_fract - self.phi) / (1 - self.phi)

    def ratio_liq(self, liq_fract):
        x = self.get_x()

        if liq_fract == 1:  # todo
            liq_fract = 0.99
        ratio_liq = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq.items():
            _d = (self.phi + (1 - self.phi) * self.bulk_dist_coeffs[index])
            ratio_liq[index] = (1 / _d * (1 - x) ** (1 / _d))
        return ratio_liq

    def ratio_liq_avg(self, liq_fract):
        x = self.get_x()
        if liq_fract == 0:
            liq_fract = 0.01
        ratio_liq_avg = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq_avg.items():
            _d = (self.phi + (1 - self.phi) * self.bulk_dist_coeffs[index])
            num = 1 - (1 - x) ** (1 / _d)
            ratio_liq_avg[index] = num / x
        return ratio_liq_avg

    def ratio_residue(self, liq_fract):
        return self.phi * self.ratio_liq(liq_fract) + (1 - self.phi) * self.ratio_sol(liq_fract)

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


class DynamicMeltingNonModal(DynamicMelting):  # todo test
    def ratio_liq(self, liq_fract):
        x = self.get_x()
        ratio_liq = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq.items():
            _d = (self.bulk_dist_coeffs[index] + self.phi * (1 - self.p))
            _p = (self.p + self.phi * (1 - self.p))
            num = (1 - x * _p / _d) ** (1 / _p - 1)
            ratio_liq[index] = num / _d
        return ratio_liq

    def ratio_sol(self, liq_fract):
        ratio_sol = self.bulk_dist_coeffs.copy()
        liq_fract = self.ratio_liq(liq_fract)
        for index, row in ratio_sol.items():
            _d = (self.bulk_dist_coeffs[index] - liq_fract * self.p) / (1 - self.p)
            ratio_sol[index] = liq_fract[index] * _d
        return ratio_sol

    def ratio_liq_avg(self, liq_fract):
        x = self.get_x()
        ratio_liq_avg = self.bulk_dist_coeffs.copy()
        for index, row in ratio_liq_avg.items():
            _d = (self.bulk_dist_coeffs[index] + self.phi * (1 - self.p))
            _p = (self.p + self.phi * (1 - self.p))
            num = 1 - (1 - x * _p / _d) ** (1 / _p)
            ratio_liq_avg[index] = num / x
        return ratio_liq_avg
