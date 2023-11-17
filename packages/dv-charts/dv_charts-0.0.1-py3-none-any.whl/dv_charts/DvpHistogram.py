# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DvpHistogram(Component):
    """A DvpHistogram component.
Plotly Express Histogram

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- bgColor (string; optional):
    Background color.

- className (string | dict; optional):
    CSS classes to be added to the component.

- data (list; optional):
    Data.

- groupbyField (string | boolean; optional):
    Group by field.

- groupbyFieldOrder (list; optional):
    Groupby field order.

- loading_state (dict; optional):
    loading state.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- nBins (number; optional):
    No. of bins.

- plotBgColor (string; optional):
    Plot background color.

- showBox (boolean; default True):
    Show box.

- showLabels (boolean; optional):
    Show Labels.

- showLegend (boolean; default True):
    Show legend.

- style (dict; optional):
    Inline CSS style.

- valueField (string; optional):
    valueField.

- wrapperHeight (number; default 500):
    wrapperHeight."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dv_charts'
    _type = 'DvpHistogram'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, valueField=Component.UNDEFINED, groupbyField=Component.UNDEFINED, wrapperHeight=Component.UNDEFINED, nBins=Component.UNDEFINED, bgColor=Component.UNDEFINED, plotBgColor=Component.UNDEFINED, className=Component.UNDEFINED, groupbyFieldOrder=Component.UNDEFINED, style=Component.UNDEFINED, showLegend=Component.UNDEFINED, showBox=Component.UNDEFINED, showLabels=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bgColor', 'className', 'data', 'groupbyField', 'groupbyFieldOrder', 'loading_state', 'nBins', 'plotBgColor', 'showBox', 'showLabels', 'showLegend', 'style', 'valueField', 'wrapperHeight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bgColor', 'className', 'data', 'groupbyField', 'groupbyFieldOrder', 'loading_state', 'nBins', 'plotBgColor', 'showBox', 'showLabels', 'showLegend', 'style', 'valueField', 'wrapperHeight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DvpHistogram, self).__init__(**args)
