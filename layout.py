from libqtile import layout
from libqtile.lazy import lazy
from libqtile.config import Click, Drag, Match

layouts = [
    layout.Columns(
        border_focus="#6abf8c",
        border_normal="#000000",
        border_width=2,
        # font = "Droid Sans",
        # fontsize = "100",
        margin=10,
    ),
    layout.MonadTall(
        border_focus="#8f8f8f",
        border_normal="#000000",
        border_width=2,
        # font = "Droid Sans",
        # fontsize = "100",
        margin=10,
    ),
    # layout.Max(),
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
