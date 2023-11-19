import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")
depsgraph_update_post: typing.List[typing.
                                   Callable[['bpy.types.Scene'], None]] = None
''' on depsgraph update (post)
'''

depsgraph_update_pre: typing.List[typing.
                                  Callable[['bpy.types.Scene'], None]] = None
''' on depsgraph update (pre)
'''

frame_change_post: typing.List[typing.
                               Callable[['bpy.types.Scene'], None]] = None
''' on frame change for playback and rendering (after)
'''

frame_change_pre: typing.List[typing.
                              Callable[['bpy.types.Scene'], None]] = None
''' on frame change for playback and rendering (before)
'''

load_factory_preferences_post: typing.List[
    typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading factory preferences (after)
'''

load_factory_startup_post: typing.List[
    typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading factory startup (after)
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

redo_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading a redo step (after)
'''

redo_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading a redo step (before)
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

undo_post: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading an undo step (after)
'''

undo_pre: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on loading an undo step (before)
'''

version_update: typing.List[typing.Callable[['bpy.types.Scene'], None]] = None
''' on ending the versioning code
'''
