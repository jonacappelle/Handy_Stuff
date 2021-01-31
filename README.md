![GitHub last commit](https://img.shields.io/github/last-commit/jonacappelle/Handy_Stuff.svg)
![GitHub follow](https://img.shields.io/github/followers/jonacappelle?label=Follow%20Me%21&style=social)
![GitHub star](https://img.shields.io/github/stars/jonacappelle/Handy_Stuff?style=social)

# Handy Stuff

## Embedded Stuff
#### Always disable `Systicks`before going into `EM2`- `EM3`!
#### Pullup resistors can draw a lot of power! --> Set `GPIO Ports` high to prevent this

### I2C on EFM32 when using I2CSPM library
- `( I2C address << 1 )`
- `IIC_WriteReadBuffer( ( I2C_ADDRESS << 1 ), wBuffer, wLength, rBuffer, rLength);`

wBuffer[0] --> I2C register address 

wBuffer[1] --> data to write

- When reading: `wLength = 1`
- When writing 1 byte: `wLength = 2`

### Add math.h to Silplicity studio project
project properties window, then to C/C++ build --> settings --> GNU ARM C linker --> Libraries, then in the Libraries (-l) window, click "Add..>" and type "m" in the window that pops up. This should allow you to add the standard C math library into the project.

### Debug tips & tricks
- No. 1: **`Clean build`** !!!
- enable necessary `clocks`
- include all `em_lib.c` files
- include all `em_lib.h` files
- include `folders` in project
- Sometimes you think it's included, but it's not!



#### Debug jumping around ***FIX***:  
- Debug --> Debug Configurations --> Exceptions --> `Enable All`
- Project properties --> C/C++ Build --> Settings --> Debug Settings --> Debug Level --> `Maximum (-g3)` or `Default (-g)`
- Project properties --> C/C++ Build --> Settings --> Optimization --> `None (-O0)` or `Optimize for debugging (-Og)`

- Problem can be invisible character in code:  
With: `#ifdef x -- #endif` check until where code runs

### Going ultra-low power
 - Disable pins using: `GPIO_PinModeSet(BLE_PORT, BLE_PIN_TX, gpioModeDisabled, 0);`
 - Do NOT use 1 at the end, this sets a pullup resistor and draws about `15 microA` per pin!!
 
 - Disable clocks to all peripherals
 
 - When using RTCDRV timer, you must use RTCDRV_DeInit() otherwise MCU will wake-up every 7-8 minutes.
 
 Correct usage:
 ```
RTCDRV_Init();
RTCDRV_AllocateTimer (&IMU_Idle_Timer );
RTCDRV_StartTimer( IMU_Idle_Timer, rtcdrvTimerTypePeriodic, 2000, (RTCDRV_Callback_t)CheckIMUidle, NULL);
RTCDRV_StopTimer( IMU_Idle_Timer );
RTCDRV_DeInit();
 ```

## PCB Design good practices

- No ground plane under antenna
- Use test-points + jumpers
- Decoupling, decoupling, decoupling!
- 100nF on VDD lines


- ALWAYS follow datasheet recommendations
- Be carefull with ```ground planes next to traces!```, this creates parasitic capacitances which may influence your circuit
- Separate DGND and AGND plane - separate by condensator or high ohm resistor


### Eagle
| Shortcut      | Action           |
| ------------- |-----------------:|
| `CHANGE PACKAGE 'xxx'`       | Change multiple footprints |
| `RATSNEST`       | FIll all planes |
| `RIPUP @;`       | Ripup ground planes after ratsnest |
| `VIA 'GND'`       | Place via connected to GND |




## Doxygen documentation

### Github pages
Add `.nojekyll` file to `/docs/` folder

Github does not recognize `/_filename` files

### Documentation example

[Click Here](https://github.com/jonacappelle/Handy_Stuff/blob/master/doxygen_template.md)

***

## Linux
### Unpack tarball
`tar -czvf xxx.tar.gz xxx`

***

## VS Code
For a full overview of shortcuts, see: [VS Shortcuts](https://github.com/jonacappelle/Handy_Stuff/blob/master/keyboard-shortcuts-windows.pdf)

| Shortcut      | Action           |
| ------------- |-----------------:|
| `ALT+Z`       | Toggle Word Wrap |
| `F1` | Command Window |
| `CTRL+K` `CTRL+O` | Open folder |
| `CTRL+:` | Toggle line comment |
| `CTRL+K+C:` | Comment |
| `CTRL+K+U:` | Uncomment |
| `SHIFT+ALT+F` | Auto format document |

## LaTeX

### LaTeX Template
[Click Here](https://github.com/jonacappelle/Handy_Stuff/blob/master/template_LaTeX.tex)

### Capitals in bibtex
Place `{...}` around capital letters

### Figure full width in IEEE template
use 
```
\begin{figure*}
    \centering
    \includegraphics{}
    \caption{Caption}
    \label{fig:my_label}
\end{figure*}
```


## Maple

maple to latex: `latex( "insert maple formula here" )`

### Formula tools
[Mathpix](https://mathpix.com/) converts pictures / screenshots to LaTeX formulas.

## Quotes
\usepackage[]{textcmds}  
\q{}

## Python

### PYTHON GRAPHS TEMPLATE LATEX
[Click Here](https://github.com/jonacappelle/Handy_Stuff/blob/master/Graphs_template.py)

### Python create virtual invironment
`python -m venv .venv`

### Set execution policy
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

### Activate venv
`.venv\Scripts\activate`

### Install necessary packages
`pip install -r requirements.txt`


## Inkscape
PDF to SVG conversion: `inkscape -l output.svg input.pdf`


***

## PCB Manufacturing
https://www.pcbway.com/  
https://jlcpcb.com/

***

## Windows
| Shortcut | Action |
| -------- | -----: |
| `WIN+E` | File explorer |
| `CTRL+SHIFT+ESC` | Task manager |
| `CTRL+ALT+DEL` | Task manager 2 |


### Chrome
| Shortcut | Action |
| -------- | -----: |
| `CTRL+T` | Open new tab |
| `CTRL+N` | Open new window |
| `CTRL+SHIFT+T`| Open recently closed tab |
| `CTRL+W`| Close tab |

### PowerPoint
#### Progress bar on dia's
- Search `Macro's`
- `Add macro`
- Add [This Code](https://github.com/jonacappelle/Handy_Stuff/blob/master/ppt_progress_bar.md)

### Change all extension in a folder
- Open `CMD` or `Powershell`
- `ren *.LRV *.mp4`

***

## Adobe suite
### Lightroom
- HDR photo's auto stack: `photo` --> `Auto stack by capture time`

| Shortcut | Action |
| -------- | -----: |
| `CTRL+H` | Make HDR |
| `CTRL+SHIFT+H` | HDR based on previous settings |

***
