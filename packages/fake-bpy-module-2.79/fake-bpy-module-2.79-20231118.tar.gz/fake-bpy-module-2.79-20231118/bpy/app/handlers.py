import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")
frame_change_post: typing.List[typing.
                               Callable[['bpy.types.Scene'], None]] = None
''' on frame change for playback and rendering (after)
'''

frame_change_pre: typing.List[typing.
                              Callable[['bpy.types.Scene'], None]] = None
''' on frame change for playback and rendering (before)
'''

game_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on ending the game engine
'''

game_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on starting the game engine
'''

load_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading a new blend file (after)
'''

load_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading a new blend file (before)
'''

persistent = None
''' Function decorator for callback functions not to be removed when loading new files
'''

render_cancel: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on canceling a render job
'''

render_complete: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on completion of render job
'''

render_init: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on initialization of a render job
'''

render_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on render (after)
'''

render_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on render (before)
'''

render_stats: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on printing render statistics
'''

render_write: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on writing a render frame (directly after the frame is written)
'''

save_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on saving a blend file (after)
'''

save_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on saving a blend file (before)
'''

scene_update_post: typing.List[typing.
                               Callable[['bpy.types.Scene'], None]] = None
''' on every scene data update. Does not imply that anything changed in the scene, just that the dependency graph was reevaluated, and the scene was possibly updated by Blender's animation system.
'''

scene_update_pre: typing.List[typing.
                              Callable[['bpy.types.Scene'], None]] = None
''' on every scene data update. Does not imply that anything changed in the scene, just that the dependency graph is about to be reevaluated, and the scene is about to be updated by Blender's animation system.
'''

version_update: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on ending the versioning code
'''
