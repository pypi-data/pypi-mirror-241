# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DvpDesScatter(Component):
    """A DvpDesScatter component.
A component to build scatter

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

- labels (dict; optional):
    labels - A dict to remape the numbers into category.

- missingValues (list; default [99999, 88888, 9999, 8888, 8881, 7777, 8883, 6666]):
    missingValues.

- style (dict; optional):
    Inline CSS style.

- variable (string; optional):
    Variable Y Field.

- variable2 (string; optional):
    Variable 2 X Field.

- wrapperHeight (string | number; default 425):
    wrapperHeight."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dv_charts'
    _type = 'DvpDesScatter'
    @_explicitize_args
    def __init__(self, data=Component.UNDEFINED, variable=Component.UNDEFINED, variable2=Component.UNDEFINED, groupBy=Component.UNDEFINED, missingValues=Component.UNDEFINED, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, alias=Component.UNDEFINED, labels=Component.UNDEFINED, wrapperHeight=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alias', 'className', 'data', 'groupBy', 'labels', 'missingValues', 'style', 'variable', 'variable2', 'wrapperHeight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alias', 'className', 'data', 'groupBy', 'labels', 'missingValues', 'style', 'variable', 'variable2', 'wrapperHeight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DvpDesScatter, self).__init__(**args)
