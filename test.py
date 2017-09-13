def binary(str):
    return int(str.replace(' ', ''), 2)

# enter
device.send_raw([
    (0xA1, 0x01, 0x00, 0x00, 0x28, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

# cancel
device.send_raw([
    (0xA1, 0x01, 0x00, 0x00, 0x29, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

# pause
device.send_raw([
    (0xA1, 0x03, 0xB1, 0x00),
    (0xA1, 0x03, 0x00, 0x00)
])

device.send_raw([
    (0xA1, 0x01, 0x00, 0x00, 72, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

# pause 2 (this works...)
device.send_raw([
    (0xA1, 0x03, 1, 0xB1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x03, 1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

# play... this works
device.send_raw([
    (0xA1, 0x03, 0xB0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

# fast forward
device.send_raw([
    (0xA1, 0x03, binary('11111111'), binary('11111111'), 0xFF, 0xFF, 0xFF, 0xFF, 0xFF),
    (0xA1, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

# pause
device.send_raw([
    (0xA1, 0x03, 0xB3, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

device.send_raw([
    (0xA1, 0x03, 1, 0xB7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x03, 1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

# plays then immediately pauses?!
device.send_raw([
    (0xA1, 0x03, 1, 0xB8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x03, 1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

device.send_raw([
    (0xA1, 0x03, 1, 0xB8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0xA1, 0x03, 1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
])

import time
for i in range(1, 30):
    print(hex(0xB1 + i))
    device.send_raw([
        (0xA1, 0x03, 0xB1 - i, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
        (0xA1, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
    ])
    time.sleep(1)







        elif command == commands.PLAY:
            self.socket.send(bytes(bytearray((0xA1, 0x01, 0x00, 0x00, 232, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.PAUSE:
            self.socket.send(bytes(bytearray((0xA1, 0x01, 0x00, 0x00, 72, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.NEXT_TRACK:
            self.socket.send(bytes(bytearray((0xA1, 0x01, 0x00, 0x00, 235, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.PREV_TRACK:
            self.socket.send(bytes(bytearray((0xA1, 0x01, 0x00, 0x00, 234, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))

            self.socket.send(bytes(bytearray((0xA1, 0x03, 0xB1))))
            self.socket.send(bytes(bytearray((0xA1, 0x03, 0x00))))


        elif command == commands.PLAY:
            self.socket.send(bytes(bytearray((0xA1, 0x01, 1, 0xB0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x01, 1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.PAUSE:
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 0xB1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.NEXT_TRACK:
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 181, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.PREV_TRACK:
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 182, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))

        elif command == commands.PLAY:
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 0xB0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.PAUSE:
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 0xB1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.NEXT_TRACK:
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 181, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
        elif command == commands.PREV_TRACK:
            self.socket.send(bytes(bytearray((0xA1, 0x03, 1, 182, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))
            self.socket.send(bytes(bytearray((0xA1, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))))

'05010906a101850105077501950819e029e715002501810295037508150025640507190029658100c0050c0901a1018503050c150025017501950709b809b609cd09b509e209ea09e9093009b009b1c0'
'05010906a101850175019508050719e029e715002501810295017508810395057501050819012905910295017503910395067508150026ff000507190029ff8100c0050c0901a1018503150025017501950b0a23020a21020ab10109b809b609cd09b509e209ea09e9093009B009B181029501750d8103c0'

thing = [
0x05, 0x01,        # Usage Page (Generic Desktop Ctrls)  
0x09, 0x06,        # Usage (Keyboard)

0xA1, 0x01,        # Collection (Application)  
0x85, 0x01,        #   Report ID (1)
0x05, 0x07,        #   Usage Page (Kbrd/Keypad)  
0x75, 0x01,        #   Report Count (1)  
0x95, 0x08,        #   Report Size (8)  
0x19, 0xE0,        #   Usage Minimum (0xE0)  
0x29, 0xE7,        #   Usage Maximum (0xE7)  
0x15, 0x00,        #   Logical Minimum (0)  
0x25, 0x01,        #   Logical Maximum (1)  
0x81, 0x02,        #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)  
0x95, 0x01,        #   Report Count (1)  
0x75, 0x08,        #   Report Size (8)  
0x15, 0x00,        #   Logical Minimum (0)  
0x25, 0x64,        #   Logical Maximum (100)  
0x05, 0x07,        #   Usage Page (Kbrd/Keypad)  
0x19, 0x00,        #   Usage Minimum (0x00)  
0x29, 0x65,        #   Usage Maximum (0x65)  
0x81, 0x00,        #   Input (Data,Array,Abs,No Wrap,Linear,Preferred State,No Null Position)  
0xC0,              # End Collection

0x05, 0x0C,        # Usage Page (Consumer)
0x09, 0x01,        # Usage (Consumer Control)  
0xA1, 0x01,        # Collection (Application)  
0x85, 0x03,        #   Report ID (3)  
0x05, 0x0C,        #   Usage Page (Consumer)  
0x15, 0x00,        #   Logical Minimum (0)  
0x25, 0x01,        #   Logical Maximum (1)  
0x75, 0x01,        #   Report Count (1)  
0x95, 0x08,        #   Report Size (8)
0x09, 0xcd, # Usage (Play/Pause)
0x09, 0xe2, # Usage (Mute)
0x09, 0xea, # Usage (Volume Decrement)
0x09, 0xe9, # Usage (Volume Increment)
0x09, 0x30, # Usage (Power)
0x09, 0xB0, # Usage (Play)
0x09, 0xB1, # Usage (Pause)
0x09, 0xB2, # Usage (Record)
0x09, 0xB3, # Usage (Fast Forward)
0x09, 0xB4, # Usage (Rewind)
0x09, 0xb5, # Usage (Scan Next Track)
0x09, 0xb6, # Usage (Scan Previous Track)
0x09, 0xB7, # Usage (Stop)
0x09, 0xb8, # Usage (Eject)
0xC0
]             # End Collection