import serial
import time

class VaddioCamera:
    def __init__(self, serial_port, baud_rate=9600):
        self.serial_connection = serial.Serial(serial_port, baud_rate)

    def _send_command(self, command):
        self.serial_connection.write(bytes(command))

    def close(self):
        self.serial_connection.close()

    def set_camera_address(self, address):
        command = [0x88, 0x30, address, 0xFF]
        self._send_command(command)

    def if_clear(self):
        command = [0x88, 0x01, 0x00, 0x01, 0xFF]
        self._send_command(command)

    def command_cancel(self, socket_number):
        command = [0x80 + socket_number, 0x2F, 0xFF]
        self._send_command(command)

    def power_on(self):
        command = [0x81, 0x01, 0x04, 0x00, 0x02, 0xFF]
        self._send_command(command)

    def power_off(self):
        command = [0x81, 0x01, 0x04, 0x00, 0x03, 0xFF]
        self._send_command(command)

    def zoom_stop(self):
        command = [0x81, 0x01, 0x04, 0x07, 0x00, 0xFF]
        self._send_command(command)

    def zoom_in(self, speed=2):
        command = [0x81, 0x01, 0x04, 0x07, 0x20 + speed, 0xFF]
        self._send_command(command)

    def zoom_out(self, speed=2):
        command = [0x81, 0x01, 0x04, 0x07, 0x30 + speed, 0xFF]
        self._send_command(command)

    def zoom_direct(self, position):
        p = (position & 0xF000) >> 12
        q = (position & 0x0F00) >> 8
        r = (position & 0x00F0) >> 4
        s = (position & 0x000F)
        command = [0x81, 0x01, 0x04, 0x47, p, q, r, s, 0xFF]
        self._send_command(command)

    def zoom_direct_variable(self, position, speed):
        p = (position & 0xF000) >> 12
        q = (position & 0x0F00) >> 8
        r = (position & 0x00F0) >> 4
        s = (position & 0x000F)
        command = [0x81, 0x01, 0x7E, 0x01, 0x4A, speed, p, q, r, s, 0xFF]
        self._send_command(command)

    def focus_stop(self):
        command = [0x81, 0x01, 0x04, 0x08, 0x00, 0xFF]
        self._send_command(command)

    def focus_far(self, speed=2):
        command = [0x81, 0x01, 0x04, 0x08, 0x20 + speed, 0xFF]
        self._send_command(command)

    def focus_near(self, speed=2):
        command = [0x81, 0x01, 0x04, 0x08, 0x30 + speed, 0xFF]
        self._send_command(command)

    def focus_auto(self):
        command = [0x81, 0x01, 0x04, 0x38, 0x02, 0xFF]
        self._send_command(command)

    def focus_manual(self):
        command = [0x81, 0x01, 0x04, 0x38, 0x03, 0xFF]
        self._send_command(command)

    def focus_direct(self, position):
        p = (position & 0xF000) >> 12
        q = (position & 0x0F00) >> 8
        r = (position & 0x00F0) >> 4
        s = (position & 0x000F)
        command = [0x81, 0x01, 0x04, 0x48, p, q, r, s, 0xFF]
        self._send_command(command)

    def backlight_on(self):
        command = [0x81, 0x01, 0x04, 0x33, 0x02, 0xFF]
        self._send_command(command)

    def backlight_off(self):
        command = [0x81, 0x01, 0x04, 0x33, 0x03, 0xFF]
        self._send_command(command)

    def memory_reset(self, preset):
        command = [0x81, 0x01, 0x04, 0x3F, 0x00, preset, 0xFF]
        self._send_command(command)

    def memory_set(self, preset):
        command = [0x81, 0x01, 0x04, 0x3F, 0x01, preset, 0xFF]
        self._send_command(command)

    def memory_recall(self, preset):
        command = [0x81, 0x01, 0x04, 0x3F, 0x02, preset, 0xFF]
        self._send_command(command)

    def pan_tilt_drive(self, direction, pan_speed, tilt_speed):
        command = [0x81, 0x01, 0x06, 0x01, pan_speed, tilt_speed, direction[0], direction[1], 0xFF]
        self._send_command(command)

    def pan_tilt_stop(self):
        command = [0x81, 0x01, 0x06, 0x01, 0x00, 0x00, 0x03, 0x03, 0xFF]
        self._send_command(command)

    def pan_tilt_absolute(self, pan_position, tilt_position, pan_speed, tilt_speed):
        y1 = (pan_position & 0xF000) >> 12
        y2 = (pan_position & 0x0F00) >> 8
        y3 = (pan_position & 0x00F0) >> 4
        y4 = (pan_position & 0x000F)
        z1 = (tilt_position & 0xF000) >> 12
        z2 = (tilt_position & 0x0F00) >> 8
        z3 = (tilt_position & 0x00F0) >> 4
        z4 = (tilt_position & 0x000F)
        command = [0x81, 0x01, 0x06, 0x02, pan_speed, tilt_speed, y1, y2, y3, y4, z1, z2, z3, z4, 0xFF]
        self._send_command(command)

    def pan_tilt_home(self):
        command = [0x81, 0x01, 0x06, 0x04, 0xFF]
        self._send_command(command)

    def pan_tilt_reset(self):
        command = [0x81, 0x01, 0x06, 0x05, 0xFF]
        self._send_command(command)
