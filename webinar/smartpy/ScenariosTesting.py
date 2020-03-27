import smartpy as sp

class MyContract(sp.Contract):
    def __init__(self, myParameter1, myParameter2, _admin):
        self.init(myParameter1 = myParameter1,
                  myParameter2 = myParameter2,
                  admin = _admin)

    @sp.entry_point
    def entry1(self, params):
        sp.verify(self.data.myParameter1 + params <= 100)
        self.data.myParameter1 += params
        
        
    @sp.entry_point
    def entry2(self, params):
        sp.verify(self.data.myParameter2 - params >= 0)
        self.data.myParameter2 -= params
        
    @sp.entry_point
    def reset(self):
        sp.verify(self.data.admin <= sp.sender)
        self.data.myParameter1 = 50
        self.data.myParameter2 = 50


# Tests
@sp.add_test(name = "Test My Contract")
def tester():
    admin = sp.test_account("Administrator")
    alice = sp.test_account("Alice")
    # bob   = sp.test_account("Robert")
    
    # We define a test scenario, together with some outputs and checks
    scenario = sp.test_scenario()

    # We first define a contract and add it to the scenario
    c = MyContract(50, 50, admin.address)
    scenario += c
    
    # scenario.h1("Running through some tests")

    # # # And call some of its entry points
    # scenario += c.entry1(12)
    # scenario += c.entry1(50).run(valid = False) # this is expected to fail
    # scenario += c.entry2(5)
    # scenario += c.entry2(50).run(valid = False) 

    # # Finally, we check its final storage
    # scenario.h4("Verifying myParameter1 = 62, and myParameter1 = 45")
    # scenario.verify(c.data.myParameter1 == 62)
    # scenario.verify(c.data.myParameter2 == 45)

    # scenario += c.entry1(14).run(sender = admin, amount = sp.mutez(10000))
    # scenario += c.reset().run(sender = admin)
    
    # scenario.show(c.data.myParameter1 * 12)
    # x = scenario.compute(c.data.myParameter1 * 12)
    # scenario.verify(x == 500)
    # #scenario.simulation(c)
