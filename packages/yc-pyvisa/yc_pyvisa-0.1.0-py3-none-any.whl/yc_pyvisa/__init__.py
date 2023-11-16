import pyvisa as visa
import time
import statistics
import threading
import ctypes
import time
vol = 0
def call_back(usesr,id,what,param1,param2):
    global vol
    print(type(usesr))
    print(usesr)
    print(id)
    print(what)
    print(param2)
    print(param1[0])
    vol = param1[1]
    print(param1[1])
    print(2)
    return 0
class EKA1080P:
    def __init__(self,callback = None):
        self.dll = ctypes.WinDLL('model_II.dll')
        if callback == None:
            self.call_backfunc = call_back
        else:
            self.call_backfunc = callback
        print(self.dll)
        time.sleep(3)
        dllFunc = self.dll.MpaEnum
        dllFunc.argtypes = [ctypes.POINTER(ctypes.c_uint64),ctypes.c_uint32]
        dllFunc.restype = ctypes.c_int64
        intList=[0]
        inIntBuf=(ctypes.c_uint64 * len(intList))(*intList)
        ret = dllFunc(inIntBuf,len(intList))
        self.deviceid = inIntBuf[0]
        print("devices:",ret)
        print("id:",self.deviceid)
        self.gCallbackFuncList = []
        self.set_call_back()
        self.MpaStart(1)

    def setVoltage(self, volt, CH=1):
        global vol
        dllFunc = self.dll.MpaSetVoltage
        dllFunc.argtypes = [ctypes.c_uint64,ctypes.c_float]
        dllFunc.restype = ctypes.c_int64
        while dllFunc(self.deviceid,float(volt)) != 0:
            continue

    def set_call_back(self):
        dllFunc = self.dll.MpaSetCallback
        # dllFunc.argtypes = [ctypes.CFUNCTYPE,ctypes.c_uint64]
        callbackFunc= ctypes.CFUNCTYPE(ctypes.c_int64,ctypes.c_uint64,ctypes.c_uint64,ctypes.c_uint32,ctypes.POINTER(ctypes.c_float),ctypes.c_uint64)(self.call_backfunc)
        self.gCallbackFuncList.append(callbackFunc)
        dllFunc(callbackFunc,33)
    def MpaStart(self, volt, CH=1):
        dllFunc = self.dll.MpaStart
        dllFunc.argtypes = [ctypes.c_uint64,ctypes.c_float]
        dllFunc.restype = ctypes.c_int64
        while dllFunc(self.deviceid,float(volt)) != 0:
            continue

class VisaInstrument:

    def __init__(self, divice_addr = 'GPIB0::1::INSTR'):
        """
        initialize visa instrument resource
        :param ip: (str) ip address of Papaya
        :param gpib_address: (str) GPIB address of instrument
        """
        self.lock = threading.RLock()
        try:
            resource_name = divice_addr
            print(resource_name)
            rm = visa.ResourceManager()
            self.instr = rm.open_resource(resource_name)
            self.instr.timeout = 10000
            self.cls()
        except Exception as e:
            print(e)

    def query(self,str):
        self.lock.acquire()
        resule = self.instr.query(str)
        self.lock.release()
        return resule
    def write(self,str):
        self.lock.acquire()
        result = self.instr.write(str)
        self.lock.release()
        return result
    def close(self):
        self.instr.close()

    def cls(self):
        try:
            self.write('*CLS')
        except ValueError:
            print('*CLS fails to clear')

    def _set_ESE(self, x):
        try:
            cmd = '*ESE ' + str(x)
            self.write(cmd)
        except ValueError:
            print ('*ESE write fails')

    def _get_ESE(self, x):
        try:
            resp = self.query('*ESE?')
            self._output = float(resp)
        except ValueError:
            print('*ESE query fails')
        return self._output

    ESE = property(_get_ESE, _set_ESE, "ESE property")

    def _set_SRE(self, x):
        try:
            cmd = '*SRE ' + str(x)
            self.write(cmd)
        except ValueError:
            print ('*SRE write fails')

    def _get_SRE(self, x):
        try:
            resp = self.query('*SRE?')
            self._output = float(resp)
        except ValueError:
            print('*SRE query fails')
        return self._output

    SRE = property(_get_SRE, _set_SRE, "SRE property")

    def queryIDN(self):
        try:
            data = self.query('*IDN?')
            return data
        except ValueError:
            print('*IDN query fails')

