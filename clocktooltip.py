from libqtile.widget import Clock
from qtile_extras.widget.mixins import TooltipMixin


class ClockTooltip(Clock, TooltipMixin):
    def __init__(self, *args, **kwargs):
        Clock.__init__(self, *args, **kwargs)
        TooltipMixin.__init__(self, **kwargs)
        self.add_defaults(TooltipMixin.defaults)

        # The tooltip text is set in the following variable
        self.tooltip_text = Clock


# Add an instance of TooltipTextBox to your bar
# e.g. TooltipTextBox("This space available for rent.")
