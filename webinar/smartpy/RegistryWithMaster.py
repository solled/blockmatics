import smartpy as sp

class Registry(sp.Contract):
    def __init__(self, creator):
        self.init(master = creator, registry = sp.map(tkey = sp.TAddress, tvalue = sp.TInt) )

    @sp.entryPoint
    def addRecord(self, params):
        self.data.registry[sp.sender] = params.amount
        
        
    @sp.entryPoint
    def addRecordMaster(self, params):
        sp.verify(sp.sender == self.data.master)
        self.data.registry[params.account] = params.amount


@addTest(name = "RegistryTest")
def test():
    scenario = sp.testScenario()
    # Create HTML output for debugging
    scenario.h1("Registry")

    creator = sp.address("tz1QxtZ5N63UbhV1DpF99sUjPUqj1aXNP7ey")

    # Instantiate Registry contract
    c1 = Registry(creator)
    
    # Print contract instance to HTML
    scenario += c1
    
    scenario += c1.addRecord(amount = 10000).run(sender = creator)
    scenario += c1.addRecord(amount = 2222).run(sender = "tz1-address-2345")
    scenario += c1.addRecord(amount = 31313131).run(sender = "tz1-address-3456")
    scenario += c1.addRecordMaster(account = sp.address("tz1-address-1234"), amount = 99999).run(sender = creator)
    scenario += c1.addRecordMaster(account = sp.address("tz1-address-4567"), amount = 2134).run(sender = "tz1-address-1234")
