# File: /example/fragments/combo_box.py
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

from gtklara import GTKlara


class ComboBox(GTKlara):
    ignore_signals = ["changed"]

    def __init__(self, children=[], **kwargs):
        super().__init__(children, kwargs, __file__)
        self._items = self._props["items"] if "items" in self._props else {}
        widget = self._get("@active")
        if not widget:
            return
        for key in self._items.keys():
            widget.append_text(key)
        widget.connect("changed", self.handle_changed)
        if "on_changed" in self._props:
            self._on_changed = self._prop("on_changed")

    def handle_changed(self, widget):
        text = list(self._items.keys())[widget.get_active()]
        value = self._items[text] if text in self._items else None
        if hasattr(self, "_on_changed"):
            self._on_changed(value)
