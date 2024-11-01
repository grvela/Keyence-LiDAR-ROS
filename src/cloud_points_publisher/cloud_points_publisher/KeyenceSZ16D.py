import serial
import binascii

class KeyenceSZ16D:

    def __init__(self):
        self.commands = {
            "request_measured_value": b'\x90\x00\x18\xEB',
            "start_continuous_sending": b'\x91\x00\x2B\xDA',
            "request_all_conditions": b'\x92\x00\x7E\x89',
            "request_OSSD_state": b'\x93\x00\x4D\xB8', 
            "request_zone_condition": b'\x94\x00\xD4\x2F',
            "request_SZ_state": b'\x95\x00\xE7\x1E',
            "request_interlock_condition": b'\x96\x00\xB2\x4D',
            "request_error_or_alert_number": b'\x97\x00\x81\x7C',
            "request_AUX_condition": b'\x98\x00\x91\x42',
            "request_input_condition": b'\x99\x00\xA2\x73',
            "request_selected_bank_number": b'\x9A\x00\xF7\x20',
            "request_zone_data": b'\x9B\x00\xC4\x11',
            "request_measurement_range": b'\x9C\x00\x5D\x86',
            "request_OSSD_OFF_history": b'\x9D\x00\x6E\xB7',
            "request_working_time": b'\x9E\x00\x3B\xE4',
            "set_measurement_range": b'\x80\x00',
            "select_reading_zone": b'\x82\x00',
            "start_or_stop_the_communication_monitor": b'\x8B\x00',
            "set_communication_bank_number": b'\x8D\x00',
            "stop_continuous_sending": b'\xA0\x00\x1D\x7E',
            "reset_communication_monitoring_timer": b'\xAA\x00\xF2\xB5',
        }

        try:
            self.serial_port = serial.Serial('/dev/ttyS1', 38400, 8, 'N', 1, None)
        except serial.SerialException as error:
            print(error)
    
    def execute_command(self, command):
        try:
            self.serial_port.write(self.commands[command])
        except serial.SerialException as error:
            print(error)

    def listen(self, num_bytes):
        while self.serial_port.in_waiting < num_bytes:
            pass
        
        buffer = self.serial_port.read(num_bytes) 
        
        return buffer    

    def get_laser_scan(self):
        buffer = [] 
        data = []
        value = []
        points = []
        
        self.execute_command("request_measured_value")
        buffer = self.listen(1513)
        
        data = buffer[6:-2]
        data = data[3:]
        
        value = [data[i : i + 1] for i in range(len(data))]     
        
        value = [binascii.hexlify(value[i]) for i in range(len(value))]
        
        list_int = [int(item, 16) for item in value]

        for i in range(len(list_int)):
            if i % 2 == 0:
                upper_level = (list_int[i] & 63) << 8
            else:
                lower_level = upper_level + list_int[i]
                points.append(lower_level)

        points_f = []
        for i in range(len(points)):
            points_f.append(float(points[i]) / 1000.0)
        return points_f 
    

if __name__ == '__main__':
    app = KeyenceSZ16D()
    app.execute_command("stop_continuous_sending")
    app.get_laser_scan()
    buffer = app.listen(1513)
    while True:
        cloud_points = app.get_laser_scan()
        print(len(cloud_points))