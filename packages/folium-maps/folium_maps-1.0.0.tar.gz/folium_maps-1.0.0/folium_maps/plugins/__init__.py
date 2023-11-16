# -*- coding: utf-8 -*-

"""
Folium plugins
--------------

Wrap some of the most popular leaflet external plugins.

"""

from folium_maps.plugins.antpath import AntPath
from folium_maps.plugins.polyline_offset import PolyLineOffset
from folium_maps.plugins.beautify_icon import BeautifyIcon
from folium_maps.plugins.boat_marker import BoatMarker
from folium_maps.plugins.draw import Draw
from folium_maps.plugins.dual_map import DualMap
from folium_maps.plugins.fast_marker_cluster import FastMarkerCluster
from folium_maps.plugins.feature_group_sub_group import FeatureGroupSubGroup
from folium_maps.plugins.float_image import FloatImage
from folium_maps.plugins.fullscreen import Fullscreen
from folium_maps.plugins.geocoder import Geocoder
from folium_maps.plugins.heat_map import HeatMap
from folium_maps.plugins.heat_map_withtime import HeatMapWithTime
from folium_maps.plugins.locate_control import LocateControl
from folium_maps.plugins.marker_cluster import MarkerCluster
from folium_maps.plugins.measure_control import MeasureControl
from folium_maps.plugins.minimap import MiniMap
from folium_maps.plugins.mouse_position import MousePosition
from folium_maps.plugins.pattern import CirclePattern, StripePattern
from folium_maps.plugins.polyline_text_path import PolyLineTextPath
from folium_maps.plugins.scroll_zoom_toggler import ScrollZoomToggler
from folium_maps.plugins.search import Search
from folium_maps.plugins.semicircle import SemiCircle
from folium_maps.plugins.terminator import Terminator
from folium_maps.plugins.time_slider_choropleth import TimeSliderChoropleth
from folium_maps.plugins.timestamped_geo_json import TimestampedGeoJson
from folium_maps.plugins.timestamped_wmstilelayer import TimestampedWmsTileLayers

__all__ = [
    'AntPath',
    'BeautifyIcon',
    'BoatMarker',
    'CirclePattern',
    'Draw',
    'DualMap',
    'FastMarkerCluster',
    'FeatureGroupSubGroup',
    'FloatImage',
    'Fullscreen',
    'Geocoder',
    'HeatMap',
    'HeatMapWithTime',
    'LocateControl',
    'MarkerCluster',
    'MeasureControl',
    'MiniMap',
    'MousePosition',
    'PolyLineTextPath',
    'PolyLineOffset',
    'ScrollZoomToggler',
    'Search',
    'SemiCircle',
    'StripePattern',
    'Terminator',
    'TimeSliderChoropleth',
    'TimestampedGeoJson',
    'TimestampedWmsTileLayers',
]
