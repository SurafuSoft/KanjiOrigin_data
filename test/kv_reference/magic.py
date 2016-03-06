#!/usr/bin/kivy
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MagicLayout(BoxLayout):

    def change_text(self):
        print("Chaning text")
        # TODO get text from id: important_text