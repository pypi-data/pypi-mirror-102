
Requirements:
- alacritty
- fzf


Config:
Write a python file (~/.config/pycher/config.py) that defines a dictionary (tag, command) named "commands"

```python
commands = {
    "uh oh": "playerctl -p spotify open spotify:album:3PzrNuMGWGpp8WOfrmpkaU"
}
```


for i3 users, you might want to add this to your `.i3/config`

```
for_window [class="Pycher"] floating enable
for_window [class="Pycher"] resize set width 500
for_window [class="Pycher"] move position center
```
