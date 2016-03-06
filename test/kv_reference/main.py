#!/usr/bin/kivy
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from os.path import dirname, join, isfile, exists

class FooScreen(Screen):
    # 'content' refers to the id of the BoxLayout in FooScreen in foo.kv
    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(FooScreen, self).add_widget(*args)

class FooApp(App):
    def build(self):
        self.title = 'Foo'

        # References
        self.sm = self.root.ids.sm  # ScreenManager
        #self.bcontent = self.sm.ids.content # id content in BoxLayout in ScreenManager
        self.screen_widget = FooScreen()  # FooScreen

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

    def create_reference(self):
        print("\nrefs:")
        print("Screenmanager ids:\n{}".format(self.sm.ids))
        #print("Screenwidget ids:\n{}".format(self.bcontent.ids))
        print("Screenwidget ids:\n{}".format(self.screen_widget.ids))
        self.screen_boxlayout = self.screen_widget.ids['content']  # proper id content in BoxLayout in ScreenManager?
        print("Screenboxlayout ids:\n{}".format(self.screen_boxlayout.ids))


if __name__ == '__main__':
    FooApp().run()
