class Employee:
    def __init__(self, ID = None, Name = None,Email = None, Password = None, Role= None):
        self.ID = ID
        self.Name = Name
        self.Email = Email
        self.Password = Password
        self.Role = Role

    def __str__(self):
        info = "{}\t{}\t{}\t{}\t{}\t".format(self.ID, self.Name, self.Email, self.Password,self.Role)
        return info
