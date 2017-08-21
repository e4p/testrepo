

# Working with fluidsim

## Evaluate the file

Quickly we can check what frames are ready to be rendered using
the framestats blender script that will quickly output some of
the metadata stored in the scene context.

```
$ docker run -v="$(pwd):/media" -w="/media" \
        eparker05/blender:2.78c-noentrypoint \
        blender -b -noaudio bmw27_cpu.blend -P framestats.py

Scene 'Scene' frames: 1..1000 = 1000
```

With bmw27_cpu.blend we see that there are 260 frames ready to
be rendered, from 741 to 1000 (inclusive).

### Rendering one frame locally

docker run -v="$(pwd):/media" -w="/media" \
    eparker05/blender:2.78c-noentrypoint \
    blender \
        -y -b -noaudio \
        bmw27_cpu.blend \
        -F PNG \
        -o ./out/bmw_#### -f 373
