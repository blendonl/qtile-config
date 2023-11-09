from libqtile import layout
from libqtile.config import Click, Drag, Key, Group, ScratchPad, Match, DropDown
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy
import binds
import screen


mod = "mod4"
terminal = guess_terminal()

binds.setModAndTerminal(mod, terminal)
keys = binds.setKeys()


screens = screen.getScreens()

lazy.spawn("autorandr --change home")


groups = [
    ScratchPad(
        "0",
        [
            DropDown(
                "alacritty",
                "alacritty",
                height=0.65,
                width=0.8,
                x=0.1,
                y=0.1,
                on_focus_lost_hide=True,
                opacity=0.55,
                warp_pointer=False,
            ),
            DropDown(
                "alacritty1",
                "alacritty",
                height=0.65,
                width=0.8,
                x=0.1,
                y=0.1,
                on_focus_lost_hide=True,
                opacity=0.55,
                warp_pointer=False,
            ),
            DropDown(
                "chrome",
                "firefox",
                height=0.75,
                width=0.8,
                x=0.1,
                y=0.1,
                on_focus_lost_hide=True,
                opacity=0.55,
                warp_pointer=False,
            ),
        ],
    ),
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
    # Group(i) for i in "123456789"
]

for i in "123456789":
    keys.extend(
        [
            Key(
                [],
                "F1",
                lazy.group["0"].dropdown_toggle("alacritty"),
            ),
            Key(
                [],
                "F2",
                lazy.group["0"].dropdown_toggle("alacritty1"),
            ),
            Key(
                [],
                "F3",
                lazy.group["0"].dropdown_toggle("chrome"),
            ),
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i,
                lazy.group[i].toscreen(),
                desc="Switch to group {}".format(i),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i,
                lazy.window.togroup(i, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus="#6abf8c",
        border_normal="#000000",
        border_width=1,
        # font = "Droid Sans",
        # fontsize = "100",
        margin=5,
    ),
    layout.MonadTall(
        border_focus="#8f8f8f",
        border_normal="#000000",
        border_width=2,
        # font = "Droid Sans",
        # fontsize = "100",
        margin=10,
    ),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=7,
)
extension_defaults = widget_defaults.copy()


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#6abf8c",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
