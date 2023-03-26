from doctest import master
from email.mime import image
from logging import shutdown
from multiprocessing.pool import ApplyResult
from tkinter import*
import tkinter
from tracemalloc import start
from turtle import width
import webbrowser
import customtkinter
import os
import time
import tkinter.font as font
import random
import pygame
loaded = False
startMenuOpened = 0


def gui():
    global startMenuOpened
    global soundPercentage
    global osShutdown
    global loaded
    customtkinter.set_appearance_mode("Dark")  
    customtkinter.set_default_color_theme("blue")  

    app = customtkinter.CTk()  
    app.geometry("1750x875")
    app.title("Vast v1.0")

    title = customtkinter.CTkLabel(master=app,text="Vast",bg="darkblue")
    title.config(font=("Omicron", 30))
    title.pack()

    sliderTest = customtkinter.CTkSlider(master=app,)

    def browserButton():
        def youtubeButton():
            webbrowser.open("https://youtube.com")
            browserList.destroy()
        def googleButton():
            webbrowser.open("https://google.com")
            browserList.destroy()
        def customSiteButton():
            print("Please enter a URL (Type in cancel to cancel the process)")
            get_url = input("")
            if get_url == "cancel":
                print("Canceled")
                browserList.destroy()
            else:    
                print("Redirecting to default browser (2s)...")
                time.sleep(1)
                print("Redirecting to default browser (1s)...")
                time.sleep(1)
                webbrowser.open(get_url)
                time.sleep(5)
                customSiteButton()
                browserList.destroy()
        def gmailButton():
            webbrowser.open("https://gmail.com")
            browserList.destroy()

        browserList = customtkinter.CTk()
        browserList.title("Browser Lists")
        browserList.geometry("400x350")

        google = customtkinter.CTkButton(master=browserList,text="    Google    ",command=googleButton,height=50)
        google.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)

        youtube = customtkinter.CTkButton(master=browserList,text="    Youtube    ",command=youtubeButton,height=50)
        youtube.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

        gmail = customtkinter.CTkButton(master=browserList,text="    Gmail    ",command=gmailButton,height=50)
        gmail.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

        openCustomSite = customtkinter.CTkButton(master=browserList,text="    Custom    ",command=customSiteButton,height=50)
        openCustomSite.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

        browserList.mainloop()

    def startMenuButton():
        startMenu = customtkinter.CTk()
        startMenu.title("Start Menu")
        startMenu.geometry("750x650")


        settings = customtkinter.CTkButton(master=startMenu, text="       Settings      ",width=40,height=40, command=settingsButton)
        settings.place(relx=0.1,rely=0.85,anchor=tkinter.CENTER)
                
        reboot = customtkinter.CTkButton(master=startMenu, text="       Reboot PC      ",width=40,height=40, command=shutdownButton) 
        reboot.place(relx=0.1,rely=0.95,anchor=tkinter.CENTER)

        startMenu.mainloop()


    def appButton():
        appLists = customtkinter.CTk()
        appLists.geometry("500x500")
        appLists.title("App Lists")
        appTitle = customtkinter.CTkLabel(master=appLists,text="App Lists")
        appTitle.config(font=("Courier",30))
        appTitle.pack()
        def calc():
            calc = customtkinter.CTk()
            calc.title("Calculator")
            calc.geometry("400x450")
                
            calc.mainloop()
        calculator = customtkinter.CTkButton(master=appLists,text="         Calculator         ",command=calc)
        calculator.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)
        appLists.mainloop()
    def gameButton():
        GameList = customtkinter.CTk()
        GameList.geometry("600x750")
        GameList.title("Games")
        GameList.mainloop()
    def settingsButton():
        def switchThemeLight():
            customtkinter.set_appearance_mode("Light")
        def switchThemeDark():
            customtkinter.set_appearance_mode("Dark")
        settingsWindow = customtkinter.CTk()
        settingsWindow.title("Settings")
        settingsWindow.geometry("650x500")
        settingsText = customtkinter.CTkLabel(master=settingsWindow,text="Settings")
        settingsText.pack()
        settingsText.config(font=("Courier",30))
        themeLabel = customtkinter.CTkLabel(master=settingsWindow,text="Themes")
        themeLabel.pack(pady=45)
        themeLabel.config(font=("Courier",20))
        themeSwitchLight = customtkinter.CTkButton(master=settingsWindow,text="          Light Theme         ",width=50,height=30,command=switchThemeLight)
        themeSwitchLight.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)
        themeSwitchDark = customtkinter.CTkButton(master=settingsWindow,text="           Dark Theme         ",width=50,height=30,command=switchThemeDark)
        themeSwitchDark.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)
        settingsWindow.mainloop()
    def shutdownButton():
        shutdownConfirmWindow = customtkinter.CTk()
        shutdownConfirmWindow.geometry("650x250")
        shutdownConfirmWindow.title("Reboot Confirmation")
        def restart():
            os.system("shutdown /r /t 10")
            print("System will restart within 10 seconds")
        def cancel():
            print("System restart has been canceled")
            shutdownConfirmWindow.destroy()
        label = customtkinter.CTkLabel(master=shutdownConfirmWindow,text="Are you sure you want to reboot your PC?")
        label.pack(pady=10)
        label.config(font=("Courier",20))
        shutdownConfirmYes = customtkinter.CTkButton(master=shutdownConfirmWindow,text="          Yes         ",command=restart)
        shutdownConfirmYes.place(relx=0.3,rely=0.5,anchor=tkinter.CENTER)
        shutdownConfirmNo = customtkinter.CTkButton(master=shutdownConfirmWindow,text="          No          ",command=cancel)
        shutdownConfirmNo.place(relx=0.7,rely=0.5,anchor=tkinter.CENTER)
        shutdownConfirmWindow.mainloop()
    def exitButtonFunc():
        global osShutdown
        osShutdown = True
        app.destroy()
        exit()
    exitButton = customtkinter.CTkButton(master=app,text="          Exit          ",width=40,height=50, command=exitButtonFunc)
    exitButton.place(relx=0.935,rely=0.945,anchor=tkinter.CENTER)

    browser = customtkinter.CTkButton(master=app, text="          Browsers          ",width=40,height=50, command=browserButton)
    browser.place(relx=0.0455, rely=0.1, anchor=tkinter.CENTER)

    apps = customtkinter.CTkButton(master=app, text="          Apps          ",width=40,height=50, command=appButton)
    apps.place(relx=0.0375,rely=0.185,anchor=tkinter.CENTER)

    games = customtkinter.CTkButton(master=app, text="          Games          ",width=30,height=50, command=gameButton)
    games.place(relx=0.04,rely=0.275,anchor=tkinter.CENTER)
    
    startMenu = customtkinter.CTkButton(master=app, text="       Start Menu      ",width=40,height=50, command=startMenuButton)
    startMenu.place(relx=0.01,rely=0.925)

    app.attributes('-alpha', True)
    app.mainloop()
    

osShutdown = False


gui()
if osShutdown == True:
    exit()

#compile after every update
