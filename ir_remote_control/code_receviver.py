import pulseio
import board
import adafruit_irremote

pulsein = pulseio.PulseIn(board.GP7, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()


while True:
    pulses = decoder.read_pulses(pulsein)
    try:
        code = decoder.decode_bits(pulses)
        btn_pressed_code = code[-1]
        
        if btn_pressed_code == 16:
            print("LEFT")
        elif btn_pressed_code == 24:
            print("UP")
        elif btn_pressed_code == 90:
            print("RIGHT")
        elif btn_pressed_code == 74:
            print("DOWN")
        elif btn_pressed_code == 56:
            print("MIDDLE")
        
    except adafruit_irremote.IRDecodeException as e:     # failed to decode
        print("Failed to decode: ", e.args)

    print("----------------------------")