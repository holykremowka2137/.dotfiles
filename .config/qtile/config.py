from libqtile import bar, layout, widget, hook, extension, qtile
from libqtile.backend.wayland.inputs import InputConfig
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration
from qtile_extras.widget.groupbox2 import GroupBoxRule, ScreenRule

import subprocess, os

alt = "mod1"
term = "alacritty"

# if qtile.core.name  ==  "x11":
#     term = "alacritty"
# elif qtile.core.name  ==  "wayland":
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
    Key([alt], "space", lazy.group.next_window()),

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
    "type:keyboard": InputConfig(kb_options = "caps:escape_shifted_capslock"),
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
    Group("0", label = "零 ", layout = "monadtall"),
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
    use_widget_background = True,
    radius = 15,
    filled = True,
    group = True,
)

pll = PowerLineDecoration(path = "back_slash")
plr = PowerLineDecoration(path = "forward_slash")

rd = {"decorations": [rd]}
rd_pll = {"decorations": [rd, pll]}
pll = {"decorations": [pll]}
plr = {"decorations": [plr]}
rd_plr = {"decorations": [rd, plr]}

# if qtile.current_layout.name == "max": 
# bar_clr = catppuccin["mantle"]
# if qtile.current_layout.name == "monadtall":
bar_clr = "#00000000"

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
                widget.TextBox(
                    fmt = " 󰌠 ",
                    background = catppuccin["pink"],
                    foreground = catppuccin["base"],
                    fontsize = 30,
                    **pll
                ),
                # widget.Spacer(length = 5, background = catppuccin["pink"], **plr),
                # widget.TextBox(
                #     fmt = " ",
                #     background = catppuccin["pink"],
                #     **plr
                # ),
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
                    **rd
                ),
                widget.TextBox(
                    fmt = "",
                    background = catppuccin["base"],
                    **rd
                ),
                widget.Spacer(length = 460, background = bar_clr),
                widget.Clock(
                    format = " 🗓️%a %d.%m.%Y 🕧%H:%M ",
                    **rd
                ),
                widget.Spacer(background = bar_clr),
                # widget.Systray(**rd),
                widget.StatusNotifier(padding = 6, **rd),
                widget.Spacer(length = 10, background = bar_clr),
                widget.Spacer(length = 10, **rd),
                widget.Volume(
                    fmt = "🔊{}",
                    # **rd_plr
                ),
                widget.Backlight(
                    fmt = "🔆{}",
                    backlight_name = "intel_backlight",
                    brightness_file = "brightness",
                    # **rd_plr
                ),
                widget.ThermalSensor(
                    tag_sensor = "Core 0",
                    fmt = "🔥{}",
                    # **rd_plr
                ),
                widget.Battery(
                    charge_char = "🔌",
                    discharge_char = "🔋",
                    unknown_char = "‼️",
                    format = "{char}{percent:2.0%}",
                    full_char = "🔋",
                    update_interval = 1,
                    show_short_text = False,
                    # **rd_plr
                ),
                widget.CurrentLayout(
                    background = catppuccin["pink"],
                    fmt = "{} ",
                    foreground = catppuccin["base"],
                    # max_chars = 3,
                    **rd
                ),
            ],
            40,
            background = bar_clr,
            border_color = bar_clr,
            border_width = [4, 10, 0, 10],
            # width = [4, 10, 0, 10],
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
        Match(wm_class = "mpv"),  
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
