# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DesRender(Component):
    """A DesRender component.
Descriptive stats inputs

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- inputs (dict; optional):
    Inputs."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dv_charts'
    _type = 'DesRender'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, inputs=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'inputs']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'inputs']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DesRender, self).__init__(**args)
