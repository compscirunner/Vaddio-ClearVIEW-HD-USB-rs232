from VaddioCamera import VaddioCamera
from time import sleep
camera = VaddioCamera('/dev/ttyUSB0')
#camera.power_on()
# loop through all possible addresses pan and tilt from Pan Range: 8044 – 7FBC (-32,700 to +32,700)
# Tilt Range: E891 – 4C2B (-5,999 to +19,499)
# Lets loop through all possible addresses in the pan range 50 steps at a time
# and tilt to 0x0000

for i in range(0x8044, 0x7FBC):
    camera.pan_tilt_absolute(i, 0x0000, 0x18, 0x18)
    sleep(1)


camera.pan_tilt_absolute(0x7FBC, 0x0000, 0x18, 0x18)
sleep(1)
camera.pan_tilt_absolute(0x8044, 0x0000, 0x18, 0x18)


# camera.pan_tilt_absolute(0x8000, 0x0000, 0x18, 0x18)
# camera.zoom_in(2)
# zoom = camera.get_zoom_position()
# print(zoom)
# #camera.pan_tilt_drive([0x02, 0x01], 0x18, 0x18)
# sleep(10)
# camera.zoom_out(2)
# sleep(5)
# camera.zoom_stop()
# camera.pan_tilt_stop()
# zoom = camera.get_zoom_position()
# print(zoom)
# #camera.pan_tilt_home()
# camera.tally_on()
# status = camera.get_pan_tilt_position()
# # print(status)
#response = camera.inquire_zoom_position()
#print(response)
