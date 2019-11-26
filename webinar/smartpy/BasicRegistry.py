import smartpy as sp

class Registry(sp.Contract):
    def __init__(self):
        self.init(registry = sp.map(tkey = sp.TAddress, tvalue = sp.TInt) )

    @sp.entryPoint
    def addRecord(self, params):
        self.data.registry[sp.sender] = params.amount


@addTest(name = "RegistryTest")
def test():
    scenario = sp.testScenario()
    # Create HTML output for debugging
    scenario.h1("Registry")
    
    # Initialize test addresses
    addr1 = sp.address("tz1-address-1234")
    addr2 = sp.address("tz1-address-2345")
    addr3 = sp.address("tz1-address-3456")

    # Instantiate Registry contract
    c1 = Registry()
    
    # Print contract instance to HTML
    scenario += c1
    
    scenario += c1.addRecord(amount = 10000).run(sender = addr1)
    scenario += c1.addRecord(amount = 2222).run(sender = addr2)
    scenario += c1.addRecord(amount = 31313131).run(sender = addr3)
    
    scenario.h2("Adding second record")
