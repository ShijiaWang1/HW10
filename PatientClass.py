class Patient:

    def __init__(self, ID, name, address, phone, veteran_status):
        self.ID = ID
        self.name = name
        self. address = address
        self. phone = phone
        self.veteran_status = veteran_status
    
    def set_ID(self, ID):
        self.ID = ID
    
    def get_ID(self):
        return self.ID
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address
    
    def get_address(self):
        return self.address

    def set_phone(self, phone):
        self.phone =phone

    def get_phone(self):
        return self.phone

    def set_veteran_status(self, veteran_status):
        self.veteran_status = veteran_status
    
    def get_veteran_status(self):
        return self.veteran_status