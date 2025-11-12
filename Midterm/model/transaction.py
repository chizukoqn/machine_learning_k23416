class Transaction:
    def __init__(self, Id=None, InvoiceNo=None, StockCode=None,
                 Description=None, Quantity=None, InvoiceDate=None,
                 UnitPrice=None, CustomerID=None, Country=None):
        self.Id = Id
        self.InvoiceNo = InvoiceNo
        self.StockCode = StockCode
        self.Description = Description
        self.Quantity = Quantity
        self.InvoiceDate = InvoiceDate
        self.UnitPrice = UnitPrice
        self.CustomerID = CustomerID
        self.Country = Country

    def __repr__(self):
        return (f"<Transaction(Id={self.Id}, InvoiceNo={self.InvoiceNo}, "
                f"StockCode='{self.StockCode}', Quantity={self.Quantity}, "
                f"UnitPrice={self.UnitPrice}, CustomerID={self.CustomerID}, "
                f"Country='{self.Country}')>")
