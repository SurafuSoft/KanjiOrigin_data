#!/usr/bin/kivy
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty


kv_foo = '''
<FooScreen>:
    BoxLayout:
        id: content
        orientation: 'vertical'
        spacing: '20dp'
        padding: '8dp'
        size_hint: (1, 1)

BoxLayout:
    orientation: 'vertical'

    Label:
        id: important_text
        size_hint_y: 0.3
        text: app.imp_text

    Button:
        id: magic_change
        size_hint_y: 0.3
        text: "Change text above to text below (after screen switch)"
        on_press: app.change_text()

    ScreenManager:
        id: sm
        on_current_screen:
            idx = app.screen_names.index(args[1].name)
'''


class FooScreen(Screen):
    # 'content' refers to the id of the BoxLayout in FooScreen in foo.kv
    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(FooScreen, self).add_widget(*args)

class FooApp(App):
    imp_text = StringProperty("Should change to text from id: magic_text")

    def build(self):
        self.title = 'Foo'
        self.root = root = Builder.load_string(kv_foo)

        # Trying stuff with References, fail code
        self.sm = self.root.ids.sm  # ScreenManager
        #self.bcontent = self.sm.ids.content # id content in BoxLayout in ScreenManager
        self.screen_widget = FooScreen()  # FooScreen

        # Setting up screens for screen manager
        self.screens = {}
        self.available_screens = [kv_mainmenu, kv_magic]
        self.screen_names = ['MainMenu', 'Magic']
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

    # Load kv files
    def load_screen(self, index):
        if index in self.screens:
            return self.screens[index]
        screen = Builder.load_string(self.available_screens[index])
        self.screens[index] = screen
        # if index refers to 'Magic' (kv_magic), create reference
        if index == 1:
            Clock.schedule_once(lambda dt: self.create_reference())
        return screen

    # Trying to get id's, fail code
    def create_reference(self):
        print("\nrefs:")
        print("Screenmanager ids:\n{}".format(self.sm.ids))
        #print("Screenwidget ids:\n{}".format(self.bcontent.ids))
        print("Screenwidget ids:\n{}".format(self.screen_widget.ids))
        self.screen_boxlayout = self.screen_widget.ids['content']  # proper id content in BoxLayout in ScreenManager?
        print("Screenboxlayout ids:\n{}".format(self.screen_boxlayout.ids))

    def change_text(self):
        print("Changing text")
        # TODO get text from id: magic_text
        # self.imp_text = text from magic_text


kv_mainmenu = '''
FooScreen:
    id: mainm
    name: 'MainMenu'

    Button:
        text: 'Magic'
        on_release: app.go_screen(1)
'''

kv_magic = '''
<MagicLayout>
    id: magic_layout
    orientation: 'vertical'

    Label:
        id: magic_text
        text: root.m_text

FooScreen:
    id: magic_screen
    name: 'Magic'

    MagicLayout
'''


class MagicLayout(BoxLayout):
    m_text = StringProperty("Reference between widgets test")


if __name__ == '__main__':
    FooApp().run()

