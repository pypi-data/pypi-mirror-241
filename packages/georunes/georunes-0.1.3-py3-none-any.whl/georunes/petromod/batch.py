from georunes.petromod.modeler import calculate_p, PetroModeler


class Batch(PetroModeler):
    def ratio_liq(self, liq_fract):
        ratio_liq = 1 / (self.bulk_dist_coeffs * (1 - liq_fract) + liq_fract)
        return ratio_liq

    def ratio_sol(self, liq_fract):
        return self.ratio_liq(liq_fract) * self.bulk_dist_coeffs


class BatchNonModal(Batch):
    def __init__(self, bulk_dist_coeffs, melt_propotions, part_coeffs):
        Batch.__init__(self, bulk_dist_coeffs)
        self.p = calculate_p(melt_propotions, part_coeffs)

    def ratio_liq(self, liq_fract):
        ratio_liq = 1 / (self.bulk_dist_coeffs + liq_fract * (1 - self.p))
        return ratio_liq

    def ratio_sol(self, liq_fract):
        ratio_sol = self.bulk_dist_coeffs.copy()
        num = self.bulk_dist_coeffs - self.p * liq_fract
        for index, row in ratio_sol.items():
            ratio_sol[index] = (num / (1 - liq_fract)) / (self.bulk_dist_coeffs[index] + liq_fract * (1 - self.p))
        return ratio_sol
