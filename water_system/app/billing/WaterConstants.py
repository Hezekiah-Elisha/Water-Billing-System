class WaterConstants:
    METER_RENT = 204.0
    SEWER_CHARGE = 153.0
    CONSUMPTION_CHARGE = 0.5

    # setters and getters
    def get_meter_rent(self):
        return self.METER_RENT
    
    def get_sewer_charge(self):
        return self.SEWER_CHARGE
    
    def get_consumption_charge(self):
        return self.CONSUMPTION_CHARGE
    
    def set_meter_rent(self, meter_rent):
        self.METER_RENT = meter_rent

    def set_sewer_charge(self, sewer_charge):
        self.SEWER_CHARGE = sewer_charge

    def set_consumption_charge(self, consumption_charge):
        self.CONSUMPTION_CHARGE = consumption_charge

    def __repr__(self):
        return f'<WaterConstants {self.METER_RENT} {self.SEWER_CHARGE} {self.CONSUMPTION_CHARGE}>'