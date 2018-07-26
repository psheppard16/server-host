__author__ = 'psheppard16'
from Screens.screen import Screen
from tkinter import *

class MainMenu(Screen):
    def __init__(self, window):
        super().__init__(window, "mainMenu")
        self.playB = Button(self.window.root, text="Play!", command=self.play, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.playB.pack(in_=self.f, pady=15)
        self.instructionsB = Button(self.window.root, text="Instructions", command=self.instructions, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.instructionsB.pack(in_=self.f, pady=15)
        self.optionsB = Button(self.window.root, text="Options", command=self.options, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.optionsB.pack(in_=self.f, pady=15)

    def options(self):
        self.window.rMenu = "options"

    def play(self):
        self.window.rMenu = "serverEngine"

    def instructions(self):
        self.window.rMenu = "instructions"