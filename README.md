![GitHub last commit](https://img.shields.io/github/last-commit/jonacappelle/Handy_Stuff.svg)

# Handy Stuff

## Embedded Stuff
#### Always disable `Systicks`before going into `EM2`- `EM3`!
#### Pullup resistors can draw a lot of power! --> Set `GPIO Ports` high to prevent this

## Doxygen documentation

### Github pages
Add `.nojekyll` file to `/docs/` folder

Github does not recognize `/_filename` files

### Documentation example

``` 
/**************************************************************************//**
 * @brief
 *   xxx
 *
 * @details
 *	 xxx
 *
 * @note
 * 	 xxx
 *
 * @warning
 *   xxx
 *
 * @param[in/out] naam
 *   @li 'true' - xxx
 *   @li 'false' - xxx
 *
 *****************************************************************************/
 ```

***

## Linux
### Unpack tarball
`tar -czvf xxx.tar.gz xxx`

***

## VS Code
| Shortcut      | Action           |
| ------------- |-----------------:|
| `ALT+Z`       | Toggle Word Wrap |
| `F1` | Command Window |
| `CTRL+K` `CTRL+O` | Open folder |
| `CTRL+:` | Toggle line comment |

### Python Graphs

```
import matplotlib.pyplot as plt
import numpy as np
import csv

#Clean B&W Graphs
plt.style.use('grayscale')

x=[]
y=[]

with open('input_file.csv', 'r') as csvfile:
    line_count = 0
    plots = csv.reader(csvfile, delimiter=',') #choose your own delimiter
    for row in plots:
        if line_count < 1:  # lijn zonder data
            print('lijn zonder data')
            line_count += 1
        else:
            x.append(float(row[0]))
            y.append(float(row[1]))

# Plot graph
plt.plot(x,y)

# Add legend, to plot more than just the first letter, use ".legend(('xxx',))"
plt.legend(('Test',))

# Type plot
#plt.hist(y,x, histtype='bar')
#plt.stem(x, y, markerfmt=" ", use_line_collection=True)
plt.axis([0,0.00008,-2,10])
plt.title('Switching spanning')

#X&Y labels
plt.xlabel('Tijd [s]')
plt.ylabel('Spanning [V]')

#Saveas, uncomment to save
#plt.savefig('switching_freq.png')

# Show
plt.show()
```

***

## PCB Manufacturing
https://www.pcbway.com/

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
```
' Author : Mirza Elahi
' Date : 07 Jul, 2016
Sub AddProgressBar()
    ' Parameters to set
    progressBarHeight = 3.5 ' height of the progress bar
    FillColor = RGB(251, 0, 6) ' Fill color of the progress bar
    LineColor = FillColor ' Line color of the progress bar
    BackgroundColor = RGB(255, 255, 255) ' background color of the progress bar
    fontColor = FillColor
    startingSlideNo = 1
    noFontSize = 13
    showSlideNo = True ' Set this to False if you dont want to show total slide no
    'Slider Making
    On Error Resume Next
        With ActivePresentation
            sHeight = .PageSetup.SlideHeight - progressBarHeight
            n = 0
            j = 0
            For i = 1 To .Slides.Count
                If .Slides(i).SlideShowTransition.Hidden Then j = j + 1
            Next i: 
            For i = startingSlideNo To .Slides.Count
                .Slides(i).Shapes("progressBar").Delete
                .Slides(i).Shapes("progressBarBackground").Delete
                .Slides(i).Shapes("pageNumber").Delete
                If .Slides(i).SlideShowTransition.Hidden = msoFalse Then
                    ' Background setting
                    ' Underscore used for continuation of line
                    Set sliderBack = .Slides(i).Shapes.AddShape( _
                                        msoShapeRectangle, 0, _
                                        sHeight, (.Slides.Count - j) _
                                        * .PageSetup.SlideWidth _
                                        / (.Slides.Count - j), _
                                        progressBarHeight)
                    With sliderBack
                        .Fill.ForeColor.RGB = BackgroundColor
                        .Line.ForeColor.RGB = BackgroundColor
                        .Name = "progressBarBackground"
                        End With
                    ' Main Slider setting
                    Set slider = .Slides(i).Shapes.AddShape( _
                                        msoShapeRectangle, 0, _
                                        sHeight, (i - n) * _
                                        .PageSetup.SlideWidth _
                                        / (.Slides.Count - j), _
                                        progressBarHeight)
                    With slider
                        ' enable this line to set theme color
                        '.Fill.ForeColor.RGB = ActivePresentation.SlideMaster.ColorScheme.Colors( _
                        ppFill).RGB
                        .Fill.ForeColor.RGB = FillColor
                        .Line.ForeColor.RGB = LineColor
                        .Name = "progressBar"
                    End With
                    Set pageNumber = .Slides(i).Shapes.AddTextbox( _
                                        msoTextOrientationHorizontal, _
                                        ((.Slides.Count - j) * _
                                        .PageSetup.SlideWidth / _
                                        (.Slides.Count - j)) - 50, _
                                        .PageSetup.SlideHeight - 23, 100, 10)
                    ' Slide No
                    If showSlideNo = True Then
                        With pageNumber
                            .TextFrame.TextRange.Text = Str(i - n) & "/" & _
                                    Str(ActivePresentation.Slides.Count - j)
                            With .TextFrame.TextRange.Font
                                .Bold = msoFalse
                                .Size = noFontSize
                                .Color = fontColor
                            End With
                            .Name = "pageNumber"
                        End With
                    End If

                Else
                    n = n + 1
                End If
            Next i:
        End With
End Sub

Sub RemoveProgressBar()
    On Error Resume Next
    With ActivePresentation
        For i = 1 To .Slides.Count
            .Slides(i).Shapes("progressBar").Delete
            .Slides(i).Shapes("progressBarBackground").Delete
            .Slides(i).Shapes("pageNumber").Delete
        Next i:
    End With
End Sub
```


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