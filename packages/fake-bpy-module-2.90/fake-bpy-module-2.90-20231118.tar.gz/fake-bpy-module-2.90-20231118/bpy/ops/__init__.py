import sys
import typing
from . import nla
from . import cloth
from . import ui
from . import mask
from . import simulation
from . import file
from . import pose
from . import dpaint
from . import import_mesh
from . import boid
from . import lattice
from . import import_curve
from . import node
from . import particle
from . import poselib
from . import constraint
from . import armature
from . import material
from . import workspace
from . import anim
from . import wm
from . import sculpt
from . import text
from . import gizmogroup
from . import screen
from . import preferences
from . import fluid
from . import curve
from . import ptcache
from . import texture
from . import scene
from . import camera
from . import cachefile
from . import collection
from . import script
from . import image
from . import info
from . import clip
from . import marker
from . import object
from . import import_scene
from . import paintcurve
from . import export_scene
from . import uv
from . import render
from . import world
from . import brush
from . import action
from . import gpencil
from . import mesh
from . import console
from . import paint
from . import outliner
from . import safe_areas
from . import sequencer
from . import palette
from . import ed
from . import cycles
from . import rigidbody
from . import view2d
from . import view3d
from . import font
from . import buttons
from . import sound
from . import export_anim
from . import graph
from . import mball
from . import transform
from . import surface
from . import export_mesh
from . import import_anim

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
