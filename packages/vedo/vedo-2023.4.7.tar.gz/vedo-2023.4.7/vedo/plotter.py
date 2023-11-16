#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import sys
import time
from typing import Callable
import numpy as np

try:
    import vedo.vtkclasses as vtk
except ImportError:
    import vtkmodules.all as vtk

import vedo
from vedo import settings
from vedo import utils
from vedo import backends
from vedo import addons


__docformat__ = "google"

__doc__ = """
This module defines the main class Plotter to manage actors and 3D rendering.

![](https://vedo.embl.es/images/basic/multirenderers.png)
"""

__all__ = ["Plotter", "show", "close"]

########################################################################################
class Event:
    """
    This class holds the info from an event in the window, works as dictionary too
    """
    __slots__ = [
        "name",
        "title",
        "id",
        "timerid",
        "time",
        "priority",
        "at",
        "actor",
        "picked3d",
        "keyPressed",  # obsolete, will disappear. Use "keypress"
        "keypress",
        "picked2d",
        "delta2d",
        "angle2d",
        "speed2d",
        "delta3d",
        "speed3d",
        "isPoints",
        "isMesh",
        "isAssembly",
        "isVolume",
        "isPicture",
        "isActor2D",
    ]

    def __init__(self):
        return

    def __getitem__(self, key):
        """Make the class work like a dictionary too"""
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Make the class work like a dictionary too"""
        setattr(self, key, value)

    def __repr__(self):
        f = "---------- <vedo.plotter.Event object> ----------\n"
        for n in self.__slots__:
            try:
                if n == "actor" and self.actor and self.actor.name:
                        f += f"event.{n} = {self.actor.name} ({self.actor.npoints} points)\n"
                else:
                    f += f"event.{n} = " + str(self[n]).replace("\n", "")[:60] + "\n"
            except AttributeError:
                pass
                
        return f

    def keys(self):
        return self.__slots__


##############################################################################################
def show(
    *actors,
    at=None,
    shape=(1, 1),
    N=None,
    pos=(0, 0),
    size="auto",
    screensize="auto",
    title="vedo",
    bg="white",
    bg2=None,
    axes=None,
    interactive=None,
    offscreen=False,
    sharecam=True,
    resetcam=True,
    zoom=None,
    viewup="",
    azimuth=0.0,
    elevation=0.0,
    roll=0.0,
    camera=None,
    mode=0,
    new=False,
):
    """
    Create on the fly an instance of class Plotter and show the object(s) provided.

    Allowed input objects types are:
        ``str, Mesh, Volume, Picture, Assembly
        vtkPolyData, vtkActor, vtkActor2D, vtkImageActor,
        vtkAssembly or vtkVolume``

    Arguments:
        at : (int)
            number of the renderer to plot to, in case of more than one exists
        shape : (list, str)
            Number of sub-render windows inside of the main window. E.g.:
            specify two across with shape=(2,1) and a two by two grid
            with shape=(2, 2).  By default there is only one renderer.

            Can also accept a shape as string descriptor. E.g.:
            - shape="3|1" means 3 plots on the left and 1 on the right,
            - shape="4/2" means 4 plots on top of 2 at bottom.

        axes : (int)
            set the type of axes to be shown:
            - 0,  no axes
            - 1,  draw three gray grid walls
            - 2,  show cartesian axes from (0,0,0)
            - 3,  show positive range of cartesian axes from (0,0,0)
            - 4,  show a triad at bottom left
            - 5,  show a cube at bottom left
            - 6,  mark the corners of the bounding box
            - 7,  draw a 3D ruler at each side of the cartesian axes
            - 8,  show the `vtkCubeAxesActor` object
            - 9,  show the bounding box outLine
            - 10, show three circles representing the maximum bounding box
            - 11, show a large grid on the x-y plane
            - 12, show polar axes
            - 13, draw a simple ruler at the bottom of the window

            Axis type-1 can be fully customized by passing a dictionary.
            Check `vedo.addons.Axes()` for the full list of options.
        azimuth/elevation/roll : (float)
            move camera accordingly the specified value
        viewup : (str, list)
            either `['x', 'y', 'z']` or a vector to set vertical direction
        resetcam : (bool)
            re-adjust camera position to fit objects
        camera : (dict, vtkCamera)
            camera parameters can further be specified with a dictionary
            assigned to the `camera` keyword (E.g. `show(camera={'pos':(1,2,3), 'thickness':1000,})`):
            - **pos** (list),  the position of the camera in world coordinates
            - **focal_point** (list), the focal point of the camera in world coordinates
            - **viewup** (list), the view up direction for the camera
            - **distance** (float), set the focal point to the specified distance from the camera position.
            - **clipping_range** (float), distance of the near and far clipping planes along the direction of projection.
            - **parallel_scale** (float),
            scaling used for a parallel projection, i.e. the height of the viewport
            in world-coordinate distances. The default is 1. Note that the "scale" parameter works as
            an "inverse scale", larger numbers produce smaller images.
            This method has no effect in perspective projection mode.
            - **thickness** (float),
            set the distance between clipping planes. This method adjusts the far clipping
            plane to be set a distance 'thickness' beyond the near clipping plane.
            - **view_angle** (float),
            the camera view angle, which is the angular height of the camera view
            measured in degrees. The default angle is 30 degrees.
            This method has no effect in parallel projection mode.
            The formula for setting the angle up for perfect perspective viewing is:
            angle = 2*atan((h/2)/d) where h is the height of the RenderWindow
            (measured by holding a ruler up to your screen) and d is the distance
            from your eyes to the screen.
        interactive : (bool)
            pause and interact with window (True) or continue execution (False)
        rate : (float)
            maximum rate of `show()` in Hertz
        mode : (int, str)
            set the type of interaction:
            - 0 = TrackballCamera [default]
            - 1 = TrackballActor
            - 2 = JoystickCamera
            - 3 = JoystickActor
            - 4 = Flight
            - 5 = RubberBand2D
            - 6 = RubberBand3D
            - 7 = RubberBandZoom
            - 8 = Terrain
            - 9 = Unicam
            - 10 = Image
        new : (bool)
            if set to `True`, a call to show will instantiate
            a new Plotter object (a new window) instead of reusing the first created.
    """
    if len(actors) == 0:
        actors = None
    elif len(actors) == 1:
        actors = actors[0]
    else:
        actors = utils.flatten(actors)

    if vedo.plotter_instance and not new:  # Plotter exists
        plt = vedo.plotter_instance

    else:  # Plotter must be created

        if utils.is_sequence(at):  # user passed a sequence for "at"

            if not utils.is_sequence(actors):
                vedo.logger.error("in show() input must be a list.")
                raise RuntimeError()
            if len(at) != len(actors):
                vedo.logger.error("in show() lists 'input' and 'at' must have equal lengths")
                raise RuntimeError()
            if shape == (1, 1) and N is None:
                N = max(at) + 1

        elif at is None and (N or shape != (1, 1)):

            if not utils.is_sequence(actors):
                e = "in show(), N or shape is set, but input is not a sequence\n"
                e += "              you may need to specify e.g. at=0"
                vedo.logger.error(e)
                raise RuntimeError()
            at = list(range(len(actors)))

        plt = Plotter(
            shape=shape,
            N=N,
            pos=pos,
            size=size,
            screensize=screensize,
            title=title,
            axes=axes,
            sharecam=sharecam,
            resetcam=resetcam,
            interactive=interactive,
            offscreen=offscreen,
            bg=bg,
            bg2=bg2,
        )

    # use _plt_to_return because plt.show() can return a k3d plot
    _plt_to_return = None

    if utils.is_sequence(at):

        for i, act in enumerate(actors):
            _plt_to_return = plt.show(
                act,
                at=i,
                zoom=zoom,
                resetcam=resetcam,
                viewup=viewup,
                azimuth=azimuth,
                elevation=elevation,
                roll=roll,
                camera=camera,
                interactive=False,
                mode=mode,
                bg=bg,
                bg2=bg2,
                axes=axes,
            )

        if (
            interactive
            or len(at) == N
            or (isinstance(shape[0], int) and len(at) == shape[0] * shape[1])
        ):
            # note that shape can be a string
            if plt.interactor and not offscreen and (interactive is None or interactive):
                plt.interactor.Start()

    else:

        _plt_to_return = plt.show(
            actors,
            at=at,
            zoom=zoom,
            resetcam=resetcam,
            viewup=viewup,
            azimuth=azimuth,
            elevation=elevation,
            roll=roll,
            camera=camera,
            interactive=interactive,
            mode=mode,
            bg=bg,
            bg2=bg2,
            axes=axes,
        )

    return _plt_to_return


def close():
    """Close the last created Plotter instance if it exists."""
    if not vedo.plotter_instance:
        return
    vedo.plotter_instance.close()
    return


########################################################################
class Plotter:
    """Main class to manage actors."""
    def __init__(
        self,
        shape=(1, 1),
        N=None,
        pos=(0, 0),
        size="auto",
        screensize="auto",
        title="vedo",
        bg="white",
        bg2=None,
        axes=None,
        sharecam=True,
        resetcam=True,
        interactive=None,
        offscreen=False,
        qt_widget=None,
        wx_widget=None,
    ):
        """
        Arguments:
            shape : (str, list)
                shape of the grid of renderers in format (rows, columns). Ignored if N is specified.
            N : (int)
                number of desired renderers arranged in a grid automatically.
            pos : (list)
                (x,y) position in pixels of top-left corner of the rendering window on the screen
            size : (str, list)
                size of the rendering window. If 'auto', guess it based on screensize.
            screensize : (list)
                physical size of the monitor screen in pixels
            bg : (color, str)
                background color or specify jpg image file name with path
            bg2 : (color)
                background color of a gradient towards the top
            axes : (int)

                Note that Axes type-1 can be fully customized by passing a dictionary `axes=dict()`.
                Check out `vedo.addons.Axes()` for the available options.
                - 0,  no axes
                - 1,  draw three gray grid walls
                - 2,  show cartesian axes from (0,0,0)
                - 3,  show positive range of cartesian axes from (0,0,0)
                - 4,  show a triad at bottom left
                - 5,  show a cube at bottom left
                - 6,  mark the corners of the bounding box
                - 7,  draw a 3D ruler at each side of the cartesian axes
                - 8,  show the VTK CubeAxesActor object
                - 9,  show the bounding box outLine,
                - 10, show three circles representing the maximum bounding box,
                - 11, show a large grid on the x-y plane (use with zoom=8)
                - 12, show polar axes.
                - 13, draw a simple ruler at the bottom of the window

            sharecam : (bool)
                if False each renderer will have an independent vtkCamera
            interactive : (bool)
                if True will stop after show() to allow interaction w/ window
            offscreen : (bool)
                if True will not show the rendering window
            qt_widget : (QVTKRenderWindowInteractor)
                render in a Qt-Widget using an QVTKRenderWindowInteractor.
                Overrides offscreen to True.
                Overrides interactive to False.
                See examples `qt_windows1.py` and `qt_windows2.py`
        """
        vedo.plotter_instance = self

        if qt_widget is not None:
            # overrides the interactive and offscreen properties
            interactive = False
            offscreen = True

        if wx_widget is not None:
            # overrides the interactive property
            interactive = False

        if interactive is None:
            if N == 1:
                interactive = True
            elif N or shape != (1, 1):
                interactive = False
            else:
                interactive = True

        self.actors = []  # list of actors to be shown
        self.clicked_actor = None  # holds the actor that has been clicked
        self.renderer = None  # current renderer
        self.renderers = []  # list of renderers
        self.shape = shape  # don't remove this line
        self._interactive = interactive  # allows to interact with renderer
        self.axes = axes  # show axes type nr.
        self.title = title  # window title
        self.sharecam = sharecam  # share the same camera if multiple renderers
        self.picker = None  # the vtkPicker object
        self.picked2d = None  # 2d coords of a clicked point on the rendering window
        self.picked3d = None  # 3d coords of a clicked point on an actor
        self.offscreen = offscreen
        self.resetcam = resetcam
        self.last_event = None

        self.qt_widget = qt_widget  #  QVTKRenderWindowInteractor
        self.wx_widget = wx_widget  # wxVTKRenderWindowInteractor

        self.skybox = None

        # mostly internal stuff:
        self.hover_legends = []
        self.backgrcol = bg
        self.pos = pos  # used by vedo.file_io
        self.justremoved = None
        self.axes_instances = []
        self.clock = 0
        self.sliders = []
        self.buttons = []
        self.widgets = []
        self.cutter_widget = None
        self.hint_widget = None
        self.background_renderer = None
        self.size = size
        self.interactor = None
        self.camera = None

        self._icol = 0
        self._clockt0 = time.time()
        self._extralight = None
        self._cocoa_initialized = False
        self._bg = bg  # used by backend notebooks

        #####################################################################
        if settings.default_backend != "vtk":
            if settings.default_backend == "2d":
                self.offscreen = True
                if self.size == "auto":
                    self.size = (800, 600)

            elif settings.default_backend == "k3d":
                self._interactive = False
                self.interactor = None
                self.window = None
                self.camera = None  # let the backend choose
                if self.size == "auto":
                    self.size = (1000, 1000)
                #############################################################
                return  ######################################################
                #############################################################
        #####################################################################

        # build the rendering window:
        self.window = vtk.vtkRenderWindow()

        self.window.GlobalWarningDisplayOff()
        self.window.SetWindowName(self.title)

        # more settings
        if settings.use_depth_peeling:
            self.window.SetAlphaBitPlanes(settings.alpha_bit_planes)
        self.window.SetMultiSamples(settings.multi_samples)

        self.window.SetPolygonSmoothing(settings.polygon_smoothing)
        self.window.SetLineSmoothing(settings.line_smoothing)
        self.window.SetPointSmoothing(settings.point_smoothing)

        # sort out screen size
        if screensize == "auto":
            screensize = (2160, 1440)  # might go wrong, use a default 1.5 ratio

            ### BUG in GetScreenSize in VTK 9.1.0
            ### https://discourse.vtk.org/t/vtk9-1-0-problems/7094/3
            if settings.hack_call_screen_size:  # True

                vtkvers = vedo.vtk_version
                if not self.offscreen and (vtkvers[0] < 9 or vtkvers[0] == 9 and vtkvers[1] == 0):
                    aus = self.window.GetScreenSize()
                    if aus and len(aus) == 2 and aus[0] > 100 and aus[1] > 100:  # seems ok
                        if aus[0] / aus[1] > 2:  # looks like there are 2 or more screens
                            screensize = (int(aus[0] / 2), aus[1])
                        else:
                            screensize = aus

        x, y = screensize

        if N:  # N = number of renderers. Find out the best

            if shape != (1, 1):  # arrangement based on minimum nr. of empty renderers
                vedo.logger.warning("having set N, shape is ignored.")

            nx = int(np.sqrt(int(N * y / x) + 1))
            ny = int(np.sqrt(int(N * x / y) + 1))
            lm = [
                (nx, ny),
                (nx, ny + 1),
                (nx - 1, ny),
                (nx + 1, ny),
                (nx, ny - 1),
                (nx - 1, ny + 1),
                (nx + 1, ny - 1),
                (nx + 1, ny + 1),
                (nx - 1, ny - 1),
            ]
            ind, minl = 0, 1000
            for i, m in enumerate(lm):
                l = m[0] * m[1]
                if N <= l < minl:
                    ind = i
                    minl = l
            shape = lm[ind]

        ##################################################
        if isinstance(shape, str):

            if "|" in shape:
                if self.size == "auto":
                    self.size = (800, 1200)
                n = int(shape.split("|")[0])
                m = int(shape.split("|")[1])
                rangen = reversed(range(n))
                rangem = reversed(range(m))
            else:
                if self.size == "auto":
                    self.size = (1200, 800)
                m = int(shape.split("/")[0])
                n = int(shape.split("/")[1])
                rangen = range(n)
                rangem = range(m)

            if n >= m:
                xsplit = m / (n + m)
            else:
                xsplit = 1 - n / (n + m)
            if settings.window_splitting_position:
                xsplit = settings.window_splitting_position

            for i in rangen:
                arenderer = vtk.vtkRenderer()
                if "|" in shape:
                    arenderer.SetViewport(0, i / n, xsplit, (i + 1) / n)
                else:
                    arenderer.SetViewport(i / n, 0, (i + 1) / n, xsplit)
                self.renderers.append(arenderer)

            for i in rangem:
                arenderer = vtk.vtkRenderer()

                if "|" in shape:
                    arenderer.SetViewport(xsplit, i / m, 1, (i + 1) / m)
                else:
                    arenderer.SetViewport(i / m, xsplit, (i + 1) / m, 1)
                self.renderers.append(arenderer)

            for r in self.renderers:
                r.SetUseHiddenLineRemoval(settings.hidden_line_removal)
                r.SetLightFollowCamera(settings.light_follows_camera)

                r.SetUseDepthPeeling(settings.use_depth_peeling)
                # r.SetUseDepthPeelingForVolumes(settings.use_depth_peeling)
                if settings.use_depth_peeling:
                    r.SetMaximumNumberOfPeels(settings.max_number_of_peels)
                    r.SetOcclusionRatio(settings.occlusion_ratio)
                r.SetUseFXAA(settings.use_fxaa)
                r.SetPreserveDepthBuffer(settings.preserve_depth_buffer)

                r.SetBackground(vedo.get_color(self.backgrcol))

                self.axes_instances.append(None)

            self.shape = (n + m,)

        elif utils.is_sequence(shape) and isinstance(shape[0], dict):
            # passing a sequence of dicts for renderers specifications

            if self.size == "auto":
                self.size = (1200, 900)

            for rd in shape:
                x0, y0 = rd["bottomleft"]
                x1, y1 = rd["topright"]
                bg_ = rd.pop("bg", "white")
                bg2_ = rd.pop("bg2", None)

                arenderer = vtk.vtkRenderer()
                arenderer.SetUseHiddenLineRemoval(settings.hidden_line_removal)
                arenderer.SetLightFollowCamera(settings.light_follows_camera)

                arenderer.SetUseDepthPeeling(settings.use_depth_peeling)
                # arenderer.SetUseDepthPeelingForVolumes(settings.use_depth_peeling)
                if settings.use_depth_peeling:
                    arenderer.SetMaximumNumberOfPeels(settings.max_number_of_peels)
                    arenderer.SetOcclusionRatio(settings.occlusion_ratio)
                arenderer.SetUseFXAA(settings.use_fxaa)
                arenderer.SetPreserveDepthBuffer(settings.preserve_depth_buffer)

                arenderer.SetViewport(x0, y0, x1, y1)
                arenderer.SetBackground(vedo.get_color(bg_))
                if bg2_:
                    arenderer.GradientBackgroundOn()
                    arenderer.SetBackground2(vedo.get_color(bg2_))

                self.renderers.append(arenderer)
                self.axes_instances.append(None)

            self.shape = (len(shape),)

        else:

            if isinstance(self.size, str) and self.size == "auto":
                # figure out a reasonable window size
                f = 1.5
                xs = y / f * shape[1]  # because y<x
                ys = y / f * shape[0]
                if xs > x / f:  # shrink
                    xs = x / f
                    ys = xs / shape[1] * shape[0]
                if ys > y / f:
                    ys = y / f
                    xs = ys / shape[0] * shape[1]
                self.size = (int(xs), int(ys))
                if shape == (1, 1):
                    self.size = (int(y / f), int(y / f))  # because y<x
            else:
                self.size = (self.size[0], self.size[1])

            image_actor = None
            bgname = str(self.backgrcol).lower()
            if ".jpg" in bgname or ".jpeg" in bgname or ".png" in bgname:
                self.window.SetNumberOfLayers(2)
                self.background_renderer = vtk.vtkRenderer()
                self.background_renderer.SetLayer(0)
                self.background_renderer.InteractiveOff()
                self.background_renderer.SetBackground(vedo.get_color(bg2))
                image_actor = vedo.Picture(self.backgrcol)
                self.window.AddRenderer(self.background_renderer)
                self.background_renderer.AddActor(image_actor)

            for i in reversed(range(shape[0])):
                for j in range(shape[1]):
                    arenderer = vtk.vtkRenderer()
                    arenderer.SetUseHiddenLineRemoval(settings.hidden_line_removal)
                    arenderer.SetLightFollowCamera(settings.light_follows_camera)
                    arenderer.SetTwoSidedLighting(settings.two_sided_lighting)

                    arenderer.SetUseDepthPeeling(settings.use_depth_peeling)
                    # arenderer.SetUseDepthPeelingForVolumes(settings.use_depth_peeling)
                    if settings.use_depth_peeling:
                        arenderer.SetMaximumNumberOfPeels(settings.max_number_of_peels)
                        arenderer.SetOcclusionRatio(settings.occlusion_ratio)
                    arenderer.SetUseFXAA(settings.use_fxaa)
                    arenderer.SetPreserveDepthBuffer(settings.preserve_depth_buffer)

                    if image_actor:
                        arenderer.SetLayer(1)

                    arenderer.SetBackground(vedo.get_color(self.backgrcol))
                    if bg2:
                        arenderer.GradientBackgroundOn()
                        arenderer.SetBackground2(vedo.get_color(bg2))

                    x0 = i / shape[0]
                    y0 = j / shape[1]
                    x1 = (i + 1) / shape[0]
                    y1 = (j + 1) / shape[1]
                    arenderer.SetViewport(y0, x0, y1, x1)
                    self.renderers.append(arenderer)
                    self.axes_instances.append(None)
            self.shape = shape

        if self.renderers:
            self.renderer = self.renderers[0]
            self.camera = self.renderer.GetActiveCamera()
            self.camera.SetParallelProjection(settings.use_parallel_projection)

        if self.size[0] == "f":  # full screen
            self.size = "fullscreen"
            self.window.SetFullScreen(True)
            self.window.BordersOn()
        else:
            self.window.SetSize(int(self.size[0]), int(self.size[1]))

        if self.wx_widget is not None:
            settings.immediate_rendering = False  # override
            self.window = self.wx_widget.GetRenderWindow()  # overwrite
            self.interactor = self.window.GetInteractor()
            for r in self.renderers:
                self.window.AddRenderer(r)
            self.wx_widget.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
            self.camera = self.renderer.GetActiveCamera()
            ########################
            return  ################
            ########################

        if self.qt_widget is not None:
            self.interactor = self.qt_widget.GetRenderWindow().GetInteractor()
            self.window = self.qt_widget.GetRenderWindow()  # overwrite
            ########################
            return  ################
            ########################

        self.window.SetPosition(pos)

        for r in self.renderers:
            self.window.AddRenderer(r)
            # set the background gradient if any
            if settings.background_gradient_orientation > 0:
                try:
                    modes = [
                        vtk.vtkViewport.GradientModes.VTK_GRADIENT_VERTICAL,
                        vtk.vtkViewport.GradientModes.VTK_GRADIENT_HORIZONTAL,
                        vtk.vtkViewport.GradientModes.VTK_GRADIENT_RADIAL_VIEWPORT_FARTHEST_SIDE,
                        vtk.vtkViewport.GradientModes.VTK_GRADIENT_RADIAL_VIEWPORT_FARTHEST_CORNER,
                    ]
                    r.SetGradientMode(modes[settings.background_gradient_orientation])
                    r.GradientBackgroundOn()
                except AttributeError:
                    pass

        if self.offscreen:
            if self.axes in (4, 5):
                self.axes = 0  # does not work with those
            self.window.SetOffScreenRendering(True)
            self._interactive = False
            self.interactor = None
            ########################
            return  ################
            ########################

        self.interactor = vtk.vtkRenderWindowInteractor()

        self.interactor.SetRenderWindow(self.window)
        vsty = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(vsty)

        if settings.enable_default_mouse_callbacks:
            self.interactor.AddObserver("LeftButtonPressEvent", self._mouseleftclick)

        if settings.enable_default_keyboard_callbacks:
            self.interactor.AddObserver("KeyPressEvent", self._keypress)

        # self._timer_event_id = None
        # if settings.allow_interaction:
            # def win_interact(iren, event):  # flushing interactor events
            #     if event == "TimerEvent":
            #         iren.ExitCallback()
            # self._timer_event_id = self.interactor.AddObserver("TimerEvent", win_interact)

    ##################################################################### ..init ends here.


    # def allow_interaction(self):
    #     """Call this method from inside a loop to allow mouse and keyboard interaction."""
    #     if (
    #         self.interactor
    #         and self._timer_event_id is not None
    #         and settings.immediate_rendering
    #     ):
    #         self._repeatingtimer_id = self.interactor.CreateRepeatingTimer(1)
    #         self.interactor.Start()
    #         if self.interactor:
    #             self.interactor.DestroyTimer(self._repeatingtimer_id)
    #         self._repeatingtimer_id = None
    #     return self

    def __iadd__(self, actors):
        self.add(actors)
        return self

    def __isub__(self, actors):
        self.remove(actors)
        return self

    def __enter__(self):
        # context manager like in "with Plotter() as plt:"
        return self

    def __exit__(self, *args, **kwargs):
        # context manager like in "with Plotter() as plt:"
        self.close()

    def process_events(self):
        if self.interactor:
            try:
                self.interactor.ProcessEvents()
            except AttributeError:
                pass
        return self

    def at(self, nren, yren=None):
        """
        Select the current renderer number as an int.
        Can also use the [nx, ny] format.
        """
        if yren is not None:
            nren = (yren) * self.shape[1] + (nren)
            if nren < 0 or nren > len(self.renderers):
                vedo.logger.error(f"at({nren, yren}) is malformed!")
                raise RuntimeError

        self.renderer = self.renderers[nren]
        self.camera = self.renderer.GetActiveCamera()
        return self


    def add(self, *actors, at=None):
        """
        Append the input objects to the internal list of actors to be shown.
        This method is typically used in loops or callback functions.

        Arguments:
            at : (int)
                add the object at the specified renderer
        """
        if at is not None:
            ren = self.renderers[at]
        else:
            ren = self.renderer

        actors = utils.flatten(actors)
        actors = self._scan_input(actors)

        for a in actors:
            if isinstance(a, vtk.vtkInteractorObserver):
                a.add_to(self)
                continue

            if a not in self.actors:
                self.actors.append(a)

            if ren:
                ren.AddActor(a)

                if hasattr(a, "rendered_at"):
                    ir = self.renderers.index(ren)
                    a.rendered_at.add(ir)

                if hasattr(a, "scalarbar") and a.scalarbar:
                    ren.AddActor(a.scalarbar)

                if hasattr(a, "_isfollower") and a._isfollower:  # set by mesh.follow_camera()
                    a.SetCamera(self.camera)

        return self

    def remove(self, *actors, at=None):
        """
        Remove input object to the internal list of actors to be shown.
        This method is typically used in loops or callback functions.
        Objects to be removed can be referenced by their assigned name.

        Arguments:
            at : (int)
                remove the object at the specified renderer
        """
        if at is not None:
            ren = self.renderers[at]
        else:
            ren = self.renderer

        actors = utils.flatten(actors)

        actors_in_ren = None

        actors_r = []
        for i, a in enumerate(actors):

            if isinstance(a, vtk.vtkInteractorObserver):
                a.remove_from(self)
                continue ###

            if isinstance(a, str):
                if actors_in_ren is None:
                    actors_in_ren = self.get_meshes(
                        include_non_pickables=True,
                        unpack_assemblies=False,
                    )

                for b in set(self.actors + actors_in_ren):
                    if hasattr(b, "name") and a in b.name:
                        actors_r.append(b)

            else:
                actors_r.append(a)

        for a in set(actors_r):
            if ren:
                ren.RemoveActor(a)
                if hasattr(a, "rendered_at"):
                    ir = self.renderers.index(ren)
                    a.rendered_at.discard(ir)
                if hasattr(a, "scalarbar") and a.scalarbar:
                    ren.RemoveActor(a.scalarbar)
                if hasattr(a, "_caption") and a._caption:
                    ren.RemoveActor(a._caption)
                if hasattr(a, "shadows") and a.shadows:
                    for sha in a.shadows:
                        ren.RemoveActor(sha)
                if hasattr(a, "trail") and a.trail:
                    ren.RemoveActor(a.trail)
                    a.trail_points = []
                    if hasattr(a.trail, "shadows") and a.trail.shadows:
                        for sha in a.trail.shadows:
                            ren.RemoveActor(sha)

            if a in self.actors:
                i = self.actors.index(a)
                del self.actors[i]

        return self

    def remove_lights(self):
        """Remove all the present lights in the current renderer."""
        if self.renderer:
            self.renderer.RemoveAllLights()
        return self

    def pop(self, at=None):
        """
        Remove the last added object from the rendering window.
        This method is typically used in loops or callback functions.
        """
        if at is not None and not isinstance(at, int):
            # wrong usage pitfall
            vedo.logger.error("argument of pop() must be an integer")
            raise RuntimeError()

        if self.actors:
            self.remove(self.actors[-1], at)
        return self

    def render(self, resetcam=False):
        """Render the scene. This method is typically used in loops or callback functions."""
        if not self.window:
            return self

        if self.wx_widget:
            if resetcam:
                self.renderer.ResetCamera()
            self.wx_widget.Render()
            return self

        if self.qt_widget:
            if resetcam:
                self.renderer.ResetCamera()
            self.qt_widget.Render()
            return self

        if self.interactor:
            if not self.interactor.GetInitialized():
                self.interactor.Initialize()

        self.camera = self.renderer.GetActiveCamera()
        if resetcam:
            self.renderer.ResetCamera()

        self.window.Render()
        return self

    def interactive(self):
        """
        Start window interaction.
        Analogous to `show(..., interactive=True)`.
        """
        if self.interactor:
            self.interactor.Start()
        return self

    def use_depth_peeling(self, at=None, value=True):
        """
        Specify whether use depth peeling algorithm at this specific renderer
        Call this method before the first rendering.
        """
        if at is None:
            ren = self.renderer
        else:
            ren = self.renderers[at]
        ren.SetUseDepthPeeling(value)
        return self

    def background(self, c1=None, c2=None, at=None, mode=0):
        """Set the color of the background for the current renderer.
        A different renderer index can be specified by keyword ``at``.

        Arguments:
            c1 : (list)
                background main color.
            c2 : (list)
                background color for the upper part of the window.
            at : (int)
                renderer index.
            mode : (int)
                background mode (needs vtk version >= 9.3)
                    0 = vertical,
                    1 = horizontal,
                    2 = radial farthest side,
                    3 = radia farthest corner.
        """
        if not self.renderers:
            return self
        if at is None:
            r = self.renderer
        else:
            r = self.renderers[at]

        if r:
            if c1 is not None:
                r.SetBackground(vedo.get_color(c1))
                self._bg = r.GetBackground()  # notebooks
            if c2 is not None:
                r.GradientBackgroundOn()
                r.SetBackground2(vedo.get_color(c2))
                if mode:
                    try: # only works with vtk>=9.3
                        modes = [
                            vtk.vtkViewport.GradientModes.VTK_GRADIENT_VERTICAL,
                            vtk.vtkViewport.GradientModes.VTK_GRADIENT_HORIZONTAL,
                            vtk.vtkViewport.GradientModes.VTK_GRADIENT_RADIAL_VIEWPORT_FARTHEST_SIDE,
                            vtk.vtkViewport.GradientModes.VTK_GRADIENT_RADIAL_VIEWPORT_FARTHEST_CORNER,
                        ]
                        r.SetGradientMode(modes[settings.background_gradient_orientation])
                    except AttributeError:
                        pass

            else:
                r.GradientBackgroundOff()
        return self

    ##################################################################
    def get_meshes(self, at=None, include_non_pickables=False, unpack_assemblies=True):
        """
        Return a list of Meshes from the specified renderer.

        Arguments:
            at : (int)
                specify which renderer to look at.
            include_non_pickables : (bool)
                include non-pickable objects
            unpack_assemblies : (bool)
                unpack assemblies into their components
        """
        if at is None:
            renderer = self.renderer
            at = self.renderers.index(renderer)
        elif isinstance(at, int):
            renderer = self.renderers[at]

        has_global_axes = False
        if isinstance(self.axes_instances[at], vedo.Assembly):
            has_global_axes = True

        if unpack_assemblies:
            acs = renderer.GetActors()
        else:
            acs = renderer.GetViewProps()

        actors = []
        acs.InitTraversal()
        for _ in range(acs.GetNumberOfItems()):

            if unpack_assemblies:
                a = acs.GetNextItem()
            else:
                a = acs.GetNextProp()

            if isinstance(a, vtk.vtkVolume):
                continue

            if include_non_pickables or a.GetPickable():
                if a == self.axes_instances[at]:
                    continue
                if has_global_axes and a in self.axes_instances[at].actors:
                    continue
                actors.append(a)
        return actors

    def get_volumes(self, at=None, include_non_pickables=False):
        """
        Return a list of Volumes from the specified renderer.

        Arguments:
            at : (int)
                specify which renderer to look at
            include_non_pickables : (bool)
                include non-pickable objects
        """
        if at is None:
            renderer = self.renderer
            at = self.renderers.index(renderer)
        elif isinstance(at, int):
            renderer = self.renderers[at]

        vols = []
        acs = renderer.GetVolumes()
        acs.InitTraversal()
        for _ in range(acs.GetNumberOfItems()):
            a = acs.GetNextItem()
            if include_non_pickables or a.GetPickable():
                vols.append(a)
        return vols

    def reset_camera(self, tight=None):
        """
        Reset the camera position and zooming.
        If tight (float) is specified the zooming reserves a padding space in the xy-plane
        expressed in percent of the average size.
        """
        if tight is None:
            self.renderer.ResetCamera()
        else:
            x0, x1, y0, y1, z0, z1 = self.renderer.ComputeVisiblePropBounds()

            cam = self.renderer.GetActiveCamera()

            self.renderer.ComputeAspect()
            aspect = self.renderer.GetAspect()
            angle = np.pi * cam.GetViewAngle() / 180.0
            dx, dy = (x1 - x0) * 0.999, (y1 - y0) * 0.999
            dist = max(dx / aspect[0], dy) / np.sin(angle / 2) / 2

            cam.SetViewUp(0, 1, 0)
            cam.SetPosition(x0 + dx / 2, y0 + dy / 2, dist * (1 + tight))
            cam.SetFocalPoint(x0 + dx / 2, y0 + dy / 2, 0)
            if cam.GetParallelProjection():
                ps = max(dx / aspect[0], dy) / 2
                cam.SetParallelScale(ps * (1 + tight))
            self.renderer.ResetCameraClippingRange(x0, x1, y0, y1, z0, z1)
        return self

    def reset_viewup(self, smooth=True):
        """
        Reset the orientation of the camera to the closest orthogonal direction and view-up.
        """
        vbb = addons.compute_visible_bounds()[0]
        x0, x1, y0, y1, z0, z1 = vbb
        mx, my, mz = (x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2
        d = self.camera.GetDistance()

        viewups = np.array([
            (0, 1, 0), ( 0, -1,  0),
            (0, 0, 1), ( 0,  0, -1),
            (1, 0, 0), (-1,  0,  0),
        ])
        positions = np.array([
            (mx, my, mz+d), (mx, my, mz-d),
            (mx, my+d, mz), (mx, my-d, mz),
            (mx+d, my, mz), (mx-d, my, mz),
        ])

        vu = np.array(self.camera.GetViewUp())
        vui = np.argmin(np.linalg.norm(viewups - vu, axis=1))

        poc = np.array(self.camera.GetPosition())
        foc = np.array(self.camera.GetFocalPoint())
        a = poc - foc
        b = positions - foc
        a = a / np.linalg.norm(a)
        b = b.T * (1 / np.linalg.norm(b, axis=1))
        pui = np.argmin(np.linalg.norm(b.T - a, axis=1))

        if smooth:
            outtimes = np.linspace(0, 1, num=11, endpoint=True)
            for t in outtimes:
                vv = vu * (1 - t) + viewups[vui] * t
                pp = poc * (1 - t) + positions[pui] * t
                ff = foc * (1 - t) + np.array([mx, my, mz]) * t
                self.camera.SetViewUp(vv)
                self.camera.SetPosition(pp)
                self.camera.SetFocalPoint(ff)
                self.render()

            # interpolator does not respect parallel view...:
            # cam1 = dict(
            #     pos=poc,
            #     viewup=vu,
            #     focal_point=(mx,my,mz),
            #     clipping_range=self.camera.GetClippingRange()
            # )
            # # cam1 = self.camera
            # cam2 = dict(
            #     pos=positions[pui],
            #     viewup=viewups[vui],
            #     focal_point=(mx,my,mz),
            #     clipping_range=self.camera.GetClippingRange()
            # )
            # vcams = self.move_camera([cam1, cam2], output_times=outtimes, smooth=0)
            # for c in vcams:
            #     self.renderer.SetActiveCamera(c)
            #     self.render()
        else:

            self.camera.SetViewUp(viewups[vui])
            self.camera.SetPosition(positions[pui])
            self.camera.SetFocalPoint(mx, my, mz)

        self.renderer.ResetCameraClippingRange()

        # vbb, _, _, _ = addons.compute_visible_bounds()
        # x0,x1, y0,y1, z0,z1 = vbb
        # self.renderer.ResetCameraClippingRange(x0, x1, y0, y1, z0, z1)
        self.render()
        return self

    def move_camera(self, cameras, t=0, times=(), smooth=True, output_times=()):
        """
        Takes as input two cameras set camera at an interpolated position:

        Cameras can be vtkCamera or dictionaries in format:

            `dict(pos=..., focal_point=..., viewup=..., distance=..., clipping_range=...)`

        Press `shift-C` key in interactive mode to dump a python snipplet
        of parameters for the current camera view.
        """
        nc = len(cameras)
        if len(times) == 0:
            times = np.linspace(0, 1, num=nc, endpoint=True)

        assert len(times) == nc

        cin = vtk.vtkCameraInterpolator()

        # cin.SetInterpolationTypeToLinear() # bugged?
        if nc > 2 and smooth:
            cin.SetInterpolationTypeToSpline()

        for i, cam in enumerate(cameras):
            vcam = cam
            if isinstance(cam, dict):
                vcam = utils.camera_from_dict(cam)
            cin.AddCamera(times[i], vcam)

        mint, maxt = cin.GetMinimumT(), cin.GetMaximumT()
        rng = maxt - mint

        if len(output_times) == 0:
            cin.InterpolateCamera(t * rng, self.camera)
            self.renderer.SetActiveCamera(self.camera)
            return [self.camera]
        else:
            vcams = []
            for tt in output_times:
                c = vtk.vtkCamera()
                cin.InterpolateCamera(tt * rng, c)
                vcams.append(c)
            return vcams

    def fly_to(self, point):
        """
        Fly camera to the specified point.

        Arguments:
            point : (list)
                point in space to place camera.

        Example:
            ```python
            from vedo import *
            cone = Cone()
            plt = Plotter(axes=1)
            plt.show(cone)
            plt.fly_to([1,0,0])
            plt.interactive().close()
            ```
        """
        if self.interactor:
            self.resetcam = False
            self.interactor.FlyTo(self.renderer, point)
            self.camera = self.renderer.GetActiveCamera()
        return self

    def look_at(self, plane="xy"):
        """Move the camera so that it looks at the specified cartesian plane"""
        cam = self.renderer.GetActiveCamera()
        fp = np.array(cam.GetFocalPoint())
        p = np.array(cam.GetPosition())
        dist = np.linalg.norm(fp - p)
        plane = plane.lower()
        if "x" in plane and "y" in plane:
            cam.SetPosition(fp[0], fp[1], fp[2] + dist)
            cam.SetViewUp(0.0, 1.0, 0.0)
        elif "x" in plane and "z" in plane:
            cam.SetPosition(fp[0], fp[1] - dist, fp[2])
            cam.SetViewUp(0.0, 0.0, 1.0)
        elif "y" in plane and "z" in plane:
            cam.SetPosition(fp[0] + dist, fp[1], fp[2])
            cam.SetViewUp(0.0, 0.0, 1.0)
        else:
            vedo.logger.error(f"in plotter.look() cannot understand argument {plane}")
        return self

    def record(self, filename=".vedo_recorded_events.log"):
        """
        Record camera, mouse, keystrokes and all other events.
        Recording can be toggled on/off by pressing key "R".

        Arguments:
            filename : (str)
                ascii file to store events. The default is '.vedo_recorded_events.log'.

        Returns:
            a string descriptor of events.

        Examples:
            - [record_play.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/record_play.py)
        """
        erec = vtk.vtkInteractorEventRecorder()
        erec.SetInteractor(self.interactor)
        erec.SetFileName(filename)
        erec.SetKeyPressActivationValue("R")
        erec.EnabledOn()
        erec.Record()
        self.interactor.Start()
        erec.Stop()
        erec.EnabledOff()
        with open(filename, "r", encoding="UTF-8") as fl:
            events = fl.read()
        erec = None
        return events

    def play(self, events=".vedo_recorded_events.log", repeats=0):
        """
        Play camera, mouse, keystrokes and all other events.

        Arguments:
            events : (str)
                file o string of events. The default is '.vedo_recorded_events.log'.
            repeats : (int)
                number of extra repeats of the same events. The default is 0.

        Examples:
            - [record_play.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/record_play.py)
        """
        erec = vtk.vtkInteractorEventRecorder()
        erec.SetInteractor(self.interactor)

        if events.endswith(".log"):
            erec.ReadFromInputStringOff()
            erec.SetFileName(events)
        else:
            erec.ReadFromInputStringOn()
            erec.SetInputString(events)

        erec.Play()
        for _i in range(repeats):
            erec.Rewind()
            erec.Play()
        erec.EnabledOff()
        erec = None
        return self

    def parallel_projection(self, value=True, at=None):
        """
        Use parallel projection `at` a specified renderer.
        Object is seen from "infinite" distance, e.i. remove any perspective effects.
        An input value equal to -1 will toggle it on/off.
        """
        if at is not None:
            r = self.renderers[at]
        else:
            r = self.renderer
        if value == -1:
            val = r.GetActiveCamera().GetParallelProjection()
            value = not val
        r.GetActiveCamera().SetParallelProjection(value)
        r.Modified()
        return self

    def fov(self, angle):
        """
        Set the field of view angle for the camera.
        This is the angle of the camera frustum in the horizontal direction.
        High values will result in a wide-angle lens (fish-eye effect),
        and low values will result in a telephoto lens.

        Default value is 30 degrees.
        """
        self.renderer.GetActiveCamera().UseHorizontalViewAngleOn()
        self.renderer.GetActiveCamera().SetViewAngle(angle)
        return self

    def zoom(self, zoom):
        """Apply a zooming factor for the current camera view"""
        self.renderer.GetActiveCamera().Zoom(zoom)
        return self
    
    def azimuth(self, angle):
        """Rotate camera around the view up vector."""
        self.renderer.GetActiveCamera().Azimuth(angle)
        return self
    
    def elevation(self, angle):
        """Rotate the camera around the cross product of the negative
        of the direction of projection and the view up vector."""
        self.renderer.GetActiveCamera().Elevation(angle)
        return self
    
    def roll(self, angle):
        """Roll the camera about the direction of projection."""
        self.renderer.GetActiveCamera().Roll(angle)
        return self
    
    def dolly(self, value):
        """Move the camera towards (value>0) or away from (value<0) the focal point."""
        self.renderer.GetActiveCamera().Dolly(value)
        return self


    ##################################################################
    def add_slider(
        self,
        sliderfunc: Callable,
        xmin,
        xmax,
        value=None,
        pos=4,
        title="",
        font="",
        title_size=1,
        c=None,
        alpha=1,
        show_value=True,
        delayed=False,
        **options,
    ):
        """
        Add a `vedo.addons.Slider2D` which can call an external custom function.

        Arguments:
            sliderfunc : (Callable)
                external function to be called by the widget
            xmin : (float)
                lower value of the slider
            xmax : (float)
                upper value
            value : (float)
                current value
            pos : (list, str)
                position corner number: horizontal [1-5] or vertical [11-15]
                it can also be specified by corners coordinates [(x1,y1), (x2,y2)]
                and also by a string descriptor (eg. "bottom-left")
            title : (str)
                title text
            font : (str)
                title font face. Check [available fonts here](https://vedo.embl.es/fonts).
            title_size : (float)
                title text scale [1.0]
            show_value : (bool)
                if True current value is shown
            delayed : (bool)
                if True the callback is delayed until when the mouse button is released
            alpha : (float)
                opacity of the scalar bar texts
            slider_length : (float)
                slider length
            slider_width : (float)
                slider width
            end_cap_length : (float)
                length of the end cap
            end_cap_width : (float)
                width of the end cap
            tube_width : (float)
                width of the tube
            title_height : (float)
                width of the title
            tformat : (str)
                format of the title

        Examples:
            - [sliders1.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/sliders1.py)
            - [sliders2.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/sliders2.py)

            ![](https://user-images.githubusercontent.com/32848391/50738848-be033480-11d8-11e9-9b1a-c13105423a79.jpg)
        """
        if c is None:  # automatic black or white
            c = (0.8, 0.8, 0.8)
            if np.sum(vedo.get_color(self.backgrcol)) > 1.5:
                c = (0.2, 0.2, 0.2)
        else:
            c = vedo.get_color(c)

        slider2d = addons.Slider2D(
            sliderfunc,
            xmin,
            xmax,
            value,
            pos,
            title,
            font,
            title_size,
            c,
            alpha,
            show_value,
            delayed,
            **options,
        )

        if self.renderer:
            slider2d.renderer = self.renderer
            if self.interactor:
                slider2d.interactor = self.interactor
                slider2d.on()
                self.sliders.append([slider2d, sliderfunc])
        return slider2d


    def add_slider3d(
        self,
        sliderfunc,
        pos1,
        pos2,
        xmin,
        xmax,
        value=None,
        s=0.03,
        t=1,
        title="",
        rotation=0.0,
        c=None,
        show_value=True,
    ):
        """
        Add a 3D slider widget which can call an external custom function.

        Arguments:
            sliderfunc : (function)
                external function to be called by the widget
            pos1 : (list)
                first position 3D coordinates
            pos2 : (list)
                second position coordinates
            xmin : (float)
                lower value
            xmax : (float)
                upper value
            value : (float)
                initial value
            s : (float)
                label scaling factor
            t : (float)
                tube scaling factor
            title : (str)
                title text
            c : (color)
                slider color
            rotation : (float)
                title rotation around slider axis
            show_value : (bool)
                if True current value is shown

        Examples:
            - [sliders3d.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/sliders3d.py)

            ![](https://user-images.githubusercontent.com/32848391/52859555-4efcf200-312d-11e9-9290-6988c8295163.png)
        """
        if c is None:  # automatic black or white
            c = (0.8, 0.8, 0.8)
            if np.sum(vedo.get_color(self.backgrcol)) > 1.5:
                c = (0.2, 0.2, 0.2)
        else:
            c = vedo.get_color(c)

        slider3d = addons.Slider3D(
            sliderfunc, pos1, pos2, xmin, xmax, value, s, t, title, rotation, c, show_value
        )
        slider3d.renderer = self.renderer
        slider3d.interactor = self.interactor
        slider3d.on()
        self.sliders.append([slider3d, sliderfunc])
        return slider3d


    def add_button(
        self,
        fnc=None,
        states=("On", "Off"),
        c=("w", "w"),
        bc=("green4", "red4"),
        pos=(0.7, 0.1),
        size=24,
        font="Courier",
        bold=True,
        italic=False,
        alpha=1,
        angle=0,
    ):
        """
        Add a button to the renderer window.

        Arguments:
            states : (list)
                a list of possible states, e.g. ['On', 'Off']
            c : (list)
                a list of colors for each state
            bc : (list)
                a list of background colors for each state
            pos : (list)
                2D position in pixels from left-bottom corner
            size : (float)
                size of button font
            font : (str)
                font type. Check [available fonts here](https://vedo.embl.es/fonts).
            bold : (bool)
                bold font face (False)
            italic : (bool)
                italic font face (False)
            alpha : (float)
                opacity level
            angle : (float)
                anticlockwise rotation in degrees

        Returns:
            `vedo.addons.Button` object.

        Examples:
            - [buttons.py](https://github.com/marcomusy/vedo/blob/master/examples/basic/buttons.py)

            ![](https://user-images.githubusercontent.com/32848391/50738870-c0fe2500-11d8-11e9-9b78-92754f5c5968.jpg)
        """
        if self.interactor:
            bu = addons.Button(fnc, states, c, bc, pos, size, font, bold, italic, alpha, angle)
            self.renderer.AddActor2D(bu)
            self.buttons.append(bu)
            # bu.function_id = self.add_callback("LeftButtonPress", bu.function, enable_picking=False)
            bu.function_id = bu.add_observer("pick", bu.function, priority=10)
            return bu

    def add_spline_tool(
        self, points, pc="k", ps=8, lc="r4", ac="g5", lw=2, closed=False, interactive=False
    ):
        """
        Add a spline tool to the current plotter.
        Nodes of the spline can be dragged in space with the mouse.
        Clicking on the line itself adds an extra point.
        Selecting a point and pressing del removes it.

        Arguments:
            points : (Mesh, Points, array)
                the set of vertices forming the spline nodes.
            pc : (str)
                point color. The default is 'k'.
            ps : (str)
                point size. The default is 8.
            lc : (str)
                line color. The default is 'r4'.
            ac : (str)
                active point marker color. The default is 'g5'.
            lw : (int)
                line width. The default is 2.
            closed : (bool)
                spline is meant to be closed. The default is False.

        Returns:
            a `SplineTool` object.

        Examples:
            - [spline_tool.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/spline_tool.py)

            ![](https://vedo.embl.es/images/basic/spline_tool.png)
        """
        sw = addons.SplineTool(points, pc, ps, lc, ac, lw, closed)
        if self.interactor:
            sw.SetInteractor(self.interactor)
        else:
            vedo.logger.error("in add_spline_tool(), No interactor found.")
            raise RuntimeError
        sw.On()
        sw.Initialize(sw.points.polydata())
        if sw.closed:
            sw.representation.ClosedLoopOn()
        sw.representation.SetRenderer(self.renderer)
        sw.representation.BuildRepresentation()
        sw.Render()
        if interactive:
            self.interactor.Start()
        else:
            self.interactor.Render()
        return sw

    def add_icon(self, icon, pos=3, size=0.08):
        """Add an inset icon mesh into the same renderer.

        Arguments:
            pos : (int, list)
                icon position in the range [1-4] indicating one of the 4 corners,
                or it can be a tuple (x,y) as a fraction of the renderer size.
            size : (float)
                size of the square inset.

        Examples:
            - [icon.py](https://github.com/marcomusy/vedo/tree/master/examples/other/icon.py)
        """
        iconw = addons.Icon(icon, pos, size)

        iconw.SetInteractor(self.interactor)
        iconw.EnabledOn()
        iconw.InteractiveOff()
        self.widgets.append(iconw)
        return iconw


    def add_global_axes(self, axtype=None, c=None):
        """Draw axes on scene. Available axes types:

        Arguments:
            axtype : (int)
                - 0,  no axes,
                - 1,  draw three gray grid walls
                - 2,  show cartesian axes from (0,0,0)
                - 3,  show positive range of cartesian axes from (0,0,0)
                - 4,  show a triad at bottom left
                - 5,  show a cube at bottom left
                - 6,  mark the corners of the bounding box
                - 7,  draw a 3D ruler at each side of the cartesian axes
                - 8,  show the vtkCubeAxesActor object
                - 9,  show the bounding box outLine
                - 10, show three circles representing the maximum bounding box
                - 11, show a large grid on the x-y plane
                - 12, show polar axes
                - 13, draw a simple ruler at the bottom of the window

            Axis type-1 can be fully customized by passing a dictionary axes=dict().

        Example:
            ```python
            from vedo import Box, show
            b = Box(pos=(0, 0, 0), length=80, width=90, height=70).alpha(0.1)
            show(
                b,
                axes={
                    "xtitle": "Some long variable [a.u.]",
                    "number_of_divisions": 4,
                    # ...
                },
            )
            ```

        Examples:
            - [custom_axes1.py](https://github.com/marcomusy/vedo/blob/master/examples/pyplot/custom_axes1.py)
            - [custom_axes2.py](https://github.com/marcomusy/vedo/blob/master/examples/pyplot/custom_axes2.py)
            - [custom_axes3.py](https://github.com/marcomusy/vedo/blob/master/examples/pyplot/custom_axes3.py)
            - [custom_axes4.py](https://github.com/marcomusy/vedo/blob/master/examples/pyplot/custom_axes4.py)

            <img src="https://user-images.githubusercontent.com/32848391/72752870-ab7d5280-3bc3-11ea-8911-9ace00211e23.png" width="600">
        """
        addons.add_global_axes(axtype, c)
        return self

    def add_legend_box(self, **kwargs):
        """Add a legend to the top right.

        Examples:
            - [legendbox.py](https://github.com/marcomusy/vedo/blob/master/examples/examples/basic/legendbox.py),
            - [flag_labels1.py](https://github.com/marcomusy/vedo/blob/master/examples/examples/other/flag_labels1.py)
            - [flag_labels2.py](https://github.com/marcomusy/vedo/blob/master/examples/examples/other/flag_labels2.py)
        """
        acts = self.get_meshes()
        lb = addons.LegendBox(acts, **kwargs)
        self.add(lb)
        return self

    def add_hint(
        self,
        obj,
        text="",
        c="k",
        bc="yellow8",
        font="Calco",
        size=18,
        justify=0,
        angle=0,
        delay=100,
    ):
        """
        Create a pop-up hint style message when hovering an object.
        Use add_hint(False) to disable all hints.

        Arguments:
            obj : (Mesh, Points)
                the object to associate the pop-up to
            text : (str)
                string description of the pop-up
            delay : (int)
                milliseconds to wait before pop-up occurs
        """
        if self.offscreen:
            return self

        if vedo.vtk_version[0] == 9 and "Linux" in vedo.sys_platform:  # Linux vtk9 is bugged
            vedo.logger.warning("add_hint() is not available on Linux platforms.")
            return self

        if obj is False:
            self.hint_widget.EnabledOff()
            self.hint_widget = None
            return self

        if text is False and self.hint_widget:
            self.hint_widget.RemoveBalloon(obj)
            return self

        if text == "":
            if obj.name:
                text = obj.name
            elif obj.filename:
                text = obj.filename
            else:
                return self

        if not self.hint_widget:
            self.hint_widget = vtk.vtkBalloonWidget()

            rep = vtk.vtkBalloonRepresentation()
            rep.SetBalloonLayoutToImageRight()

            trep = rep.GetTextProperty()
            trep.SetFontFamily(vtk.VTK_FONT_FILE)
            trep.SetFontFile(utils.get_font_path(font))
            trep.SetFontSize(size)
            trep.SetColor(vedo.get_color(c))
            trep.SetBackgroundColor(vedo.get_color(bc))
            trep.SetShadow(False)
            trep.SetJustification(justify)
            trep.UseTightBoundingBoxOn()

            self.hint_widget.ManagesCursorOff()
            self.hint_widget.SetTimerDuration(delay)
            self.hint_widget.SetInteractor(self.interactor)
            if angle:
                rep.SetOrientation(angle)
                rep.SetBackgroundOpacity(0)
            self.hint_widget.SetRepresentation(rep)
            self.widgets.append(self.hint_widget)
            if self.interactor.GetInitialized():
                self.hint_widget.EnabledOn()
            else:
                vedo.logger.warning("add_hint() must be called after show(). Skip.")
                return self

        bst = self.hint_widget.GetBalloonString(obj)
        if bst:
            self.hint_widget.UpdateBalloonString(obj, text)
        else:
            self.hint_widget.AddBalloon(obj, text)

        return self


    def add_shadows(self):
        """Add shadows at the current renderer."""
        shadows = vtk.vtkShadowMapPass()
        seq = vtk.vtkSequencePass()
        passes = vtk.vtkRenderPassCollection()
        passes.AddItem(shadows.GetShadowMapBakerPass())
        passes.AddItem(shadows)
        seq.SetPasses(passes)
        camerapass = vtk.vtkCameraPass()
        camerapass.SetDelegatePass(seq)
        self.renderer.SetPass(camerapass)
        return self

    def add_ambient_occlusion(self, radius, bias=0.01, blur=True, samples=100):
        """
        Screen Space Ambient Occlusion.

        For every pixel on the screen, the pixel shader samples the depth values around
        the current pixel and tries to compute the amount of occlusion from each of the sampled
        points.

        Arguments:
            radius : (float)
                radius of influence in absolute units
            bias : (float)
                bias of the normals
            blur : (bool)
                add a blurring to the sampled positions
            samples : (int)
                number of samples to probe

        Examples:
            - [ssao.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/ssao.py)

            ![](https://vedo.embl.es/images/basic/ssao.jpg)
        """
        lights = vtk.vtkLightsPass()

        opaque = vtk.vtkOpaquePass()

        ssaoCam = vtk.vtkCameraPass()
        ssaoCam.SetDelegatePass(opaque)

        ssao = vtk.vtkSSAOPass()
        ssao.SetRadius(radius)
        ssao.SetBias(bias)
        ssao.SetBlur(blur)
        ssao.SetKernelSize(samples)
        ssao.SetDelegatePass(ssaoCam)

        translucent = vtk.vtkTranslucentPass()

        volpass = vtk.vtkVolumetricPass()
        ddp = vtk.vtkDualDepthPeelingPass()
        ddp.SetTranslucentPass(translucent)
        ddp.SetVolumetricPass(volpass)

        over = vtk.vtkOverlayPass()

        collection = vtk.vtkRenderPassCollection()
        collection.AddItem(lights)
        collection.AddItem(ssao)
        collection.AddItem(ddp)
        collection.AddItem(over)

        sequence = vtk.vtkSequencePass()
        sequence.SetPasses(collection)

        cam = vtk.vtkCameraPass()
        cam.SetDelegatePass(sequence)

        self.renderer.SetPass(cam)
        return self

    def add_depth_of_field(self, autofocus=True):
        """Add a depth of field effect in the scene."""
        lights = vtk.vtkLightsPass()

        opaque = vtk.vtkOpaquePass()

        dofCam = vtk.vtkCameraPass()
        dofCam.SetDelegatePass(opaque)

        dof = vtk.vtkDepthOfFieldPass()
        dof.SetAutomaticFocalDistance(autofocus)
        dof.SetDelegatePass(dofCam)

        collection = vtk.vtkRenderPassCollection()
        collection.AddItem(lights)
        collection.AddItem(dof)

        sequence = vtk.vtkSequencePass()
        sequence.SetPasses(collection)

        cam = vtk.vtkCameraPass()
        cam.SetDelegatePass(sequence)

        self.renderer.SetPass(cam)
        return self

    def _add_skybox(self, hdrfile):
        # many hdr files are at https://polyhaven.com/all

        if utils.vtk_version_at_least(9):
            reader = vtk.vtkHDRReader()
            # Check the image can be read.
            if not reader.CanReadFile(hdrfile):
                vedo.logger.error(f"Cannot read HDR file {hdrfile}")
                return self
            reader.SetFileName(hdrfile)
            reader.Update()

            texture = vtk.vtkTexture()
            texture.SetColorModeToDirectScalars()
            texture.SetInputData(reader.GetOutput())

            # Convert to a cube map
            tcm = vtk.vtkEquirectangularToCubeMapTexture()
            tcm.SetInputTexture(texture)
            # Enable mipmapping to handle HDR image
            tcm.MipmapOn()
            tcm.InterpolateOn()

            self.renderer.SetEnvironmentTexture(tcm)
            self.renderer.UseImageBasedLightingOn()
            self.skybox = vtk.vtkSkybox()
            self.skybox.SetTexture(tcm)
            self.renderer.AddActor(self.skybox)

        else:
            vedo.logger.error("add_skybox not supported in this VTK version. Skip.")

        return self

    def add_renderer_frame(self, c=None, alpha=None, lw=None, padding=None):
        """
        Add a frame to the renderer subwindow.

        Arguments:
            c : (color)
                color name or index
            alpha : (float)
                opacity level
            lw : (int)
                line width in pixels.
            padding : (float)
                padding space in pixels.
        """
        if c is None:  # automatic black or white
            c = (0.9, 0.9, 0.9)
            if np.sum(vedo.plotter_instance.renderer.GetBackground()) > 1.5:
                c = (0.1, 0.1, 0.1)
        renf = addons.RendererFrame(c, alpha, lw, padding)
        self.renderer.AddActor(renf)
        return self

    def add_hover_legend(
        self,
        at=None,
        c=None,
        pos="bottom-left",
        font="Calco",
        s=0.75,
        bg="auto",
        alpha=0.1,
        maxlength=24,
        use_info=False,
    ):
        """
        Add a legend with 2D text which is triggered by hovering the mouse on an object.

        The created text object are stored in plotter.hover_legends

        Arguments:
            c : (color)
                Text color. If None then black or white is chosen automatically
            pos : (str)
                text positioning
            font : (str)
                text font type. Check [available fonts here](https://vedo.embl.es/fonts).
            s : (float)
                text size scale
            bg : (color)
                background color of the 2D box containing the text
            alpha : (float)
                box transparency
            maxlength : (int)
                maximum number of characters per line
            use_info : (bool)
                visualize the content of the `obj.info` attribute

        Examples:
            - [hover_legend.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/hover_legend.py)
            - [earthquake_browser.py](https://github.com/marcomusy/vedo/tree/master/examples/pyplot/earthquake_browser.py)

            ![](https://vedo.embl.es/images/pyplot/earthquake_browser.jpg)
        """
        hoverlegend = vedo.shapes.Text2D(pos=pos, font=font, c=c, s=s, alpha=alpha, bg=bg)

        if at is None:
            at = self.renderers.index(self.renderer)

        def _legfunc(evt):
            if not evt.actor or not self.renderer or at != evt.at:
                if hoverlegend._mapper.GetInput():  # clear and return
                    hoverlegend._mapper.SetInput("")
                    self.interactor.Render()
                return

            if use_info:
                if hasattr(evt.actor, "info"):
                    t = str(evt.actor.info)
                else:
                    return
            else:
                t, tp = "", ""
                if evt.isMesh:
                    tp = "Mesh "
                elif evt.isPoints:
                    tp = "Points "
                # elif evt.isVolume:
                #     tp = "Volume "
                elif evt.isPicture:
                    tp = "Pict "
                elif evt.isAssembly:
                    tp = "Assembly "
                else:
                    return

                if evt.isAssembly:
                    if not evt.actor.name:
                        t += f"Assembly object of {len(evt.actor.unpack())} parts\n"
                    else:
                        t += f"Assembly name: {evt.actor.name} ({len(evt.actor.unpack())} parts)\n"
                else:
                    if evt.actor.name:
                        t += f"{tp}name"
                        if evt.isPoints:
                            t += "  "
                        if evt.isMesh:
                            t += "  "
                        t += f": {evt.actor.name[:maxlength]}".ljust(maxlength) + "\n"

                if evt.actor.filename:
                    t += f"{tp}filename: "
                    t += f"{os.path.basename(evt.actor.filename[-maxlength:])}".ljust(maxlength)
                    t += "\n"
                    if not evt.actor.file_size:
                        evt.actor.file_size, evt.actor.created = vedo.file_io.file_info(evt.actor.filename)
                    if evt.actor.file_size:
                        t += "             : "
                        sz, created = evt.actor.file_size, evt.actor.created
                        t += f"{created[4:-5]} ({sz})" + "\n"

                if evt.isPoints:
                    indata = evt.actor.polydata(False)
                    if indata.GetNumberOfPoints():
                        t += (
                            f"#points/cells: {indata.GetNumberOfPoints()}"
                            f" / {indata.GetNumberOfCells()}"
                        )
                    pdata = indata.GetPointData()
                    cdata = indata.GetCellData()
                    if pdata.GetScalars() and pdata.GetScalars().GetName():
                        t += f"\nPoint array  : {pdata.GetScalars().GetName()}"
                        if pdata.GetScalars().GetName() == evt.actor.mapper().GetArrayName():
                            t += " *"
                    if cdata.GetScalars() and cdata.GetScalars().GetName():
                        t += f"\nCell  array  : {cdata.GetScalars().GetName()}"
                        if cdata.GetScalars().GetName() == evt.actor.mapper().GetArrayName():
                            t += " *"

                if evt.isPicture:
                    t = f"{os.path.basename(evt.actor.filename[:maxlength+10])}".ljust(maxlength+10)
                    t += f"\nImage shape: {evt.actor.shape}"
                    pcol = self.color_picker(evt.picked2d)
                    t += f"\nPixel color: {vedo.colors.rgb2hex(pcol/255)} {pcol}"

            # change box color if needed in 'auto' mode
            if evt.isPoints and "auto" in str(bg):
                actcol = evt.actor.GetProperty().GetColor()
                if hoverlegend._mapper.GetTextProperty().GetBackgroundColor() != actcol:
                    hoverlegend._mapper.GetTextProperty().SetBackgroundColor(actcol)

            # adapt to changes in bg color
            bgcol = self.renderers[at].GetBackground()
            _bgcol = c
            if _bgcol is None:  # automatic black or white
                _bgcol = (0.9, 0.9, 0.9)
                if sum(bgcol) > 1.5:
                    _bgcol = (0.1, 0.1, 0.1)
                if len(set(_bgcol).intersection(bgcol)) < 3:
                    hoverlegend.color(_bgcol)

            if hoverlegend._mapper.GetInput() != t:
                hoverlegend._mapper.SetInput(t)
                self.interactor.Render()

        self.add(hoverlegend, at=at)
        self.hover_legends.append(hoverlegend)
        self.add_callback("MouseMove", _legfunc)
        return self


    #####################################################################
    def add_scale_indicator(
        self, pos=(0.7, 0.05), s=0.02, length=2, lw=4, c="k1", alpha=1, units="", gap=0.05
    ):
        """
        Add a Scale Indicator. Only works in parallel mode (no perspective).

        Arguments:
            pos : (list)
                fractional (x,y) position on the screen.
            s : (float)
                size of the text.
            length : (float)
                length of the line.
            units : (str)
                string to show units.
            gap : (float)
                separation of line and text.

        Example:
            ```python
            from vedo import settings, Cube, Plotter
            settings.use_parallel_projection = True # or else it does not make sense!
            cube = Cube().alpha(0.2)
            plt = Plotter(size=(900,600), axes=dict(xtitle='x (um)'))
            plt.add_scale_indicator(units='um', c='blue4')
            plt.show(cube, "Scale indicator with units").close()
            ```
            ![](https://vedo.embl.es/images/feats/scale_indicator.png)
        """
        ppoints = vtk.vtkPoints()  # Generate the polyline
        psqr = [[0.0, gap], [length / 10, gap]]
        dd = psqr[1][0] - psqr[0][0]
        for i, pt in enumerate(psqr):
            ppoints.InsertPoint(i, pt[0], pt[1], 0)
        lines = vtk.vtkCellArray()
        lines.InsertNextCell(len(psqr))
        for i in range(len(psqr)):
            lines.InsertCellPoint(i)
        pd = vtk.vtkPolyData()
        pd.SetPoints(ppoints)
        pd.SetLines(lines)

        wsx, wsy = self.window.GetSize()
        if not settings.use_parallel_projection:
            vedo.logger.warning("add_scale_indicator called with use_parallel_projection OFF. Skip.")
            return None

        rlabel = vtk.vtkVectorText()
        rlabel.SetText("scale")
        tf = vtk.vtkTransformPolyDataFilter()
        tf.SetInputConnection(rlabel.GetOutputPort())
        t = vtk.vtkTransform()
        t.Scale(s * wsy / wsx, s, 1)
        tf.SetTransform(t)

        app = vtk.vtkAppendPolyData()
        app.AddInputConnection(tf.GetOutputPort())
        app.AddInputData(pd)

        mapper = vtk.vtkPolyDataMapper2D()
        mapper.SetInputConnection(app.GetOutputPort())
        cs = vtk.vtkCoordinate()
        cs.SetCoordinateSystem(1)
        mapper.SetTransformCoordinate(cs)

        fractor = vtk.vtkActor2D()
        csys = fractor.GetPositionCoordinate()
        csys.SetCoordinateSystem(3)
        fractor.SetPosition(pos)
        fractor.SetMapper(mapper)
        fractor.GetProperty().SetColor(vedo.get_color(c))
        fractor.GetProperty().SetOpacity(alpha)
        fractor.GetProperty().SetLineWidth(lw)
        fractor.GetProperty().SetDisplayLocationToForeground()

        def sifunc(iren, ev):
            wsx, wsy = self.window.GetSize()
            ps = self.camera.GetParallelScale()
            newtxt = utils.precision(ps / wsy * wsx * length * dd, 3)
            if units:
                newtxt += " " + units
            if rlabel.GetText() != newtxt:
                rlabel.SetText(newtxt)

        self.renderer.AddActor(fractor)
        self.interactor.AddObserver("MouseWheelBackwardEvent", sifunc)
        self.interactor.AddObserver("MouseWheelForwardEvent", sifunc)
        self.interactor.AddObserver("InteractionEvent", sifunc)
        sifunc(0, 0)
        return fractor

    def fill_event(self, ename="", pos=(), enable_picking=True):
        """
        Create an Event object with information of what was clicked.

        If `enable_picking` is False, no picking will be performed.
        This can be useful to avoid double picking when using buttons.
        """    
        if not self.interactor:
            return Event()

        if len(pos):
            x, y = pos
            self.interactor.SetEventPosition(pos)
        else:
            x, y = self.interactor.GetEventPosition()
        self.renderer = self.interactor.FindPokedRenderer(x, y)

        self.picked2d = (x, y)

        key = self.interactor.GetKeySym()
        if key:
            if "_L" in key or "_R" in key:
                # skip things like Shift_R
                key = ""  # better than None
            else:
                if self.interactor.GetShiftKey():
                    key = key.upper()

                if key == "MINUS":  # fix: vtk9 is ignoring shift chars..
                    key = "underscore"
                elif key == "EQUAL":  # fix: vtk9 is ignoring shift chars..
                    key = "plus"
                elif key == "SLASH":  # fix: vtk9 is ignoring shift chars..
                    key = "?"

                if self.interactor.GetControlKey():
                    key = "Ctrl+" + key

                if self.interactor.GetAltKey():
                    key = "Alt+" + key

        if enable_picking:
            if not self.picker:
                self.picker = vtk.vtkPropPicker()

            self.picker.PickProp(x, y, self.renderer)

            xp, yp = self.interactor.GetLastEventPosition()
            actor = self.picker.GetProp3D()
            delta3d = np.array([0, 0, 0])
            if actor:
                picked3d = np.array(self.picker.GetPickPosition())
                if isinstance(actor, vedo.base.Base3DProp):  # needed!
                    if actor.picked3d is not None:
                        delta3d = picked3d - actor.picked3d
                actor.picked3d = picked3d
            else:
                picked3d = None

            if not actor:  # try 2D
                actor = self.picker.GetActor2D()

            dx, dy = x - xp, y - yp

        event = Event()
        event.name = ename
        event.title = self.title
        event.id = -1  # will be set by the timer wrapper function
        event.timerid = -1  # will be set by the timer wrapper function
        event.priority = -1  # will be set by the timer wrapper function
        event.time = time.time()
        event.at = self.renderers.index(self.renderer)
        event.keyPressed = key  # obsolete, will disappear. Use "keypress"
        event.keypress = key
        if enable_picking:
            event.actor = actor
            event.picked3d = picked3d
            event.picked2d = (x, y)
            event.delta2d = (dx, dy)
            event.angle2d = np.arctan2(dy, dx)
            event.speed2d = np.sqrt(dx * dx + dy * dy)
            event.delta3d = delta3d
            event.speed3d = np.sqrt(np.dot(delta3d, delta3d))
            event.isPoints = isinstance(actor, vedo.Points)
            event.isMesh = isinstance(actor, vedo.Mesh)
            event.isAssembly = isinstance(actor, vedo.Assembly)
            event.isVolume = isinstance(actor, vedo.Volume)
            event.isPicture = isinstance(actor, vedo.Picture)
            event.isActor2D = isinstance(actor, vtk.vtkActor2D)
        return event


    def add_callback(self, event_name, func, priority=0.0, enable_picking=True):
        """
        Add a function to be executed while show() is active.

        Return a unique id for the callback.

        The callback function (see example below) exposes a dictionary
        with the following information:
        - `name`: event name,
        - `id`: event unique identifier,
        - `priority`: event priority (float),
        - `interactor`: the interactor object,
        - `at`: renderer nr. where the event occurred
        - `keypress`: key pressed as string
        - `actor`: object picked by the mouse
        - `picked3d`: point picked in world coordinates
        - `picked2d`: screen coords of the mouse pointer
        - `delta2d`: shift wrt previous position (to calculate speed, direction)
        - `delta3d`: ...same but in 3D world coords
        - `angle2d`: angle of mouse movement on screen
        - `speed2d`: speed of mouse movement on screen
        - `speed3d`: speed of picked point in world coordinates
        - `isPoints`: True if of class
        - `isMesh`: True if of class
        - `isAssembly`: True if of class
        - `isVolume`: True if of class Volume
        - `isPicture`: True if of class

        If `enable_picking` is False, no picking will be performed.
        This can be useful to avoid double picking when using buttons.

        Frequently used events are:
        - `KeyPress`, `KeyRelease`: listen to keyboard events
        - `LeftButtonPress`, `LeftButtonRelease`: listen to mouse clicks
        - `MiddleButtonPress`, `MiddleButtonRelease`
        - `RightButtonPress`, `RightButtonRelease`
        - `MouseMove`: listen to mouse pointer changing position
        - `MouseWheelForward`, `MouseWheelBackward`
        - `Enter`, `Leave`: listen to mouse entering or leaving the window
        - `Pick`, `StartPick`, `EndPick`: listen to object picking
        - `ResetCamera`, `ResetCameraClippingRange`
        - `Error`, `Warning`
        - `Char`
        - `Timer`

        Check the complete list of events [here](https://vtk.org/doc/nightly/html/classvtkCommand.html).

        Example:
            ```python
            from vedo import *

            def func(evt):
                # this function is called every time the mouse moves
                # (evt is a dotted dictionary)
                if not evt.actor:
                    return  # no hit, return
                print("point coords =", evt.picked3d)
                # print("full event dump:", evt)

            elli = Ellipsoid()
            plt = Plotter(axes=1)
            plt.add_callback('mouse hovering', func)
            plt.show(elli).close()
            ```

        Examples:
            - [spline_draw.py](https://github.com/marcomusy/vedo/tree/master/examples/advanced/spline_draw.py)
            - [colorlines.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/colorlines.py)

                ![](https://vedo.embl.es/images/advanced/spline_draw.png)

            - ..and many others!
        """
        from vtkmodules.util.misc import calldata_type

        if not self.interactor:
            return None

        #########################################
        @calldata_type(vtk.VTK_INT)
        def _func_wrap(iren, ename, timerid=None):
            event = self.fill_event(ename=ename, enable_picking=enable_picking)
            event.timerid = timerid
            event.id = cid
            event.priority = priority
            self.last_event = event
            func(event)
            return  ## _func_wrap
        #########################################

        event_name = utils.get_vtk_name_event(event_name)

        # Not compatible with ProcessEvents()
        if "MouseMove" in event_name or "Timer" in event_name:
            settings.allow_interaction = False

        cid = self.interactor.AddObserver(event_name, _func_wrap, priority)
        # print(f"Registering event: {event_name} with id={cid}")
        return cid

    def remove_callback(self, cid):
        """
        Remove a callback function by its id
        or a whole category of callbacks by their name.

        Arguments:
            cid : (int, str)
                Unique id of the callback.
                If an event name is passed all callbacks of that type are removed.
        """
        if self.interactor:
            if isinstance(cid, str):
                cid = utils.get_vtk_name_event(cid)
                self.interactor.RemoveObservers(cid)
            else:
                self.interactor.RemoveObserver(cid)
        return self

    def timer_callback(self, action, timer_id=None, dt=1, one_shot=False):
        """
        Start or stop an existing timer.

        Arguments:
            action : (str)
                Either "create"/"start" or "destroy"/"stop"
            timer_id : (int)
                When stopping the timer, the ID of the timer as returned when created
            dt : (int)
                time in milliseconds between each repeated call
            one_shot : (bool)
                create a one shot timer of prescribed duration instead of a repeating one

        Examples:
            - [timer_callback1.py](https://github.com/marcomusy/vedo/tree/master/examples/advanced/timer_callback1.py)
            - [timer_callback2.py](https://github.com/marcomusy/vedo/tree/master/examples/advanced/timer_callback2.py)

            ![](https://vedo.embl.es/images/advanced/timer_callback1.jpg)
        """
        if action in ("create", "start"):
            if timer_id is not None:
                vedo.logger.warning("you set a timer_id but it will be ignored.")
            if one_shot:
                timer_id = self.interactor.CreateOneShotTimer(dt)
            else:
                timer_id = self.interactor.CreateRepeatingTimer(dt)
            return timer_id

        elif action in ("destroy", "stop"):
            if timer_id is not None:
                self.interactor.DestroyTimer(timer_id)
            else:
                vedo.logger.warning("please set a timer_id. Cannot stop timer.")
        else:
            e = f"in timer_callback(). Cannot understand action: {action}\n"
            e += " allowed actions are: ['start', 'stop']. Skipped."
            vedo.logger.error(e)
        return timer_id

    def add_observer(self, event_name, func, priority=0):
        """
        Add a callback function that will be called when an event occurs.
        Consider using `add_callback()` instead.
        """
        event_name = utils.get_vtk_name_event(event_name)
        idd = self.interactor.AddObserver(event_name, func, priority)
        return idd

    def compute_world_coordinate(
        self, pos2d, at=None, objs=(), bounds=(), offset=None, pixeltol=None, worldtol=None
    ):
        """
        Transform a 2D point on the screen into a 3D point inside the rendering scene.
        If a set of meshes is passed then points are placed onto these.

        Arguments:
            pos2d : (list)
                2D screen coordinates point.
            at : (int)
                renderer number.
            objs : (list)
                list of Mesh objects to project the point onto.
            bounds : (list)
                specify a bounding box as [xmin,xmax, ymin,ymax, zmin,zmax].
            offset : (float)
                specify an offset value.
            pixeltol : (int)
                screen tolerance in pixels.
            worldtol : (float)
                world coordinates tolerance.

        Returns:
            numpy array, the point in 3D world coordinates.

        Examples:
            - [cut_freehand.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/cut_freehand.py)
            - [mousehover3.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/mousehover3.py)

            ![](https://vedo.embl.es/images/basic/mousehover3.jpg)
        """
        if at is not None:
            renderer = self.renderers[at]
        else:
            renderer = self.renderer

        if not objs:
            pp = vtk.vtkFocalPlanePointPlacer()
        else:
            pp = vtk.vtkPolygonalSurfacePointPlacer()
            for ob in objs:
                pp.AddProp(ob)

        if len(bounds) == 6:
            pp.SetPointBounds(bounds)
        if pixeltol:
            pp.SetPixelTolerance(pixeltol)
        if worldtol:
            pp.SetWorldTolerance(worldtol)
        if offset:
            pp.SetOffset(offset)

        worldPos = [0, 0, 0]
        worldOrient = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pp.ComputeWorldPosition(renderer, pos2d, worldPos, worldOrient)
        # validw = pp.ValidateWorldPosition(worldPos, worldOrient)
        # validd = pp.ValidateDisplayPosition(renderer, pos2d)
        return np.array(worldPos)

    def compute_screen_coordinates(self, obj, full_window=False):
        """
        Given a 3D points in the current renderer (or full window),
        find the screen pixel coordinates.

        Example:
            ```python
            from vedo import *

            elli = Ellipsoid().rotate_y(30)

            plt = Plotter()
            plt.show(elli)

            xyscreen = plt.compute_screen_positions(elli)
            print('xyscreen coords:', xyscreen)

            # simulate an event happening at one point
            event = plt.fill_event(pos=xyscreen[123])
            print(event)
            ```
        """
        if isinstance(obj, vedo.base.Base3DProp):
            pts = obj.points()
        elif utils.is_sequence(obj):
            pts = obj
        p2d = []
        cs = vtk.vtkCoordinate()
        cs.SetCoordinateSystemToWorld()
        cs.SetViewport(self.renderer)
        for p in pts:
            cs.SetValue(p)
            if full_window:
                p2d.append(cs.GetComputedDisplayValue(self.renderer))
            else:
                p2d.append(cs.GetComputedViewportValue(self.renderer))
        return np.array(p2d, dtype=int)
    
    def pick_area(self, pos1, pos2, at=None):
        """
        Pick all objects within a box defined by two corner points in 2D screen coordinates.
        
        Returns a frustum Mesh that contains the visible field of view.
        This can be used to select objects in a scene or select vertices.

        Example:
            ```python
            from vedo import *

            settings.enable_default_mouse_callbacks = False

            def mode_select(objs):
                print("Selected objects:", objs)
                d0 = mode.start_x, mode.start_y # display coords
                d1 = mode.end_x, mode.end_y

                frustum = plt.pick_area(d0, d1)
                infru = frustum.inside_points(mesh)
                col = np.random.randint(0, 10)
                infru.ps(10).c(col)
                plt.add(frustum, infru).render()

            mesh = Mesh(dataurl+"cow.vtk").c("k5").lw(1)

            mode = interactor_modes.BlenderStyle()
            mode.callback_select = mode_select

            plt = Plotter().user_mode(mode)
            plt.show(mesh, axes=1)
            ```
        """
        if at is not None:
            ren = self.renderers[at]
        else:
            ren = self.renderer
        area_picker = vtk.vtkAreaPicker()
        area_picker.AreaPick(pos1[0], pos1[1], pos2[0], pos2[1], ren)
        planes = area_picker.GetFrustum()

        fru = vtk.vtkFrustumSource()
        fru.SetPlanes(planes)
        fru.ShowLinesOff()
        fru.Update()

        afru = vedo.Mesh(fru.GetOutput())
        afru.alpha(0.1).lw(1).pickable(False)
        afru.name = "Frustum"
        return afru


    def _scan_input(self, wannabeacts):
        # scan the input of show
        if not utils.is_sequence(wannabeacts):
            wannabeacts = [wannabeacts]

        scannedacts = []
        for a in wannabeacts:  # scan content of list

            if a is None:
                pass

            elif isinstance(a, vtk.vtkActor):

                scannedacts.append(a)

                if isinstance(a, vedo.base.BaseActor):
                    if a.shadows:
                        # a.update_shadows()
                        scannedacts.extend(a.shadows)

                    if a.trail and a.trail not in self.actors:
                        # a.update_trail()
                        scannedacts.append(a.trail)
                        # trails may also have shadows:
                        if a.trail.shadows:
                            # a.trail.update_shadows()
                            scannedacts.extend(a.trail.shadows)

                    if a._caption and a._caption not in self.actors:
                        scannedacts.append(a._caption)

            elif isinstance(a, vtk.vtkActor2D):
                scannedacts.append(a)

            elif isinstance(a, vtk.vtkAssembly):
                scannedacts.append(a)
                if a.trail and a.trail not in self.actors:
                    scannedacts.append(a.trail)

            elif isinstance(a, (vedo.Volume, vedo.VolumeSlice)):
                scannedacts.append(a)

            elif isinstance(a, vtk.vtkImageData):
                scannedacts.append(vedo.Volume(a))

            elif isinstance(a, vedo.TetMesh):
                # check ugrid is all made of tets
                ugrid = a.inputdata()
                uarr = ugrid.GetCellTypesArray()
                celltypes = np.unique(utils.vtk2numpy(uarr))
                ncelltypes = len(celltypes)
                if ncelltypes > 1 or (ncelltypes == 1 and celltypes[0] != 10):
                    scannedacts.append(a.tomesh())
                else:
                    if not ugrid.GetPointData().GetScalars():
                        if not ugrid.GetCellData().GetScalars():
                            # add dummy array for vtkProjectedTetrahedraMapper to work:
                            a.celldata["DummyOneArray"] = np.ones(a.ncells)
                    scannedacts.append(a)

            elif isinstance(a, vedo.UGrid):
                scannedacts.append(a.tomesh())

            elif isinstance(a, vtk.vtkVolume):  # order matters! dont move above TetMesh
                vvol = vedo.Volume(a.GetMapper().GetInput())
                vprop = vtk.vtkVolumeProperty()
                vprop.DeepCopy(a.GetProperty())
                vvol.SetProperty(vprop)
                scannedacts.append(vvol)

            elif isinstance(a, str):
                # assume a 2D comment was given
                changed = False  # check if one already exists so to just update text
                if self.renderer:  # might be jupyter
                    acs = self.renderer.GetActors2D()
                    acs.InitTraversal()
                    for i in range(acs.GetNumberOfItems()):
                        act = acs.GetNextItem()
                        if isinstance(act, vedo.shapes.Text2D):
                            aposx, aposy = act.GetPosition()
                            if aposx < 0.01 and aposy > 0.99:  # "top-left"
                                act.text(a)  # update content! no appending nada
                                changed = True
                                break
                    if not changed:
                        out = vedo.shapes.Text2D(a)  # append a new one
                        scannedacts.append(out)

            elif isinstance(a, vtk.vtkImageActor):
                scannedacts.append(a)

            elif isinstance(a, vtk.vtkBillboardTextActor3D):
                scannedacts.append(a)

            elif isinstance(a, vtk.vtkLight):
                self.renderer.AddLight(a)

            elif isinstance(a, vtk.vtkMultiBlockDataSet):
                for i in range(a.GetNumberOfBlocks()):
                    b = a.GetBlock(i)
                    if isinstance(b, vtk.vtkPolyData):
                        scannedacts.append(vedo.Mesh(b))
                    elif isinstance(b, vtk.vtkImageData):
                        scannedacts.append(vedo.Volume(b))

            elif "PolyData" in str(type(a)):  # assume pyvista or vtkPolydata
                scannedacts.append(vedo.Mesh(a))

            elif "dolfin" in str(type(a)):  # assume a dolfin.Mesh object
                import vedo.dolfin as dlf
                scannedacts.append(dlf.MeshActor(a))

            elif "trimesh" in str(type(a)):
                scannedacts.append(utils.trimesh2vedo(a))

            elif "meshlab" in str(type(a)):
                if "MeshSet" in str(type(a)):
                    for i in range(a.number_meshes()):
                        if a.mesh_id_exists(i):
                            scannedacts.append(utils.meshlab2vedo(a.mesh(i)))
                else:
                    scannedacts.append(utils.meshlab2vedo(a))

            elif isinstance(a, (vtk.vtkProp, vtk.vtkInteractorObserver)):
                scannedacts.append(a)

            else:
                vedo.logger.error(f"cannot understand input in show(): {type(a)}")
        return scannedacts


    def show(
        self,
        *actors,
        at=None,
        axes=None,
        resetcam=None,
        zoom=False,
        interactive=None,
        viewup="",
        azimuth=0.0,
        elevation=0.0,
        roll=0.0,
        camera=None,
        mode=0,
        rate=None,
        bg=None,
        bg2=None,
        size=None,
        title=None,
    ):
        """
        Render a list of objects.

        Arguments:
            at : (int)
                number of the renderer to plot to, in case of more than one exists

            axes : (int)
                axis type-1 can be fully customized by passing a dictionary.
                Check `addons.Axes()` for the full list of options.
                set the type of axes to be shown:
                - 0,  no axes
                - 1,  draw three gray grid walls
                - 2,  show cartesian axes from (0,0,0)
                - 3,  show positive range of cartesian axes from (0,0,0)
                - 4,  show a triad at bottom left
                - 5,  show a cube at bottom left
                - 6,  mark the corners of the bounding box
                - 7,  draw a 3D ruler at each side of the cartesian axes
                - 8,  show the `vtkCubeAxesActor` object
                - 9,  show the bounding box outLine
                - 10, show three circles representing the maximum bounding box
                - 11, show a large grid on the x-y plane
                - 12, show polar axes
                - 13, draw a simple ruler at the bottom of the window

            azimuth/elevation/roll : (float)
                move camera accordingly the specified value

            viewup: str, list
                either `['x', 'y', 'z']` or a vector to set vertical direction

            resetcam : (bool)
                re-adjust camera position to fit objects

            camera : (dict, vtkCamera)
                camera parameters can further be specified with a dictionary
                assigned to the ``camera`` keyword (E.g. `show(camera={'pos':(1,2,3), 'thickness':1000,})`):
                - pos, `(list)`,  the position of the camera in world coordinates
                - focal_point `(list)`, the focal point of the camera in world coordinates
                - viewup `(list)`, the view up direction for the camera
                - distance `(float)`, set the focal point to the specified distance from the camera position.
                - clipping_range `(float)`, distance of the near and far clipping planes along the direction of projection.
                - parallel_scale `(float)`,
                scaling used for a parallel projection, i.e. the height of the viewport
                in world-coordinate distances. The default is 1. Note that the "scale" parameter works as
                an "inverse scale", larger numbers produce smaller images.
                This method has no effect in perspective projection mode.

                - thickness `(float)`,
                set the distance between clipping planes. This method adjusts the far clipping
                plane to be set a distance 'thickness' beyond the near clipping plane.

                - view_angle `(float)`,
                the camera view angle, which is the angular height of the camera view
                measured in degrees. The default angle is 30 degrees.
                This method has no effect in parallel projection mode.
                The formula for setting the angle up for perfect perspective viewing is:
                angle = 2*atan((h/2)/d) where h is the height of the RenderWindow
                (measured by holding a ruler up to your screen) and d is the distance
                from your eyes to the screen.

            interactive : (bool)
                pause and interact with window (True) or continue execution (False)

            rate : (float)
                maximum rate of `show()` in Hertz

            mode : (int, str)
                set the type of interaction:
                - 0 = TrackballCamera [default]
                - 1 = TrackballActor
                - 2 = JoystickCamera
                - 3 = JoystickActor
                - 4 = Flight
                - 5 = RubberBand2D
                - 6 = RubberBand3D
                - 7 = RubberBandZoom
                - 8 = Terrain
                - 9 = Unicam
                - 10 = Image
                - Check out `vedo.interaction_modes` for more options.
        """
        if self.wx_widget:
            return self

        if self.renderers:  # in case of notebooks

            if at is None:
                at = self.renderers.index(self.renderer)

            else:

                if at >= len(self.renderers):
                    t = f"trying to show(at={at}) but only {len(self.renderers)} renderers exist"
                    vedo.logger.error(t)
                    return self

                self.renderer = self.renderers[at]

        if title is not None:
            self.title = title

        if size is not None:
            self.size = size
            if self.size[0] == "f":  # full screen
                self.size = "fullscreen"
                self.window.SetFullScreen(True)
                self.window.BordersOn()
            else:
                self.window.SetSize(int(self.size[0]), int(self.size[1]))

        if settings.default_backend == "vtk":
            if str(bg).endswith(".hdr"):
                self._add_skybox(bg)
            else:
                if bg is not None:
                    self.backgrcol = vedo.get_color(bg)
                    self.renderer.SetBackground(self.backgrcol)
                if bg2 is not None:
                    self.renderer.GradientBackgroundOn()
                    self.renderer.SetBackground2(vedo.get_color(bg2))

        if axes is not None:
            if isinstance(axes, vedo.Assembly):  # user passing show(..., axes=myaxes)
                actors = list(actors)
                actors.append(axes)  # move it into the list of normal things to show
                axes = 0
            self.axes = axes

        if self.offscreen:
            interactive = False
            self._interactive = False

        # camera stuff
        if resetcam is not None:
            self.resetcam = resetcam

        if camera is not None:
            self.resetcam = False
            if isinstance(camera, vtk.vtkCamera):
                # see discussion #961
                cameracopy = vtk.vtkCamera()
                cameracopy.DeepCopy(camera)
                self.camera = cameracopy
            else:
                self.camera = utils.camera_from_dict(camera)
            if self.renderer:
                self.renderer.SetActiveCamera(self.camera)

        if self.renderer:
            self.camera = self.renderer.GetActiveCamera()

        self.add(actors)

        # Backend ###############################################################
        if settings.default_backend != "vtk":
            if settings.default_backend in ["k3d"]:
                return backends.get_notebook_backend(self.actors)
        #########################################################################

        for ia in utils.flatten(actors):
            if isinstance(ia, vedo.base.Base3DProp):
                try:
                    # fix gray color labels and title to white or black
                    ltc = np.array(ia.scalarbar.GetLabelTextProperty().GetColor())
                    if np.linalg.norm(ltc - (0.5, 0.5, 0.5)) / 3 < 0.05:
                        c = (0.9, 0.9, 0.9)
                        if np.sum(self.renderer.GetBackground()) > 1.5:
                            c = (0.1, 0.1, 0.1)
                        ia.scalarbar.GetLabelTextProperty().SetColor(c)
                        ia.scalarbar.GetTitleTextProperty().SetColor(c)
                except AttributeError:
                    pass

        if self.sharecam:
            for r in self.renderers:
                r.SetActiveCamera(self.camera)

        if self.qt_widget is not None:
            self.qt_widget.GetRenderWindow().AddRenderer(self.renderer)


        if self.axes is not None:
            if viewup != "2d" or self.axes in [1, 8] or isinstance(self.axes, dict):
                bns = self.renderer.ComputeVisiblePropBounds()
                addons.add_global_axes(self.axes, bounds=bns)

        # Backend ###############################################################
        if settings.default_backend in ["ipyvtk", "trame"]:
            return backends.get_notebook_backend()
        #########################################################################

        if self.resetcam:
            self.renderer.ResetCamera()

        if len(self.renderers) > 1:
            self.add_renderer_frame()

        if settings.default_backend == "2d" and not zoom:
            zoom = "tightest"

        if zoom:
            if zoom == "tight":
                self.reset_camera(tight=0.04)
            elif zoom == "tightest":
                self.reset_camera(tight=0.0001)
            else:
                self.camera.Zoom(zoom)
        if elevation:
            self.camera.Elevation(elevation)
        if azimuth:
            self.camera.Azimuth(azimuth)
        if roll:
            self.camera.Roll(roll)

        if len(viewup) > 0:
            b = self.renderer.ComputeVisiblePropBounds()
            cm = np.array([(b[1] + b[0]) / 2, (b[3] + b[2]) / 2, (b[5] + b[4]) / 2])
            sz = np.array([(b[1] - b[0]), (b[3] - b[2]), (b[5] - b[4])])
            if viewup == "x":
                sz = np.linalg.norm(sz)
                self.camera.SetViewUp([1, 0, 0])
                self.camera.SetPosition(cm + sz)
            elif viewup == "y":
                sz = np.linalg.norm(sz)
                self.camera.SetViewUp([0, 1, 0])
                self.camera.SetPosition(cm + sz)
            elif viewup == "z":
                sz = np.array([(b[1] - b[0]) * 0.7, -(b[3] - b[2]) * 1.0, (b[5] - b[4]) * 1.2])
                self.camera.SetViewUp([0, 0, 1])
                self.camera.SetPosition(cm + 2 * sz)
            elif utils.is_sequence(viewup):
                sz = np.linalg.norm(sz)
                self.camera.SetViewUp(viewup)
                cpos = np.cross([0, 1, 0], viewup)
                self.camera.SetPosition(cm - 2 * sz * cpos)

        self.renderer.ResetCameraClippingRange()

        if self.interactor and not self.interactor.GetInitialized():
            self.interactor.Initialize()
            self.interactor.RemoveObservers("CharEvent")

        if settings.immediate_rendering:
            self.window.Render()  ##################### <-------------- Render

        # 2d ####################################################################
        if settings.default_backend == "2d":
            return backends.get_notebook_backend()
        #########################################################################

        self.window.SetWindowName(self.title)

        try:
            # Needs "pip install pyobjc" on Mac OSX
            if (
                self._cocoa_initialized is False
                and "Darwin" in vedo.sys_platform
                and not self.offscreen
            ):
                self._cocoa_initialized = True
                from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps
                pid = os.getpid()
                x = NSRunningApplication.runningApplicationWithProcessIdentifier_(int(pid))
                x.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)
        except:
            pass
            # vedo.logger.debug("On Mac OSX try: pip install pyobjc")

        if self.interactor:  # can be offscreen..

            if interactive is not None:
                self._interactive = interactive

            self.user_mode(mode)

            if self._interactive:
                self.interactor.Start()
                
            if rate:
                if self.clock is None:  # set clock and limit rate
                    self._clockt0 = time.time()
                    self.clock = 0.0
                else:
                    t = time.time() - self._clockt0
                    elapsed = t - self.clock
                    mint = 1.0 / rate
                    if elapsed < mint:
                        time.sleep(mint - elapsed)
                    self.clock = time.time() - self._clockt0

        return self


    def add_inset(self, *actors, **options):
        """Add a draggable inset space into a renderer.

        Arguments:
            at : (int)
                specify the renderer number
            pos : (list)
                icon position in the range [1-4] indicating one of the 4 corners,
                or it can be a tuple (x,y) as a fraction of the renderer size.
            size : (float)
                size of the square inset
            draggable : (bool)
                if True the subrenderer space can be dragged around
            c : (color)
                color of the inset frame when dragged

        Examples:
            - [inset.py](https://github.com/marcomusy/vedo/tree/master/examples/other/inset.py)

            ![](https://user-images.githubusercontent.com/32848391/56758560-3c3f1300-6797-11e9-9b33-49f5a4876039.jpg)
        """
        if not self.interactor:
            return None
        pos = options.pop("pos", 0)
        size = options.pop("size", 0.1)
        c = options.pop("c", "lb")
        at = options.pop("at", None)
        draggable = options.pop("draggable", True)

        if not self.renderer:
            vedo.logger.warning("call add_inset() only after first rendering of the scene.")
            save_int = self._interactive
            self.show(interactive=0)
            self._interactive = save_int
        widget = vtk.vtkOrientationMarkerWidget()
        r, g, b = vedo.get_color(c)
        widget.SetOutlineColor(r, g, b)
        if len(actors) == 1:
            widget.SetOrientationMarker(actors[0])
        else:
            widget.SetOrientationMarker(vedo.Assembly(actors))

        widget.SetInteractor(self.interactor)

        if utils.is_sequence(pos):
            widget.SetViewport(pos[0] - size, pos[1] - size, pos[0] + size, pos[1] + size)
        else:
            if pos < 2:
                widget.SetViewport(0, 1 - 2 * size, size * 2, 1)
            elif pos == 2:
                widget.SetViewport(1 - 2 * size, 1 - 2 * size, 1, 1)
            elif pos == 3:
                widget.SetViewport(0, 0, size * 2, size * 2)
            elif pos == 4:
                widget.SetViewport(1 - 2 * size, 0, 1, size * 2)
        widget.EnabledOn()
        widget.SetInteractive(draggable)
        if at is not None and at < len(self.renderers):
            widget.SetCurrentRenderer(self.renderers[at])
        else:
            widget.SetCurrentRenderer(self.renderer)
        self.widgets.append(widget)
        return widget

    def clear(self, at=None, deep=False):
        """Clear the scene from all meshes and volumes."""
        if at is not None:
            renderer = self.renderers[at]
        else:
            renderer = self.renderer
        if not renderer:
            return self

        if deep:
            renderer.RemoveAllViewProps()
        else:
            for a in set(self.get_meshes() + self.get_volumes() + self.actors + self.axes_instances):
                if isinstance(a, vedo.shapes.Text2D):
                    continue
                self.remove(a)
                try:
                    if a.scalarbar:
                        self.remove(a.scalarbar)
                except AttributeError:
                    pass
            self.actors = []
        return self

    def break_interaction(self):
        """Break window interaction and return to the python execution flow"""
        if self.interactor:
            self.interactor.ExitCallback()
        return self

    def user_mode(self, mode):
        """
        Modify the user interaction mode.

        Examples:
            ```python
            from vedo import *
            mode = interactor_modes.MousePan()
            mesh = Mesh(dataurl+"cow.vtk")
            plt = Plotter().user_mode(mode)
            plt.show(mesh, axes=1)
           ```
        See also:
        [interactors](https://vtk.org/doc/nightly/html/classvtkInteractorStyle.html)
        """
        if not self.interactor:
            return None

        if isinstance(mode, (str, int)):
            # Set the style of interaction
            # see https://vtk.org/doc/nightly/html/classvtkInteractorStyle.html
            if mode in (0, "TrackballCamera"):
                if self.qt_widget:
                    self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
            elif mode in (1, "TrackballActor"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballActor())
            elif mode in (2, "JoystickCamera"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleJoystickCamera())
            elif mode in (3, "JoystickActor"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleJoystickActor())
            elif mode in (4, "Flight"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleFlight())
            elif mode in (5, "RubberBand2D"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleRubberBand2D())
            elif mode in (6, "RubberBand3D"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleRubberBand3D())
            elif mode in (7, "RubberBandZoom"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleRubberBandZoom())
            elif mode in (8, "Terrain"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleTerrain())
            elif mode in (9, "Unicam"):
                self.interactor.SetInteractorStyle(vtk.vtkInteractorStyleUnicam())
            elif mode in (10, "Image", "image", "2d"):
                astyle = vtk.vtkInteractorStyleImage()
                astyle.SetInteractionModeToImage3D()
                self.interactor.SetInteractorStyle(astyle)
            else:
                vedo.logger.warning(f"Unknown interaction mode: {mode}")

        elif isinstance(mode, vtk.vtkInteractorStyleUser):
            # set a custom interactor style
            mode.interactor = self.interactor
            mode.renderer = self.renderer
            mode.SetInteractor(self.interactor)
            mode.SetDefaultRenderer(self.renderer)
            self.interactor.SetInteractorStyle(mode)

        return self

    def close_window(self):
        """Close the current or the input rendering window.

        Examples:
            - [closewindow.py](https://github.com/marcomusy/vedo/tree/master/examples/basic/closewindow.py)
        """
        vedo.last_figure = None
        self.sliders = []
        self.buttons = []
        self.widgets = []
        self.hover_legends = []
        self.background_renderer = None
        self._extralight = None

        self.hint_widget = None
        self.cutter_widget = None

        for r in self.renderers:
            r.RemoveAllObservers()
        if hasattr(self, "window") and self.window:
            if hasattr(self, "interactor") and self.interactor:
                self.interactor.ExitCallback()
                try:
                    self.interactor.SetDone(True)
                except AttributeError:
                    pass
                self.interactor.TerminateApp()

                # self.interactor = None
            self.window.Finalize()  # this must be done here

            if hasattr(self, "interactor") and self.interactor:
                if "Darwin" in vedo.sys_platform:
                    try:
                        self.interactor.ProcessEvents()
                    except:
                        pass
                self.interactor = None

            self.window = None

        self.renderer = None  # current renderer
        self.renderers = []
        self.camera = None
        self.skybox = None
        return self

    def close(self):
        """Close the Plotter instance and release resources."""
        self.close_window()
        self.actors = []
        if vedo.plotter_instance == self:
            vedo.plotter_instance = None

    def screenshot(self, filename="screenshot.png", scale=1, asarray=False):
        """
        Take a screenshot of the Plotter window.

        Arguments:
            scale : (int)
                set image magnification as an integer multiplicating factor
            asarray : (bool)
                return a numpy array of the image instead of writing a file
        """
        return vedo.file_io.screenshot(filename, scale, asarray)

    def topicture(self, scale=1):
        """
        Generate a Picture object from the current rendering window.

        Arguments:
            scale : (int)
                set image magnification as an integer multiplicating factor
        """
        if settings.screeshot_large_image:
            w2if = vtk.vtkRenderLargeImage()
            w2if.SetInput(self.renderer)
            w2if.SetMagnification(scale)
        else:
            w2if = vtk.vtkWindowToImageFilter()
            w2if.SetInput(self.window)
            if hasattr(w2if, "SetScale"):
                w2if.SetScale(scale, scale)
            if settings.screenshot_transparent_background:
                w2if.SetInputBufferTypeToRGBA()
            w2if.ReadFrontBufferOff()  # read from the back buffer
        w2if.Update()
        return vedo.picture.Picture(w2if.GetOutput())

    def export(self, filename="scene.npz", binary=False):
        """
        Export scene to file to HTML, X3D or Numpy file.

        Examples:
            - [export_x3d.py](https://github.com/marcomusy/vedo/tree/master/examples/other/export_x3d.py)
            - [export_numpy.py](https://github.com/marcomusy/vedo/tree/master/examples/other/export_numpy.py)
        """
        vedo.file_io.export_window(filename, binary=binary)
        return self

    def color_picker(self, xy, verbose=False):
        """Pick color of specific (x,y) pixel on the screen."""
        w2if = vtk.vtkWindowToImageFilter()
        w2if.SetInput(self.window)
        w2if.ReadFrontBufferOff()
        w2if.Update()
        nx, ny = self.window.GetSize()
        varr = w2if.GetOutput().GetPointData().GetScalars()

        arr = utils.vtk2numpy(varr).reshape(ny, nx, 3)
        x, y = int(xy[0]), int(xy[1])
        if y < ny and x < nx:

            rgb = arr[y, x]

            if verbose:
                vedo.printc(":rainbow:Pixel", [x, y], "has RGB[", end="")
                vedo.printc("█", c=[rgb[0], 0, 0], end="")
                vedo.printc("█", c=[0, rgb[1], 0], end="")
                vedo.printc("█", c=[0, 0, rgb[2]], end="")
                vedo.printc("] = ", end="")
                cnm = vedo.get_color_name(rgb)
                if np.sum(rgb) < 150:
                    vedo.printc(
                        rgb.tolist(),
                        vedo.colors.rgb2hex(np.array(rgb) / 255),
                        c="w",
                        bc=rgb,
                        invert=1,
                        end="",
                    )
                    vedo.printc("  -> " + cnm, invert=1, c="w")
                else:
                    vedo.printc(
                        rgb.tolist(), vedo.colors.rgb2hex(np.array(rgb) / 255), c=rgb, end=""
                    )
                    vedo.printc("  -> " + cnm, c=cnm)

            return rgb

        return None

    #######################################################################
    def _mouseleftclick(self, iren, event):

        x, y = iren.GetEventPosition()

        renderer = iren.FindPokedRenderer(x, y)
        picker = vtk.vtkPropPicker()
        picker.PickProp(x, y, renderer)

        self.renderer = renderer

        clicked_actor = picker.GetActor()
        # clicked_actor2D = picker.GetActor2D()

        # print('_mouseleftclick mouse at', x, y)
        # print("picked Volume:",   [picker.GetVolume()])
        # print("picked Actor2D:",  [picker.GetActor2D()])
        # print("picked Assembly:", [picker.GetAssembly()])
        # print("picked Prop3D:",   [picker.GetProp3D()])

        if not clicked_actor:
            clicked_actor = picker.GetAssembly()

        if not clicked_actor:
            clicked_actor = picker.GetProp3D()

        if not hasattr(clicked_actor, "GetPickable") or not clicked_actor.GetPickable():
            return

        self.picked3d = picker.GetPickPosition()
        self.picked2d = np.array([x, y])

        if not clicked_actor:
            return

        self.justremoved = None

        self.clicked_actor = clicked_actor
        if hasattr(clicked_actor, "picked3d"):  # might be not a vedo obj
            clicked_actor.picked3d = picker.GetPickPosition()
            x, y = iren.GetEventPosition()

        # -----------
        if "Histogram1D" in picker.GetAssembly().__class__.__name__:
            histo = picker.GetAssembly()
            if histo.verbose:
                x = self.picked3d[0]
                idx = np.digitize(x, histo.edges) - 1
                f = histo.frequencies[idx]
                cn = histo.centers[idx]
                vedo.colors.printc(f"{histo.name}, bin={idx}, center={cn}, value={f}")


    #######################################################################
    def _keypress(self, iren, event):

        # NB: qt creates and passes a vtkGenericRenderWindowInteractor

        key = iren.GetKeySym()

        if "_L" in key or "_R" in key:
            return

        if iren.GetShiftKey():
            key = key.upper()

        if iren.GetControlKey():
            key = "Ctrl+" + key

        if iren.GetAltKey():
            key = "Alt+" + key

        # utils.vedo.printc('Pressed key:', key, c='y', box='-')
        # print(key, iren.GetShiftKey(), iren.GetAltKey(), iren.GetControlKey(),
        #       iren.GetKeyCode(), iren.GetRepeatCount())
        # iren.ExitCallback()
        # return

        x, y = iren.GetEventPosition()
        renderer = iren.FindPokedRenderer(x, y)

        if key in ["q", "Ctrl+q", "Ctrl+w", "Escape"]:
            iren.ExitCallback()
            return

        elif key == "F1":
            vedo.logger.info("Execution aborted. Exiting python kernel now.")
            iren.ExitCallback()
            sys.exit(0)

        elif key == "Down":
            if self.clicked_actor in self.get_meshes():
                self.clicked_actor.GetProperty().SetOpacity(0.02)
                bfp = self.clicked_actor.GetBackfaceProperty()
                if bfp and hasattr(self.clicked_actor, "_bfprop"):
                    self.clicked_actor._bfprop = bfp  # save it
                    self.clicked_actor.SetBackfaceProperty(None)
            else:
                for a in self.get_meshes():
                    a.GetProperty().SetOpacity(0.02)
                    bfp = a.GetBackfaceProperty()
                    if bfp and hasattr(a, "_bfprop"):
                        a._bfprop = bfp
                        a.SetBackfaceProperty(None)

        elif key == "Left":
            if self.clicked_actor in self.get_meshes():
                ap = self.clicked_actor.GetProperty()
                aal = max([ap.GetOpacity() * 0.75, 0.01])
                ap.SetOpacity(aal)
                bfp = self.clicked_actor.GetBackfaceProperty()
                if bfp and hasattr(self.clicked_actor, "_bfprop"):
                    self.clicked_actor._bfprop = bfp
                    self.clicked_actor.SetBackfaceProperty(None)
            else:
                for a in self.get_meshes():
                    ap = a.GetProperty()
                    aal = max([ap.GetOpacity() * 0.75, 0.01])
                    ap.SetOpacity(aal)
                    bfp = a.GetBackfaceProperty()
                    if bfp and hasattr(a, "_bfprop"):
                        a._bfprop = bfp
                        a.SetBackfaceProperty(None)

        elif key == "Right":
            if self.clicked_actor in self.get_meshes():
                ap = self.clicked_actor.GetProperty()
                aal = min([ap.GetOpacity() * 1.25, 1.0])
                ap.SetOpacity(aal)
                if (
                    aal == 1
                    and hasattr(self.clicked_actor, "_bfprop")
                    and self.clicked_actor._bfprop
                ):
                    # put back
                    self.clicked_actor.SetBackfaceProperty(self.clicked_actor._bfprop)
            else:
                for a in self.get_meshes():
                    ap = a.GetProperty()
                    aal = min([ap.GetOpacity() * 1.25, 1.0])
                    ap.SetOpacity(aal)
                    if aal == 1 and hasattr(a, "_bfprop") and a._bfprop:
                        a.SetBackfaceProperty(a._bfprop)

        elif key in ("slash", "Up"):
            if self.clicked_actor in self.get_meshes():
                self.clicked_actor.GetProperty().SetOpacity(1)
                if hasattr(self.clicked_actor, "_bfprop") and self.clicked_actor._bfprop:
                    self.clicked_actor.SetBackfaceProperty(self.clicked_actor._bfprop)
            else:
                for a in self.get_meshes():
                    a.GetProperty().SetOpacity(1)
                    if hasattr(a, "_bfprop") and a._bfprop:
                        a.SetBackfaceProperty(a._bfprop)

        elif key == "P":
            if self.clicked_actor in self.get_meshes():
                acts = [self.clicked_actor]
            else:
                acts = self.get_meshes()
            for ia in acts:
                try:
                    ps = ia.GetProperty().GetPointSize()
                    if ps > 1:
                        ia.GetProperty().SetPointSize(ps - 1)
                    ia.GetProperty().SetRepresentationToPoints()
                except AttributeError:
                    pass

        elif key == "U":
            pval = renderer.GetActiveCamera().GetParallelProjection()
            renderer.GetActiveCamera().SetParallelProjection(not pval)
            if pval:
                renderer.ResetCamera()

        elif key == "p":
            if self.clicked_actor in self.get_meshes():
                acts = [self.clicked_actor]
            else:
                acts = self.get_meshes()
            for ia in acts:
                try:
                    ps = ia.GetProperty().GetPointSize()
                    ia.GetProperty().SetPointSize(ps + 2)
                    ia.GetProperty().SetRepresentationToPoints()
                except AttributeError:
                    pass

        elif key == "w":
            if self.clicked_actor and self.clicked_actor in self.get_meshes():
                self.clicked_actor.GetProperty().SetRepresentationToWireframe()
            else:
                for a in self.get_meshes():
                    if a.GetProperty().GetRepresentation() == 1:  # toggle
                        a.GetProperty().SetRepresentationToSurface()
                    else:
                        a.GetProperty().SetRepresentationToWireframe()

        elif key == "r":
            renderer.ResetCamera()

        elif key == "h":
            msg = (
                "  ============================================================\n"
                " | Press: i     print info about selected object              |\n"
                " |        I     print the RGB color under the mouse           |\n"
                " |        y     show the pipeline for this object as a graph  |\n"
                " |        <-->  use arrows to reduce/increase opacity         |\n"
                " |        w/s   toggle wireframe/surface style                |\n"
                " |        p/P   change point size of vertices                 |\n"
                " |        l     toggle edges visibility                       |\n"
                " |        x     toggle mesh visibility                        |\n"
                " |        X     invoke a cutter widget tool                   |\n"
                " |        1-3   change mesh color                             |\n"
                " |        4     use data array as colors, if present          |\n"
                " |        5-6   change background color(s)                    |\n"
                " |        09+-  (on keypad) or +/- to cycle axes style        |\n"
                " |        k     cycle available lighting styles               |\n"
                " |        K     cycle available shading styles                |\n"
                " |        A     toggle anti-aliasing                          |\n"
                " |        D     toggle depth-peeling (for transparencies)     |\n"
                " |        o/O   add/remove light to scene and rotate it       |\n"
                " |        n     show surface mesh normals                     |\n"
                " |        a     toggle interaction to Actor Mode              |\n"
                " |        j     toggle interaction to Joystick Mode           |\n"
                " |        U     toggle perspective/parallel projection        |\n"
                " |        r     reset camera position                         |\n"
                " |        R     reset camera orientation to orthogonal view   |\n"
                " |        .     fly camera towards last clicked point         |\n"
                " |        C     print current camera settings                 |\n"
                " |        S     save a screenshot                             |\n"
                " |        E/F   export 3D scene to numpy file or X3D          |\n"
                " |        q     return control to python script               |\n"
                " |        Esc   abort execution and exit python kernel        |\n"
                " |------------------------------------------------------------|\n"
                " | Mouse: Left-click    rotate scene / pick actors            |\n"
                " |        Middle-click  pan scene                             |\n"
                " |        Right-click   zoom scene in or out                  |\n"
                " |        Cntrl-click   rotate scene                          |\n"
                " |------------------------------------------------------------|\n"
                " |   Check out the documentation at:  https://vedo.embl.es    |\n"
                "  ============================================================"
            )
            vedo.printc(msg, dim=True)

            msg = " vedo " + vedo.__version__ + " "
            vedo.printc(msg, invert=True, dim=True, end="")
            vtkVers = vtk.vtkVersion().GetVTKVersion()
            msg = "| vtk " + str(vtkVers)
            msg += " | numpy " + str(np.__version__)
            msg += " | python " + str(sys.version_info[0]) + "." + str(sys.version_info[1])
            vedo.printc(msg, invert=False, dim=True)
            return

        elif key == "a":
            iren.ExitCallback()
            cur = iren.GetInteractorStyle()
            if isinstance(cur, vtk.vtkInteractorStyleTrackballCamera):
                msg = "\nInteractor style changed to TrackballActor\n"
                msg += "  you can now move and rotate individual meshes:\n"
                msg += "  press X twice to save the repositioned mesh\n"
                msg += "  press 'a' to go back to normal style"
                vedo.printc(msg)
                iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballActor())
            else:
                iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
            iren.Start()
            return

        elif key == "A":  # toggle antialiasing
            msam = self.window.GetMultiSamples()
            if not msam:
                self.window.SetMultiSamples(8)
            else:
                self.window.SetMultiSamples(0)
            msam = self.window.GetMultiSamples()
            if msam:
                vedo.printc(f"Antialiasing is now set to {msam} samples", c=bool(msam))
            else:
                vedo.printc("Antialiasing is now disabled", c=bool(msam))

        elif key == "D":  # toggle depthpeeling
            udp = not renderer.GetUseDepthPeeling()
            renderer.SetUseDepthPeeling(udp)
            # self.renderer.SetUseDepthPeelingForVolumes(udp)
            # print(self.window.GetAlphaBitPlanes())
            if udp:
                self.window.SetAlphaBitPlanes(1)
                renderer.SetMaximumNumberOfPeels(settings.max_number_of_peels)
                renderer.SetOcclusionRatio(settings.occlusion_ratio)
            self.interactor.Render()
            wasUsed = renderer.GetLastRenderingUsedDepthPeeling()
            rnr = self.renderers.index(renderer)
            vedo.printc(f"Depth peeling is now set to {udp} for renderer nr.{rnr}", c=udp)
            if not wasUsed and udp:
                vedo.printc("\t...but last rendering did not actually used it!", c=udp, invert=True)
            return

        elif key == "j":
            iren.ExitCallback()
            cur = iren.GetInteractorStyle()
            if isinstance(cur, vtk.vtkInteractorStyleJoystickCamera):
                iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
            else:
                vedo.printc("\nInteractor style changed to Joystick,", end="")
                vedo.printc(" press j to go back to normal.")
                iren.SetInteractorStyle(vtk.vtkInteractorStyleJoystickCamera())
            iren.Start()
            return

        elif key == "period":
            if self.picked3d:
                self.fly_to(self.picked3d)
            return

        elif key == "S":
            vedo.file_io.screenshot("screenshot.png")
            vedo.printc(r":camera: Saved rendering window to 'screenshot.png'", c="b")
            return

        elif key == "C":
            # Precision needs to be 7 (or even larger) to guarantee a consistent camera when
            #   the model coordinates are not centered at (0, 0, 0) and the mode is large.
            # This could happen for plotting geological models with UTM coordinate systems
            cam = renderer.GetActiveCamera()
            vedo.printc("\n###################################################", c="y")
            vedo.printc("## Template python code to position this camera: ##", c="y")
            vedo.printc("cam = dict(", c="y")
            vedo.printc("    position=" + utils.precision(cam.GetPosition(), 6) + ",", c="y")
            vedo.printc("    focal_point=" + utils.precision(cam.GetFocalPoint(), 6) + ",", c="y")
            vedo.printc("    viewup=" + utils.precision(cam.GetViewUp(), 6) + ",", c="y")
            if settings.use_parallel_projection:
                vedo.printc('    parallel_scale='+utils.precision(cam.GetParallelScale(),6)+',', c='y')
            else:
                vedo.printc('    distance='     +utils.precision(cam.GetDistance(),6)+',', c='y')
            vedo.printc('    clipping_range='+utils.precision(cam.GetClippingRange(),6)+',', c='y')
            vedo.printc(')', c='y')
            vedo.printc('show(mymeshes, camera=cam)', c='y')
            vedo.printc('###################################################', c='y')
            return

        elif key == "R":
            self.reset_viewup()

        elif key == "s":
            if self.clicked_actor and self.clicked_actor in self.get_meshes():
                self.clicked_actor.GetProperty().SetRepresentationToSurface()
            else:
                for a in self.get_meshes():
                    a.GetProperty().SetRepresentationToSurface()

        elif key == "1":
            self._icol += 1
            if isinstance(self.clicked_actor, vedo.Points):
                self.clicked_actor.GetMapper().ScalarVisibilityOff()
                pal = vedo.colors.palettes[settings.palette % len(vedo.colors.palettes)]
                self.clicked_actor.GetProperty().SetColor(pal[(self._icol) % 10])

        elif key == "2":
            self._icol += 1
            settings.palette += 1
            settings.palette = settings.palette % len(vedo.colors.palettes)
            if isinstance(self.clicked_actor, vedo.Points):
                self.clicked_actor.GetMapper().ScalarVisibilityOff()
                pal = vedo.colors.palettes[settings.palette % len(vedo.colors.palettes)]
                self.clicked_actor.GetProperty().SetColor(pal[(self._icol) % 10])

        elif key == "3":
            bsc = ["b5", "cyan5", "g4", "o5", "p5", "r4", "teal4", "yellow4"]
            self._icol += 1
            if isinstance(self.clicked_actor, vedo.Points):
                self.clicked_actor.GetMapper().ScalarVisibilityOff()
                self.clicked_actor.GetProperty().SetColor(vedo.get_color(bsc[(self._icol) % len(bsc)]))

        elif key == "4":
            if self.clicked_actor:
                acts = [self.clicked_actor]
            else:
                acts = self.get_meshes()
            for ia in acts:
                if not hasattr(ia, "_cmap_name"):
                    continue
                cmap_name = ia._cmap_name
                if not cmap_name:
                    cmap_name = "rainbow"
                if isinstance(ia, vedo.pointcloud.Points):
                    arnames = ia.pointdata.keys()
                    if len(arnames) > 0:
                        arnam = arnames[ia._scals_idx]
                        if arnam and ("normals" not in arnam.lower()):  # exclude normals
                            ia.cmap(cmap_name, arnam, on="points")
                            vedo.printc("..active point data set to:", arnam, c="g", bold=0)
                            ia._scals_idx += 1
                            if ia._scals_idx >= len(arnames):
                                ia._scals_idx = 0
                    else:
                        arnames = ia.celldata.keys()
                        if len(arnames) > 0:
                            arnam = arnames[ia._scals_idx]
                            if arnam and ("normals" not in arnam.lower()):  # exclude normals
                                ia.cmap(cmap_name, arnam, on="cells")
                                vedo.printc("..active cell array set to:", arnam, c="g", bold=0)
                                ia._scals_idx += 1
                                if ia._scals_idx >= len(arnames):
                                    ia._scals_idx = 0

        elif key == "5":
            bgc = np.array(renderer.GetBackground()).sum() / 3
            if bgc <= 0:
                bgc = 0.223
            elif 0 < bgc < 1:
                bgc = 1
            else:
                bgc = 0
            renderer.SetBackground(bgc, bgc, bgc)

        elif key == "6":
            bg2cols = [
                "lightyellow",
                "darkseagreen",
                "palegreen",
                "steelblue",
                "lightblue",
                "cadetblue",
                "lavender",
                "white",
                "blackboard",
                "black",
            ]
            bg2name = vedo.get_color_name(renderer.GetBackground2())
            if bg2name in bg2cols:
                idx = bg2cols.index(bg2name)
            else:
                idx = 4
            if idx is not None:
                bg2name_next = bg2cols[(idx + 1) % (len(bg2cols) - 1)]
            if not bg2name_next:
                renderer.GradientBackgroundOff()
            else:
                renderer.GradientBackgroundOn()
                renderer.SetBackground2(vedo.get_color(bg2name_next))

        elif key in ["plus", "equal", "KP_Add", "minus", "KP_Subtract"]:  # cycle axes style
            clickedr = self.renderers.index(renderer)
            if self.axes_instances[clickedr]:
                if hasattr(self.axes_instances[clickedr], "EnabledOff"):  # widget
                    self.axes_instances[clickedr].EnabledOff()
                else:
                    try:
                        renderer.RemoveActor(self.axes_instances[clickedr])
                    except:
                        pass
                self.axes_instances[clickedr] = None
            if not self.axes:
                self.axes = 0
            if isinstance(self.axes, dict):
                self.axes = 1
            if key in ["minus", "KP_Subtract"]:
                if not settings.use_parallel_projection and self.axes == 0:
                    self.axes -= 1  # jump ruler doesnt make sense in perspective mode
                bns = self.renderer.ComputeVisiblePropBounds()
                addons.add_global_axes(axtype=(self.axes - 1) % 15, c=None, bounds=bns)
            else:
                if not settings.use_parallel_projection and self.axes == 12:
                    self.axes += 1  # jump ruler doesnt make sense in perspective mode
                bns = self.renderer.ComputeVisiblePropBounds()
                addons.add_global_axes(axtype=(self.axes + 1) % 15, c=None, bounds=bns)
            self.interactor.Render()

        elif "KP_" in key or key in [
            "Insert",
            "End",
            "Down",
            "Next",
            "Left",
            "Begin",
            "Right",
            "Home",
            "Up",
            "Prior",
        ]:
            # change axes style
            asso = {
                "KP_Insert": 0,
                "KP_0": 0,
                "KP_End": 1,
                "KP_1": 1,
                "KP_Down": 2,
                "KP_2": 2,
                "KP_Next": 3,
                "KP_3": 3,
                "KP_Left": 4,
                "KP_4": 4,
                "KP_Begin": 5,
                "KP_5": 5,
                "KP_Right": 6,
                "KP_6": 6,
                "KP_Home": 7,
                "KP_7": 7,
                "KP_Up": 8,
                "KP_8": 8,
                "Prior": 9,  # on windows OS
                "Insert": 0,
                "End": 1,
                "Down": 2,
                "Next": 3,
                "Left": 4,
                "Begin": 5,
                "Right": 6,
                "Home": 7,
                "Up": 8,
                "Prior": 9,
            }
            clickedr = self.renderers.index(renderer)
            if key in asso:
                if self.axes_instances[clickedr]:
                    if hasattr(self.axes_instances[clickedr], "EnabledOff"):  # widget
                        self.axes_instances[clickedr].EnabledOff()
                    else:
                        try:
                            renderer.RemoveActor(self.axes_instances[clickedr])
                        except:
                            pass
                    self.axes_instances[clickedr] = None
                bounds = renderer.ComputeVisiblePropBounds()
                addons.add_global_axes(axtype=asso[key], c=None, bounds=bounds)
                self.interactor.Render()

        if key == "O":
            renderer.RemoveLight(self._extralight)
            self._extralight = None

        elif key == "o":
            vbb, sizes, _, _ = addons.compute_visible_bounds()
            cm = utils.vector((vbb[0] + vbb[1]) / 2, (vbb[2] + vbb[3]) / 2, (vbb[4] + vbb[5]) / 2)
            if not self._extralight:
                vup = renderer.GetActiveCamera().GetViewUp()
                pos = cm + utils.vector(vup) * utils.mag(sizes)
                self._extralight = addons.Light(pos, focal_point=cm)
                renderer.AddLight(self._extralight)
                print("Press again o to rotate light source, or O to remove it.")
            else:
                cpos = utils.vector(self._extralight.GetPosition())
                x, y, z = self._extralight.GetPosition() - cm
                r, th, ph = utils.cart2spher(x, y, z)
                th += 0.2
                if th > np.pi:
                    th = np.random.random() * np.pi / 2
                ph += 0.3
                cpos = utils.spher2cart(r, th, ph) + cm
                self._extralight.SetPosition(cpos)

            self.window.Render()

        elif key == "l":
            if self.clicked_actor in self.get_meshes():
                acts = [self.clicked_actor]
            else:
                acts = self.get_meshes()
            for ia in acts:
                try:
                    ev = ia.GetProperty().GetEdgeVisibility()
                    ia.GetProperty().SetEdgeVisibility(not ev)
                    ia.GetProperty().SetRepresentationToSurface()
                    ia.GetProperty().SetLineWidth(0.1)
                except AttributeError:
                    pass

        elif key == "k":  # lightings
            if self.clicked_actor in self.get_meshes():
                acts = [self.clicked_actor]
            else:
                acts = self.get_meshes()
            shds = ("default", "metallic", "plastic", "shiny", "glossy", "off")
            for ia in acts:
                try:
                    lnr = (ia._ligthingnr + 1) % 6
                    ia.lighting(shds[lnr])
                    ia._ligthingnr = lnr
                except AttributeError:
                    pass

        elif key == "K":  # shading
            if self.clicked_actor in self.get_meshes():
                acts = [self.clicked_actor]
            else:
                acts = self.get_meshes()
            for ia in acts:
                if isinstance(ia, vedo.Mesh):
                    ia.compute_normals(cells=False)
                    intrp = ia.GetProperty().GetInterpolation()
                    # print(intrp, ia.GetProperty().GetInterpolationAsString())
                    if intrp > 0:
                        ia.GetProperty().SetInterpolation(0)  # flat
                    else:
                        ia.GetProperty().SetInterpolation(2)  # phong

        elif key == "n":  # show normals to an actor
            if self.clicked_actor in self.get_meshes():
                if self.clicked_actor.GetPickable():
                    self.renderer.AddActor(vedo.shapes.NormalLines(self.clicked_actor))
                    iren.Render()
            else:
                print("Click an actor and press n to add normals.")

        elif key == "x":
            if self.justremoved is None:
                if self.clicked_actor in self.get_meshes() or isinstance(
                    self.clicked_actor, vtk.vtkAssembly
                ):
                    self.justremoved = self.clicked_actor
                    self.renderer.RemoveActor(self.clicked_actor)
            else:
                self.renderer.AddActor(self.justremoved)
                self.renderer.Render()
                self.justremoved = None

        elif key == "X":
            if self.clicked_actor:
                if not self.cutter_widget:
                    self.cutter_widget = addons.BoxCutter(self.clicked_actor)
                    self.add(self.cutter_widget)
                    print("Press Shift+X to close the cutter box widget, Ctrl+s to save the cut section.")
                else:
                    self.remove(self.cutter_widget)
                    self.cutter_widget = None
            else:
                for a in self.actors:
                    if isinstance(a, vtk.vtkVolume):
                        addons.add_cutter_tool(a)
                        return

                vedo.printc("Click object and press X to open the cutter box widget.", c=4)

        elif key == "E":
            vedo.printc(r":camera: Exporting 3D window to file", c="blue", end="")
            vedo.file_io.export_window("scene.npz")
            vedo.printc(". Try:\n> vedo scene.npz", c="blue")

        elif key == "F":
            vedo.file_io.export_window("scene.x3d")
            vedo.printc(":idea: Try: firefox scene.html", c="blue")

        elif key == "i":  # print info
            if self.clicked_actor:
                utils.print_info(self.clicked_actor)
            else:
                utils.print_info(self)

        elif key == "I":  # print color under the mouse
            x, y = iren.GetEventPosition()
            self.color_picker([x, y], verbose=True)

        elif key == "y":
            if self.clicked_actor and self.clicked_actor.pipeline:
                # self.clicked_actor.pipeline =  utils.OperationNode(
                #         "show", parents=[self.clicked_actor],
                #         shape="circle",
                # )
                self.clicked_actor.pipeline.show()

        if iren:
            iren.Render()
