# hk-horn
Hollow Knight Mods (Packages) Manager =)

(In current time in Alpha..)

## Installation..
```bash
pip install --upgrade hk_horn
```

## Usage
### Help
```bash
# with `python -m`
python -m horn -h
# or if included in PATH:
horn -h
```
#### output:
```bash
Usage: horn.py [OPTIONS] COMMAND [ARGS]...

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  find
  info
  install
```

### Mods search
```bash
horn find --name HK
```
#### output:
```bash
'HKHKHKHKHK' 1.5.0.0
'HKMP HealthDisplay' 0.0.6.0
'HKMirror' 2.1.0.0
'HKMP' 2.4.1.0
'HKMP Prop Hunt' 0.0.2.1
'HKVR' 0.0.0.0
'HkmpPouch' 1.0.0.0
'SmashKnight' 1.0.0.0
'HKmote' 1.4.0.0
'HKTracker' 3.4.1.1
'HKTool Legacy' 1.11.8.0
'HKTool' 2.2.1.0
'HKTimer' 0.1.1.0
'HKMP.ModDiff' 1.0.2.0
'HKMP Tag' 2.3.1.0
'HKRoomLogger' 1.0.8467.33528
```

### Mod info
```bash
horn info HKMP
```
or
```bash
horn info HKMP --version 2.4.1.0
```
#### output:
```bash
Mod(
    name='HKMP',
    description='Hollow Knight Multiplayer allows people to host games and let others join them in their adventures.',
    version='2.4.1.0',
    link='https://github.com/Extremelyd1/HKMP/releases/download/v2.4.1/HKMP.zip',
    dependencies=None,
    repository='https://github.com/Extremelyd1/HKMP/',
    issues=None,
    tags=None,
    authors=['Extremelyd1']
)
```

### Mods installation (will update in future)
```bash
horn install 'HKMP' --path=/path/to/game/mods/dir/Games/Hollow\ Knight/Hollow\ Knight_Data/Managed/Mods
```
#### output:
```bash
[11/19/23 04:30:25] INFO     Searching package 'HKMP'                                                                                                                                                     api.py:397
                    INFO     Searching field(s) ptrn(s) `{'name': '^HKMP$'}`                                                                                                                              api.py:283
                    INFO     Installing package `'HKMP'==2.4.1.0`                                                                                                                                         api.py:415
[11/19/23 04:30:27] INFO     Downloading `https://github.com/Extremelyd1/HKMP/releases/download/v2.4.1/HKMP.zip` to path `~/.cache/horn/pkg/HKMP.zip`                                           api.py:361
[11/19/23 04:30:28] INFO     Unpacking `~/.cache/horn/pkg/HKMP.zip` to path `~/PortWINE/PortProton/prefixes/DEFAULT/drive_c/Games/Hollow Knight/Hollow Knight_Data/Managed/Mods/HKMP` api.py:379
                    INFO     Installation of package `'HKMP'==2.4.1.0` complete!                                                                                                                          api.py:424
Status:  OK
```
