import sys
import typing
from . import marker
from . import buttons
from . import script
from . import nla
from . import font
from . import view2d
from . import text
from . import pose
from . import screen
from . import workspace
from . import gpencil
from . import import_scene
from . import gizmogroup
from . import clip
from . import preferences
from . import export_anim
from . import fluid
from . import render
from . import console
from . import palette
from . import sculpt
from . import surface
from . import export_mesh
from . import scene
from . import object
from . import cloth
from . import boid
from . import cachefile
from . import brush
from . import poselib
from . import rigidbody
from . import info
from . import camera
from . import image
from . import node
from . import mask
from . import dpaint
from . import transform
from . import armature
from . import import_anim
from . import action
from . import ptcache
from . import uv
from . import particle
from . import wm
from . import import_curve
from . import ui
from . import import_mesh
from . import safe_areas
from . import collection
from . import sound
from . import material
from . import export_scene
from . import file
from . import ed
from . import world
from . import mball
from . import anim
from . import paintcurve
from . import paint
from . import curve
from . import graph
from . import sequencer
from . import texture
from . import outliner
from . import lattice
from . import constraint
from . import mesh
from . import view3d
from . import cycles

GenericType = typing.TypeVar("GenericType")


class BPyOps:
    pass


class BPyOpsSubMod:
    pass


class BPyOpsSubModOp:
    def get_rna_type(self):
        ''' 

        '''
        pass

    def idname(self):
        ''' 

        '''
        pass

    def idname_py(self):
        ''' 

        '''
        pass

    def poll(self, args):
        ''' 

        '''
        pass
