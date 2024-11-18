"""
Cole Levi
100922405

This code is a replication of a vending machine.
"""

import PySimpleGUI as sg
import time

# Optional GPIO imports for Raspberry Pi hardware
hardware_present = False
try:
    from gpiozero import Button, Servo
    key1 = Button(5)  # Button setup for GPIO pin 5
    servo = Servo(17)  # Servo setup for GPIO pin 17
    hardware_present = True
except ModuleNotFoundError:
    print("Not running on Raspberry Pi. GPIO disabled.")

# States for the vending machine
class State:
    def on_entry(self, machine):
        pass  # What happens when entering this state

    def on_exit(self, machine):
        pass  # What happens when leaving this state

    def handle_event(self, machine, event):
        pass  # How this state deals with incoming events

# Adding coins or selecting products
class AddCoinsState(State):
    
    def handle_event(self, machine, event):
        # If product is selected and there's enough money, dispense the product
        if event in machine.products and machine.amount >= machine.products[event]['price']:
            machine.amount -= machine.products[event]['price']
            print(f"Dispensing {machine.products[event]['name']}...")
            machine.go_to_state('deliver_product')
        elif event == 'RETURN':  # Cancel transaction and return coins
            print("Returning all coins...")
            machine.amount = 0
            machine.go_to_state('waiting')

# Waiting for coins
class WaitingState(State):
    def on_entry(self, machine):
        print("Machine ready. Waiting for coins...")

    def handle_event(self, machine, event):
        # Handle coin insertion events
        if event in ['50', '100', '150', '200', '250']:  # Valid coin values
            coin_value = int(event)
            machine.amount += coin_value  # Add the coin value to the total amount
            print(f"Added {coin_value} cents. Total: {machine.amount}")
            machine.go_to_state('add_coins')
        elif event == 'RETURN':  # Handle coin return
            print("Returning all coins...")
            machine.amount = 0
            machine.go_to_state('waiting')

# Deliver product
class DeliverProductState(State):
    def on_entry(self, machine):
        if hardware_present:
            # Simulate a real servo action (assuming you're using hardware to dispense)
            print("Servo activated to deliver product.")
            servo.min()  # Simulate dispensing action
            time.sleep(1)
            servo.mid()  # Reset servo position
            time.sleep(1)
            servo.max()  # Simulate a completed action

        print("Product delivered. Returning to waiting state.")
        machine.go_to_state('waiting')

# Main vending machine class
class VendingMachine:
    def __init__(self):
        self.states = {}  # Store states in a dictionary
        self.state = None  # Current state
        self.event = None  # Current event
        self.amount = 0  # Total money inserted
        self.products = {  # Product list with prices (in cents)
            'A': {'name': 'Chocolate', 'price': 150},  # 1.50
            'B': {'name': 'Chips', 'price': 200},     # 2.00
            'C': {'name': 'Soda', 'price': 250},      # 2.50
            'D': {'name': 'Candy', 'price': 100},     # 1.00
            'E': {'name': 'Gum', 'price': 50},        # 0.50
        }

    # Add a state to the machine
    def add_state(self, state_name, state_instance):
        self.states[state_name] = state_instance

    # Transition to a different state
    def go_to_state(self, state_name):
        if self.state:
            self.state.on_exit(self)   
        self.state = self.states[state_name]
        self.state.on_entry(self)

    # Process the current event
    def update(self):
        if self.event:
            self.state.handle_event(self, self.event)

    # Handle button press (for GPIO)
    def button_action(self):
        self.event = 'RETURN'
        self.update()

# Main program logic
def main():
    # Set up the vending machine and its states
    vending = VendingMachine()
    vending.add_state('waiting', WaitingState())
    vending.add_state('add_coins', AddCoinsState())
    vending.add_state('deliver_product', DeliverProductState())
    vending.go_to_state('waiting')

    # GPIO setup for button handling
    if hardware_present:
        key1.when_pressed = vending.button_action

    # GUI layout for the vending machine
    layout = [
        [sg.Text('Select a Product:')],
        [sg.Button('A: Chocolate - 1.50'), sg.Button('B: Chips - 2.00'), sg.Button('C: Soda - 2.50')],
        [sg.Button('D: Candy - 1.00'), sg.Button('E: Gum - 0.50')],
        [sg.Text('Insert Coins:')],
        [sg.Button('50c', key='50'), sg.Button('1.00', key='100'), sg.Button('1.50', key='150'),
         sg.Button('2.00', key='200'), sg.Button('2.50', key='250')],
        [sg.Button('Return Coins')],
        [sg.Text('Amount Inserted: 0', key='-AMOUNT-')],
        [sg.Exit()]
    ]

    window = sg.Window('Vending Machine', layout)

    # Event loop for the GUI
    while True:
        
        event, _ = window.read(timeout=100)  # Check for user actions
        
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            print("Shutting down vending machine.")
            break
        elif event in vending.products.keys():  # Handle product selection
            vending.event = event
            vending.update()
            window['-AMOUNT-'].update(f"Amount Inserted: {vending.amount}")
        elif event == 'Return Coins':  # Handle return action
            vending.event = 'RETURN'
            vending.update()
            window['-AMOUNT-'].update(f"Amount Inserted: {vending.amount}")
        elif event in ['50', '100', '150', '200', '250']:  # Handle coin insertions
            vending.event = event
            vending.update()
            window['-AMOUNT-'].update(f"Amount Inserted: {vending.amount}")

    window.close()

# Run the program
if __name__ == '__main__':
    main()
