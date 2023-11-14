from libqtile.config import Screen
from libqtile import bar
from libqtile.widget import Clock
import clocktooltip


# from libqtile.lazy import lazy
from qtile_extras import widget as extrawidgets
# from qtile_extras.resources import wallpapers

decoration_group = {"decorations": [], "marginLeft": 20}


screens = [
    Screen(
        # wallpaper=wallpapers.WALLPAPER_TRIANGLES_ROUNDED,
        # wallpaper_mode="fill",
        top=bar.Bar(
            [
                # extrawidgets.CurrentLayoutIcon(),
                # widget.CurrentLayout(),
                extrawidgets.GroupBox(),
                # widget.Prompt(),
                extrawidgets.Spacer(),
                extrawidgets.Systray(),
                extrawidgets.WiFiIcon(),
                extrawidgets.UPowerWidget(),
                # widget.WindowName(),
                # extrawidgets.BrightnessControl(**decoration_group),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                # extrawidgets.Systray(**decoration_group),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                clocktooltip.ClockTooltip(format="%I:%M %p"),
                extrawidgets.Clock(format=" (%a %d/%m)%I:%M %p "),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    Screen(
        top=bar.Bar(
            [
                extrawidgets.CurrentLayout(**decoration_group),
                extrawidgets.GroupBox(),
                extrawidgets.Spacer(),
                extrawidgets.ALSAWidget(**decoration_group),
                extrawidgets.Battery(
                    format="{percent:1.0%} ({hour:d}:{min:02d})",
                    low_foreground="#ff0000",
                    low_percentage=0.2,
                ),
            ],
            28,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]
