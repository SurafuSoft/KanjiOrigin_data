#!/usr/bin/kivy
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty
from os.path import dirname, join, isfile, exists

class FooScreen(Screen):
    # 'content' refers to the id of the BoxLayout in FooScreen in foo.kv
    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(FooScreen, self).add_widget(*args)

class FooApp(App):
    imp_text = StringProperty("Should change to text from id: magic_text")
    screen_magic = ObjectProperty()
    magic_layout = ObjectProperty()

    def build(self):
        self.title = 'Foo'

        # References
        self.sm = self.root.ids.sm  # ScreenManager

        # Setting up screens for screen manager
        self.screens = {}
        self.available_screens = (['MainMenu', 'Magic'])
        self.screen_names = self.available_screens
        curdir = dirname(__file__)
        self.available_screens = [join(curdir,
            '{}.kv'.format(fn)) for fn in self.available_screens]
        self.go_screen(0)

    # Go to other screen
    def go_screen(self, idx):
        print("Change MainScreen to: {}".format(idx))
        self.index = idx
        # Go to not main menu
        if idx == 0:
            self.root.ids.sm.switch_to(self.load_screen(idx), direction='right')
        # Go to main menu
        else:
            self.root.ids.sm.switch_to(self.load_screen(idx), direction='left')

    def load_screen(self, index):
        if index in self.screens:
            return self.screens[index]
        screen = Builder.load_file(self.available_screens[index].lower())
        self.screens[index] = screen
        # if index refers to 'Magic', create reference
        if index == 1:
            Clock.schedule_once(lambda dt: self.create_reference())
        return screen

    # Trying to get id's
    def create_reference(self):
        print("\nrefs:")
        # Get screen from ScreenManager
        self.screen_magic = self.sm.get_screen(self.screen_names[1])
        # screen.boxlayout.magiclayout
        self.magic_layout = self.screen_magic.children[0].children[0]

    def change_text(self):
        # Get text from id: magic_text
        if self.magic_layout:
            self.imp_text = self.magic_layout.ids['magic_text'].text

if __name__ == '__main__':
    FooApp().run()

