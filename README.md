# youtube-pauser

A python script that plays/pauses youtube videos wherever you are.

------------

## Dependencies
`python3` and `pip3` are required.  
`xdotool` for Linux is also used.

```bash
sudo apt-get install xdotool
```

```bash
sudo apt-get install python3-pip
```

------------

## Usage
Just execute `pauser.py` as:

```bash
python3 pauser.py
```

You can bind this script to any key in your OS. Make sure you have proper executable permission as:
```bash
chmod u+x pauser.py
```

### In i3wm you can bind it as:
```bash
bindsym $mod+m exec --no-startup-id path_to_pauser/pauser.py
```

The play/pause works assuming that you have a single video playing in a single window in a separate workspace.

------------

## Configuration
The configuration is loaded from `config.json`.
```json
{
    "desktop_number" : 0,
    "window_name" : "YouTube"
}
```

The **desktop_number** is the desktop number for your window manager. For example, in **i3wm**, 0 means 10.

------


