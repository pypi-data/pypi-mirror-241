# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DvpScatter(Component):
    """A DvpScatter component.
Scatter

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- annotations (list; optional):
    annotations.

- className (string | dict; optional):
    CSS classes to be added to the component.

- data (list; optional):
    Data.

- groupbyField (string | boolean; optional):
    Group by field.

- legendLayout (a value equal to: 'vertical', 'horizontal'; optional):
    legend Layout.

- legendPosition (a value equal to: 'top', 'right'; optional):
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

- regrs (list; optional):
    Regression equations in a list of dict.

- showLegend (boolean; optional):
    Show legend.

- size (number | list; default 3):
    Size or size range.

- sizeField (string; optional):
    Size Field.

- style (dict; optional):
    Inline CSS style.

- xAxisTitle (string; optional):
    X axis title.

- xField (string; default 'x'):
    x Field.

- yAxisTitle (string; optional):
    Y axis title.

- yField (string; default 'y'):
    y Field."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dv_charts'
    _type = 'DvpScatter'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, xField=Component.UNDEFINED, yField=Component.UNDEFINED, xAxisTitle=Component.UNDEFINED, yAxisTitle=Component.UNDEFINED, groupbyField=Component.UNDEFINED, sizeField=Component.UNDEFINED, regrs=Component.UNDEFINED, legendLayout=Component.UNDEFINED, legendPosition=Component.UNDEFINED, showLegend=Component.UNDEFINED, size=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, annotations=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'annotations', 'className', 'data', 'groupbyField', 'legendLayout', 'legendPosition', 'loading_state', 'regrs', 'showLegend', 'size', 'sizeField', 'style', 'xAxisTitle', 'xField', 'yAxisTitle', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'annotations', 'className', 'data', 'groupbyField', 'legendLayout', 'legendPosition', 'loading_state', 'regrs', 'showLegend', 'size', 'sizeField', 'style', 'xAxisTitle', 'xField', 'yAxisTitle', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DvpScatter, self).__init__(**args)