#8x 01 7E 01 0A 00 02 FF
#8x 01 7E 01 0A 00 02 FF
    def tally_on(self):
        command = [0x81, 0x01, 0x7E, 0x01, 0x0A, 0x00, 0x02, 0xFF]
        self._send_command(command)

    def tally_off(self):
        command = [0x81, 0x01, 0x7E, 0x01, 0x0A, 0x00, 0x03, 0xFF]
        self._send_command(command)

    def preset_pan_tilt_zoom_speed(self, pan_speed, tilt_speed, zoom_speed):
        command = [0x81, 0x01, 0x7E, 0x01, 0x0B, pan_speed, tilt_speed, zoom_speed, 0xFF]
        self._send_command(command)

    def get_power_status(self):
        command = [0x81, 0x09, 0x04, 0x00, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(4)
        return response[2] == 0x02

    def get_zoom_position(self):
        command = [0x81, 0x09, 0x04, 0x47, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(7)
        return (response[2] << 12) + (response[3] << 8) + (response[4] << 4) + response[5]

    def get_focus_position(self):
        command = [0x81, 0x09, 0x04, 0x48, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(7)
        return (response[2] << 12) + (response[3] << 8) + (response[4] << 4) + response[5]

    def get_backlight_status(self):
        command = [0x81, 0x09, 0x04, 0x33, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(4)
        return response[2] == 0x02

    def get_memory_preset(self):
        command = [0x81, 0x09, 0x04, 0x3F, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(4)
        return response[2]

    def get_pan_tilt_max_speed(self):
        command = [0x81, 0x09, 0x06, 0x11, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(5)
        return response[2], response[3]

    def get_pan_tilt_position(self):
        command = [0x81, 0x09, 0x06, 0x12, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(11)
        pan_position = (response[2] << 12) + (response[3] << 8) + (response[4] << 4) + response[5]
        tilt_position = (response[6] << 12) + (response[7] << 8) + (response[8] << 4) + response[9]
        return pan_position, tilt_position

    def get_tally_status(self):
        command = [0x81, 0x09, 0x7E, 0x01, 0x0A, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(4)
        return response[2] == 0x02

    def get_preset_speed(self):
        command = [0x81, 0x09, 0x7E, 0x01, 0x0B, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(6)
        return response[2], response[3], response[4]

    def get_motor_config(self):
        command = [0x81, 0x09, 0x7E, 0x01, 0x70, 0xFF]
        self._send_command(command)
        response = self.serial_connection.read(4)
        return response[2] == 0x00