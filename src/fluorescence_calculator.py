class FluorescenceCalculator:
    def __init__(self, F0, Fm, Ft, qN, F0ND, FmND):
        self.F0 = F0  # minimum fluorescence
        self.Fm = Fm  # maximum fluorescence
        self.Ft = Ft  # fluorescence at time t
        self.qN = qN  # non-photochemical quenching
        self.F0ND = F0ND  # minimum fluorescence in non-dark adapted
        self.FmND = FmND  # maximum fluorescence in non-dark adapted

    def calculate_Fv_Fm(self):
        """Calculate Fv/Fm ratio"""
        return (self.Fm - self.F0) / self.Fm if self.Fm != 0 else 0

    def calculate_ETR(self, PPFD):
        """Calculate Electron Transport Rate (ETR)"""
        Fv_Fm = self.calculate_Fv_Fm()
        return Fv_Fm * PPFD * 0.84  # Assuming a specific conversion factor

    def calculate_NPQ(self):
        """Calculate Non-Photochemical Quenching (NPQ)"""
        return (self.Fm - self.F0ND) / self.FmND if self.FmND != 0 else 0

    def calculate_qP(self):
        """Calculate Photochemical Quenching (qP)"""
        return (self.Fm - self.Ft) / (self.Fm - self.F0) if (self.Fm - self.F0) != 0 else 0

    def calculate_PhiPSII(self):
        """Calculate quantum yield of Photosystem II (ΦPSII)"""
        return self.calculate_qP() * (1 - self.qN)

    def validate_parameters(self):
        """Validation method for input parameters"""
        if self.F0 < 0 or self.Fm < 0 or self.Ft < 0:
            raise ValueError("Fluorescence values must be non-negative")
        if self.qN < 0 or self.qN > 1:
            raise ValueError("Non-photochemical quenching must be between 0 and 1")