[[Blender Addons]]


[[#MACHINE3tools]]
[[#Snap measure]]
[[#ND]]
[[#K-Tools]]

---
## MACHINE3tools

- I like to enable `cursor` and `modes` pie menus

| Combo          | Effect     |
| -------------- | ---------- |
| CTRL + ALT + A | Align tool |

---
## Snap measure

| Combo                                          | Effect                             |
| ---------------------------------------------- | ---------------------------------- |
| CTRL + SHIFT + V                               | Enter measure mode                 |
| (In mode) + ALT                                | Change points                      |
| (In mode) + ALT + (Hover over midpoint) + LMB  | Select Line                        |
| (In mode) + ALT + (Hover over any point) + RMB | Delete Line                        |
| (In mode) + ALT + (Hover over any point) + Q   | Snap measure pie menu              |
| CTRL + SHIFT + ALT + V                         | **CUSTOM BINDING** - Open Pie Menu |
### Change Bevel Radius

- Bevel edge as normal
- In Snap measure n-panel, click bevel
- Select a loop of bevelled vertices
- Add the opposite bevelled vertices bottom

---
## ND

| Combo     | Effect                   | Conflicts                                                                                         |
| --------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| SHIFT + 2 | Opens the ND Main menu   |                                                                                                   |
| ALT + S   | Opens the ND Sketch menu | - Reset scale                                                                                     |
| F         | Opens Fast menu          | - F is `focus` in `machine3` tools<br>- F is make face in vertex mode. Now have to press it twice |
| ALT + V   | Opens ND Viewport menu   |                                                                                                   |
### Separate into a new object 

In vanilla the work flow is
- Select what you want to separate -> `SHIFT + D` (duplicate) -> `P` -> selection

ND has another workflow but you must be in object mode
- Sketch menu -> geo-lift
  
 I have it on quick favourites
 
---
## K-Tools

This is the JSON for the toolbar colours

```json
{
    "object_mode_color": [
        0.1411742866039276,
        0.349015474319458,
        0.5804011821746826,
        0.8999999761581421
    ],
    "edit_mode_color": [
        0.7843121886253357,
        0.31764522194862366,
        0.18823552131652832,
        0.8999999761581421
    ],
    "sculpt_mode_color": [
        0.5199999809265137,
        0.25999999046325684,
        0.1599999964237213,
        0.8999999761581421
    ],
    "pose_mode_color": [
        0.4399999976158142,
        0.20000000298023224,
        0.5199999809265137,
        0.8999999761581421
    ],
    "vertex_paint_color": [
        0.15000000596046448,
        0.44999998807907104,
        0.2800000011920929,
        0.8999999761581421
    ],
    "weight_paint_color": [
        0.5400000214576721,
        0.3799999952316284,
        0.07999999821186066,
        0.8999999761581421
    ],
    "texture_paint_color": [
        0.10000000149011612,
        0.44999998807907104,
        0.44999998807907104,
        0.8999999761581421
    ],
    "gpencil_draw_color": [
        0.5799999833106995,
        0.18000000715255737,
        0.3199999928474426,
        0.8999999761581421
    ],
    "animation_play_color": [
        0.07999999821186066,
        0.44999998807907104,
        0.18000000715255737,
        0.8999999761581421
    ],
    "color_timeline_dopesheet": true,
    "color_graph_editor": true,
    "color_nla_editor": true,
    "draw_playback_overlay": true
}
```