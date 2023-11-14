from libqtile.config import Key, Group, ScratchPad, Match, DropDown


groups = [Group(i) for i in "123456789"]

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "alacritty",
                "alacritty",
                height=0.65,
                width=0.8,
                x=0.1,
                y=0.1,
                on_focus_lost_hide=True,
                opacity=0.90,
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
                opacity=0.90,
                warp_pointer=False,
            ),
            DropDown(
                "chrome",
                "google-chrome-stable",
                match=Match(wm_class="google-chrome"),
                height=0.75,
                width=0.8,
                x=0.1,
                y=0.1,
                on_focus_lost_hide=True,
                # opacity=0.55,
                warp_pointer=False,
            ),
        ],
    ),
)
