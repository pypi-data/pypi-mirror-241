import sys
import typing
from . import poselib
from . import wm
from . import action
from . import export_scene
from . import time
from . import import_anim
from . import info
from . import ptcache
from . import export_anim
from . import view2d
from . import palette
from . import mask
from . import lattice
from . import particle
from . import world
from . import transform
from . import text
from . import paint
from . import cachefile
from . import object
from . import surface
from . import camera
from . import scene
from . import font
from . import rigidbody
from . import texture
from . import export_mesh
from . import armature
from . import nla
from . import sound
from . import console
from . import import_scene
from . import material
from . import buttons
from . import render
from . import fluid
from . import image
from . import lamp
from . import group
from . import import_mesh
from . import anim
from . import outliner
from . import script
from . import uv
from . import file
from . import boid
from . import node
from . import ed
from . import logic
from . import cycles
from . import cloth
from . import screen
from . import clip
from . import pose
from . import ui
from . import curve
from . import gpencil
from . import mball
from . import brush
from . import graph
from . import sculpt
from . import paintcurve
from . import mesh
from . import safe_areas
from . import constraint
from . import dpaint
from . import sequencer
from . import import_curve
from . import marker
from . import view3d
from . import sketch

GenericType = typing.TypeVar("GenericType")


class BPyOps:
    pass


class BPyOpsSubMod:
    pass


class BPyOpsSubModOp:
    def get_instance(self):
        ''' 

        '''
        pass

    def get_rna(self):
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
