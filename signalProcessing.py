#Tutorial link: https://ataspinar.com/2018/04/04/machine-learning-with-signal-processing-techniques/
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fftfreq, ifft
import pandas as pd
from scipy.fft import fft,ifft
homePage=Tk()
homePage.geometry("1000x300")
frm1=Frame(homePage)
frm1.place(x=0,y=0)
lblNumberOfSamples=Label(frm1,text="Enter number of samples").grid(row=0,column=0,sticky=W)
entryNumberOfSamples=Entry(frm1,width=5)
entryNumberOfSamples.grid(row=0,column=1,sticky=W)
lblStartPoint=Label(frm1,text="Enter the start time").grid(row=0,column=2,sticky=W)
entryStartPoint=Entry(frm1,width=5)
entryStartPoint.grid(row=0,column=3)
lblEndPoint=Label(frm1,text="Enter the end time").grid(row=0,column=4,sticky=W)
entryEndPoint=Entry(frm1,width=5)
entryEndPoint.grid(row=0,column=5)

#Create to show Beta signal
lblfBeta=Label(frm1,text="Enter the Beta's frequency (Beta>13Hz)").grid(row=1,column=0,sticky=W)
entryfBeta=Entry(frm1,width=5)
entryfBeta.grid(row=1,column=1)
lblABeta=Label(frm1,text="Enter the amplitude of Beta's frequency (Action potential>+40mv)").grid(row=1,column=2,sticky=W)
entryABeta=Entry(frm1,width=5)
entryABeta.grid(row=1,column=3)
def showBetaSignal():
    try:
        N=int(entryNumberOfSamples.get())*(int(entryEndPoint.get())-int(entryStartPoint.get()))
        t=np.linspace(int(entryStartPoint.get()),int(entryEndPoint.get()),N)
        signalBeta=int(entryABeta.get())*np.sin(2*math.pi*int(entryfBeta.get())*t)
        plt.plot(t,signalBeta)
        plt.title("Beta signal with frequencey " +entryfBeta.get()+" Hz")
        plt.show()
    except ValueError:
        print("This is not a number")
btnDisplayBeta=Button(frm1,text="Display Beta signal",command=showBetaSignal)
btnDisplayBeta.grid(row=1,column=4,sticky=W)
#Create to show Alpha signal
lblfAlpha=Label(frm1,text="Enter the Alpha's frequency (8Hz<Alpha<13Hz)").grid(row=2,column=0,sticky=W)
entryfAlpha=Entry(frm1,width=5)
entryfAlpha.grid(row=2,column=1)
lblAAlpha=Label(frm1,text="Enter the amplitude of Alpha's frequency (Action potential>+40mv)").grid(row=2,column=2,sticky=W)
entryAAlpha=Entry(frm1,width=5)
entryAAlpha.grid(row=2,column=3)

def showAlphaSignal():
    try:
        N=int(entryNumberOfSamples.get())*(int(entryEndPoint.get())-int(entryStartPoint.get()))
        t=np.linspace(int(entryStartPoint.get()),int(entryEndPoint.get()),N)
        signalAlpha=int(entryAAlpha.get())*np.sin(2*math.pi*int(entryfAlpha.get())*t)
        plt.plot(t,signalAlpha)
        plt.title("Alpfa signal with frequencey "+entryfAlpha.get()+" Hz")
        plt.show()
    except ValueError:
        print("This is not a number")
btnDisplayAlpha=Button(frm1,text="Display Alpha signal",command=showAlphaSignal)
btnDisplayAlpha.grid(row=2,column=4,sticky=W)
#Create to show Theta signal
lblfTheta=Label(frm1,text="Enter the Theta's frequency (4Hz<Tetha<8Hz)").grid(row=3,column=0,sticky=W)
entryfTheta=Entry(frm1,width=5)
entryfTheta.grid(row=3,column=1)
lblATheta=Label(frm1,text="Enter the amplitude of Theta's frequency (Action potential>+40mv)").grid(row=3,column=2,sticky=W)
entryATheta=Entry(frm1,width=5)
entryATheta.grid(row=3,column=3)