class Agilent_E3649A(VisaInstrument):
    def __init__(self, gpib_addr='GPIB0::1::INSTR'):
        try:
            VisaInstrument.__init__(self,gpib_addr)
        except Exception as e:
            print(e)

    def _get_outputOnOff(self):
        """
        query output state
        :return: 0(OFF) or 1(ON)
        """
        try:
            resp = self.query('OUTP?')
            self._outputOnOff = resp.rstrip()
        except ValueError:
            print('Agilent E3649A query outp on/off fails')
        return self._outputOnOff

    def _set_outputOnOff(self, x):
        """
        turn output on or off
        :param x: either ON or OFF
        :return: None
        """
        try:
            self.write('OUTP ' + str(x))
        except ValueError:
            print('Agilent E3649A write outp on/off fails')
        self._outputOnOff = x

    outputOnOff = property(_get_outputOnOff, _set_outputOnOff, "outputOnOff property")

    def queryCurrent(self, output_num=None):
        """
        query current of selected output
        :param output_num: (int) the output to query (None|1|2);
            default value None uses the output previously set.
        :return: (float) current
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            resp = self.query('MEAS:CURR:DC?')
            return float(resp)
        except visa.VisaIOError or ValueError:
            print('Agilent E3649A query current fails')

    def setCurrent(self, curr, output_num=None):
        """
        query current of selected output
        :param curr: (float) the desired current level
        :param output_num: (int) the output to query (None|1|2);
            default value None uses the output previously set.
        :return: None
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            self.write('CURR ' + str(curr))
        except visa.VisaIOError or ValueError:
            print('Agilent E3649A query current fails')

    def queryVoltage(self, output_num=None):
        """
        query voltage of selected output
        :param output_num: (int) the output to read (None|1|2);
            default value None uses the output previously set.
        :return: (float) voltage
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            resp = self.query('MEAS:VOLT:DC?')
            return float(resp)
        except visa.VisaIOError or ValueError:
            print('Agilent E3649A query voltage fails')

    def setVoltage(self, volt, output_num=None):
        """
        set voltage of selected output
        :param volt: (float) the desired voltage level
        :param output_num: (int) the output to set (None|1|2);
            default value None uses the output previously set.
        :return: None
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            self.write('VOLT ' + str(volt))
        except visa.VisaIOError or ValueError:
            print('Agilent E3649A set voltage fails')

    def selectOutput(self, output_num):
        """
        select which output to modify
        :param output_num: (int) the output to modify (1|2)
        :return: None
        """
        try:
            self.write('INST:NSEL ' + str(output_num))
        except visa.VisaIOError:
            print('Agilent E3649A select output fails')

    def queryOutputRange(self, output_num=None):
        """
        query range setting of selected output
        :param output_num: (int) the output to read (None|1|2);
            default value None uses the output previously set.
        :return: (str) P35V or P60V
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            resp = self.query(':VOLT:RANG?')
            return resp.rstrip()
        except visa.VisaIOError:
            print('Agilent E3649A query output range fails')

    def setOutputRange(self, volt_range, output_num=None):
        """
        set voltage range of selected output
        :param volt_range: the voltage range to set output to (P35V|LOW|P60V|HIGH)
        :param output_num: (int) the output to modify (None|1|2);
            default value None uses the output previously set.
        :return: None
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            self.write(':VOLT:RANG ' + str(volt_range))
        except visa.VisaIOError:
            print('Agilent E3649A set output voltage fails')

    def setOutputLow(self, output_num=None):
        """
        set voltage range of selected output to 35V
        :param output_num: (int) the output to modify (None|1|2);
            default value None uses the output previously set.
        :return: None
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            self.write(':VOLT:RANG LOW')
        except visa.VisaIOError:
            print('Agilent E3649A set output voltage LOW fails')

    def setOutputHigh(self, output_num=None):
        """
        set voltage range of output to 60V
        :param output_num: (int) the output to modify (None|1|2);
            default value None uses the output previously set.
        :return: None
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            self.write(':VOLT:RANG HIGH')
        except visa.VisaIOError:
            print('Agilent E3649A set output voltage HIGH fails')

    def enableVoltageProtection(self, enable=1, output_num=None):
        """
        enable or disable the overvoltage protection function.
        :param enable: (0|1|OFF|ON)
        :param output_num: output_num: (int) the output to modify (None|1|2);
            default value None uses the output previously set.
        :return: None
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            self.write(':VOLT:PROT:STAT ' + str(enable))
        except visa.VisaIOError:
            print('Agilent E3649A enable voltage protection fails')

    def setVoltageProtection(self, volt, output_num=None):
        """
        set the voltage level at which the overvoltage protection
        (OVP) circuit will trip.
        :param volt:  voltage level, 'MIN', or 'MAX'
        :param output_num: (int) the output to modify (None|1|2);
            default value None uses the output previously set.
        :return: None
        """
        try:
            if output_num:
                self.write('INST:NSEL ' + str(output_num))
            self.write(':VOLT:PROT ' + str(volt))
        except visa.VisaIOError:
            print('Agilent E3649A set output voltage protection fails')

    def queryVoltageProtection(self, output_num=None):
        """
        query the protection state and voltage level at which the
        overvoltage protection (OVP) circuit will trip.
        :param output_num: (int) the output to modify (None|1|2);
            default value None uses the output previously set.
        :return: tuple (int, str) consisting of enable 0 (OFF) or 1 (ON)
            and the voltage trip level.
        """
        try:
            ena = self.query('VOLT:PROT:STAT?')
            level = self.query('VOLT:PROT?')
            return ena.rstrip(), level.rstrip()
        except visa.VisaIOError:
            print('Agilent E3649A query output voltage protection fails')

class ZLG1104(VisaInstrument):
    def __init__(self,gpib_addr = 'USB0::0x04CC::0x121C::123456789::RAW'):
        try:
            VisaInstrument.__init__(self,gpib_addr)
            print(self.query("*IDN?"))
            # self.write(":TIMebase:SCALe 10ns")
            # self.write(":CHANnel1:SCALe 1V")
            # self.write(":CHANnel2:SCALe 1V")
            # self.write(":CHANnel3:SCALe 1V")
            # self.write(":CHANnel4:SCALe 1V")
            # print(self.query(":CHANnel1:SCALe?"))
            # self.write(":CHANnel1:OFFSet -1.5")
            # self.write(":CHANnel2:OFFSet -1.5")
            # self.write(":CHANnel3:OFFSet -1.5")
            # self.write(":CHANnel4:OFFSet -1.5")
            # print(self.query(":CHANnel1:OFFSet?"))
        except Exception as e:
            print(e)
    def Get_Frequency(self,ch=1):
        i = 0
        buff = []
        buff.clear()
        self.write(":CHANnel1:DISPlay ON")
        self.write(":MEASure:FREQuency CHANnel"+str(ch))
        self.write(":TIMebase:SCALe " +"200us")
        self.write(":TIMebase:SCALe " +"500us")
        time.sleep(1)
        while True:
            freq = int(eval(self.query(":MEASure:FREQuency:AVERage? CHANnel"+str(ch))))
            if(freq > 0 and freq <100000000):
                buff.append(freq)
                if(i>=10):
                    break
                i+=1
        return statistics.median(buff)
    def Set_Timebase(self,str_time):
        self.write(":TIMebase:SCALe " +str_time)

    def Get_Vol(self,ch=1):
        i = 0
        buff = []
        buff.clear()
        time.sleep(0.5)
        self.write(":CHANnel"+str(ch)+":DISPlay ON")
        self.write(":MEASure:VAVG DISPlay,CHANnel"+str(ch))
        while True:
            freq = eval(self.query(":MEASure:VAVG:CURRent? DISPlay,CHANnel"+str(ch)))
            if(freq > 0 and freq<=100):
                buff.append(freq)
                if(i>=10):
                    break
                i+=1

        return statistics.median(buff)
class ZLG2014(ZLG1104):
    def __init__(self, port='ASRL7::INSTR'):
        try:
            VisaInstrument.__init__(self,port)
            self.instr.baud_rate = 9600
            print(self.query("*IDN?"))
            self.write(":TIMebase:SCALe 10ns")
            self.write(":CHANnel1:SCALe 1V")
            self.write(":CHANnel2:SCALe 1V")
            self.write(":CHANnel3:SCALe 1V")
            self.write(":CHANnel4:SCALe 1V")
            print(self.query(":CHANnel1:SCALe?"))
            self.write(":CHANnel1:OFFSet -1.5")
            self.write(":CHANnel2:OFFSet -1.5")
            self.write(":CHANnel3:OFFSet -1.5")
            self.write(":CHANnel4:OFFSet -1.5")
            print(self.query(":CHANnel1:OFFSet?"))
        except Exception as e:
            print(e)
class Agilent_66319d(VisaInstrument):
    def __init__(self, port='GPIB0::6::INSTR'):
        try:
            VisaInstrument.__init__(self,port)
            self.write('*RST')
            self.write('*CLS')
        except Exception as e:
            print(e)
    def setVoltage(self, volt, CH=1):
        """
        set voltage of selected output
        :param volt: (float) the desired voltage level
        :param output_num: (int) the output to set (None|1|2);
            default value None uses the output previously set.
        :return: None
        """
        try:
            if (CH == 1):
                self.write('OUTP ON')
                self.write('DISPlay:CHANnel 1')
                self.write('VOLT ' + str(volt))
            if (CH == 2):
                self.write('OUTP ON')
                self.write('DISPlay:CHANnel 2')
                self.write('VOLT2 ' + str(volt))
        except visa.VisaIOError or ValueError:
            print('Agilent 66319d set voltage fails')
    def Get_Curr(self, CH=1):
        """
        get curr of selected output
        :param ch: (int) the output to set (None|1|2);
            default value None uses the output previously set.
        :return: curr
        """
        self.cls()
        buff = []
        buff.clear()
        i = 0
        try:
            if(CH == 1):
                cmd = "MEAS:CURR?"
            else:
                cmd = "MEAS:CURR2?"
            while True:
                curr = eval(self.query(cmd))
                if(curr != 0):
                    buff.append(curr)
                    i+=1
                if(i>=10):
                    break
            return statistics.median(buff)
        except visa.VisaIOError or ValueError:
            print('Agilent 66319d set voltage fails')
            return False
class Agilent_34410A(VisaInstrument):
    def __init__(self, port='USB0::0x0957::0x0607::MY47028448::INSTR'):
        try:
            VisaInstrument.__init__(self,port)
            self.write('*RST')
        except Exception as e:
            print(e)

    def Read_Curr(self):
        self.cls()
        try:
            cmd = "Meas:Curr:DC?"
            while True:
                curr = eval(self.query(cmd))
                if(curr != 0):
                    return curr
        except visa.VisaIOError or ValueError:
            print('Agilent 34410A get Curr fails')
            return False

    def Read_Volt(self):
        buff = []
        buff.clear()
        i = 0
        try:
            while True:
                curr = eval(self.query('Meas:Volt:DC?'))
                if(curr != 0):
                    buff.append(curr)
                    i+=1
                if(i>5):
                    break
        except visa.VisaIOError or ValueError:
            print('Agilent 34410A get Volt fails')
        return statistics.median(buff)

class RIGOL_DP832A(VisaInstrument):
    def __init__(self, port='GPIB0::5::INSTR'):
        try:
            VisaInstrument.__init__(self,port)
            self.write('*RST')
            self.write('*CLS')
        except Exception as e:
            print(e)
    def setVoltage(self, volt, CH=1):
        """
        set voltage of selected output
        :param volt: (float) the desired voltage level
        :param output_num: (int) the output to set (None|1|2|3);
            default value None uses the output previously set.
        :return: None
        """
        try:
            self.write('OUTP CH'+str(CH)+",ON")
            self.write(":APPL CH"+str(CH)+","+str(volt)+",1")
        except visa.VisaIOError or ValueError:
            print('Agilent 66319d set voltage fails')
    def Get_Curr(self, CH=1):
        """
        get curr of selected output
        :param ch: (int) the output to set (None|1|2);
            default value None uses the output previously set.
        :return: curr
        """
        self.cls()
        buff = []
        buff.clear()
        i = 0
        try:
            cmd = ":MEAS:CURR? CH"+str(CH)
            while True:
                curr = eval(self.query(cmd))
                if(curr != 0):
                    buff.append(curr)
                    i+=1
                if(i>=10):
                    break
            return statistics.median(buff)
        except visa.VisaIOError or ValueError:
            print('RIGOL DP832A Get Curr fails')
            return False