from curses import window
from tkinter.ttk import LabelFrame
from turtle import bgcolor
import qrcode # Used for making QR codes
import subprocess #Used for interacting with the CMD for net info
import tkinter # GUI framework
#Accessing Network Information and filtering out the information we need

# Getting name of current wifi network
SSIDinfo = subprocess.check_output(['netsh', 'wlan', 'show', 'interface']).decode('utf-8').split('\n')
SSIDinfo = [b.split(":")[1][1:-1] for b in SSIDinfo if "SSID" in b]
SSIDinfo = SSIDinfo [0]
#print (SSIDinfo)

#Getting password of current wifi network
Wifipass = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', SSIDinfo, 'key=clear']).decode('utf-8').split('\n')
Wifipass = [b.split(":")[1][1:-1] for b in Wifipass if "Key Content" in b]
Wifipass  = Wifipass[0]
#print (Wifipass)

# Making the QR code (and saving it)
img = qrcode.make("WIFI:S:{};T:WPA;P:{};;".format(SSIDinfo,Wifipass))
type(img)
img.save("{} QR Code.png".format(SSIDinfo))





#Making the core GUI for QR code

window = tkinter.Tk()

window.title('Wifi QR Code Generator by Savva | Current network: {}'.format(SSIDinfo))
window = tkinter.Canvas(window,width = 450, height = 450)

#Frame for introduction to service
introframe = LabelFrame(window)
introframe.pack(padx=10, pady=10)
intro = tkinter.Label(introframe, text="Welcome. Current network is {} - the password is {}".format(SSIDinfo,Wifipass))
intro.pack()

#QR display Frame
QRdisplayframe = tkinter.Frame(window, background='black')
QRdisplayframe.pack(padx=100, pady=30)
image = tkinter.PhotoImage(file = '{} QR Code.png'.format(SSIDinfo))
QRImage = tkinter.Label(QRdisplayframe, image= image).pack(side = tkinter.LEFT, padx=10, pady=10)

window.pack()

#Additional Features

#Keeping the GUI running
window.mainloop()
