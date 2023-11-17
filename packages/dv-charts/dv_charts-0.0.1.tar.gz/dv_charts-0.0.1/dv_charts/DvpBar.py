# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DvpBar(Component):
    """A DvpBar component.
Antd Bar

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string | dict; optional):
    CSS classes to be added to the component.

- colors (dict; optional):
    Dict of colors.

- data (list; optional):
    Data.

- direction (a value equal to: 'vertical', 'horizontal'; optional):
    Direction.

- groupbyField (string | boolean; optional):
    Group by field.

- hideXaxis (boolean; optional):
    Whether to hide x axis.

- hideYaxis (boolean; optional):
    Whether to hide y axis.

- isPercent (boolean; optional):
    100% percent mode.

- isStack (boolean; optional):
    Stack mode.

- labelField (string; optional):
    Field to show as label.

- labelPosition (a value equal to: 'top', 'right', 'middle'; default 'middle'):
    Label Position.

- legendLayout (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    legend Layout.

- legendPosition (a value equal to: 'top', 'right'; default 'right'):
    Legend Position.

- loading_state (dict; optional):
    loading state.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- padding (number; optional):
    Padding.

- showLabels (boolean; default True):
    Show Labels.

- showLegend (boolean; default True):
    Show legend.

- style (dict; optional):
    Inline CSS style.

- wrapperHeight (string | number; optional):
    wrapperHeight.

- xAxisTitle (string; optional):
    X axis title.

- xField (string; optional):
    X axis.

- yAxisTitle (string; optional):
    Y axis title.

- yField (string; optional):
    X axis."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dv_charts'
    _type = 'DvpBar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, xField=Component.UNDEFINED, yField=Component.UNDEFINED, xAxisTitle=Component.UNDEFINED, yAxisTitle=Component.UNDEFINED, hideXaxis=Component.UNDEFINED, hideYaxis=Component.UNDEFINED, wrapperHeight=Component.UNDEFINED, padding=Component.UNDEFINED, colors=Component.UNDEFINED, groupbyField=Component.UNDEFINED, labelField=Component.UNDEFINED, isStack=Component.UNDEFINED, isPercent=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, direction=Component.UNDEFINED, legendLayout=Component.UNDEFINED, legendPosition=Component.UNDEFINED, labelPosition=Component.UNDEFINED, showLegend=Component.UNDEFINED, showLabels=Component.UNDEFINED, onReady=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'colors', 'data', 'direction', 'groupbyField', 'hideXaxis', 'hideYaxis', 'isPercent', 'isStack', 'labelField', 'labelPosition', 'legendLayout', 'legendPosition', 'loading_state', 'padding', 'showLabels', 'showLegend', 'style', 'wrapperHeight', 'xAxisTitle', 'xField', 'yAxisTitle', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'colors', 'data', 'direction', 'groupbyField', 'hideXaxis', 'hideYaxis', 'isPercent', 'isStack', 'labelField', 'labelPosition', 'legendLayout', 'legendPosition', 'loading_state', 'padding', 'showLabels', 'showLegend', 'style', 'wrapperHeight', 'xAxisTitle', 'xField', 'yAxisTitle', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DvpBar, self).__init__(**args)
