import pytest
from vending_machine_<your_initials> import VendingMachine, WaitingState, AddCoinsState, DeliverProductState

# Test the state transitions and logic
def test_vending_machine():
    # Initialize the machine
    vending = VendingMachine()
    vending.add_state('waiting', WaitingState())
    vending.add_state('add_coins', AddCoinsState())
    vending.add_state('deliver_product', DeliverProductState())
    vending.go_to_state('waiting')

    # Check initial state
    assert vending.state.__class__.__name__ == 'WaitingState'

    # Simulate inserting money
    vending.event = '200'
    vending.update()
    assert vending.state.__class__.__name__ == 'AddCoinsState'
    assert vending.amount == 200

    # Simulate selecting a product
    vending.event = 'A'
    vending.update()
    assert vending.state.__class__.__name__ == 'DeliverProductState'
    assert vending.amount == 50  # Remaining amount
