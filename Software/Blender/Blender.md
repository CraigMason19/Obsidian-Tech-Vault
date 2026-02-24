#software 

An open source program for 3D modelling & rendering.

Allows scripting via [[Python]]

---

[Blender Launcher](https://victor-ix.github.io/Blender-Launcher-V2/) 
- (Used to download and manage versions)

[[#Useful links]]
- [[#Models]]
- [[#Images & textures]]
- [[#Other]]
- [[#Tutorials]]
	- [[#Shorts]]

[[#Unit Scale]]
[[#Bambu Mini A1]]

[[#Light Linking]]
- [[#Change lighting in the compositor]]

---
## Useful links

### Models

[https://www.turbosquid.com/3d-model/free](https://www.turbosquid.com/3d-model/free)

[https://www.cgtrader.com](https://www.cgtrader.com)

[https://3dsky.org](https://3dsky.org)

[https://dimensiva.com](https://dimensiva.com)

[https://3dmodelhaven.com](https://3dmodelhaven.com)

[https://www.blendswap.com](https://www.blendswap.com)

[https://sketchfab.com](https://sketchfab.com)

### Images & textures

[https://pixabay.com](https://pixabay.com)

[https://www.pngwave.com](https://www.pngwave.com) 

[https://www.textures.com/?secure=](https://www.textures.com/?secure=)

[http://texturelib.com](http://texturelib.com)

[https://www.cgbookcase.com/textures/](https://www.cgbookcase.com/textures/)

[https://texture.ninja](https://texture.ninja)

[https://www.cgbookcase.com/textures](https://www.cgbookcase.com/textures)

### Other

[http://pinterest.com/](http://pinterest.com/)

[https://www.artstation.com](https://www.artstation.com)

[https://coolors.co/palettes](https://coolors.co/palettes)

### Tutorials

#### Shorts
- [SouthernShotty - Colored light falloff](https://www.youtube.com/watch?v=qc5KlGvOlVY&list=WL&index=70&pp=iAQBsAgC)


---
# Unit Scale

## Setting up the metric units

There are 3 types of unit measurements in Blender

- "None" represents simple 'unit' based measurement.
- "Metric" represents "millimetres", "meters" etc.
- "Imperial" represents "inches", "foot", "mile" etc.

Metric units are the default standard of measurement in 3D printing. So switching to “Metric” units in “Properties Window > Scene > Units > Length” sets the base unit to "1 Meter" and "Scale: 1.000" this means;
  
- 0.001 = 1mm (one millimeter)
- 0.010 = 1cm (one centimetre)
- 0.100 = 1dm (one decimetre/ten centimetres)
- 1.000 = 1m (one metre)
- 1000.000 = 1km (one kilometre)

---
## Bambu Mini A1

- Scene properties
	- Set units to metric
	- Set scale as 1
	- Set length to meters

Now in blender every meter will be a a mm on the plate. 
E.g. In blender a cube of 10 x 10 x 10 will be a 1cm cube. 

**NOTE:** By default, not doing anything blender 1 unit is 1mm

---



## Scanning and then printing images 1:1

# Editing Video

## General

  

Load in the video file ( .ts, for example) and make sure the screen size and FPS match the video’s information.

  

In the screen with the audio and video tracks press Right Arrow to seek frame by frame and press K to cut them

  

Page up and Page down to cycle between cuts and markers

  

H / (Alt + H) to mute / unmute tracks

  

Importing files imports at the current location of the playhead. So make sure playhead is at the begging to start on frame 0

## Playhead

  

In the playback context menu, click on the Follow playhead checkbox to allow the playhead to 

play anywhere as long as the playhead is within the frame region

## Display Waveform

  

Select the audio track, in the right panel Adjust -> Sound -> Display waveform checkbox

  

## Using custom FPS 

If you have a FPS not in the selected list (29.97, for example) you can set a custom FPS and change the base so it becomes a whole number.

  

E.g. 29.97 becomes 2997, the base 1 becomes 100. 

2997 / 100 = 29.97

## Exporting  .TS files

Export in .AVI format in H.264 mode and encode with .MP3 codec

  

# Texturing & UV’s

select all in uv editor pack Islands -> little box at the bottom will show pack islands -> It adjusts the margin between islands

default 0.0001

## Texture Islands

If you turn off the UV sync selection you can select a texture island and move it as needed.

  

To control the margins between islands, when unwrapping you can change the margin box (default 0.001, 0.03 is a good value).

## Baking normal maps

- Create a plane that will hold the texture (make sure it has uv’s).
    
- Create a new image texture that will be our normal map (no need for alpha).
    
- Create a new material for the plane and add an image texture but don’t connect it. Set it to the texture we previously created.
    
- Move the object(s) to bake just above the plane.
    
- Make sure the plane has been selected last!!
    
- Switch to cycles
    
- In the bake settings -> Switch the bake type to Normal, make sure selected to active is checked, under the expanded arrow set the ray distance to 1m.
    

  

BAKE!

  

Remember to save the image!!!

  



## Dynamic Topology

The default setting is RELATIVE, CONSTANT is good as it stays the same even over different zoom levels

# Materials

## Fake user

If you give a  material to a fake user it will be kept, so it is not flushed (deleted) when you exit blender.



# Texture painting

Press F to adjust the brush size, watch out for the strength value.

## Texture display

Create a new brush in the texture menu, then back in texture painting workspace load in the texture and set the mapping to Stencil. Click on Image Aspect to preserve the aspect. 

  

Under the display dropdown set the texture alpha to about 25%. The button on the right of the texture alpha will make the texture disappear when painting. 

  

Movement

Move - Hold RMB

Scale - Shift + hold RMB

Rotate = CTRL + RMB




# Things I keep forgetting

## Proportional Editing

When you are moving something in this mode press “G” to move it and scroll up and down on the mouse wheel. This will increase/decrease the white circle which will show which other things are effected 

## Move Camera to Viewport position

CTRL + ALT + Num0

## Empty Objects and cleaning the Outliner

Place all items you want as an ‘object’ by creating an empty object and dragging the objects into it in the Outliner. If you want to duplicate or delete the object, right click on the object in the outliner -> select Hierarchy. Then proceed as normal. 

Note: Not needed in 2.8+

## Render Slots

In the rendering tab you can change which slot you render to (Slot 1 -> 8). If you press 'J' in you can cycle between your last two render slots to compare them quickly



## Mirror modifier

To make changes to on a symmetrical object you can use the mirror modifier to work on one side only. Create an object of the size you want and centre it at the origin, create a loop cut (CTRL + R) and delete the opposite vertices. Then add the mirror modifier to make changes on both sides simultaneously.

  

To create the full model you can click apply , however, make sure to create a backup if you need to make changes again 

## Orthographic Camera

In the camera properties panel, set the camera type to orthographic and set the camera rotation to…

 X: 54.736 Y: 0 Z: 45

## Vertex slide

press “GG” and you can slide a vertex along connected edges

## Resetting transforms quickly

ALT + G (translation) ALT + R (rotation) ALT + S (scale)

## Hiding objects

With a current selection press H to hide, SHIFT + H to hide everything else and ALT + H to bring everything back

## Cleaning up the node editor

Select multiple nodes and Join (CTRL + J) to add a frame around the nodes. Press F2 to rename (as in windows) and can add a text file to the frame offering explanations (Scripting editor window to create &  write scripts)

## Zooming to objects

Full stop key on the number pad

## Render Region

In Cycles (NOT Eevee) use CTRL + B to create a box region. This saves on rendering time in cycles as it only renders a small region. CTRL + ALT + B to undo the region.

  

There are crop and render region options in the render setting tab

## Loop cut bevel

Use the bevel short with loop cuts to create uniform thick faces

## Align vertices

Enable the loop tools add-on. Select all the vertices and on the right hand panel (N) select edit->loop tools->space

## Make local

If you link an object into your scene you will not be able to modify it. If you wish you can append the model or you can make a local copy. If you wish to do this go to Object -> Relations -> Make Local -> data and materials

## Installing new and old versions

Download the newest version you want and install it to E:/Blender and make sure to import the previous versions settings. 

  

If you want to use a different version you can download it as a zip, extract it and run the .exe. To install an old version go to [https://download.blender.org/release/](https://download.blender.org/release/)

  

## Cinematic Camera Renders

When deciding on a few shots to use your camera for, add a keyframe to each camera position. This helps speed up camera placement and is great when rendering one frame only

## Viewport to 4 views

To separate the viewport into 4 views (3 orthographic perspectives, 1 perspective perspective). ALT + CTRL + Q

  
**




## Light Linking

Create light groups in `View Layer > Light Groups` (this should be done first)

For a light go to `Object Properties > Shading > Light Group

### Change lighting in the compositor

- Set each light you want to split into its own light group
- These layers will then show in the render passes which can be changed via nodes in the compositor


 