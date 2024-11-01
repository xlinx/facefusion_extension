
### FF extension - QuickTrim Button
- QuickTrim Layout
![quickTrim_UI.png](images%2FquickTrim_UI.png)
- QuickTrim Button manual
![quickTrim123456.png](images%2FquickTrim123456.png)

### FF extension - Auto Messaging Realtime (Notify)
- working on...

![AMR_set.png](images%2FAMR_set.png)

### FaceFusion ext change log


- quick trim-button
- change temp folder from c to other place(extracting frames)
  - save ur SSD write-life
  - 30fps x 60sec x 60min x 2mb(1080p) = 108000MB
- quick trim-button v2
- enable listening on 0.0.0.0; share on LAN
- Notify by IM app realtime. Every X frame.
  - ex: https://github.com/xlinx/sd-webui-decadetw-auto-messaging-realtime
- git patch. idea from discord @henryruhs
  - [now ext version]
  - git show bc6626756 > ./applyExt.patch
  - git apply ./my-changes.patch


ext-Installation
------------
step 1. (official-way)
- editing facefusion.ini
- ui_layouts =
  - add facefusion_extension.QuickTrim
  - add facefusion_extension.Auto_Messaging_Realtime
- this repo has multi extension; u can choose by ur self.
```
[uis]
open_browser =
ui_layouts = facefusion_extension.QuickTrim facefusion_extension.Auto_Messaging_Realtime
ui_workflow =
```
step 2. (git clone)
- goto \facefusion\facefusion\uis\layouts
- type
```
git clone https://github.com/xlinx/facefusion_extension.git
```
- or download manualy
  - if u click download from git, then rename folder name
  - facefusion_extension-master -> facefusion_extension

FaceFusion
==========
- https://docs.facefusion.io/
