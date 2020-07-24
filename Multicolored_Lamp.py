# https://py.checkio.org/en/mission/multicolored-lamp/


class Lamp():
    def __init__(self):
        self.state = ''
        self.lights = ['Green', 'Red', 'Blue', 'Yellow']

    def light(self):
        self.state = self.lights[0]
        self.lights = self.lights[1:]
        if self.state == 'Yellow':
            self.lights = ['Green', 'Red', 'Blue', 'Yellow']
        return self.state

    def __str__(self):
        return self.state


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding completed")