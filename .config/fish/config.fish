#!/usr/bin/env fish

set -e fish_user_paths
set -g fish_user_paths $HOME/.local/bin $HOME/.cargo/bin $fish_user_paths

set fish_greeting

set -gx VISUAL "foot -e nvim"
set -gx EDITOR "nvim"
set -gx SUDO_EDITOR "nvim"
set -gx TERM "foot"
set -gx TERMINAL "foot"

set -gx GTK_IM_MODULE "fcitx"
set -gx QT_IM_MODULE "fcitx"
set -gx XMODIFIERS "@im=fcitx"

set USB32 "/run/media/victoria/0012-D687/"
set USB16 "/run/media/victoria/3FAC-3165/"

set -g fish_key_bindings fish_vi_key_bindings

set -g fish_color_normal cdd6f4
set -g fish_color_command 89b4fa
set -g fish_color_param f2cdcd
set -g fish_color_keyword f38ba8
set -g fish_color_quote a6e3a1
set -g fish_color_redirection f5c2e7
set -g fish_color_end fab387
set -g fish_color_comment 7f849c
set -g fish_color_error f38ba8
set -g fish_color_gray 6c7086
set -g fish_color_selection --background=313244
set -g fish_color_search_match --background=313244 set fish_color_option a6e3a1
set -g fish_color_operator f5c2e7
set -g fish_color_escape eba0ac
set -g fish_color_autosuggestion 6c7086
set -g fish_color_cancel f38ba8
set -g fish_color_cwd f9e2af
set -g fish_color_user 94e2d5
set -g fish_color_host 89b4fa
set -g fish_color_host_remote a6e3a1
set -g fish_color_status f38ba8
set -g fish_pager_color_progress 6c7086
set -g fish_pager_color_prefix f5c2e7
set -g fish_pager_color_completion cdd6f4
set -g fish_pager_color_description 6c7086

alias gc "cd ~/.config/"
alias gcf "cd ~/.config/fish/"
alias gcn "cd ~/.config/nvim/"
alias gcq "cd ~/.config/qtile/"
alias gd "cd ~/Documents/"
alias grd "cd ~/Repos/dotfiles/"
alias grdlb "cd ~/Repos/dotfiles/.local/bin/"
alias grdc "cd ~/Repos/dotfiles/.config/"
alias gme "cd ~/Music/Eurobeat/"
alias gr "cd ~/Repos/"
alias glb "cd ~/.local/bin/"
alias gml "cd ~/Music/Luzne_Piosenki/"
alias gm "cd ~/Music/"
alias gp "cd ~/Pictures/"
alias gpr "cd ~/Projects/"
alias gprr "cd ~/Projects/Rust/"
alias gv "cd ~/Videos/"
alias .. "cd .."
alias ... "cd ../.."
alias .2 "cd ../.."
alias .3 "cd ../../.."
alias .4 "cd ../../../.."

alias gadd "git add"
alias gadd. "git add ."
alias gbranch "git branch"
alias gchanges "gadda && gcommit \"changes\" && gpush"
alias gclone "git clone"
alias gcommit "git commit -m"
alias gdiff "git diff"
alias glog "git log"
alias gmerge "git merge"
alias gpull "git pull"
alias gpush "git push"
alias grestore "git restore"
alias gstatus "git status"
alias gusual "gadda && gcommit \"usual\" && gpush"
alias gwords "gadda && gcommit \"words\" && gpush"
alias gsmallchanges "gadda && gcommit \"small changes\" && gpush"

abbr v "nvim"
abbr vv "nvim ~/.config/nvim/"
abbr valac "nvim ~/.config/alacritty/alacritty.toml"
abbr vbash "nvim ~/.bashrc"
abbr vkitty "nvim ~/.config/kitty/kitty.conf"
abbr vfoot "nvim ~/.config/foot/foot.ini"
abbr vsway "nvim ~/.config/sway/config"
abbr vqtile "nvim ~/.config/qtile/config.py"
abbr vfish "nvim ~/.config/fish/config.fish"
abbr vlf "nvim ~/.config/lf/lfrc"
abbr vyazi "nvim ~/.config/yazi/"
abbr vrofi "nvim ~/.config/rofi/config.rasi"
abbr vstar "nvim ~/.config/starship.toml"
alias emacs "emacsclient -nc -a emacs"
# fuck u, leather man

alias mirror "sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias mirrora "sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"
alias mirrord "sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
alias mirrors "sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"

alias eb "mpv --no-video --term-osd-bar --shuffle ~/Music/Eurobeat"
alias lp "mpv --no-video --term-osd-bar --shuffle ~/Music/Luzne_Piosenki"
alias msc "mpv --no-video --term-osd-bar --shuffle"

abbr p "paru"
abbr pos "paru && sudo flatpak update"
abbr rns "paru -Rns"
abbr s "paru -S"

alias cbuild "cargo build"
alias ccheck "cargo check"
alias cnew "cargo new"
alias crun "cargo run"

alias ls "eza -al --color=always --group-directories-first"
alias la "eza -a --color=always --group-directories-first"
alias ll "eza -l --color=always --group-directories-first"
alias lt "eza -aT --color=always --group-directories-first"
alias lt. "lt | grep"
alias ls. "ls | grep"

#alias rf "mv -t ~/.local/share/Trash/files/"
abbr rf "rm -rf"
alias cp "cp -ri"
alias ln "ln -i"
alias mv "mv -i"
alias rm "rm -i"
alias mkdir "mkdir -pv"

alias ebthunar "thunar ~/Music/Eurobeat"
alias lpthunar "thunar ~/Music/Luzne_Piosenki"
alias mscthunar "thunar ~/Music"

alias eblf "lf ~/Music/Eurobeat"
alias lplf "lf ~/Music/Luzne_Piosenki"
alias msclf "lf ~/Music"

alias ebyazi "yazi ~/Music/Eurobeat"
alias lpyazi "yazi ~/Music/Luzne_Piosenki"
alias mscyazi "yazi ~/Music"

alias ebya "yazi ~/Music/Eurobeat"
alias lpya "yazi ~/Music/Luzne_Piosenki"
alias mscya "yazi ~/Music"

alias cpu "sudo auto-cpufreq --stats"
alias grep "grep -i --color=always"

alias ytm "yt-dlp -f \"bestaudio/best\" --embed-thumbnail --add-metadata --extract-audio --audio-format best"
alias ytv "yt-dlp -f \"bestvideo[ext=mp3]+bestaudio[ext=m4a]/best[ext=mp4]/best\" --embed-thumbnail --add-metadata --embed-chapters"

abbr efish "exec fish"
abbr ebash "exec bash"
abbr updb "sudo updatedb"
abbr pq "python ~/.config/qtile/config.py"
alias alias. "alias | grep"

#starship init fish | source
