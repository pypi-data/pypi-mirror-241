# File: /example/fragments/radio.py
# Project: gtklara
# File Created: 18-11-2023 15:39:42
# Author: Clay Risser
# -----
# BitSpur (c) Copyright 2022 - 2023
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gtklara import GTKlara, Gtk


class Radio(GTKlara):
    def __init__(self, children=[], **kwargs):
        super().__init__(children, kwargs, __file__)
        self._options = self._props["options"] if "options" in self._props else {}
        hidden_radio_button = Gtk.RadioButton("", "")
        hidden_radio_button.set_active(True)
        radio_buttons = []
        previous = hidden_radio_button
        for name, description in self._options.items():
            radio_button = Gtk.RadioButton(name, description, group=previous)
            previous = radio_button
            radio_button.set_active(False)
            radio_button.connect("toggled", self.handle_toggled)
            radio_buttons.append(radio_button)
        self._clear("@active")
        self._add("@active", radio_buttons)
        if "on_changed" in self._props:
            self._on_changed = self._props["on_changed"]

    def handle_toggled(self, widget):
        if widget.get_active():
            label = widget.get_label()
            value = self._options[label] if label in self._options else None
            if hasattr(self, "_on_changed"):
                self._on_changed(value)
