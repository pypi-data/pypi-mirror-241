# YICHIP ��������

UPDATE:
- 2022-02-17�������θ���,�޸�ʾ������ȡ��ѹ����,���ڸ��Ӿ�׼
- 2022-02-17���ڶ��θ���,����RIGOL DP832A��ͨ��ֱ����Դ����
- 2022-01-29����һ�θ���,��ʼ����ɶ�ʾ����(ZDS1104,ZDS2014),��Դ(AgilentE3649A,Agilent66319D),̨ʽ���ñ�(Agilent34410A)

## YC-PYVISA����

VISA��������������ܹ����ǶԴ���GPIB��VXI��PXI������(RS232/485)����̫����USB��/��IEEE 1394�ӿڵ�����ϵͳ�������á���̺͹����ų��ı�׼���򵥵�˵���������˹�ͨ�����������Ե��н飬VISA���������ת���������������������.

PyVisa��ͨ�������ӿ��������Ƹ��ָ����Ĳ���������Python��.

����Ŀ��YICHIPʹ�õĲ�������ͨ��PyVisa�����˶��η�װ,�Դﵽ������Ŀ�������,�����Զ������Ե�Ŀ��

## ��װ

Using pip:

```cmd
pip3 install yc-pyvisa
```

## ����ӿ�

ǰ��˵��visa�ǶԴ���GPIB��VXI��PXI������(RS232/485)����̫����USB��/��IEEE 1394�ӿڵ�����ϵͳ�������á���̺͹����ų��ı�׼,������Բ�ͬ�Ľӿ�,��Ҫ��װ��ͬ������,����ֱ�Ӱ�װʹ��.��������һ���ӿ����ӵ�����,�Ұ�װ������,����ֱ�ӱ�pyvisa����.

### GPIB�ӿ�

�Ƚ�ͨ�õ���GPIB�ӿ�,��ų�����
<center>
    <img src="https://qzxx.com/wp-content/uploads/2017/11/788e43dadc14671.jpg" width="400">
    <center>GPIB������</center>
</center>
<center>
    <img src="https://media.rs-online.com/t_large/F7600341-01.jpg" width="400">
    <center>GPIB�ӿ�</center>
</center>

ע��:һ��GPIB���������Կ��ƶ��GPIB�豸,ͨ�������߲Ŀ���չ����ӿ�

<center>
    <img src="https://gss0.baidu.com/9fo3dSag_xI4khGko9WTAnF6hhy/zhidao/wh%3D600%2C800/sign=40cb661ad93f8794d3aa4028e22b22cc/a6efce1b9d16fdfa7ddf434cb98f8c5495ee7be5.jpg" width="400">
</center>

### USB�ӿ�

USB�ӿ�Ӧ�ñȽϷ������,ͨ����type-B(2.0)�ӿ�,������ƽʱ��������Jlink���߲�,�ҾͲ���ͼƬ��

һ�������USB�豸�������������ڶ�Ӧ�ĳ��̵Ĺ����ҵ�,���Ǹ��˾��ô������Ƚ��鷳,�������������GPIB�ӿڲ�������GPIB�������Ļ����ֱ����GPIBȥ��������,�����ҷ������ǹ�˾��ʾ������û��GPIB�ӿ�,������Ŀǰ���Ƶ�ZLG��ʾ����,���չ����ṩ�ķ�����û�а취��Win10�ϰ�װ������,���Ժ����һ��ṩһƪ�̳�,ר������ZLGʾ������������װ

### RS-232�ӿ�

�ô����������շ�ָ�������,��Ҳ���ұȽ��Ƽ���һ�ַ�ʽ,�Ͼ��򴮿�������һ��������׵�����,ֻ��Ҫһ��RS-232���߾ͺ���,��ų�����
<center>
    <img src="https://image-c.ehsy.com/uploadfile/opc/img/2018/09/10/20180910142455231.jpg" width="400">
    <center>RS-232</center>
</center>

### ����

��������ֱ�����Ӿ���,һ���������涼����ֱ������,������Ҫ����Լ����ֲ�.

## ������װ

