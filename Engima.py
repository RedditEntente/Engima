import random

class EnigmaMachine:
    def __init__(self):
        self.rotor_order = [0, 1, 2]
        """random.shuffle(self.rotor_order)"""
        self.rotors = [
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]
        self.reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        self.positions = [0, 0, 0]
        self.ring_settings = [0, 0, 0]

    def set_rotor_order(self, order):
        self.rotor_order = order

    def set_positions(self, positions):
        self.positions = positions

    def set_ring_settings(self, settings):
        self.ring_settings = settings

    def rotate_rotors(self):
        self.positions[0] = (self.positions[0] + 1) % 26
        if self.positions[0] == self.rotor_notch_position(self.rotor_order[0]):
            self.positions[1] = (self.positions[1] + 1) % 26
        if self.positions[1] == self.rotor_notch_position(self.rotor_order[1]):
            self.positions[2] = (self.positions[2] + 1) % 26

    def rotor_notch_position(self, rotor):
        if rotor == 0:
            return 16
        elif rotor == 1:
            return 4
        elif rotor == 2:
            return 21

    def substitute(self, char, rotor_index, forward=True):
        if forward:
            shifted_char = (ord(char) - ord('A') + self.positions[rotor_index] - self.ring_settings[rotor_index]) % 26
            return self.rotors[self.rotor_order[rotor_index]][shifted_char]
        else:
            shifted_char = (self.rotors[self.rotor_order[rotor_index]].index(char) - self.positions[rotor_index] + self.ring_settings[rotor_index]) % 26
            return chr(shifted_char + ord('A'))

    def reflect(self, char):
        return self.reflector[ord(char) - ord('A')]

    def encrypt_char(self, char):
        self.rotate_rotors()
        char = self.substitute(char, 0)
        char = self.substitute(char, 1)
        char = self.substitute(char, 2)
        char = self.reflect(char)
        char = self.substitute(char, 2, False)
        char = self.substitute(char, 1, False)
        char = self.substitute(char, 0, False)
        return char

    def encrypt(self, message):
        encrypted_message = ""
        for char in message.upper():
            if char.isalpha():
                encrypted_message += self.encrypt_char(char)
            else:
                encrypted_message += char
        return encrypted_message

    

# Example usage:
enigma = EnigmaMachine()
enigma.set_positions([0, 0, 0])
enigma.set_ring_settings([0, 0, 0])
encrypted_text = enigma.encrypt("Stilicho")
print(encrypted_text)
