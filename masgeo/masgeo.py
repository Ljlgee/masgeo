"""Main module."""

import ipyleaflet as ipyl

class Map(ipyl.Map):
    def __init__(self, center=[34.540833, 108.923611], zoom=5,**kwargs):
        super().__init__(center=center,zoom=zoom,**kwargs)
        self.add_control(ipyl.LayersControl())
