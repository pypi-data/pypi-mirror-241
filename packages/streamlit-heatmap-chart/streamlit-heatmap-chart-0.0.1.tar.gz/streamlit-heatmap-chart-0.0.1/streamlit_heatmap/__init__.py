import os
import streamlit.components.v1 as components

_RELEASE = True 

if not _RELEASE:
    _HeatMap_chart = components.declare_component(
        "HeatMap_chart",
        url="http://localhost:3001",
    )
else:
    
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _HeatMap_chart = components.declare_component("HeatMap_chart", path=build_dir)

def HeatMap_chart(data=None, styles=None, heatmapLayout=None, key=None):
    
    component_value = _HeatMap_chart(data=data, styles=styles, heatmapLayout=heatmapLayout, key=key, default=0)

    return component_value
