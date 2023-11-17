# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DvpNumStats(Component):
    """A DvpNumStats component.
A component to describe numerical variables

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

- missingValues (list; default [99999, 88888, 9999, 8888, 8881, 8882, 7777, 6666]):
    missingValues.

- pagination (dict; default {    defaultPageSize: 20,    hideOnSinglePage: True,    showSizeChanger: False,}):
    Config of pagination. You can ref table pagination config or full
    pagination document, hide it by setting it to False.

    `pagination` is a dict with keys:

    - current (number; optional)

    - disabled (boolean; optional)

    - hideOnSinglePage (boolean; optional)

    - pageSize (number; optional)

    - pageSizeOptions (list of numbers; optional)

    - position (a value equal to: 'topLeft', 'topCenter', 'topRight', 'bottomLeft', 'bottomCenter', 'bottomRight'; optional)

    - showQuickJumper (boolean; optional)

    - showSizeChanger (boolean; optional)

    - showTotal (boolean; optional)

    - showTotalPrefix (string; optional)

    - showTotalSuffix (string; optional)

    - simple (boolean; optional)

    - size (a value equal to: 'default', 'small'; optional)

    - total (number; optional) | boolean | dict

- style (dict; optional):
    Inline CSS style.

- variable (string; optional):
    Variable.

- variable2 (string; optional):
    Variable 2."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dv_charts'
    _type = 'DvpNumStats'
    @_explicitize_args
    def __init__(self, data=Component.UNDEFINED, variable=Component.UNDEFINED, variable2=Component.UNDEFINED, groupBy=Component.UNDEFINED, missingValues=Component.UNDEFINED, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, alias=Component.UNDEFINED, labels=Component.UNDEFINED, pagination=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'alias', 'className', 'data', 'groupBy', 'labels', 'missingValues', 'pagination', 'style', 'variable', 'variable2']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'alias', 'className', 'data', 'groupBy', 'labels', 'missingValues', 'pagination', 'style', 'variable', 'variable2']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DvpNumStats, self).__init__(**args)
