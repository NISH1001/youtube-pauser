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
> For now, it is required that only one tab is playing audio. If there are other tabs where videos are paused, they will be played because
the tool sends `Space` key event to every tab.
------------

## Configuration
The configuration is loaded from `config.json`.
```json
{
    "desktop_number" : 0,
    "window_name" : "YouTube",
    "browser" : "Chromium"
}
```

The **desktop_number** is the desktop number for your window manager. For example, in **i3wm**, 0 means 10.

------

## Working Mechanism
- Fetch all the instances of the browser windows, say **Chromium**
- In each window, send tab switch event using `Ctrl+Tab`
- In each tab, check if title consists of **YouTube**
- If the tile meets the condition, send `Space` key event

------


