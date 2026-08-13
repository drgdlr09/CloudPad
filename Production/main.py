import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Columns: GPIO2, 3, 4 - Rows: GPIO5, 6, 7
keyboard.col_pins = (board.GPIO2, board.GPIO3, board.GPIO4)
keyboard.row_pins = (board.GPIO5, board.GPIO6, board.GPIO7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW  # flip to ROW2COL if nothing registers

# Encoder: A=GPIO8, B=GPIO9, switch=GPIO10
encoder = EncoderHandler()
encoder.pins = ((board.GPIO8, board.GPIO9, board.GPIO10),)  # A, B, button
keyboard.modules.append(encoder)

keyboard.keymap = [[
    KC.LGUI(KC.N1), KC.LGUI(KC.N2), KC.LGUI(KC.N3),
    KC.LGUI(KC.N4), KC.LGUI(KC.N5), KC.LGUI(KC.N6),
    KC.LGUI(KC.N7), KC.LGUI(KC.N8), KC.LGUI(KC.N9),
]]

# Rotary encoder: counterclockwise = volume down, clockwise = volume up, press = mute
encoder.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]

if __name__ == '__main__':
    keyboard.go()