def showThetaSignal():
    try:
        N=int(entryNumberOfSamples.get())*(int(entryEndPoint.get())-int(entryStartPoint.get()))
        t=np.linspace(int(entryStartPoint.get()),int(entryEndPoint.get()),N)
        signalTheta=int(entryATheta.get())*np.sin(2*math.pi*int(entryfTheta.get())*t)
        plt.plot(t,signalTheta)
        plt.title("Tetha signal with frequencey "+entryfTheta.get()+" Hz")
        plt.show()
    except ValueError:
        print("This is not number.")
btnDisplayTheta=Button(frm1,text="Display Theta signal",command=showThetaSignal)
btnDisplayTheta.grid(row=3,column=4,sticky=W)
#Create to show Delta Signal
lblfDelta=Label(frm1,text="Enter the Delta's frequency (0.5Hz<Delta<4Hz").grid(row=4,column=0,sticky=W)
entryfDelta=Entry(frm1,width=5)
entryfDelta.grid(row=4,column=1)
lblADelta=Label(frm1,text="Enter the amplitude of Delta's frequency (Action potential>+40mv)").grid(row=4,column=2,sticky=W)
entryADelta=Entry(frm1,width=5)
entryADelta.grid(row=4,column=3)

def showDeltaSignal():
    try:
        N=int(entryNumberOfSamples.get())*(int(entryEndPoint.get())-int(entryStartPoint.get()))
        t=np.linspace(int(entryStartPoint.get()),int(entryEndPoint.get()),N)
        signalDelta=int(entryADelta.get())*np.sin(2*math.pi*int(entryfDelta.get())*t)
        plt.plot(t,signalDelta)
        plt.title("Delta signal with frequencey "+entryfDelta.get()+" Hz")
        plt.show()
    except ValueError:
        print("Value is not a number.")
btnDisplayDelta=Button(frm1,text="Display Delta signal",command=showDeltaSignal)
btnDisplayDelta.grid(row=4,column=4,sticky=W)

def createEEGSignal():
    try:
        N=int(entryNumberOfSamples.get())*(int(entryEndPoint.get())-int(entryStartPoint.get()))
        t=np.linspace(int(entryStartPoint.get()),int(entryEndPoint.get()),N)
        EEGSignale=int(entryABeta.get())*np.sin(2*math.pi*int(entryfBeta.get())*t)+int(entryAAlpha.get())*np.sin(2*math.pi*int(entryfAlpha.get())*t)+int(entryATheta.get())*np.sin(2*math.pi*int(entryfTheta.get())*t)+int(entryADelta.get())*np.sin(2*math.pi*int(entryfDelta.get())*t)
        plt.plot(t,EEGSignale)
        plt.title("EEG Signal in the time domain in the interval time of "+entryStartPoint.get()+" second to "+entryEndPoint.get()+" second.")
        plt.show()
    except ValueError:
        print("This is not a number.")
btnCreateEEG=Button(frm1,text="Generate EEG",command=createEEGSignal)
btnCreateEEG.grid(row=5,column=0)

def calculateFFTFunc():
    try:
        N=int(entryNumberOfSamples.get())*(int(entryEndPoint.get())-int(entryStartPoint.get()))
        # T=(int(entryEndPoint.get())-int(entryStartPoint.get()))/N
        t=np.linspace(int(entryStartPoint.get()),int(entryEndPoint.get()),N)
        EEGSignale_t=int(entryABeta.get())*np.sin(2*math.pi*int(entryfBeta.get())*t)+int(entryAAlpha.get())*np.sin(2*math.pi*int(entryfAlpha.get())*t)+int(entryATheta.get())*np.sin(2*math.pi*int(entryfTheta.get())*t)+int(entryADelta.get())*np.sin(2*math.pi*int(entryfDelta.get())*t)
        fftOfEEGSignal=fft(EEGSignale_t)
        frequency=np.linspace(int(entryStartPoint.get()),int(entryNumberOfSamples.get())/2,N//2)
        plt.plot(frequency,np.abs(fftOfEEGSignal))
        plt.show()
    except ValueError:
        print("This is not a number.")
btnCalculateFFT=Button(frm1,text="Calculate FFT of EEG",command=calculateFFTFunc)
btnCalculateFFT.grid(row=5,column=1)
homePage.mainloop()
