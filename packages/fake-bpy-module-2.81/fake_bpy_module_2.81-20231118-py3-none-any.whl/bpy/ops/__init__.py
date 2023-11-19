import sys
import typing
from . import camera
from . import material
from . import preferences
from . import import_curve
from . import fluid
from . import boid
from . import export_scene
from . import export_mesh
from . import export_anim
from . import node
from . import rigidbody
from . import anim
from . import mesh
from . import info
from . import world
from . import nla
from . import mball
from . import wm
from . import surface
from . import graph
from . import object
from . import palette
from . import font
from . import import_mesh
from . import text
from . import console
from . import marker
from . import sculpt
from . import sound
from . import ptcache
from . import workspace
from . import constraint
from . import view3d
from . import clip
from . import paint
from . import scene
from . import armature
from . import brush
from . import import_anim
from . import file
from . import image
from . import curve
from . import outliner
from . import ui
from . import sequencer
from . import view2d
from . import transform
from . import gpencil
from . import cachefile
from . import texture
from . import lattice
from . import script
from . import mask
from . import ed
from . import screen
from . import safe_areas
from . import gizmogroup
from . import buttons
from . import action
from . import particle
from . import render
from . import pose
from . import dpaint
from . import paintcurve
from . import import_scene
from . import cloth
from . import poselib
from . import collection
from . import uv
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
