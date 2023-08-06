# Fipibar

Fip radio plugin for Polybar with Spotify and Last FM integration from
Spotibar.

## Installation:

For now, Fip Groove is the only station accessible and there is no Spotify or
Last FM integration. Installation needs the following config in your polybar
config:

```
[module/fipibar-toggle-playback]
type = custom/script
exec = echo "GRUUV:  "
click-left = fipibar --toggle-playback
format-underline = #bb6622
format-padding = 2

[module/fipibar-song-details]
type = custom/script
exec = fipibar --get-currently-playing
exec-if = [ $(ps aux | grep fipibar | grep -v grep | wc -l) -eq 1 ]
format-underline = #bb6622
format-padding = 2
```
