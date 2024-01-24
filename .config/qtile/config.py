from libqtile import bar, layout, widget, hook, extension, qtile
from libqtile.backend.wayland.inputs import InputConfig
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration
from qtile_extras.widget.groupbox2 import GroupBoxRule, ScreenRule

import subprocess, os

alt = "mod1"
term = "foot"

# if qtile.core.name == "x11":
#     term = "alacritty"
# elif qtile.core.name == "wayland":
#     term = "foot"

@lazy.layout.function
def increase_gaps(layout, step = 10):
    if not hasattr(layout, "margin"):
        return
    
    if not isinstance(layout.margin, int):
        return

    layout.margin = max(layout.margin + step, 0)
    layout.group.layout_all()

keys = [
    Key([alt], "j", lazy.layout.down()),
    Key([alt], "k", lazy.layout.up()),
    Key([alt], "h", lazy.layout.left()),
    Key([alt], "l", lazy.layout.right()),

    Key([alt, "shift"], "h",
        lazy.layout.shuffle_left().when(layout = ["columns", "monadtall"]),
    ),
    Key([alt, "shift"], "l",
        lazy.layout.shuffle_right().when(layout = ["columns", "monadtall"]),
    ),
    Key([alt, "shift"], "j",
        lazy.layout.shuffle_down().when(layout = ["columns", "monadtall"]),
    ),
    Key([alt, "shift"], "k",
        lazy.layout.shuffle_up().when(layout = ["columns", "monadtall"]),
    ),

    Key([alt, "control"], "j", lazy.layout.grow_down()),
    Key([alt, "control"], "k", lazy.layout.grow_up()),
    Key([alt, "control"], "h", lazy.layout.grow_left()),
    Key([alt, "control"], "l", lazy.layout.grow_right()),

    Key([alt, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([alt, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([alt], "Return", lazy.layout.toggle_split()),
    Key([alt], "n", lazy.layout.normalize()),

    Key([alt], "i", lazy.layout.grow()),
    Key([alt], "m", lazy.layout.shrink()),
    Key([alt], "n", lazy.layout.normalize()),
    Key([alt], "r", lazy.layout.reset()),
    Key([alt], "o", lazy.layout.maximize()),
    Key([alt, "shift"], "space", lazy.layout.flip()),

    Key([alt], "equal", increase_gaps()),
    Key([alt], "minus", increase_gaps(step = -10)),

    Key([alt], "Return", lazy.spawn(term)),
    Key([alt], "e", lazy.spawn("thunar")),
    Key([alt], "b", lazy.spawn("librewolf")),
    # Key([alt], "v", lazy.spawn("emacsclient -c -a 'emacs' ")),
    Key([alt], "v", lazy.spawn("alacritty -e nvim")),
    Key([alt], "d", lazy.spawn("discord")),
    
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 2%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 2%-")),
    
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 2%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 2%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q -D pulse set Master toggle")),
    
    Key([alt], "Print", lazy.spawn("flameshot full")),
    Key([], "Print", lazy.spawn("grim -g '$(slurp)' - | convert - -shave 1x1 PNG:- | wl-copy")),

    Key([alt], "q", lazy.window.kill()),
    Key([alt], "f", lazy.window.toggle_fullscreen()),
    Key([alt], "t", lazy.window.toggle_floating()),
    Key([alt], "Tab", lazy.next_layout()),

    Key([alt, "control"], "r", lazy.reload_config()),
    Key([alt, "control"], "Delete", lazy.spawn("shutdown -h now")),
    Key([alt], "w", lazy.spawn("rofi -show drun")),
    Key([alt, "shift"], "w", lazy.spawn("rofi -show emoji")),

    Key([alt, "control"], "F1", lazy.core.change_vt(1)),
    Key([alt, "control"], "F2", lazy.core.change_vt(2)),
    Key([alt, "control"], "F3", lazy.core.change_vt(3)),
    Key([alt, "control"], "F4", lazy.core.change_vt(4)),
    Key([alt, "control"], "F5", lazy.core.change_vt(5)),
    Key([alt, "control"], "F6", lazy.core.change_vt(6)),
    Key([alt, "control"], "F7", lazy.core.change_vt(7)),
]

wl_input_rules = {
    "type:keyboard": InputConfig(kb_options="caps:escape_shifted_capslock"),
}

groups = [
    Group("1", label = "一", layout = "monadtall"),
    Group("2", label = "ニ", layout = "max", matches = [Match(wm_class = "LibreWolf")]),
    Group("3", label = "三", layout = "monadtall"),
    Group("4", label = "四", layout = "monadtall"),
    Group("5", label = "五", layout = "max", matches = [Match(wm_class = "discord")]),
    Group("6", label = "六", layout = "monadtall"),
    Group("7", label = "七", layout = "monadtall"),
    Group("8", label = "八", layout = "monadtall"),
    Group("9", label = "九", layout = "monadtall"),
    Group("0", label = "零", layout = "monadtall"),
]

# groups = [
#     Group("1", label = "一", layout = "columns"),
#     Group("2", label = "ニ", layout = "max", matches = [Match(wm_class = "LibreWolf")]),
#     Group("3", label = "三", layout = "columns"),
#     Group("4", label = "四", layout = "columns"),
#     Group("5", label = "五", layout = "max", matches = [Match(wm_class = "discord")]),
#     Group("6", label = "六", layout = "columns"),
#     Group("7", label = "七", layout = "columns"),
#     Group("8", label = "八", layout = "columns"),
#     Group("9", label = "九", layout = "columns"),
#     Group("0", label = "零", layout = "columns"),
# ]

for i in groups:
    keys.extend(
        [
            Key([alt], i.name, lazy.group[i.name].toscreen()),
            Key([alt, "shift"], i.name, lazy.window.togroup(i.name, switch_group = True)),
            Key([alt, "control"], i.name, lazy.window.togroup(i.name)),
        ]
    )

catppuccin = {
    "rosewater": "#f5e0dc",
    "flamingo": "#f2cdcd",
    "pink": "#f5c2e7",
    "mauve": "#cba6f7",
    "red": "#f38ba8",
    "maroon": "#eba0ac",
    "peach": "#fab387",
    "yellow": "#f9e2af",
    "green": "#a6e3a1",
    "teal": "#94e2d5",
    "sky": "#89dceb",
    "sapphire": "#74c7ec",
    "blue": "#89b4fa",
    "lavender": "#b4befe",
    "text": "#cdd6f4",
    "subtext1": "#bac2de",
    "subtext0": "#a6adc8",
    "overlay2": "#9399b2",
    "overlay1": "#7f849c",
    "overlay0": "#6c7086",
    "surface2": "#585b70",
    "surface1": "#45475a",
    "surface0": "#313244",
    "base": "#1e1e2e",
    "mantle": "#181825",
    "crust": "#11111b",
}

layouts = [
    layout.Columns(
        border_focus = catppuccin["pink"],
        border_normal = catppuccin["base"], 
        border_on_single = True, 
        border_width = 2, 
        fair = True,
        margin = 10,
        wrap_focus_stack = False,
    ),
    layout.MonadTall(
        border_focus = catppuccin["pink"],
        border_normal = catppuccin["base"], 
        border_on_single = True, 
        border_width = 2, 
        margin = 10,
        wrap_focus_stack = False,
    ),
    layout.Max(),
]

rd = RectDecoration(
    use_widget_background=True,
    radius=16,
    filled=True,
    group=True,
    clip=True
)

pl = PowerLineDecoration(path="forward_slash")

rd_pl = {"decorations": [rd, pl]}
rd_no_pl = {"decorations": [rd]}

widget_defaults = dict(
    background = catppuccin["base"],
    font = "JetBrains Mono Medium",
    fontsize = 15,
    foreground = catppuccin["text"],
    padding = 0,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper = "/home/victoria/.config/qtile/wallpapers/albedo-wallpaper3.png",
        wallpaper_mode = "fill",
        top = bar.Bar(
            [
                widget.Spacer(
                    length = 10,
                    background = "#00000000", 
                ),    
                widget.Spacer(length = 10, **rd_no_pl),
                widget.GroupBox2(
                    disable_drag = True,
                    font = "Noto Sans Mono CJK JP",
                    fontsize = 22,
                    hide_unused = False,
                    padding_x = 3,
                    rules = [
                        GroupBoxRule(block_colour = catppuccin["overlay0"]).when(screen = ScreenRule.THIS, occupied = True),
                        GroupBoxRule(block_colour = catppuccin["overlay0"], text_colour = catppuccin["text"]).when(screen = ScreenRule.THIS, occupied = False),
                        GroupBoxRule(block_colour = catppuccin["green"]).when(screen = ScreenRule.OTHER),
                        GroupBoxRule(text_colour = catppuccin["pink"]).when(occupied = True),
                        GroupBoxRule(text_colour = catppuccin["overlay0"]).when(occupied = False),
                    ],
                    **rd_no_pl
                ),
                widget.Spacer(length = 10, **rd_no_pl),
                widget.Spacer(length = 10, background = "#00000000"),
                widget.TaskList(
                    border = catppuccin["pink"],
                    borderwidth = 0,
                    font = "JetBrains Mono Bold",
                    fontsize = 18,
                    foreground = catppuccin["text"],
                    highlight_method = "border",
                    icon_size = 27,
                    # markup_focused = '<span catppuccin["pink"]>{}</span>',
                    rounded = True,
                    title_width_method = "uniform",
                    txt_floating = "🗗 ",
                    txt_maximized = "🗖 ",
                    txt_minimized = "🗕 ",
                    urgent_alert_method = "border",
                    urgent_border = catppuccin["red"],
                    **rd_no_pl
                ),
                # widget.Chord(
                #     chords_colors = {
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform = lambda name: name.upper(),
                # ),
                widget.Spacer(length = 10, background = "#00000000"),
                widget.Spacer(length = 10, **rd_no_pl),
                # widget.Systray(),
                widget.StatusNotifier(
                    **rd_pl
                ),
                widget.CurrentLayoutIcon(
                    **rd_pl
                ),
                widget.Clock(
                    format = "🕧%I:%M %p",
                    **rd_pl
                ),
                widget.Volume(
                    fmt = "🔊{}",
                    **rd_pl
                ),
                widget.Battery(
                    charge_char = "🔌",
                    discharge_char = "🔋",
                    unknown_char = "‼️",
                    format = "{char}{percent:1.0%}",
                    full_char = "100%",
                    update_interval = 1,
                    **rd_pl
                ),
                widget.Backlight(
                    fmt = "🔆{}",
                    backlight_name = "intel_backlight",
                    brightness_file = "brightness",
                    **rd_pl
                ),
                widget.ThermalSensor(
                    tag_sensor = "Core 0",
                    fmt = "🔥{}",
                    **rd_pl
                ),
                widget.Clock(
                    format = "📆%Y.%m.%d",
                    **rd_pl
                ),
                widget.Spacer(length = 10, **rd_no_pl),
                widget.Spacer(
                    length = 10,
                    background = "#00000000", 
                ),    
            ],
            40,
            background = "00000000",
            width = [4, 4, 4, 4],
            # margin = 4
            # border_width = [4, 4, 4, 4],
            # border_color = [
            #     catppuccin["pink"],
            #     catppuccin["pink"],
            #     catppuccin["pink"],
            #     catppuccin["pink"]
            # ]
        ),
        # x11_drag_polling_rate = 60,
    ),
]

mouse = [
    Drag([alt], "Button1", lazy.window.set_position(),
         start = lazy.window.get_position(),
    ),
    Drag([alt], "Button3", lazy.window.set_size_floating(),
         start = lazy.window.get_size(),
    ),
    Click([alt], "Button1", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus = catppuccin["pink"],
    border_normal = catppuccin["base"], 
    border_width = 2,
    float_rules = [
        *layout.Floating.default_float_rules,
        Match(wm_class = "confirmreset"),  
        Match(wm_class = "makebranch"),  
        Match(wm_class = "maketag"),  
        Match(wm_class = "ssh-askpass"),  
        Match(title = "branchdialog"),  
        Match(title = "pinentry"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

@hook.subscribe.startup_once
def autostart():
    subprocess.run("/home/victoria/.config/qtile/autostart.sh")

wmname = "Qtile"
