#!/usr/bin/kivy
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MagicLayout(BoxLayout):
    m_text = StringProperty("Reference between widgets test")