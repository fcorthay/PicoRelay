import microcontroller
import board
                                                  # check for raspberry pi board
try:
    import cyw43
except ImportError:
    cyw43 = None
                                                                  # get pin list
board_pins = []
for pin in dir(microcontroller.pin):
    if (isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin) or
        (cyw43 and isinstance(getattr(microcontroller.pin, pin), cyw43.CywPin))):
        pins = []
        for alias in dir(board):
            if getattr(board, alias) is getattr(microcontroller.pin, pin):
                pins.append(f"board.{alias}")
                                    # Add the original GPIO name, in parentheses
        if pins:
            # Only include pins that are in board.
            pins.append(f"({str(pin)})")
            board_pins.append(" ".join(pins))
                                                              # display pin list
for pins in sorted(board_pins):
    print(pins)
