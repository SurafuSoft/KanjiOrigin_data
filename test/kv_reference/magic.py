#!/usr/bin/kivy
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MagicLayout(BoxLayout):
    m_text = StringProperty("Should change to text from id: important_text")

    def change_text(self):
        print("Chaning text")
        # TODO get text from id: important_text
