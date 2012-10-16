# -*- coding: utf-8 -*-
# #START_LICENSE###########################################################
#
#
# This file is part of the Environment for Tree Exploration program
# (ETE).  http://ete.cgenomics.org
#  
# ETE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# ETE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with ETE.  If not, see <http://www.gnu.org/licenses/>.
#
# 
#                     ABOUT THE ETE PACKAGE
#                     =====================
# 
# ETE is distributed under the GPL copyleft license (2008-2011).  
#
# If you make use of ETE in published work, please cite:
#
# Jaime Huerta-Cepas, Joaquin Dopazo and Toni Gabaldon.
# ETE: a python Environment for Tree Exploration. Jaime BMC
# Bioinformatics 2010,:24doi:10.1186/1471-2105-11-24
#
# Note that extra references to the specific methods implemented in 
# the toolkit are available in the documentation. 
# 
# More info at http://ete.cgenomics.org
#
# 
# #END_LICENSE#############################################################
__VERSION__="ete2-2.1rev539" 
import types

from PyQt4 import QtGui, QtSvg
from PyQt4 import QtCore
from qt4_gui import _GUI, _PropertiesDialog, _BasicNodeActions

import layouts
from ete2 import Tree, PhyloTree, ClusterTree
from main import TreeStyle, save
from qt4_render import _TreeScene, render, get_tree_img_map
from templates import _DEFAULT_STYLE, apply_template


__all__ = ["show_tree", "render_tree"]

_QApp = None

def init_scene(t, layout, ts):
    global _QApp

    if not ts:
        ts = TreeStyle()

    if layout and not ts.layout_fn: 
        ts.layout_fn  = layout
    elif not layout and not ts.layout_fn:
        cl = t.__class__
        try:
            ts_template = _DEFAULT_STYLE[cl]
        except KeyError, e:
            pass
        else:
            apply_template(ts, ts_template)

    if not _QApp:
        _QApp = QtGui.QApplication(["ETE"])

    scene  = _TreeScene()
    ts._scale = None
    return scene, ts

def show_tree(t, layout=None, tree_style=None):
    """ Interactively shows a tree."""
    scene, img = init_scene(t, layout, tree_style)
    tree_item, n2i, n2f = render(t, img)
    scene.init_data(t, img, n2i, n2f)

    tree_item.setParentItem(scene.master_item)
    scene.addItem(scene.master_item)
    
    size = tree_item.rect()
    w, h = size.width(), size.height()
    
    svg = QtSvg.QSvgGenerator()
    svg.setFileName("test.svg")
    svg.setSize(QtCore.QSize(w, h))
    svg.setViewBox(size)

    
    pp = QtGui.QPainter()
    pp.begin(svg)
    #pp.setRenderHint(QtGui.QPainter.Antialiasing)
    #pp.setRenderHint(QtGui.QPainter.TextAntialiasing)
    #pp.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
    scene.render(pp, tree_item.rect(), tree_item.rect(), QtCore.Qt.KeepAspectRatio)
    pp.end()

    img = QtSvg.QGraphicsSvgItem("test.svg")
    #img.setParentItem(scene.master_item)
    #scene.removeItem(tree_item)
    #tree_item.setVisible(False)
    
    mainapp = _GUI(scene)
    mainapp.show()
    _QApp.exec_()

def render_tree(t, imgName, w=None, h=None, layout=None, \
                    tree_style = None, header=None, units="px"):
    """ Render tree image into a file."""
    scene, img = init_scene(t, layout, tree_style)
    tree_item, n2i, n2f = render(t, img)

    scene.init_data(t, img, n2i, n2f)
    tree_item.setParentItem(scene.master_item)
    scene.master_item.setPos(0,0)
    scene.addItem(scene.master_item)
    save(scene, imgName, w=w, h=h, units=units)
    imgmap = get_tree_img_map(n2i)

    return imgmap
    


