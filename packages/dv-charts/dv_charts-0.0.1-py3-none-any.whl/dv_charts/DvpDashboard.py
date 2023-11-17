# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DvpDashboard(Component):
    """A DvpDashboard component.
A react drag grid components

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- allowOverlap (boolean; optional):
    Allow overlap.

- autoSize (boolean; optional):
    Auto resize.

- breakpoints (dict with strings as keys and values of type number; optional):
    Breakpoint {lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}.

- catVariables (list; optional):
    Categorical variables.

- className (string; optional):
    classname.

- cols (dict with strings as keys and values of type number | number; optional):
    Cols {lg: 12, md: 10, sm: 6, xs: 4, xxs: 2}.

- compactType (a value equal to: 'vertical', 'horizontal'; optional):
    Compact type.

- containerPadding (list of numbers | dict with strings as keys and values of type list of numbers; optional):
    Padding [x, y].

- defaultDisplayData (dict; optional):
    Default Display Data.

- defaultHeightI (number; optional):
    Default i.

- designMode (boolean; optional):
    Whether is a preview mode.

- drawerOpen (boolean; optional):
    Whether the drawer is open.

- headerChildrenPrefix (a list of or a singular dash component, string or number; optional):
    header Children Prefix.

- height (number; optional):
    Height.

- inputsChanged (number; optional):
    Whether inputs changed.

- inputsChangedInfo (dict; optional):
    inputsChanged Info.

- isBounded (boolean; optional):
    Is bounded.

- isDraggable (boolean; optional):
    Draggable.

- isResizable (boolean; optional):
    Resizable.

- key (string; optional):
    Key to identify the component.

- loading_state (dict; optional):
    Loading state.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- margin (list of numbers | dict with strings as keys and values of type list of numbers; optional):
    Margin [x, y].

- numVariables (list; optional):
    Numeric variables.

- placeholderBackground (string; optional):
    Placeholder background.

- placeholderBorder (string; optional):
    Placeholder background border.

- placeholderBorderRadius (string; optional):
    Placeholder border radius.

- placeholderOpacity (number; optional):
    Placeholder background opacity.

- publishMode (boolean; optional):
    Published mode.

- rowHeight (number; optional):
    Row height.

- saveNclicks (number; optional):
    Clicks of save button.

- style (dict; optional):
    CSS style.

- variableEntryType (a value equal to: 'list', 'groupedList'; optional):
    variableEntryType.

- widgetData (dict; optional):
    Widget Data.

- widgets (list; optional):
    List of widgets.

- wrapperStyle (dict; optional):
    Wrapper style."""
    _children_props = ['headerChildrenPrefix']
    _base_nodes = ['headerChildrenPrefix', 'children']
    _namespace = 'dv_charts'
    _type = 'DvpDashboard'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, defaultDisplayData=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, defaultHeightI=Component.UNDEFINED, wrapperStyle=Component.UNDEFINED, placeholderBackground=Component.UNDEFINED, placeholderOpacity=Component.UNDEFINED, placeholderBorder=Component.UNDEFINED, placeholderBorderRadius=Component.UNDEFINED, breakpoints=Component.UNDEFINED, cols=Component.UNDEFINED, catVariables=Component.UNDEFINED, numVariables=Component.UNDEFINED, compactType=Component.UNDEFINED, publishMode=Component.UNDEFINED, designMode=Component.UNDEFINED, height=Component.UNDEFINED, autoSize=Component.UNDEFINED, margin=Component.UNDEFINED, containerPadding=Component.UNDEFINED, drawerOpen=Component.UNDEFINED, headerChildrenPrefix=Component.UNDEFINED, inputsChanged=Component.UNDEFINED, inputsChangedInfo=Component.UNDEFINED, rowHeight=Component.UNDEFINED, saveNclicks=Component.UNDEFINED, isDraggable=Component.UNDEFINED, isResizable=Component.UNDEFINED, variableEntryType=Component.UNDEFINED, isBounded=Component.UNDEFINED, allowOverlap=Component.UNDEFINED, widgets=Component.UNDEFINED, widgetData=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allowOverlap', 'autoSize', 'breakpoints', 'catVariables', 'className', 'cols', 'compactType', 'containerPadding', 'defaultDisplayData', 'defaultHeightI', 'designMode', 'drawerOpen', 'headerChildrenPrefix', 'height', 'inputsChanged', 'inputsChangedInfo', 'isBounded', 'isDraggable', 'isResizable', 'key', 'loading_state', 'margin', 'numVariables', 'placeholderBackground', 'placeholderBorder', 'placeholderBorderRadius', 'placeholderOpacity', 'publishMode', 'rowHeight', 'saveNclicks', 'style', 'variableEntryType', 'widgetData', 'widgets', 'wrapperStyle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allowOverlap', 'autoSize', 'breakpoints', 'catVariables', 'className', 'cols', 'compactType', 'containerPadding', 'defaultDisplayData', 'defaultHeightI', 'designMode', 'drawerOpen', 'headerChildrenPrefix', 'height', 'inputsChanged', 'inputsChangedInfo', 'isBounded', 'isDraggable', 'isResizable', 'key', 'loading_state', 'margin', 'numVariables', 'placeholderBackground', 'placeholderBorder', 'placeholderBorderRadius', 'placeholderOpacity', 'publishMode', 'rowHeight', 'saveNclicks', 'style', 'variableEntryType', 'widgetData', 'widgets', 'wrapperStyle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DvpDashboard, self).__init__(**args)
