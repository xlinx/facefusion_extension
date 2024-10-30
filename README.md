FaceFusion ext change log
==========

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
method 1. (testing)
```
curl https://github.com/xlinx/facefusion_extension/blob/master/applyExt.patch | git apply -v
```
method 2. (manual)

- please replace follow file path by ur self, and restart FF

```
from
\facefusion_extension\facefusion\uis\components\trim_frame.py
to
\facefusion\facefusion\uis\components\trim_frame.py
```
FaceFusion
==========

> Industry leading face manipulation platform.

[![Build Status](https://img.shields.io/github/actions/workflow/status/facefusion/facefusion/ci.yml.svg?branch=master)](https://github.com/facefusion/facefusion/actions?query=workflow:ci)
[![Coverage Status](https://img.shields.io/coveralls/facefusion/facefusion.svg)](https://coveralls.io/r/facefusion/facefusion)
![License](https://img.shields.io/badge/license-MIT-green)


Preview
-------

![Preview](https://raw.githubusercontent.com/facefusion/facefusion/master/.github/preview.png?sanitize=true)


Installation
------------

Be aware, the [installation](https://docs.facefusion.io/installation) needs technical skills and is not recommended for beginners. In case you are not comfortable using a terminal, our [Windows Installer](https://windows-installer.facefusion.io) and [macOS Installer](https://macos-installer.facefusion.io) get you started.


Usage
-----

Run the command:

```
python facefusion.py [commands] [options]

options:
  -h, --help                                      show this help message and exit
  -v, --version                                   show program's version number and exit

commands:
    run                                           run the program
    headless-run                                  run the program in headless mode
    force-download                                force automate downloads and exit
    job-list                                      list jobs by status
    job-create                                    create a drafted job
    job-submit                                    submit a drafted job to become a queued job
    job-submit-all                                submit all drafted jobs to become a queued jobs
    job-delete                                    delete a drafted, queued, failed or completed job
    job-delete-all                                delete all drafted, queued, failed and completed jobs
    job-add-step                                  add a step to a drafted job
    job-remix-step                                remix a previous step from a drafted job
    job-insert-step                               insert a step to a drafted job
    job-remove-step                               remove a step from a drafted job
    job-run                                       run a queued job
    job-run-all                                   run all queued jobs
    job-retry                                     retry a failed job
    job-retry-all                                 retry all failed jobs
```


Documentation
-------------

Read the [documentation](https://docs.facefusion.io) for a deep dive.
