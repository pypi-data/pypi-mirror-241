# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DvpDesBar(Component):
    """A DvpDesBar component.
A component to describe categorical data

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- alias (dict; optional):
    Alias - A dict to rename the variable.

- className (string; optional):
    Classname.

- data (list; optional):
    A list of values.

- groupBy (string; optional):
    Group by.

- isPercent (boolean; default False):
    isPercent.

- labels (dict; optional):
    labels - A dict to remape the numbers into category.

- minHeight (string | number; default 250):
    minHeight.

- missingValues (list; default [99999, 88888, 9999, 8888, 8881, 8882, 7777, 6666]):
    missingValues.

- padding (number; optional):
    Padding.

- style (dict; optional):
    Inline CSS style.

- variable (string; optional):
    Variable.

- wrapperHeight (string | number; optional):
    wrapperHeight."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dv_charts'
    _type = 'DvpDesBar'
    @_explicitize_args
    def __init__(self, data=Component.UNDEFINED, variable=Component.UNDEFINED, groupBy=Component.UNDEFINED, missingValues=Component.UNDEFINED, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, alias=Component.UNDEFINED, labels=Component.UNDEFINED, padding=Component.UNDEFINED, wrapperHeight=Component.UNDEFINED, minHeight=Component.UNDEFINED, isPercent=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alias', 'className', 'data', 'groupBy', 'isPercent', 'labels', 'minHeight', 'missingValues', 'padding', 'style', 'variable', 'wrapperHeight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alias', 'className', 'data', 'groupBy', 'isPercent', 'labels', 'minHeight', 'missingValues', 'padding', 'style', 'variable', 'wrapperHeight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DvpDesBar, self).__init__(**args)
