import bpy

for s in bpy.data.scenes.values():
  print("%r:\n  frames_start: %d\n  frame_end: %d\n  total_frames: %d" % (
        s.name,
        s.frame_start,
        s.frame_end,
        s.frame_end - s.frame_start + 1, # frame_end is included.
    )
)

scene = bpy.context.scene
print(
    "Scene %r frames: %d..%d = %d" % (
        scene.name,
        scene.frame_start,
        scene.frame_end,
        scene.frame_end - scene.frame_start + 1, # frame_end is included.
    )
)

