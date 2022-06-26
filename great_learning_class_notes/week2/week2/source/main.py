# Code Walk through.
from Inheritance import CoralCard, GlobeTrotterCard, DebitCard
from Inheritance2 import ManageCoralCard
from coupling import ManageCoralCard2, ManageCard
from switch import Switch, PlasticSwitch, WifiSwitch
from Duplicity import ProcessCreditCardPayment, ProcessMobileValletPayment
from card import Card

def get_card_details(card : Card):
    print(card.get_number())
    print(card.get_subscription_fee())


def IsARelationShipImplementation():
    # 1. Define a Dictionary to be a associated with a card...
    coral_card_details = {"number": 3408214567342358,
                          "yearly_subscription_fee": 2000,
                          "yearly_subscription_fee_wavier_limit": 300000}

    # 2. Define coral card details...
    globe_trotter_card_details = {"number": 4588214567348975,
                                  "yearly_subscription_fee": 5000,
                                  "yearly_subscription_fee_wavier_limit": 500000}

    # __init__(self, card): Create an Instance of Coral Card
    # By passing the basic card details...
    coral_card = CoralCard(coral_card_details)
    global_card = GlobeTrotterCard(globe_trotter_card_details)

    get_card_details(coral_card)
    get_card_details(global_card)


def HasARelationShipImplementation():
    coral_card_details = {"number": 3408214567342358,
                          "yearly_subscription_fee": 2000,
                          "yearly_subscription_fee_wavier_limit": 300000,
                          "owner": "Kapil Dev"}

    # coral_card = CoralCard(coral_card_details)
    manage_card = ManageCoralCard(coral_card_details)

    manage_card.update_discount_amount() # Rigidity
    manage_card.record_new_transaction("Lamy", 8000)


def TightCoupling():
    globe_trotter_card_details = {"number": 4588214567348975,
                                  "yearly_subscription_fee": 5000,
                                  "yearly_subscription_fee_wavier_limit": 500000,
                                  "owner": "Kapil"}

    manage_card = ManageCoralCard2(globe_trotter_card_details)


def LooseCoupling():
    coral_card_details = {"number": 3408214567342358,
                          "yearly_subscription_fee": 2000,
                          "yearly_subscription_fee_wavier_limit": 300000}

    coral_card = CoralCard(coral_card_details)
    manage_card1 = ManageCard(coral_card, "Kapil")


def Duplicity():
    # Some Workflow in a business application which is seeking
    # for a payment to complete the functionality.

    # Accept Payment from Credit Card
    paymentProcessor = ProcessCreditCardPayment(104)
    paymentProcessor.process_payment()

    # Accept Payment from Mobile
    paymentProcessor = ProcessMobileValletPayment(104)
    paymentProcessor.process_payment()

    # now add a Business Rule (like an offer )
    # to round off to 10 for future payments...

    # Accept Payment from Credit Card
    paymentProcessor = ProcessCreditCardPayment(103)  # this should be 100
    paymentProcessor.process_payment()

    # Accept Payment from Mobile
    paymentProcessor = ProcessMobileValletPayment(106)  # this should be 110
    paymentProcessor.process_payment()


def Opaque(some_var):
    len_some_var = len(some_var)
    if len_some_var == 0:
        print("call do_some_other_thing()")
    elif len_some_var == 2:
        print("call do_some_other_thing()")
        # do_some_other_thing()
    elif len_some_var == 6:
        print("call do_yet_another_thing()")
        # do_yet_another_thing()
    elif len_some_var == 7:
        print("call do_yet_some_other_thing()")
        # do_yet_some_other_thing()


def SwitchBoard(switch: Switch):
    switch.switch_on()
    switch.switch_off()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Inheritence
    # IsARelationShipImplementation()
    # HasARelationShipImplementation()

    # Coupling
    #TightCoupling()
    #LooseCoupling()

    # Interfaces Demo using Switch (ABC Implementations)
    myCurrentSwitch = PlasticSwitch()
    SwitchBoard(myCurrentSwitch)

    myCurrentSwitch = WifiSwitch()
    SwitchBoard(myCurrentSwitch)

    # Interfaces Demo using Cards (ABC Implementations)
    myCreditCard = CoralCard({"number": 3408214567342358,
                              "yearly_subscription_fee": 2000,
                              "yearly_subscription_fee_wavier_limit": 300000})

    get_card_details(myCreditCard)

    myDebitCard = DebitCard({"number": 3408214567342359,
                             "yearly_subscription_fee": 3000})
    get_card_details(myDebitCard)

    #Rigidity, #Fragility
    #Immobility
    Duplicity()
    Opaque("GL")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
