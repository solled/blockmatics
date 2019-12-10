import smartpy as sp

class Registry(sp.Contract):
    def __init__(self, _admin):
        self.init(admin = _admin, registry = sp.map(tkey = sp.TAddress, tvalue = sp.TInt) )

    @sp.entryPoint
    def addRecord(self, params):
        self.data.registry[sp.sender] = params.amount
        
        
    @sp.entryPoint
    def addRecordAdmin(self, params):
        sp.verify(sp.sender == self.data.admin)
        self.data.registry[params.account] = params.amount


@addTest(name = "RegistryTest")
def RegistryTest():
    scenario = sp.testScenario()
    # Create HTML output for debugging
    scenario.h1("Registry")

    # Instantiate Registry contract
    c1 = Registry(sp.address("tz1QxtZ5N63UbhV1DpF99sUjPUqj1aXNP7ey"))
    
    # Print contract instance to HTML
    scenario += c1
    
    scenario += c1.addRecord(amount = 10000).run(sender = "tz1-address-1111")
    scenario += c1.addRecord(amount = 2222).run(sender = "tz1-address-2222")
    scenario += c1.addRecord(amount = 31313131).run(sender = "tz1-address-3333")
    scenario += c1.addRecordAdmin(account = sp.address("tz1-address-1111"), amount = 99999).run(sender = "tz1QxtZ5N63UbhV1DpF99sUjPUqj1aXNP7ey")
    scenario += c1.addRecordAdmin(account = sp.address("tz1-address-4444"), amount = 2134).run(sender = "tz1QxtZ5N63UbhV1DpF99sUjPUqj1aXNP7ey")
