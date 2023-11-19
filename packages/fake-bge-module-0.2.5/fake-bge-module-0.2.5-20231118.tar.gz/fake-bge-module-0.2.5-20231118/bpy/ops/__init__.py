import sys
import typing
from . import poselib
from . import brush
from . import paint
from . import clip
from . import outliner
from . import texture
from . import view2d
from . import view3d
from . import action
from . import info
from . import sound
from . import screen
from . import particle
from . import ptcache
from . import sculpt
from . import constraint
from . import import_curve
from . import import_scene
from . import transform
from . import mask
from . import mesh
from . import text
from . import group
from . import safe_areas
from . import world
from . import script
from . import lattice
from . import scene
from . import cycles
from . import file
from . import sequencer
from . import dpaint
from . import buttons
from . import logic
from . import nla
from . import surface
from . import graph
from . import import_anim
from . import export_anim
from . import gpencil
from . import lamp
from . import pose
from . import wm
from . import ui
from . import font
from . import fluid
from . import node
from . import armature
from . import mball
from . import import_mesh
from . import material
from . import palette
from . import camera
from . import curve
from . import export_mesh
from . import paintcurve
from . import marker
from . import console
from . import rigidbody
from . import export_scene
from . import ed
from . import cloth
from . import boid
from . import object
from . import render
from . import uv
from . import sketch
from . import image
from . import cachefile
from . import time
from . import anim

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
