class Procedure:

    def __init__(self, pname, date, practitioner, charges, patient_ID):
        self.pname =pname
        self.date =date
        self.practitioner= practitioner
        self.charges= charges
        self.patient_ID =patient_ID

    def set_pname(self, pname):
        self.pname = pname
    
    def get_pname(self):
        return self.pname

    def set_date(self, date):
        self.date = date
    
    def get_date(self):
        return self.date

    def set_practitioner(self, practitioner):
        self.practitioner = practitioner
    
    def get_practitioner(self):
        return self.practitioner

    def set_charges(self, charges):
        self.charges= charges

    def get_charges(self):
        return self.charges

    def set_patient_ID(self, patient_ID):
        self.patient_ID= patient_ID

    def get_patient_ID(self):
        return self.patient_ID

    def set_total(self,charges):
        self.charges += charges