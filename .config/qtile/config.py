from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from qtile_extras import widget
# from qtile_extras.widget import BorderDecoration
import os, subprocess, colors   

alt = "mod1"
shift = "shift"
control = "control"

@lazy.layout.function
def increase_gaps(layout, steps = 10):
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

    Key([alt, shift], "j", lazy.layout.shuffle_down()),
    Key([alt, shift], "k", lazy.layout.shuffle_up()),
    Key([alt, shift], "h", lazy.layout.shuffle_left()),
    Key([alt, shift], "l", lazy.layout.shuffle_right()),

    Key([alt, control], "j", lazy.layout.grow_down()),
    Key([alt, control], "k", lazy.layout.grow_up()),
    Key([alt, control], "h", lazy.layout.grow_left()),
    Key([alt, control], "l", lazy.layout.grow_right()),

    Key([alt, shift, control], "h", lazy.layout.swap_column_left()),
    Key([alt, shift, control], "l", lazy.layout.swap_column_right()),
    Key([alt, shift], "Return", lazy.layout.toggle_split()),
    Key([alt], "n", lazy.layout.normalize()),

    Key([alt], "equal", increase_gaps()),
    Key([alt], "minus", increase_gaps(step = -10)),

    Key([alt], "Return", lazy.spawn("alacritty")),
    Key([alt], "e", lazy.spawn("nemo")),
    Key([alt], "b", lazy.spawn("librewolf")),
    # Key([alt], "v", lazy.spawn("emacsclient -c -a 'emacs' ")),
    Key([alt], "v", lazy.spawn("alacritty -e nvim")),
    
    Key([], "XF86MonBrightnessUp", lazy.spawn("brillo -A 2")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brillo -U 2")),
    
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 2%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 2%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q -D pulse set Master toggle")),
    
    Key([], "Print", lazy.spawn("scrot /home/victoria/Pictures/Screenshots/Screenshot_%Y-%m-%d_%H-%M-%S.png --select --line mode=edge")),
    Key([alt], "Print", lazy.spawn("scrot /home/victoria/Pictures/Screenshots/Screenshot_%Y-%m-%d_%H-%M-%S.png --border")),

    Key([alt], "q", lazy.window.kill()),
    Key([alt], "f", lazy.window.toggle_fullscreen()),
    Key([alt], "t", lazy.window.toggle_floating()),
    Key([alt], "Tab", lazy.next_layout()),

    Key([alt, control], "r", lazy.reload_config()),
    Key([alt, shift], "q", lazy.spawn("shutdown -h now")),
    Key([alt], "w", lazy.spawn("rofi -show drun")),
    Key([alt, shift], "w", lazy.spawn("rofi -show emoji")),
]

groups = []
group_names  = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# group_labels = ["一", "ニ", "三", "四", "五", "六", "七", "八", "九", "零"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name = group_names[i],
            # layout=group_layouts[i].lower(),
            label = group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            Key([alt], i.name, lazy.group[i.name].toscreen()),
            Key([alt, shift], i.name, lazy.window.togroup(i.name, switch_group = True)),
            Key([alt, control], i.name, lazy.window.togroup(i.name)),
        ]
    )

catppuccin = {
    "flamingo": "#F3CDCD",
    "mauve": "#DDB6F2",
    "pink": "#f5c2e7",
    "maroon": "#e8a2af",
    "red": "#f28fad",
    "peach": "#f8bd96",
    "yellow": "#fae3b0",
    "green": "#abe9b3",
    "teal": "#b4e8e0",
    "blue": "#96cdfb",
    "sky": "#89dceb",
    "white": "#d9e0ee",
    "gray": "#6e6c7e",
    "black": "#1a1826",
    }

layouts = [
    layout.Columns(
        border_focus = catppuccin["pink"],
        border_normal = catppuccin["black"], 
        border_on_single = True, 
        border_width = 1, 
        fair = True,
        margin = 10, 
        wrap_focus_stack = False,
    ),
    layout.Max(),
    # layout.Floating(
    #     border_width = 1,
    #     border_focus = colors[5],
    #     border_normal = colors[0],
    # )
]

widget_defaults = dict(
    font = "JetBrains Mono NF Bold",
    fontsize = 15,
    padding = 0,
    background=catppuccin["black"],
    foreground = catppuccin["white"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper = "~/.config/qtile/wallpapers/wallpaperflare.com_wallpaper2.png",
        wallpaper_mode = "fill",

        top = bar.Bar(
            [
                widget.GroupBox(
                    disable_drag = True,
                    # hide_unused = True,
                    active = catppuccin["pink"],
                    highlight_method = "line",
                    fontsize = 20,
                    font = "JetBrains Mono NF",
                    # highlight_color = [catppuccin["black"], catppuccin["pink"]],
                    inactive = catppuccin["gray"],
                    this_current_screen_border = catppuccin["pink"],
                    this_screen_border = catppuccin["green"],
                ),
                widget.Spacer(length = 10),
                widget.TaskList(
                    background = catppuccin["black"],
                    border = catppuccin["pink"],
                    borderwidth = 0,
                    font = "JetBrains Mono NF",
                    fontsize = 17,
                    # foreground = catppuccin["sky"],
                    highlight_method = "border",
                    icon_size = 27,
                    # markup_focused = catppuccin["red"],
                    rounded = True,
                    title_width_method = "uniform",
                    txt_floating = "🗗 ",
                    txt_maximized = "🗖 ",
                    txt_minimized = "🗕 ",
                    urgent_alert_method = "border",
                    urgent_border = catppuccin["red"],
                ),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                widget.Spacer(length = 10),
                widget.Systray(),
                widget.Spacer(length = 10),
                widget.Clock(
                    format = "🕧%I:%M %p",
                ),
                widget.Spacer(length = 10),
                widget.Volume(
                    fmt = "🔊{}",
                ),
                widget.Spacer(length = 10),
                widget.Battery(
                    charge_char = "🔌",
                    discharge_char = "🔋",
                    unknown_char = "‼️",
                    format = "{char}{percent:1.0%}",
                    full_char = "100%",
                    update_interval = 1,
                ),
                widget.Spacer(length = 10),
                widget.Backlight(
                    fmt = "🔆{}",
                    backlight_name = "intel_backlight",
                    brightness_file = "brightness",
                ),
                widget.Spacer(length = 10),
                widget.ThermalSensor(
                    tag_sensor = "Core 0",
                    fmt = "🔥{}"
                ),
                widget.Spacer(length = 10),
                widget.Clock(
                    format = "📆%d.%m.%Y",
                ),
                widget.Spacer(length = 10),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

### DRAG FLOATING LAYOUTS. ###
mouse = [
    Drag([alt], "Button1", lazy.window.set_position_floating(), start = lazy.window.get_position()),
    Drag([alt], "Button3", lazy.window.set_size_floating(), start = lazy.window.get_size()),
    Click([alt], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules = [
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class = "confirmreset"),  # gitk
        Match(wm_class = "makebranch"),  # gitk
        Match(wm_class = "maketag"),  # gitk
        Match(wm_class = "ssh-askpass"),  # ssh-askpass
        Match(title = "branchdialog"),  # gitk
        Match(title = "pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def autostart():
    subprocess.run("/home/victoria/.config/qtile/autostart.sh")

# XXX: Gasp! We"re lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn"t work correctly. We may as well just lie
# and say that we"re a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java"s whitelist.
wmname = "qtile"