��Ҫ��װ:����[NI VISA](https://www.ni.com/zh-cn/support/downloads/drivers/download.ni-visa.html#442805),��ɺ�ֱ��һֱ��һ����װ����,���漯����GPIB�Ŀ���������,����Ϊ���������ṩUSB����,ͬʱΪpyvisa�ṩ���֧��

Agilent_34410Ąʽ���ñ�USB����:

���ڰ�װ�ļ��޴�,�������ﲻ�ṩ������,��������������:\\192.168.2.16\public\xubo\Agilent 34410A Driver.zip

- ��װIntruiLinkApp����װ�ļ�·����CD1\IntuiLinkApp\Setup.exe
- ��װIOLib����װ�ļ�·����CD2\Autorun\auto.exe
- ��װIVI_COM����װ�ļ�·����CD1\ivi-com\Agilent34410.1.0.18.0.msi
- ��װ����������Լ���ͨ��USB����̨ʽ���ñ�

ZLGʾ��������USB������װ:

Ŀǰֻ�ṩZDS1104 �� ZDS2014 usb�����ļ�,���ڸ�������ͨ��`NI-VISA DRIVER WIZARD`����,δ����ǩ��,����win10�ǲ�����װ��,��Ҫ[������������ǿ��ǩ��](https://iknow.lenovo.com.cn/detail/dc_132524.html),Ȼ��˫����װ�ļ�����

����������װ:

RS232�����ڹ�˾�ǱȽ�ϡ�ٵģ�����Ĵ���оƬ�ǱȽ��ϵĴ��ڣ�ֱ�Ӳ���win10 �ǲ�ʶ��ģ����ʱ��������������ᷢ�������Ѿ���װ�����ǲ���ʹ�ã����ʱ��ֻ��Ҫ�������ܵ�BING�Ϳ�����[PL2303win10������װ�̳�](https://blog.csdn.net/wtf3505/article/details/104138727)����װ��֮��Ϳ�������ʹ�ô��ڶ��������п����ˣ�������Ҫע����ǣ����������ǲ���ֱ��ʹ�õ���Ϊ�����漰�������ʵ����⣬�������ǻ�����Ҫ����һ�²����ʣ�һ������֧�ִ��ڿ��ƣ��������ǿ����޸ĵģ�����޷��ҵ���ȥ���������ֲῴ�����������⡣�������ò����ʵĴ������Ѿ���ZLG2014�Ͻ���������,������������������Ļ����͸���ճ����仰�����Ķ����ʼ����������ȥ��ȥ���ö�Ӧ�Ĳ����ʾͺ���

```python
self.instr.baud_rate = 115200
```

����:

�����ǲ���Ҫ��װ������,ֻ��Ҫ�õ��Ժ��豸����ͬһ���μ���(ע�� ZLGϵ�е�ʾ����LAN���Ʋ��ȶ�,������ʹ��)

## �������

�����氲װ��ģ�����ֱ�ӵ��뱾ģ��

```python
from yc-pyvisa import *
```

Ȼ���ʼ����Ӧ������,������Ĭ�ϵĶ�Ӧ�豸��������ַ,����ַ�б䶯�ڳ�ʼ����ʱ�������ַ�����ͺ�

```python
oscilloscope = ZLG1104()#ʾ����
oscilloscope2 = ZLG2014()#ʾ����
multimeter  = Agilent_34410A()#̨ʽ���ñ�
power = Agilent_66319d()#��Դ
power2 = AgilentE3649A()#��Դ
```

GPIB�ĵ�ַ��Ҫͨ�������Լ�ȥ����,Ҳ��ͨ�������氲װ�� NI VISA֮����ֵ�һ�����ù������(`NI MAX`),������Ӧ������ַ��Ҳ��ͨ������ȥ������Ӧ���豸��ַ��

``` python
rm = visa.ResourceManager()
new = rm.list_resources()#����һ�����飬������������еĵ�ַ
```

��������ʵ����������ͨ������ZLG��ʾ�����ǲ��ܹ�����������USB��ַ�ģ��������ʱ����ֻ��ͨ��`NI MAX`ȥ�������ĵ�ַ��ͬʱZLGʾ������USB��ַ������ȫһ�������޷����ģ����Ե�����Ҫͬʱ������̨���ϵ�ʾ������ʱ��ֻ��ͨ��1��USB+n������ȥ����ʾ������

��������������ö�Ӧ�ĺ������ƾͺ�,����:

```python
fre = oscilloscope.Get_Frequency(1)
```

���ܹ���ȡ����Ӧʾ����ͨ��1������Ƶ��

## ����

������ṩ�Ŀ�����ĺ����޷���������Ҳ���ص��ģ�ʾ�����Ĺ��ܺܶ࣬����ʱ��ԭ��ֻʵ����Ŀǰ�õõ���һЩ�����͹��ܣ�����ͨ��ȥ�������ض�Ӧ���ֲᣬ��ͬʱ����Ҳ���ṩһЩ�����ص����ֲᣬ��ͬĿ¼�£�ȥ��������Ӧ��ĳЩ���ܵ�SCIPָ�Ȼ������ɺ����ͺá���Ȼ�����ͨ��gitee �ύ�����͸����ˣ��һ��ÿһ����ȷ�ύ��������ȥ�������ʹ�ã���Ȼϣ������ܹ����Լ��ύ��ÿһ��������������������д��ע�ͣ�����������书�ܣ���Ȼ��һ���кܶຯ����ûдע�͡����������Ǻ�����ʱ���ĵģ�

## ������������

������YC3122��Ӧ��ɸƬ�����ṩһ������

```python
from ast import While
from distutils import extension
from email import charset
import os
import glob
from pickle import FALSE, NONE, TRUE
from time import sleep
import sys
from webbrowser import get
from yc_pyvisa import *
import openpyxl
import threading
from logger import *
max_val = 0
otp_buff = []
def get_cmd_result(cmd):
    result = os.popen(cmd)
    res = result.read()
    return res
def e_p():
    while('CPU Stopped' not in get_cmd_result("e p")):
        continue
    return
def e_c():
    while('CPU Running' not in get_cmd_result("e c")):
        continue
    return
def file_name(file_name):
    global max_val
    file_txt = glob.glob(file_name)
    if(file_txt == []):
        max_val = 0x100
        return
    for filename in file_txt:
        try:
            str1 = str(os.path.basename(filename))
            str1 = str1.replace('.txt',"").replace("id","")
            str1 = int(str1,16)
            if(max_val < str1):
                max_val = str1
        except Exception as e:
            print(e)
            pass
    max_val += 1
def count_bits_2(value):
    count = 0
    while(value):
        value &= value - 1
        count += 1
    return count
def auto_set_fre():
    get_cmd_result("e 20004 0155")
    sleep(0.2)
    get_cmd_result("e 20000 02")
    sleep(1)
    if("01" not in get_cmd_result("e 20001")):
        return FALSE
    fre1 = oscilloscope.Get_Frequency()
    print(fre1)
    get_cmd_result("e 20004 0165")
    get_cmd_result("e 20000 02")
    sleep(0.2)
    if("01" not in get_cmd_result("e 20001")):
        return FALSE
    fre2 = oscilloscope.Get_Frequency()
    print(fre2)
    fer = int((fre2-fre1)/16)
    result = int(0x155 + (24000000 - fre1)/fer)
    get_cmd_result("e 20004 " + hex(result).replace("0x",""))
    get_cmd_result("e 20000 02")
    sleep(0.2)
    if("01" not in get_cmd_result("e 20001")):
        return FALSE
    fre3 = oscilloscope.Get_Frequency()
    print(fre3)
    if(fre3 <24050000 and fre3 >23950000):
        return result
    while(fre3 >24050000):
        result-=1
        get_cmd_result("e 20004 " + hex(result-30).replace("0x",""))
        get_cmd_result("e 20000 02")
        sleep(0.2)
        if("01" not in get_cmd_result("e 20001")):
            return FALSE
        fre3 = oscilloscope.Get_Frequency()
        if(fre3 <24050000 and fre3 >23950000):
            return result
    while(fre3 < 23950000):
        result+=1
        get_cmd_result("e 20004 " + hex(result).replace("0x",""))
        get_cmd_result("e 20000 02")
        sleep(0.2)
        if("01" not in get_cmd_result("e 20001")):
            return FALSE
        fre3 = oscilloscope.Get_Frequency()
        if(fre3 <24050000 and fre3 >23950000):
            return result
    return result
    # power.setVoltage(5,2)
    # set_rc192_val(0x5c)
    # power.setVoltage(0,2)
    # sleep(0.1)
    # power.setVoltage(5,2)
    # fre1 = oscilloscope.Get_Frequency()
    # print(fre1)
    # set_rc192_val(0x65)
    # power.setVoltage(0,2)
    # sleep(0.1)
    # power.setVoltage(5,2)
    # fre2 = oscilloscope.Get_Frequency()
    # print(fre2)
    # fer = int((fre2-fre1)/16)
    # result = int(0x55 + (24000000 - fre1)/fer)
    # set_rc192_val(result)
    # fre3 = oscilloscope.Get_Frequency()
    # power.setVoltage(0,2)
    # sleep(0.1)
    # power.setVoltage(5,2)
    # print(fre3)
    # if(fre3 <24050000 and fre3 >23950000):
    #     return result
    # while(fre3 >24050000):
    #     result-=1
    #     set_rc192_val(result)
    #     fre3 = oscilloscope.Get_Frequency()
    #     power.setVoltage(0,2)
    #     sleep(0.1)
    #     power.setVoltage(5,2)
    #     if(fre3 <24050000 and fre3 >23950000):
    #         return result
    # while(fre3 < 23950000):
    #     result+=1
    #     set_rc192_val(result)
    #     fre3 = oscilloscope.Get_Frequency()
    #     power.setVoltage(0,2)
    #     sleep(0.1)
    #     power.setVoltage(5,2)
    #     if(fre3 <24050000 and fre3 >23950000):
    #         return result
    # return result
def set_rc192_val(input_val):
    while(True):
        if('CPU Stopped' in get_cmd_result("e p")):
            get_cmd_result("e f0c18 00000000")
            get_cmd_result("e f0c1c 00000000")
            get_cmd_result("e f0c49 30")
            get_cmd_result("e f8703 10")
            get_cmd_result("e faaa0 55")
            get_cmd_result("e faaa0 aa")
            get_cmd_result("e faaa0 17")
            get_cmd_result("e faaa4 01")
            get_cmd_result("e fa802 " + hex(input_val).replace("0x",""))
            print("input_val = %x"%input_val)
            break

def down_otp(cmd):
    get_cmd_result("e 20000 "+ cmd)
    sleep(0.1)
    while("01" not in get_cmd_result("e 20001")):
        continue
    # while(True):
    #     if('CPU Stopped' in get_cmd_result("e p")):
    #         get_cmd_result("e f853c 88")
    #         if('f8530 :                                     88'in get_cmd_result("e f853c")):
    #             get_cmd_result("e r pc c0")
    #             if('read cm0 reg f = c0\n'in get_cmd_result("e r pc")):
    #                 get_cmd_result("e otw 12c " + hex(input_val).replace("0x",""))
    #                 if(count_bits_2(input_val) % 2 == 1):
    #                     get_cmd_result("e otw 12d 81")
    #                 elif(count_bits_2(input_val) % 2 == 0):
    #                     get_cmd_result("e otw 12d c1")
    #                 break
    return
def RC192_test():
    cail_val = auto_set_fre()
    if(cail_val == None):
        error("RC192 cail_val ERROR " + str(cail_val))
    print(cail_val)
    otp_buff.append(hex(cail_val))
    down_otp("03")

def down_ft_code():
    e_p()
    os.system("tool\d.bat")

def osc_32k_cal():
    get_cmd_result("e 20000 04")
    sleep(0.1)
    if("01" not in get_cmd_result("e 20001")):
        return False
    oscilloscope.Set_Timebase("10us")
    osc32k_cail_val = oscilloscope.Get_Frequency()
    oscilloscope.Set_Timebase("100us")
    oscilloscope.write(":CHANnel1:DISPlay OFF")
    print(osc32k_cail_val)
    otp_buff.append((hex)(osc32k_cail_val))
    get_cmd_result("e 20004 " + to_hex(osc32k_cail_val))
    down_otp("05")
    return osc32k_cail_val
def DVDD_test():
    DVDD_V = oscilloscope.Get_Vol(2)
    if(DVDD_V>1.3 or DVDD_V<1.15):
        error("DVDD_V ERROR "+str(DVDD_V))
def ft_test_init():
    power.setVoltage(0,2)
    sleep(1)
    CURR_VUBT = multimeter.Read_Curr()
    if(CURR_VUBT<1e-06 or CURR_VUBT>3e-06):
        error("VBUT ERROR"+ str(CURR_VUBT))
    power.setVoltage(5,2)
    power.setVoltage(3.3,1)
    DVDD_test()
    bist_test()
    down_ft_code()
    sleep(0.6)

def xw_toExcel(data,excelname):  # xlsxwriter�ⴢ�����ݵ�excel
    try:
        workbook = openpyxl.load_workbook(excelname)  # �򿪹�����
        worksheet1 = workbook.active  # �����ӱ�
    except Exception as a:
        print(a)
        workbook = openpyxl.Workbook(excelname)
        workbook.save(filename= excelname)  # �رձ�
        workbook.close()
        workbook = openpyxl.load_workbook(excelname)  # �򿪹�����
        worksheet1 = workbook.active
    rows = worksheet1.max_row
    j = 0
    for i in data:
        j+=1
        worksheet1.cell(row=rows+1,column = j).value = i
    workbook.save(filename= excelname)  # �رձ�
    workbook.close()
def Creat_Thread(thread,*args1):
    thread_uart_read=threading.Thread(target=thread,args=args1)
    thread_uart_read.setDaemon(True)
    thread_uart_read.start()
def Check_CurrThread():
    while True:
        CURR_CHARG_IN = power.Get_Curr(2)
        if(CURR_CHARG_IN > 0.02):
            error("CURR_CHARG_IN ERROR " + str(CURR_CHARG_IN))
        sleep(1)
def read_id_txt(max_val):
    with open(".\AB_NEW_ID\id"+ hex(max_val).replace("0x","") + ".txt","r") as f:
        str = f.read().replace("\n","")
    return str
def Write_OtpBySelf():
    power.setVoltage(5,2)
    # val = int(otp_buff[6],16)
    # xor_val = 0
    # for i in range(0,4):
    #     xor_val^=val>>i&0x1
    # val|=0x80
    # val|=xor_val<<6
    # input_check = input("ȷ����¼otp��(y/n):")
    # if((input_check.lower() != 'y')):
    #     sys.exit()
    power.setVoltage(0,2)
    sleep(0.5)
    power.setVoltage(5,2)
    xw_toExcel(otp_buff,"3122_opt.xlsx")
    while(True):
        if('CPU Stopped' in get_cmd_result("e p")):
            get_cmd_result("e f853c 88")
            if('f8530 :                                     88'in get_cmd_result("e f853c")):
                get_cmd_result("e r pc c0")
                if('read cm0 reg f = c0\n'in get_cmd_result("e r pc")):
                    get_cmd_result("e otp .\AB_NEW_ID\id"+ hex(max_val).replace("0x","") + ".txt 2")
                    sleep(0.1)
                    get_cmd_result("e otp flash_178.txt 178")
                    sleep(0.1)
                    get_cmd_result("e otw 139 8f")
                    break
def bist_test():
    os.system(r"tool\bist.bat")
    str = get_cmd_result("e f8518l8")
    if("ff ff 03 00 00 00 00 00" not in str):
        error("bist test_error")
def gen_id():
    dir = (os.getcwd() + r"\AB_NEW_ID\*.txt")
    file_name(dir)
    str1 = "python f_gen3122id.py " + hex(max_val).replace("0x","")
    get_cmd_result(str1)
    otp_buff.append(read_id_txt(max_val))
def to_hex(val):
    return hex(val).replace("0x","")
def HvLdo_test():
    cail_val = 0x6
    get_cmd_result("e 20004 06")
    sleep(0.2)
    get_cmd_result("e 20000 0a")
    sleep(1)
    if("01" not in get_cmd_result("e 20001")):
        return FALSE
    vol = oscilloscope.Get_Vol(3)
    if(vol<=3.35 and vol >=3.25):
        return cail_val
    while(vol<=3.25):
        cail_val-=1
        get_cmd_result("e 20004 0"+ to_hex(cail_val))
        sleep(0.2)
        get_cmd_result("e 20000 0a")
        sleep(1)
        if("01" not in get_cmd_result("e 20001")):
            return FALSE
        vol = oscilloscope.Get_Vol(3)
        if(vol<=3.35 and vol >=3.25):
            return cail_val
        if(cail_val <= 0x0):
            return False
    while(vol>=3.35):
        cail_val+=1
        get_cmd_result("e 20004 0"+ to_hex(cail_val))
        sleep(0.2)
        get_cmd_result("e 20000 0a")
        sleep(1)
        if("01" not in get_cmd_result("e 20001")):
            return FALSE
        vol = oscilloscope.Get_Vol(3)
        if(vol<=3.35 and vol >=3.25):
            return cail_val
        if(cail_val >= 0xf):
            return False
    return cail_val
def Vcard_test(val):
    cail_val = 0x4
    if (val==0):
        valmax = 1.85
        valmin = 1.75
    if(val == 1):
        valmax = 3.05
        valmin = 2.95
    get_cmd_result("e 20004 010"+to_hex(cail_val)+"0"+str(val))
    sleep(0.2)
    get_cmd_result("e 20000 0e")
    sleep(1)
    if("01" not in get_cmd_result("e 20001")):
        return FALSE
    vol = oscilloscope.Get_Vol(4)
    if(vol<valmax and vol >valmin):
        return cail_val
    while(vol<valmin):
        cail_val+=1
        get_cmd_result("e 20004 010"+to_hex(cail_val)+"0"+str(val))
        sleep(0.2)
        get_cmd_result("e 20000 0e")
        sleep(1)
        if("01" not in get_cmd_result("e 20001")):
            return FALSE
        vol = oscilloscope.Get_Vol(4)
        if(vol<valmax and vol >valmin):
            return cail_val
        if(cail_val >= 0xf):
            return False
    while(vol>valmax):
        cail_val-=1
        get_cmd_result("e 20004 010"+to_hex(cail_val)+"0"+str(val))
        sleep(0.2)
        get_cmd_result("e 20000 0e")
        sleep(1)
        if("01" not in get_cmd_result("e 20001")):
            return FALSE
        vol = oscilloscope.Get_Vol(4)
        if(vol<valmax and vol >valmin):
            return cail_val
        if(cail_val <= 0):
            return False
    return cail_val
def charg_test():
    get_cmd_result("e fa820 321800")
    cail_val = 0x8
    get_cmd_result("e fa823 0"+to_hex(cail_val))
    sleep(0.2)
    vol = oscilloscope2.Get_Vol(1)
    valmax = 4.25
    valmin = 4.15
    if(vol<valmax and vol >valmin):
        return cail_val
    while(vol<valmin):
        cail_val+=1
        get_cmd_result("e fa823 0"+to_hex(cail_val))
        sleep(0.2)
        vol = oscilloscope2.Get_Vol(1)
        if(vol<valmax and vol >valmin):
            return cail_val
        if(cail_val >= 0xf):
            return False
    while(vol>valmax):
        cail_val-=1
        get_cmd_result("e fa823 0"+to_hex(cail_val))
        sleep(0.2)
        vol = oscilloscope2.Get_Vol(1)
        if(vol<valmax and vol >valmin):
            return cail_val
        if(cail_val <= 0):
            return False
    return cail_val
oscilloscope = ZLG1104()
oscilloscope2 = ZLG2014()
multimeter  = Agilent_34410A()
power = Agilent_66319d()
# zlg_2014 = ZLG1104("USB0::0x04CC::0x121C::123456789::RAW")
# os.environ['BAUD']="320"
if __name__ == "__main__":
    power.setVoltage(0,2)
    sleep(0.1)
    power.setVoltage(5,2)
    while(True):
        if('CPU Stopped' in get_cmd_result("e p")):
            get_cmd_result("e f853c 88")
            if('f8530 :                                     88'in get_cmd_result("e f853c")):
                get_cmd_result("e r pc c0")
                if('read cm0 reg f = c0\n'in get_cmd_result("e r pc")):
                    get_cmd_result("e otw 0 1111")
                    break
    ft_test_init()
    Creat_Thread(Check_CurrThread)
    gen_id()
    RC192_test()
    print(osc_32k_cal())

    val = HvLdo_test()
    otp_buff.append(val)
    print(val)
    down_otp("0b")
    val = Vcard_test(0)
    otp_buff.append(val)
    print(val)
    down_otp("0f")

    val = Vcard_test(1)
    otp_buff.append(val)
    print(val)
    down_otp("0f")
    # char_val = charg_test()
    # otp_buff.append(char_val)
    # print(char_val)

    print(otp_buff)
    Write_OtpBySelf()

```
