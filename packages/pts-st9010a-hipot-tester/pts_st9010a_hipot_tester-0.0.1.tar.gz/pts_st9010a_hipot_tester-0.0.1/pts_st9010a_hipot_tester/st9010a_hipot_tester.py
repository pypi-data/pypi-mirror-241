import logging
import time
import serial
from serial.tools import list_ports

TEST_MODES = {"AC": ["VOLT", "UPPC", "LOWC", "TTIM", "RTIM", "FTIM", "ARC", "FREQ", "UNITx", "CHx"],
              "DC": ["VOLT", "UPPC", "LOWC", "TTIM", "RTIM", "FTIM", "WTIM", "ARC", "RAMP", "UNITx", "CHx"],
              "IR": ["VOLT", "UPPC", "LOWC", "TTIM", "RTIM", "FTIM", "RANG", "UNITx", "CHx"],
              "OS": ["OPEN", "SHOT", "GET", "STAN", "UNITx", "CHx"],
              "CK": ["VOLT", "LOWC", "UNITx", "CHx"],
              "DK": ["VOLT", "LOWC", "UNITx", "CHx"]}
CHANNEL_VALUE = ["HIGH", "LOW", "OPEN"]
CHANNEL_SWITCH = ["ON", "OFF"]


class ST9010AHipotTester:
    """
    ``Base class for the ST90101A Hipot Tester``
    """
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)

    def __init__(self, connection_string):
        self.tic = None
        self.toc = None
        self.ser = None
        self.hipot_tester = None
        self.port = None
        self.connection_string = connection_string

    def open_connection(self):
        """
        ``Opens a serial connection with the ST90101A Hipot Tester`` \n
        """
        self.port = list(list_ports.comports())
        # self.hipot_tester = [str(p.device) for p in self.port if str(p).startswith("/dev/cu.usbserial")]
        self.ser = serial.Serial(self.connection_string, baudrate=19200, stopbits=serial.STOPBITS_TWO, timeout=1)
        self.tic = time.perf_counter()
        logging.info(f"Opening serial connection to port {self.ser} ...")

    def close_connection(self):
        """
        ``Closes a serial connection with the ST90101A Hipot Tester`` \n
        """
        self.ser.close()
        self.toc = time.perf_counter()
        logging.info(f"Testing time: {self.toc - self.tic:0.4f} seconds ! ")
        logging.info(f"Closing serial connection")

    def id_number(self):
        """
        ``This function returns the ID number`` \n
        :return: `str` : IDN
        """
        idn = "*IDN? \r \n"
        self.ser.write(idn.encode())
        read_char = self.ser.read(29).decode()
        logging.info(f":IDN: {read_char}")
        return str(read_char)

    def fetch_results(self):
        """
        ``Fetches all the measurement results`` \n
        """
        fetch = "FETch? \r \n"
        self.ser.write(fetch.encode())
        read_char = self.ser.read(120).decode()
        logging.info(f": Measurement results: {read_char}")

    def set_display(self, page):
        """
        ``Set the instrument's display page`` \n
        :param page: One of the instrument's display pages \n
                    'Meas': Test Display or Measurement page, \n
                    'Mset': Test Setup or Measurement Setting page, \n
                    'Sysm': System -> Environment page, \n
                    'Iost': System -> IO page \n
        :return None
        """
        disp = f"DISPlay:PAGE {page} \r \n"
        self.ser.write(disp.encode())
        logging.info(f": Display Set to {page}")

    def check_display(self):
        """
        ``Queries the instrument's display page`` \n
        :return str: Display page \n
        """
        disp = "DISPlay:PAGE? \r \n"
        self.ser.write(disp.encode())
        read_char = self.ser.read(29).decode()
        logging.info(f": Display: {read_char}")
        return read_char

    def start_test(self):
        """
        ``Starts Test on the ST9010A Hipot Tester`` \n
        """
        start = "FUNC:STARt \r \n"
        self.ser.write(start.encode())
        logging.info(f"Starting Test..")

    def stop_test(self):
        """
        ``Stops Test on the ST9010A Hipot Tester`` \n
        """
        stop = "FUNC:STOP \r \n"
        self.ser.write(stop.encode())
        logging.info("Stopping Test")

    # Set and get voltage for AC/DC/IR test
    def set_voltage(self, step, test_mode, voltage):
        """
        ``This function sets the voltage for the ACW/DCW/IR test`` \n
        :param step: The step for which the voltage is added in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :param voltage: The voltage to be set in Volts in range \n
                        AC TEST: 50-5000 volts \n
                        DC TEST: 50-6000 volts \n
                        IR TEST: 50-1000 volts \n
        :return: No return
        """
        if str(test_mode).upper() in TEST_MODES:
            set_voltage = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:VOLT {voltage} \r \n"
            self.ser.write(set_voltage.encode())
            logging.info(f": Setting {test_mode} voltage to : {voltage}")
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def check_voltage(self, step, test_mode):
        """
        ``This function queries the voltage for the ACW test`` \n
        :param step: The step for which the voltage is added in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :return: `float` : Voltage in volts
        """
        if str(test_mode).upper() in TEST_MODES:
            get_voltage = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:VOLT? \r \n"
            logging.info(get_voltage)
            self.ser.write(get_voltage.encode())
            read_char = self.ser.read(29).decode()
            logging.info(f": {test_mode} VOLTAGE for step {step}: {read_char}")
            return float(read_char)
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def set_current_limits(self, step, test_mode, low_limit, upper_limit):
        """
        ``This functions sets the lower and upper current limits for ACW/DCW/IR test`` \n
        :param test_mode: modes being AC/DC/IR \n
        :param step: The step for which the current is added in the range 1-20 \n
        :param low_limit: Lower current limit in range \n
                          AC TEST: 0.001 mA \n
                          DC TEST: 0.001 mA \n
                          IR TEST: 0.001 mA \n
        :param upper_limit: Upper current limit in range \n
                          AC TEST: 20.000 mA \n
                          DC TEST: 20.000 mA \n
                          IR TEST: 20.000 mA \n
        :return: No return
        """
        if str(test_mode).upper() in TEST_MODES:
            set_low_current = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:LOWC {low_limit} \r \n"
            self.ser.write(set_low_current.encode())

            set_high_current = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:UPPC {upper_limit} \r \n"
            self.ser.write(set_high_current.encode())
            logging.info(f": Current limits set to : ({low_limit}, {upper_limit}) mA")
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def check_current_limits(self, step, test_mode):
        """
        ``This function checks the lower and upper current limits set by the user/by default`` \n
        :param test_mode: modes being AC/DC/IR \n
        :param step: The step for which the current is added in the range 1-20 \n
        :return: `tuple` : Lower and upper current limits in Amps respectively
        """
        if str(test_mode).upper() in TEST_MODES:
            get_low_current = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:LOWC? \r \n"
            self.ser.write(get_low_current.encode())
            read_char_low = self.ser.read(20).decode()
            logging.info(f": Lower Current Limit for step {step}: {read_char_low} mA")

            get_high_current = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:UPPC? \r \n"
            self.ser.write(get_high_current.encode())
            read_char_high = self.ser.read(20).decode()
            logging.info(f": Upper Current Limit for step {step}: {read_char_high} mA")
            return float(read_char_low), float(read_char_high)
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def set_test_time(self, step, test_mode, test_time):
        """
        ``This functions sets the TEST time for ACW/DCW/IR tests`` \n
        :param step: The step for which the test time is set in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :param test_time: Time in range 0~999.9 (0 is OFF) seconds for ACW/DCW/IR test \n
        :return: No return
        """
        if str(test_mode).upper() in TEST_MODES:
            set_test_time = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:TTIM {test_time} \r \n"
            self.ser.write(set_test_time.encode())
            logging.info(f": Test time set to : {test_time}s")
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def check_test_time(self, step, test_mode):
        """
        ``This functions queries the TEST time for the ACW/DCW/IR test`` \n
        :param step: The step for which the test time is set in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :return: `float` : Test time in seconds
        """
        if str(test_mode).upper() in TEST_MODES:
            get_test_time = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:TTIM? \r \n"
            self.ser.write(get_test_time.encode())
            read_char_test = self.ser.read(20).decode()
            logging.info(f": TEST TIME for step {step}: {read_char_test} s")
            return float(read_char_test)
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def set_rise_time(self, step, test_mode, rise_time):
        """
        ``This functions sets the RISE time for ACW/DCW/IR tests`` \n
        :param step: The step for which the rise time is set in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :param rise_time: Time in range 0~999.9 (0 is OFF) seconds for ACW/DCW/IR test \n
        :return: No return
        """
        if str(test_mode).upper() in TEST_MODES:
            set_rise_time = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:RTIM {rise_time} \r \n"
            self.ser.write(set_rise_time.encode())
            logging.info(f": Rise time set to : {rise_time}s")
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def check_rise_time(self, step, test_mode):
        """
        ``This functions queries the RISE time for the ACW/DCW/IR test`` \n
        :param step: The step for which the rise time is set in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :return: `float` : Rise time in seconds
        """
        if str(test_mode).upper() in TEST_MODES:
            get_rise_time = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:RTIM? \r \n"
            self.ser.write(get_rise_time.encode())
            read_char_test = self.ser.read(20).decode()
            logging.info(f": RISE TIME for step {step}: {read_char_test} s")
            return float(read_char_test)
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def set_fall_time(self, step, test_mode, fall_time):
        """
        ``This functions sets the FALL time for ACW/DCW/IR tests`` \n
        :param step: The step for which the fall time is set in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :param fall_time: Time in range 0~999.9 (0 is OFF) seconds for ACW/DCW/IR test \n
        :return: No return
        """
        if str(test_mode).upper() in TEST_MODES:
            set_fall_time = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:FTIM {fall_time} \r \n"
            self.ser.write(set_fall_time.encode())
            logging.info(f": Fall time set to : {fall_time}s")
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def check_fall_time(self, step, test_mode):
        """
        ``This functions queries the FALL time for the ACW/DCW/IR test`` \n
        :param step: The step for which the fall time is set in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :return: `float` : Fall time in seconds
        """
        if str(test_mode).upper() in TEST_MODES:
            get_fall_time = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:FTIM? \r \n"
            self.ser.write(get_fall_time.encode())
            read_char_test = self.ser.read(20).decode()
            logging.info(f": FALL TIME for step {step}: {read_char_test} s")
            return float(read_char_test)
        else:
            raise OSError(f"ERROR: not the correct Test Mode : {test_mode}")

    def set_channel(self, step, test_mode, channel, chan_value):
        """
        ``This functions sets HIGH/LOW/OPEN for the scanner channel for ACW/DCW/IR test.`` \n
        :param step: The step in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :param channel: Channel in the range of 1-4 \n
        :param chan_value: Channel values being HIGH/LOW/OPEN \n
        :return: No return
        """
        if (str(test_mode).upper() in TEST_MODES) and (str(chan_value).upper() in CHANNEL_VALUE):
            set_channel_value = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:CH{channel} {str(chan_value).upper()} \r \n"
            self.ser.write(set_channel_value.encode())
        else:
            raise OSError(f"ERROR: not the correct Test Mode: {test_mode} or Channel Value {chan_value}")

    def get_channel(self, step, test_mode, channel):
        """
        ``This functions queries the set channel value for ACW/DCW/IR test.`` \n
        :param channel: Channel value set in the range for 1-4 \n
        :param step: The step in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :return: `str` : Channel value in (HIGH/LOW/OPEN)
        """
        if str(test_mode).upper() in TEST_MODES:
            check_channel_value = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:CH{channel}? \r \n"
            self.ser.write(check_channel_value.encode())
            read_char_chan_value = self.ser.read(20).decode()
            logging.info(f": CHANNEL VALUE for step {step} and channel {channel}: {read_char_chan_value}")
            return str(read_char_chan_value)
        else:
            raise OSError(f"ERROR: not the correct Test Mode: {test_mode}")

    def set_ac_freq(self, step, freq):
        """
        ``This functions sets the test frequency for ACW test.`` \n
        :param step: The step for which the AC freq is set in the range 1-20 \n
        :param freq: Set value 50/60 Hz in ACW test \n
        :return: No return
        """
        set_ac_freq = f"FUNC:SOUR:STEP {step}:AC:FREQ {freq}\r \n"
        self.ser.write(set_ac_freq.encode())

    def get_ac_freq(self, step):
        """
        ``This functions queries the test frequency for ACW test.`` \n
        :param step: The step for which the AC freq is set in the range 1-20 \n
        :return: `float` : Value for the test FREQUENCY
        """
        get_ac_freq = f"FUNC:SOUR:STEP {step}:AC:FREQ? \r \n"
        self.ser.write(get_ac_freq.encode())
        read_char_ac_freq = self.ser.read(20).decode()
        logging.info(f": AC FREQUENCY for step {step}: {read_char_ac_freq} Hz")
        return float(read_char_ac_freq)

    def set_multiple_channels(self, step, test_mode, channel, chan_switch):
        """
        ``This functions sets ON/OFF (1/0) about multiple channels for ACW/DCW/IR test.`` \n
        :param step: The step for which channel is switched in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :param channel: Channel in the range of 1-4 \n
        :param chan_switch: Channel switch being ON/OFF (1/0) \n
        :return: No return
        """
        if (str(test_mode).upper() in TEST_MODES) and (str(chan_switch).upper() in CHANNEL_SWITCH):
            set_channel_switch = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:UNIT{channel} {str(chan_switch).upper()} \r \n"
            self.ser.write(set_channel_switch.encode())
        else:
            raise OSError(f"ERROR: not the correct Test Mode: {test_mode} /Channel Value {chan_switch}")

    def check_multiple_channels(self, step, test_mode, channel):
        """
        ``This functions queries the multiple channels for ACW/DCW/IR test.`` \n
        :param channel: Channel value set in the range for 1-4 \n
        :param step: The step for which channel is switched in the range 1-20 \n
        :param test_mode: modes being AC/DC/IR \n
        :return: `str` : Channel switch being ON/OFF (1/0) \n
        """
        if str(test_mode).upper() in TEST_MODES:
            get_channel_switch = f"FUNC:SOUR:STEP {step}:{str(test_mode).upper()}:UNIT{channel}? \r \n"
            self.ser.write(get_channel_switch.encode())
            read_char_chan_switch = self.ser.read(20).decode()
            logging.info(f": CHANNEL SWITCH for step {step} and channel {channel}: {read_char_chan_switch}")
            return str(read_char_chan_switch)
        else:
            raise OSError(f"ERROR: not the correct Test Mode: {test_mode}")




