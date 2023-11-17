# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LineDrawer(Component):
    """A LineDrawer component.
Line drawer

Keyword arguments:

- id (string; optional):
    Key to identify the component.

- catVariables (list; optional):
    Categorical variables.

- form (boolean | number | string | dict | list; optional):
    Form.

- inputs (dict; optional):
    Inputs.

- loading_state (dict; optional):
    Loading state.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- numVariables (list; optional):
    Numeric variables.

- variableEntryType (a value equal to: 'list', 'groupedList'; optional):
    variableEntryType."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dv_charts'
    _type = 'LineDrawer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, form=Component.UNDEFINED, inputs=Component.UNDEFINED, catVariables=Component.UNDEFINED, numVariables=Component.UNDEFINED, variableEntryType=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'catVariables', 'form', 'inputs', 'loading_state', 'numVariables', 'variableEntryType']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'catVariables', 'form', 'inputs', 'loading_state', 'numVariables', 'variableEntryType']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(LineDrawer, self).__init__(**args)
