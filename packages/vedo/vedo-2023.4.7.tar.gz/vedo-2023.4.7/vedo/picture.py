#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

try:
    import vedo.vtkclasses as vtk
except ImportError:
    import vtkmodules.all as vtk

import vedo
from vedo import colors
from vedo import utils

__docformat__ = "google"

__doc__ = """
Submodule to work with common format images.

![](https://vedo.embl.es/images/basic/rotateImage.png)
"""

__all__ = ["Picture", "Picture2D"]


#################################################
def _get_img(obj, flip=False, translate=()):
    # get vtkImageData from numpy array or filename

    if isinstance(obj, str):
        if "https://" in obj:
            obj = vedo.file_io.download(obj, verbose=False)

        fname = obj.lower()
        if fname.endswith(".png"):
            picr = vtk.vtkPNGReader()
        elif fname.endswith(".jpg") or fname.endswith(".jpeg"):
            picr = vtk.vtkJPEGReader()
        elif fname.endswith(".bmp"):
            picr = vtk.vtkBMPReader()
        elif fname.endswith(".tif") or fname.endswith(".tiff"):
            picr = vtk.vtkTIFFReader()
            picr.SetOrientationType(vedo.settings.tiff_orientation_type)
        else:
            colors.printc("Cannot understand picture format", obj, c="r")
            return
        picr.SetFileName(obj)
        picr.Update()
        img = picr.GetOutput()

    else:
        obj = np.asarray(obj)

        if obj.ndim == 3:  # has shape (nx,ny, ncolor_alpha_chan)
            iac = vtk.vtkImageAppendComponents()
            nchan = obj.shape[2]  # get number of channels in inputimage (L/LA/RGB/RGBA)
            for i in range(nchan):
                if flip:
                    arr = np.flip(np.flip(obj[:, :, i], 0), 0).ravel()
                else:
                    arr = np.flip(obj[:, :, i], 0).ravel()
                arr = np.clip(arr, 0, 255)
                varb = utils.numpy2vtk(arr, dtype=np.uint8, name="RGBA")
                imgb = vtk.vtkImageData()
                imgb.SetDimensions(obj.shape[1], obj.shape[0], 1)
                imgb.GetPointData().AddArray(varb)
                imgb.GetPointData().SetActiveScalars("RGBA")
                iac.AddInputData(imgb)
            iac.Update()
            img = iac.GetOutput()

        elif obj.ndim == 2:  # black and white
            if flip:
                arr = np.flip(obj[:, :], 0).ravel()
            else:
                arr = obj.ravel()
            arr = np.clip(arr, 0, 255)
            varb = utils.numpy2vtk(arr, dtype=np.uint8, name="RGBA")
            img = vtk.vtkImageData()
            img.SetDimensions(obj.shape[1], obj.shape[0], 1)

            img.GetPointData().AddArray(varb)
            img.GetPointData().SetActiveScalars("RGBA")

    if len(translate) > 0:
        translate_extent = vtk.vtkImageTranslateExtent()
        translate_extent.SetTranslation(-translate[0], -translate[1], 0)
        translate_extent.SetInputData(img)
        translate_extent.Update()
        img.DeepCopy(translate_extent.GetOutput())

    return img


def _set_justification(img, pos):

    if not isinstance(pos, str):
        return img, pos

    sx, sy = img.GetDimensions()[:2]
    translate = ()
    if "top" in pos:
        if "left" in pos:
            pos = (0, 1)
            translate = (0, sy)
        elif "right" in pos:
            pos = (1, 1)
            translate = (sx, sy)
        elif "mid" in pos or "cent" in pos:
            pos = (0.5, 1)
            translate = (sx / 2, sy)
    elif "bottom" in pos:
        if "left" in pos:
            pos = (0, 0)
        elif "right" in pos:
            pos = (1, 0)
            translate = (sx, 0)
        elif "mid" in pos or "cent" in pos:
            pos = (0.5, 0)
            translate = (sx / 2, 0)
    elif "mid" in pos or "cent" in pos:
        if "left" in pos:
            pos = (0, 0.5)
            translate = (0, sy / 2)
        elif "right" in pos:
            pos = (1, 0.5)
            translate = (sx, sy / 2)
        else:
            pos = (0.5, 0.5)
            translate = (sx / 2, sy / 2)

    if len(translate) > 0:
        translate = np.array(translate).astype(int)
        translate_extent = vtk.vtkImageTranslateExtent()
        translate_extent.SetTranslation(-translate[0], -translate[1], 0)
        translate_extent.SetInputData(img)
        translate_extent.Update()
        img = translate_extent.GetOutput()

    return img, pos


#################################################
class Picture2D(vedo.BaseActor2D):
    """
    Embed an image as a static 2D image in the canvas.
    """

    def __init__(self, fig, pos=(0, 0), scale=1, ontop=False, padding=1, justify=""):
        """
        Embed an image as a static 2D image in the canvas.

        Arguments:
            fig : Picture, matplotlib.Figure, matplotlib.pyplot, vtkImageData
                the input image
            pos : (list)
                2D (x,y) position in range [0,1],
                [0,0] being the bottom-left corner
            scale : (float)
                apply a scaling factor to the image
            ontop : (bool)
                keep image on top or not
            padding : (int)
                an internal padding space as a fraction of size
                (matplotlib only)
            justify : (str)
                define the anchor point ("top-left", "top-center", ...)
        """
        vedo.BaseActor2D.__init__(self)
        # print("input type:", fig.__class__)

        self.array = None

        if utils.is_sequence(fig):
            self.array = fig
            self._data = _get_img(self.array)

        elif isinstance(fig, Picture):
            self._data = fig.inputdata()

        elif isinstance(fig, vtk.vtkImageData):
            assert fig.GetDimensions()[2] == 1, "Cannot create an Picture2D from Volume"
            self._data = fig

        elif isinstance(fig, str):
            self._data = _get_img(fig)
            self.filename = fig

        elif "matplotlib" in str(fig.__class__):
            if hasattr(fig, "gcf"):
                fig = fig.gcf()
            fig.tight_layout(pad=padding)
            fig.canvas.draw()

            # self.array = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
            # self.array = self.array.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            width, height = fig.get_size_inches() * fig.get_dpi()
            self.array = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8).reshape(
                (int(height), int(width), 4)
            )
            self.array = self.array[:, :, :3]

            self._data = _get_img(self.array)

        #############
        if scale != 1:
            newsize = np.array(self._data.GetDimensions()[:2]) * scale
            newsize = newsize.astype(int)
            rsz = vtk.vtkImageResize()
            rsz.SetInputData(self._data)
            rsz.SetResizeMethodToOutputDimensions()
            rsz.SetOutputDimensions(newsize[0], newsize[1], 1)
            rsz.Update()
            self._data = rsz.GetOutput()

        if padding:
            pass  # TODO

        if justify:
            self._data, pos = _set_justification(self._data, justify)
        else:
            self._data, pos = _set_justification(self._data, pos)

        self._mapper = vtk.vtkImageMapper()
        # self._mapper.RenderToRectangleOn() # NOT good because of aliasing
        self._mapper.SetInputData(self._data)
        self._mapper.SetColorWindow(255)
        self._mapper.SetColorLevel(127.5)
        self.SetMapper(self._mapper)

        self.GetPositionCoordinate().SetCoordinateSystem(3)
        self.SetPosition(pos)

        if ontop:
            self.GetProperty().SetDisplayLocationToForeground()
        else:
            self.GetProperty().SetDisplayLocationToBackground()

    @property
    def shape(self):
        return np.array(self._data.GetDimensions()[:2]).astype(int)


#################################################
class Picture(vedo.base.Base3DProp, vtk.vtkImageActor):
    """
    Derived class of `vtkImageActor`. Used to represent 2D pictures in a 3D world.
    """

    def __init__(self, obj=None, channels=3, flip=False):
        """
        Can be instantiated with a path file name or with a numpy array.

        By default the transparency channel is disabled.
        To enable it set channels=4.

        Use `Picture.dimensions()` to access the number of pixels in x and y.

        Arguments:
            channels :  (int, list)
                only select these specific rgba channels (useful to remove alpha)
            flip : (bool)
                flip xy axis convention (when input is a numpy array)
        """

        vtk.vtkImageActor.__init__(self)
        vedo.base.Base3DProp.__init__(self)

        if utils.is_sequence(obj) and len(obj) > 0:  # passing array
            img = _get_img(obj, flip)

        elif isinstance(obj, vtk.vtkImageData):
            img = obj

        elif isinstance(obj, str):
            img = _get_img(obj)
            self.filename = obj

        else:
            img = vtk.vtkImageData()

        # select channels
        if isinstance(channels, int):
            channels = list(range(channels))

        nchans = len(channels)
        n = img.GetPointData().GetScalars().GetNumberOfComponents()
        if nchans and n > nchans:
            pec = vtk.vtkImageExtractComponents()
            pec.SetInputData(img)
            if nchans == 4:
                pec.SetComponents(channels[0], channels[1], channels[2], channels[3])
            elif nchans == 3:
                pec.SetComponents(channels[0], channels[1], channels[2])
            elif nchans == 2:
                pec.SetComponents(channels[0], channels[1])
            elif nchans == 1:
                pec.SetComponents(channels[0])
            pec.Update()
            img = pec.GetOutput()

        self._data = img
        self.SetInputData(img)

        sx, sy, _ = img.GetDimensions()
        self.shape = np.array([sx, sy])

        self._mapper = self.GetMapper()

        self.pipeline = utils.OperationNode("Picture", comment=f"#shape {self.shape}", c="#f28482")
        ######################################################################

    def _repr_html_(self):
        """
        HTML representation of the Picture object for Jupyter Notebooks.

        Returns:
            HTML text with the image and some properties.
        """
        import io
        import base64
        from PIL import Image

        library_name = "vedo.picture.Picture"
        help_url = "https://vedo.embl.es/docs/vedo/picture.html"

        arr = self.thumbnail(zoom=1.1)

        im = Image.fromarray(arr)
        buffered = io.BytesIO()
        im.save(buffered, format="PNG", quality=100)
        encoded = base64.b64encode(buffered.getvalue()).decode("utf-8")
        url = "data:image/png;base64," + encoded
        image = f"<img src='{url}'></img>"

        help_text = ""
        if self.name:
            help_text += f"<b> {self.name}: &nbsp&nbsp</b>"
        help_text += '<b><a href="' + help_url + '" target="_blank">' + library_name + "</a></b>"
        if self.filename:
            dots = ""
            if len(self.filename) > 30:
                dots = "..."
            help_text += f"<br/><code><i>({dots}{self.filename[-30:]})</i></code>"

        pdata = ""
        if self._data.GetPointData().GetScalars():
            if self._data.GetPointData().GetScalars().GetName():
                name = self._data.GetPointData().GetScalars().GetName()
                pdata = "<tr><td><b> point data array </b></td><td>" + name + "</td></tr>"

        cdata = ""
        if self._data.GetCellData().GetScalars():
            if self._data.GetCellData().GetScalars().GetName():
                name = self._data.GetCellData().GetScalars().GetName()
                cdata = "<tr><td><b> voxel data array </b></td><td>" + name + "</td></tr>"

        img = self.GetMapper().GetInput()

        allt = [
            "<table>",
            "<tr>",
            "<td>",
            image,
            "</td>",
            "<td style='text-align: center; vertical-align: center;'><br/>",
            help_text,
            "<table>",
            "<tr><td><b> shape </b></td><td>" + str(img.GetDimensions()[:2]) + "</td></tr>",
            "<tr><td><b> in memory size </b></td><td>"
            + str(int(img.GetActualMemorySize()))
            + " KB</td></tr>",
            pdata,
            cdata,
            "<tr><td><b> intensity range </b></td><td>" + str(img.GetScalarRange()) + "</td></tr>",
            "<tr><td><b> level&nbsp/&nbspwindow </b></td><td>"
            + str(self.level())
            + "&nbsp/&nbsp"
            + str(self.window())
            + "</td></tr>",
            "</table>",
            "</table>",
        ]
        return "\n".join(allt)

    def inputdata(self):
        """Return the underlying ``vtkImagaData`` object."""
        return self._data

    def dimensions(self):
        """Return the picture dimension as number of pixels in x and y"""
        nx, ny, _ = self._data.GetDimensions()
        return np.array([nx, ny])

    def channels(self):
        """Return the number of channels in picture"""
        return self._data.GetPointData().GetScalars().GetNumberOfComponents()

    def _update(self, data):
        """Overwrite the Picture data mesh with a new data."""
        self._data = data
        self._mapper.SetInputData(data)
        self._mapper.Modified()
        nx, ny, _ = self._data.GetDimensions()
        self.shape = np.array([nx, ny])
        return self

    def clone(self, transformed=False):
        """Return an exact copy of the input Picture.
        If transform is True, it is given the same scaling and position."""
        img = vtk.vtkImageData()
        img.DeepCopy(self._data)
        pic = Picture(img)
        if transformed:
            # assign the same transformation to the copy
            pic.SetOrigin(self.GetOrigin())
            pic.SetScale(self.GetScale())
            pic.SetOrientation(self.GetOrientation())
            pic.SetPosition(self.GetPosition())

        pic.pipeline = utils.OperationNode("clone", parents=[self], c="#f7dada", shape="diamond")
        return pic

    def cmap(self, name, vmin=None, vmax=None):
        """Colorize a picture with a colormap representing pixel intensity"""
        n = self._data.GetPointData().GetNumberOfComponents()
        if n > 1:
            ecr = vtk.vtkImageExtractComponents()
            ecr.SetInputData(self._data)
            ecr.SetComponents(0, 1, 2)
            ecr.Update()
            ilum = vtk.vtkImageMagnitude()
            ilum.SetInputData(self._data)
            ilum.Update()
            img = ilum.GetOutput()
        else:
            img = self._data

        lut = vtk.vtkLookupTable()
        _vmin, _vmax = img.GetScalarRange()
        if vmin is not None:
            _vmin = vmin
        if vmax is not None:
            _vmax = vmax
        lut.SetRange(_vmin, _vmax)

        ncols = 256
        lut.SetNumberOfTableValues(ncols)
        cols = colors.color_map(range(ncols), name, 0, ncols)
        for i, c in enumerate(cols):
            lut.SetTableValue(i, *c)
        lut.Build()

        imap = vtk.vtkImageMapToColors()
        imap.SetLookupTable(lut)
        imap.SetInputData(img)
        imap.Update()
        self._update(imap.GetOutput())
        self.pipeline = utils.OperationNode(
            f"cmap", comment=f'"{name}"', parents=[self], c="#f28482"
        )
        return self

    def extent(self, ext=None):
        """
        Get or set the physical extent that the picture spans.
        Format is `ext=[minx, maxx, miny, maxy]`.
        """
        if ext is None:
            return self._data.GetExtent()

        self._data.SetExtent(ext[0], ext[1], ext[2], ext[3], 0, 0)
        self._mapper.Modified()
        return self

    def alpha(self, a=None):
        """Set/get picture's transparency in the rendering scene."""
        if a is not None:
            self.GetProperty().SetOpacity(a)
            return self
        return self.GetProperty().GetOpacity()

    def level(self, value=None):
        """Get/Set the image color level (brightness) in the rendering scene."""
        if value is None:
            return self.GetProperty().GetColorLevel()
        self.GetProperty().SetColorLevel(value)
        return self

    def window(self, value=None):
        """Get/Set the image color window (contrast) in the rendering scene."""
        if value is None:
            return self.GetProperty().GetColorWindow()
        self.GetProperty().SetColorWindow(value)
        return self

    def crop(self, top=None, bottom=None, right=None, left=None, pixels=False):
        """Crop picture.

        Arguments:
            top : (float)
                fraction to crop from the top margin
            bottom : (float)
                fraction to crop from the bottom margin
            left : (float)
                fraction to crop from the left margin
            right : (float)
                fraction to crop from the right margin
            pixels : (bool)
                units are pixels
        """
        extractVOI = vtk.vtkExtractVOI()
        extractVOI.SetInputData(self._data)
        extractVOI.IncludeBoundaryOn()

        d = self.GetInput().GetDimensions()
        if pixels:
            extractVOI.SetVOI(left, d[0] - right - 1, bottom, d[1] - top - 1, 0, 0)
        else:
            bx0, bx1, by0, by1 = 0, d[0]-1, 0, d[1]-1
            if left is not None:   bx0 = int((d[0]-1)*left)
            if right is not None:  bx1 = int((d[0]-1)*(1-right))
            if bottom is not None: by0 = int((d[1]-1)*bottom)
            if top is not None:    by1 = int((d[1]-1)*(1-top))
            extractVOI.SetVOI(bx0, bx1, by0, by1, 0, 0)
        extractVOI.Update()

        self.shape = extractVOI.GetOutput().GetDimensions()[:2]
        self._update(extractVOI.GetOutput())
        self.pipeline = utils.OperationNode(
            "crop", comment=f"shape={tuple(self.shape)}", parents=[self], c="#f28482"
        )
        return self

    def pad(self, pixels=10, value=255):
        """
        Add the specified number of pixels at the picture borders.
        Pixels can be a list formatted as [left,right,bottom,top].

        Arguments:
            pixels : (int, list)
                number of pixels to be added (or a list of length 4)
            value : (int)
                intensity value (gray-scale color) of the padding
        """
        x0, x1, y0, y1, _z0, _z1 = self._data.GetExtent()
        pf = vtk.vtkImageConstantPad()
        pf.SetInputData(self._data)
        pf.SetConstant(value)
        if utils.is_sequence(pixels):
            pf.SetOutputWholeExtent(
                x0 - pixels[0], x1 + pixels[1], 
                y0 - pixels[2], y1 + pixels[3], 
                0, 0
            )
        else:
            pf.SetOutputWholeExtent(
                x0 - pixels, x1 + pixels, 
                y0 - pixels, y1 + pixels, 
                0, 0
            )
        pf.Update()
        self._update(pf.GetOutput())
        self.pipeline = utils.OperationNode(
            "pad", comment=f"{pixels} pixels", parents=[self], c="#f28482"
        )
        return self

    def tile(self, nx=4, ny=4, shift=(0, 0)):
        """
        Generate a tiling from the current picture by mirroring and repeating it.

        Arguments:
            nx : (float)
                number of repeats along x
            ny : (float)
                number of repeats along x
            shift : (list)
                shift in x and y in pixels
        """
        x0, x1, y0, y1, z0, z1 = self._data.GetExtent()
        constant_pad = vtk.vtkImageMirrorPad()
        constant_pad.SetInputData(self._data)
        constant_pad.SetOutputWholeExtent(
            int(x0 + shift[0] + 0.5),
            int(x1 * nx + shift[0] + 0.5),
            int(y0 + shift[1] + 0.5),
            int(y1 * ny + shift[1] + 0.5),
            z0,
            z1,
        )
        constant_pad.Update()
        pic = Picture(constant_pad.GetOutput())

        pic.pipeline = utils.OperationNode(
            "tile", comment=f"by {nx}x{ny}", parents=[self], c="#f28482"
        )
        return pic

    def append(self, pictures, axis="z", preserve_extents=False):
        """
        Append the input images to the current one along the specified axis.
        Except for the append axis, all inputs must have the same extent.
        All inputs must have the same number of scalar components.
        The output has the same origin and spacing as the first input.
        The origin and spacing of all other inputs are ignored.
        All inputs must have the same scalar type.

        Arguments:
            axis : (int, str)
                axis expanded to hold the multiple images
            preserve_extents : (bool)
                if True, the extent of the inputs is used to place
                the image in the output. The whole extent of the output is the union of the input
                whole extents. Any portion of the output not covered by the inputs is set to zero.
                The origin and spacing is taken from the first input.

        Example:
            ```python
            from vedo import Picture, dataurl
            pic = Picture(dataurl+'dog.jpg').pad()
            pic.append([pic,pic], axis='y')
            pic.append([pic,pic,pic], axis='x')
            pic.show(axes=1).close()
            ```
            ![](https://vedo.embl.es/images/feats/pict_append.png)
        """
        ima = vtk.vtkImageAppend()
        ima.SetInputData(self._data)
        if not utils.is_sequence(pictures):
            pictures = [pictures]
        for p in pictures:
            if isinstance(p, vtk.vtkImageData):
                ima.AddInputData(p)
            else:
                ima.AddInputData(p.inputdata())
        ima.SetPreserveExtents(preserve_extents)
        if axis == "x":
            axis = 0
        elif axis == "y":
            axis = 1
        ima.SetAppendAxis(axis)
        ima.Update()
        self._update(ima.GetOutput())
        self.pipeline = utils.OperationNode(
            "append", comment=f"axis={axis}", parents=[self, *pictures], c="#f28482"
        )
        return self

    def resize(self, newsize):
        """Resize the image resolution by specifying the number of pixels in width and height.
        If left to zero, it will be automatically calculated to keep the original aspect ratio.

        newsize is the shape of picture as [npx, npy], or it can be also expressed as a fraction.
        """
        old_dims = np.array(self._data.GetDimensions())

        if not utils.is_sequence(newsize):
            newsize = (old_dims * newsize + 0.5).astype(int)

        if not newsize[1]:
            ar = old_dims[1] / old_dims[0]
            newsize = [newsize[0], int(newsize[0] * ar + 0.5)]
        if not newsize[0]:
            ar = old_dims[0] / old_dims[1]
            newsize = [int(newsize[1] * ar + 0.5), newsize[1]]
        newsize = [newsize[0], newsize[1], old_dims[2]]

        rsz = vtk.vtkImageResize()
        rsz.SetInputData(self._data)
        rsz.SetResizeMethodToOutputDimensions()
        rsz.SetOutputDimensions(newsize)
        rsz.Update()
        out = rsz.GetOutput()
        out.SetSpacing(1, 1, 1)
        self._update(out)
        self.pipeline = utils.OperationNode(
            "resize", comment=f"shape={tuple(self.shape)}", parents=[self], c="#f28482"
        )
        return self

    def mirror(self, axis="x"):
        """Mirror picture along x or y axis. Same as `flip()`."""
        ff = vtk.vtkImageFlip()
        ff.SetInputData(self.inputdata())
        if axis.lower() == "x":
            ff.SetFilteredAxis(0)
        elif axis.lower() == "y":
            ff.SetFilteredAxis(1)
        else:
            colors.printc("Error in mirror(): mirror must be set to x or y.", c="r")
            raise RuntimeError()
        ff.Update()
        self._update(ff.GetOutput())
        self.pipeline = utils.OperationNode(f"mirror {axis}", parents=[self], c="#f28482")
        return self

    def flip(self, axis="y"):
        """Mirror picture along x or y axis. Same as `mirror()`."""
        return self.mirror(axis=axis)

    def rotate(self, angle, center=(), scale=1, mirroring=False, bc="w", alpha=1):
        """
        Rotate by the specified angle (anticlockwise).

        Arguments:
            angle : (float)
                rotation angle in degrees
            center : (list)
                center of rotation (x,y) in pixels
        """
        bounds = self.bounds()
        pc = [0, 0, 0]
        if center:
            pc[0] = center[0]
            pc[1] = center[1]
        else:
            pc[0] = (bounds[1] + bounds[0]) / 2.0
            pc[1] = (bounds[3] + bounds[2]) / 2.0
        pc[2] = (bounds[5] + bounds[4]) / 2.0

        transform = vtk.vtkTransform()
        transform.Translate(pc)
        transform.RotateWXYZ(-angle, 0, 0, 1)
        transform.Scale(1 / scale, 1 / scale, 1)
        transform.Translate(-pc[0], -pc[1], -pc[2])

        reslice = vtk.vtkImageReslice()
        reslice.SetMirror(mirroring)
        c = np.array(colors.get_color(bc)) * 255
        reslice.SetBackgroundColor([c[0], c[1], c[2], alpha * 255])
        reslice.SetInputData(self._data)
        reslice.SetResliceTransform(transform)
        reslice.SetOutputDimensionality(2)
        reslice.SetInterpolationModeToCubic()
        reslice.SetOutputSpacing(self._data.GetSpacing())
        reslice.SetOutputOrigin(self._data.GetOrigin())
        reslice.SetOutputExtent(self._data.GetExtent())
        reslice.Update()
        self._update(reslice.GetOutput())

        self.pipeline = utils.OperationNode(
            "rotate", comment=f"angle={angle}", parents=[self], c="#f28482"
        )
        return self

    def select(self, component):
        """Select one single component of the rgb image."""
        ec = vtk.vtkImageExtractComponents()
        ec.SetInputData(self._data)
        ec.SetComponents(component)
        ec.Update()
        pic = Picture(ec.GetOutput())
        pic.pipeline = utils.OperationNode(
            "select", comment=f"component {component}", parents=[self], c="#f28482"
        )
        return pic

    def bw(self):
        """Make it black and white using luminance calibration."""
        n = self._data.GetPointData().GetNumberOfComponents()
        if n == 4:
            ecr = vtk.vtkImageExtractComponents()
            ecr.SetInputData(self._data)
            ecr.SetComponents(0, 1, 2)
            ecr.Update()
            img = ecr.GetOutput()
        else:
            img = self._data

        ecr = vtk.vtkImageLuminance()
        ecr.SetInputData(img)
        ecr.Update()
        self._update(ecr.GetOutput())
        self.pipeline = utils.OperationNode("black&white", parents=[self], c="#f28482")
        return self

    def smooth(self, sigma=3, radius=None):
        """
        Smooth a Picture with Gaussian kernel.

        Arguments:
            sigma : (int)
                number of sigmas in pixel units
            radius : (float)
                how far out the gaussian kernel will go before being clamped to zero
        """
        gsf = vtk.vtkImageGaussianSmooth()
        gsf.SetDimensionality(2)
        gsf.SetInputData(self._data)
        if radius is not None:
            if utils.is_sequence(radius):
                gsf.SetRadiusFactors(radius[0], radius[1])
            else:
                gsf.SetRadiusFactor(radius)

        if utils.is_sequence(sigma):
            gsf.SetStandardDeviations(sigma[0], sigma[1])
        else:
            gsf.SetStandardDeviation(sigma)
        gsf.Update()
        self._update(gsf.GetOutput())
        self.pipeline = utils.OperationNode(
            "smooth", comment=f"sigma={sigma}", parents=[self], c="#f28482"
        )
        return self

    def median(self):
        """
        Median filter that preserves thin lines and corners.

        It operates on a 5x5 pixel neighborhood. It computes two values initially:
        the median of the + neighbors and the median of the x neighbors.
        It then computes the median of these two values plus the center pixel.
        This result of this second median is the output pixel value.
        """
        medf = vtk.vtkImageHybridMedian2D()
        medf.SetInputData(self._data)
        medf.Update()
        self._update(medf.GetOutput())
        self.pipeline = utils.OperationNode("median", parents=[self], c="#f28482")
        return self

    def enhance(self):
        """
        Enhance a b&w picture using the laplacian, enhancing high-freq edges.

        Example:
            ```python
            from vedo import *
            pic = Picture(vedo.dataurl+'images/dog.jpg').bw()
            show(pic, pic.clone().enhance(), N=2, mode='image', zoom='tight')
            ```
            ![](https://vedo.embl.es/images/feats/pict_enhance.png)
        """
        img = self._data
        scalarRange = img.GetPointData().GetScalars().GetRange()

        cast = vtk.vtkImageCast()
        cast.SetInputData(img)
        cast.SetOutputScalarTypeToDouble()
        cast.Update()

        laplacian = vtk.vtkImageLaplacian()
        laplacian.SetInputData(cast.GetOutput())
        laplacian.SetDimensionality(2)
        laplacian.Update()

        subtr = vtk.vtkImageMathematics()
        subtr.SetInputData(0, cast.GetOutput())
        subtr.SetInputData(1, laplacian.GetOutput())
        subtr.SetOperationToSubtract()
        subtr.Update()

        color_window = scalarRange[1] - scalarRange[0]
        color_level = color_window / 2
        original_color = vtk.vtkImageMapToWindowLevelColors()
        original_color.SetWindow(color_window)
        original_color.SetLevel(color_level)
        original_color.SetInputData(subtr.GetOutput())
        original_color.Update()
        self._update(original_color.GetOutput())

        self.pipeline = utils.OperationNode("enhance", parents=[self], c="#f28482")
        return self

    def fft(self, mode="magnitude", logscale=12, center=True):
        """
        Fast Fourier transform of a picture.

        Arguments:
            logscale : (float)
                if non-zero, take the logarithm of the intensity and scale it by this factor.
            mode : (str)
                either [magnitude, real, imaginary, complex], compute the point array data accordingly.
            center : (bool)
                shift constant zero-frequency to the center of the image for display.
                (FFT converts spatial images into frequency space, but puts the zero frequency at the origin)
        """
        ffti = vtk.vtkImageFFT()
        ffti.SetInputData(self._data)
        ffti.Update()

        if "mag" in mode:
            mag = vtk.vtkImageMagnitude()
            mag.SetInputData(ffti.GetOutput())
            mag.Update()
            out = mag.GetOutput()
        elif "real" in mode:
            erf = vtk.vtkImageExtractComponents()
            erf.SetInputData(ffti.GetOutput())
            erf.SetComponents(0)
            erf.Update()
            out = erf.GetOutput()
        elif "imaginary" in mode:
            eimf = vtk.vtkImageExtractComponents()
            eimf.SetInputData(ffti.GetOutput())
            eimf.SetComponents(1)
            eimf.Update()
            out = eimf.GetOutput()
        elif "complex" in mode:
            out = ffti.GetOutput()
        else:
            colors.printc("Error in fft(): unknown mode", mode)
            raise RuntimeError()

        if center:
            center = vtk.vtkImageFourierCenter()
            center.SetInputData(out)
            center.Update()
            out = center.GetOutput()

        if "complex" not in mode:
            if logscale:
                ils = vtk.vtkImageLogarithmicScale()
                ils.SetInputData(out)
                ils.SetConstant(logscale)
                ils.Update()
                out = ils.GetOutput()

        pic = Picture(out)
        pic.pipeline = utils.OperationNode("FFT", parents=[self], c="#f28482")
        return pic

    def rfft(self, mode="magnitude"):
        """Reverse Fast Fourier transform of a picture."""

        ffti = vtk.vtkImageRFFT()
        ffti.SetInputData(self._data)
        ffti.Update()

        if "mag" in mode:
            mag = vtk.vtkImageMagnitude()
            mag.SetInputData(ffti.GetOutput())
            mag.Update()
            out = mag.GetOutput()
        elif "real" in mode:
            erf = vtk.vtkImageExtractComponents()
            erf.SetInputData(ffti.GetOutput())
            erf.SetComponents(0)
            erf.Update()
            out = erf.GetOutput()
        elif "imaginary" in mode:
            eimf = vtk.vtkImageExtractComponents()
            eimf.SetInputData(ffti.GetOutput())
            eimf.SetComponents(1)
            eimf.Update()
            out = eimf.GetOutput()
        elif "complex" in mode:
            out = ffti.GetOutput()
        else:
            colors.printc("Error in rfft(): unknown mode", mode)
            raise RuntimeError()

        pic = Picture(out)
        pic.pipeline = utils.OperationNode("rFFT", parents=[self], c="#f28482")
        return pic

    def filterpass(self, lowcutoff=None, highcutoff=None, order=3):
        """
        Low-pass and high-pass filtering become trivial in the frequency domain.
        A portion of the pixels/voxels are simply masked or attenuated.
        This function applies a high pass Butterworth filter that attenuates the
        frequency domain image with the function

        The gradual attenuation of the filter is important.
        A simple high-pass filter would simply mask a set of pixels in the frequency domain,
        but the abrupt transition would cause a ringing effect in the spatial domain.

        Arguments:
            lowcutoff : (list)
                the cutoff frequencies
            highcutoff : (list)
                the cutoff frequencies
            order : (int)
                order determines sharpness of the cutoff curve
        """
        # https://lorensen.github.io/VTKExamples/site/Cxx/ImageProcessing/IdealHighPass
        fft = vtk.vtkImageFFT()
        fft.SetInputData(self._data)
        fft.Update()
        out = fft.GetOutput()

        if highcutoff:
            blp = vtk.vtkImageButterworthLowPass()
            blp.SetInputData(out)
            blp.SetCutOff(highcutoff)
            blp.SetOrder(order)
            blp.Update()
            out = blp.GetOutput()

        if lowcutoff:
            bhp = vtk.vtkImageButterworthHighPass()
            bhp.SetInputData(out)
            bhp.SetCutOff(lowcutoff)
            bhp.SetOrder(order)
            bhp.Update()
            out = bhp.GetOutput()

        rfft = vtk.vtkImageRFFT()
        rfft.SetInputData(out)
        rfft.Update()

        ecomp = vtk.vtkImageExtractComponents()
        ecomp.SetInputData(rfft.GetOutput())
        ecomp.SetComponents(0)
        ecomp.Update()

        caster = vtk.vtkImageCast()
        caster.SetOutputScalarTypeToUnsignedChar()
        caster.SetInputData(ecomp.GetOutput())
        caster.Update()
        self._update(caster.GetOutput())
        self.pipeline = utils.OperationNode("filterpass", parents=[self], c="#f28482")
        return self

    def blend(self, pic, alpha1=0.5, alpha2=0.5):
        """
        Take L, LA, RGB, or RGBA images as input and blends
        them according to the alpha values and/or the opacity setting for each input.
        """
        blf = vtk.vtkImageBlend()
        blf.AddInputData(self._data)
        blf.AddInputData(pic.inputdata())
        blf.SetOpacity(0, alpha1)
        blf.SetOpacity(1, alpha2)
        blf.SetBlendModeToNormal()
        blf.Update()
        self._update(blf.GetOutput())
        self.pipeline = utils.OperationNode("blend", parents=[self, pic], c="#f28482")
        return self

    def warp(
        self,
        source_pts=(),
        target_pts=(),
        transform=None,
        sigma=1,
        mirroring=False,
        bc="w",
        alpha=1,
    ):
        """
        Warp an image using thin-plate splines.

        Arguments:
            source_pts : (list)
                source points
            target_pts : (list)
                target points
            transform : (vtkTransform)
                a vtkTransform object can be supplied
            sigma : (float), optional
                stiffness of the interpolation
            mirroring : (bool)
                fill the margins with a reflection of the original image
            bc : (color)
                fill the margins with a solid color
            alpha : (float)
                opacity of the filled margins
        """
        if transform is None:
            # source and target must be filled
            transform = vtk.vtkThinPlateSplineTransform()
            transform.SetBasisToR2LogR()

            parents = [self]
            if isinstance(source_pts, vedo.Points):
                parents.append(source_pts)
                source_pts = source_pts.points()
            if isinstance(target_pts, vedo.Points):
                parents.append(target_pts)
                target_pts = target_pts.points()

            ns = len(source_pts)
            nt = len(target_pts)
            if ns != nt:
                colors.printc("Error in picture.warp(): #source != #target points", ns, nt, c="r")
                raise RuntimeError()

            ptsou = vtk.vtkPoints()
            ptsou.SetNumberOfPoints(ns)

            pttar = vtk.vtkPoints()
            pttar.SetNumberOfPoints(nt)

            for i in range(ns):
                p = source_pts[i]
                ptsou.SetPoint(i, [p[0], p[1], 0])
                p = target_pts[i]
                pttar.SetPoint(i, [p[0], p[1], 0])

            transform.SetSigma(sigma)
            transform.SetSourceLandmarks(pttar)
            transform.SetTargetLandmarks(ptsou)
        else:
            # ignore source and target
            pass

        reslice = vtk.vtkImageReslice()
        reslice.SetInputData(self._data)
        reslice.SetOutputDimensionality(2)
        reslice.SetResliceTransform(transform)
        reslice.SetInterpolationModeToCubic()
        reslice.SetMirror(mirroring)
        c = np.array(colors.get_color(bc)) * 255
        reslice.SetBackgroundColor([c[0], c[1], c[2], alpha * 255])
        reslice.Update()
        self.transform = transform
        self._update(reslice.GetOutput())
        self.pipeline = utils.OperationNode("warp", parents=parents, c="#f28482")
        return self

    def invert(self):
        """
        Return an inverted picture (inverted in each color channel).
        """
        rgb = self.tonumpy()
        data = 255 - np.array(rgb)
        self._update(_get_img(data))
        self.pipeline = utils.OperationNode("invert", parents=[self], c="#f28482")
        return self

    def binarize(self, threshold=None, invert=False):
        """
        Return a new Picture where pixel above threshold are set to 255
        and pixels below are set to 0.

        Arguments:
            threshold : (float)
                input threshold value
            invert : (bool)
                invert threshold direction

        Example:
            ```python
            from vedo import Picture, show
            pic1 = Picture("https://aws.glamour.es/prod/designs/v1/assets/620x459/547577.jpg")
            pic2 = pic1.clone().invert()
            pic3 = pic1.clone().binarize()
            show(pic1, pic2, pic3, N=3, bg="blue9").close()
            ```
            ![](https://vedo.embl.es/images/feats/pict_binarize.png)
        """
        rgb = self.tonumpy()
        if rgb.ndim == 3:
            intensity = np.sum(rgb, axis=2) / 3
        else:
            intensity = rgb

        if threshold is None:
            vmin, vmax = np.min(intensity), np.max(intensity)
            threshold = (vmax + vmin) / 2

        data = np.zeros_like(intensity).astype(np.uint8)
        mask = np.where(intensity > threshold)
        if invert:
            data += 255
            data[mask] = 0
        else:
            data[mask] = 255

        self._update(_get_img(data, flip=True))

        self.pipeline = utils.OperationNode(
            "binarize", comment=f"threshold={threshold}", parents=[self], c="#f28482"
        )
        return self

    def threshold(self, value=None, flip=False):
        """
        Create a polygonal Mesh from a Picture by filling regions with pixels
        luminosity above a specified value.

        Arguments:
            value : (float)
                The default is None, e.i. 1/3 of the scalar range.
            flip: (bool)
                Flip polygon orientations

        Returns:
            A polygonal mesh.
        """
        mgf = vtk.vtkImageMagnitude()
        mgf.SetInputData(self._data)
        mgf.Update()
        msq = vtk.vtkMarchingSquares()
        msq.SetInputData(mgf.GetOutput())
        if value is None:
            r0, r1 = self._data.GetScalarRange()
            value = r0 + (r1 - r0) / 3
        msq.SetValue(0, value)
        msq.Update()
        if flip:
            rs = vtk.vtkReverseSense()
            rs.SetInputData(msq.GetOutput())
            rs.ReverseCellsOn()
            rs.ReverseNormalsOff()
            rs.Update()
            output = rs.GetOutput()
        else:
            output = msq.GetOutput()
        ctr = vtk.vtkContourTriangulator()
        ctr.SetInputData(output)
        ctr.Update()
        out = vedo.Mesh(ctr.GetOutput(), c="k").bc("t").lighting("off")

        out.pipeline = utils.OperationNode(
            "threshold", comment=f"{value: .2f}", parents=[self], c="#f28482:#e9c46a"
        )
        return out

    def tomesh(self):
        """
        Convert an image to polygonal data (quads),
        with each polygon vertex assigned a RGBA value.
        """
        dims = self._data.GetDimensions()
        gr = vedo.shapes.Grid(s=dims[:2], res=(dims[0] - 1, dims[1] - 1))
        gr.pos(int(dims[0] / 2), int(dims[1] / 2)).pickable(True).wireframe(False).lw(0)
        self._data.GetPointData().GetScalars().SetName("RGBA")
        gr.inputdata().GetPointData().AddArray(self._data.GetPointData().GetScalars())
        gr.inputdata().GetPointData().SetActiveScalars("RGBA")
        gr.mapper().SetArrayName("RGBA")
        gr.mapper().SetScalarModeToUsePointData()
        gr.mapper().ScalarVisibilityOn()
        gr.name = self.name
        gr.filename = self.filename
        gr.pipeline = utils.OperationNode("tomesh", parents=[self], c="#f28482:#e9c46a")
        return gr

    def tonumpy(self):
        """
        Get read-write access to pixels of a Picture object as a numpy array.
        Note that the shape is (nrofchannels, nx, ny).

        When you set values in the output image, you don't want numpy to reallocate the array
        but instead set values in the existing array, so use the [:] operator.
        Example: arr[:] = arr - 15

        If the array is modified call:
        ``picture.modified()``
        when all your modifications are completed.
        """
        nx, ny, _ = self._data.GetDimensions()
        nchan = self._data.GetPointData().GetScalars().GetNumberOfComponents()
        narray = utils.vtk2numpy(self._data.GetPointData().GetScalars()).reshape(ny, nx, nchan)
        narray = np.flip(narray, axis=0).astype(np.uint8)
        return narray.squeeze()

    def rectangle(self, xspan, yspan, c="green5", alpha=1):
        """Draw a rectangle box on top of current image. Units are pixels.

        Example:
            ```python
            import vedo
            pic = vedo.Picture(vedo.dataurl+"images/dog.jpg")
            pic.rectangle([100,300], [100,200], c='green4', alpha=0.7)
            pic.line([100,100],[400,500], lw=2, alpha=1)
            pic.triangle([250,300], [100,300], [200,400], c='blue5')
            vedo.show(pic, axes=1).close()
            ```
            ![](https://vedo.embl.es/images/feats/pict_drawon.png)
        """
        x1, x2 = xspan
        y1, y2 = yspan

        r, g, b = vedo.colors.get_color(c)
        c = np.array([r, g, b]) * 255
        c = c.astype(np.uint8)

        alpha = min(alpha, 1)
        if alpha <= 0:
            return self
        alpha2 = alpha
        alpha1 = 1 - alpha

        nx, ny = self.dimensions()
        if x2 > nx:
            x2 = nx - 1
        if y2 > ny:
            y2 = ny - 1

        nchan = self.channels()
        narrayA = self.tonumpy()

        canvas_source = vtk.vtkImageCanvasSource2D()
        canvas_source.SetExtent(0, nx - 1, 0, ny - 1, 0, 0)
        canvas_source.SetScalarTypeToUnsignedChar()
        canvas_source.SetNumberOfScalarComponents(nchan)
        canvas_source.SetDrawColor(255, 255, 255)
        canvas_source.FillBox(x1, x2, y1, y2)
        canvas_source.Update()
        image_data = canvas_source.GetOutput()

        vscals = image_data.GetPointData().GetScalars()
        narrayB = vedo.utils.vtk2numpy(vscals).reshape(ny, nx, nchan)
        narrayB = np.flip(narrayB, axis=0)
        narrayC = np.where(narrayB < 255, narrayA, alpha1 * narrayA + alpha2 * c)
        self._update(_get_img(narrayC))
        self.pipeline = utils.OperationNode("rectangle", parents=[self], c="#f28482")
        return self

    def line(self, p1, p2, lw=2, c="k2", alpha=1):
        """Draw a line on top of current image. Units are pixels."""
        x1, x2 = p1
        y1, y2 = p2

        r, g, b = vedo.colors.get_color(c)
        c = np.array([r, g, b]) * 255
        c = c.astype(np.uint8)

        alpha = min(alpha, 1)
        if alpha <= 0:
            return self
        alpha2 = alpha
        alpha1 = 1 - alpha

        nx, ny = self.dimensions()
        if x2 > nx:
            x2 = nx - 1
        if y2 > ny:
            y2 = ny - 1

        nchan = self.channels()
        narrayA = self.tonumpy()

        canvas_source = vtk.vtkImageCanvasSource2D()
        canvas_source.SetExtent(0, nx - 1, 0, ny - 1, 0, 0)
        canvas_source.SetScalarTypeToUnsignedChar()
        canvas_source.SetNumberOfScalarComponents(nchan)
        canvas_source.SetDrawColor(255, 255, 255)
        canvas_source.FillTube(x1, x2, y1, y2, lw)
        canvas_source.Update()
        image_data = canvas_source.GetOutput()

        vscals = image_data.GetPointData().GetScalars()
        narrayB = vedo.utils.vtk2numpy(vscals).reshape(ny, nx, nchan)
        narrayB = np.flip(narrayB, axis=0)
        narrayC = np.where(narrayB < 255, narrayA, alpha1 * narrayA + alpha2 * c)
        self._update(_get_img(narrayC))
        self.pipeline = utils.OperationNode("line", parents=[self], c="#f28482")
        return self

    def triangle(self, p1, p2, p3, c="red3", alpha=1):
        """Draw a triangle on top of current image. Units are pixels."""
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        r, g, b = vedo.colors.get_color(c)
        c = np.array([r, g, b]) * 255
        c = c.astype(np.uint8)

        alpha = min(alpha, 1)
        if alpha <= 0:
            return self
        alpha2 = alpha
        alpha1 = 1 - alpha

        nx, ny = self.dimensions()
        x1 = min(x1, nx)
        x2 = min(x2, nx)
        x3 = min(x3, nx)

        y1 = min(y1, ny)
        y2 = min(y2, ny)
        y3 = min(y3, ny)

        nchan = self.channels()
        narrayA = self.tonumpy()

        canvas_source = vtk.vtkImageCanvasSource2D()
        canvas_source.SetExtent(0, nx - 1, 0, ny - 1, 0, 0)
        canvas_source.SetScalarTypeToUnsignedChar()
        canvas_source.SetNumberOfScalarComponents(nchan)
        canvas_source.SetDrawColor(255, 255, 255)
        canvas_source.FillTriangle(x1, y1, x2, y2, x3, y3)
        canvas_source.Update()
        image_data = canvas_source.GetOutput()

        vscals = image_data.GetPointData().GetScalars()
        narrayB = vedo.utils.vtk2numpy(vscals).reshape(ny, nx, nchan)
        narrayB = np.flip(narrayB, axis=0)
        narrayC = np.where(narrayB < 255, narrayA, alpha1 * narrayA + alpha2 * c)
        self._update(_get_img(narrayC))
        self.pipeline = utils.OperationNode("triangle", parents=[self], c="#f28482")
        return self

    def add_text(
        self,
        txt,
        # pos=(0, 0),  # TODO
        width=400,
        height=200,
        alpha=1,
        c="black",
        bg=None,
        alpha_bg=1,
        font="Theemim",
        dpi=200,
        justify="bottom-left",
    ):
        """Add text to an image."""

        tp = vtk.vtkTextProperty()
        tp.BoldOff()
        tp.FrameOff()
        tp.SetColor(colors.get_color(c))
        tp.SetJustificationToLeft()
        if "top" in justify:
            tp.SetVerticalJustificationToTop()
        if "bottom" in justify:
            tp.SetVerticalJustificationToBottom()
        if "cent" in justify:
            tp.SetVerticalJustificationToCentered()
            tp.SetJustificationToCentered()
        if "left" in justify:
            tp.SetJustificationToLeft()
        if "right" in justify:
            tp.SetJustificationToRight()

        if   font.lower() == "courier": tp.SetFontFamilyToCourier()
        elif font.lower() == "times": tp.SetFontFamilyToTimes()
        elif font.lower() == "arial": tp.SetFontFamilyToArial()
        else:
            tp.SetFontFamily(vtk.VTK_FONT_FILE)
            tp.SetFontFile(utils.get_font_path(font))

        if bg:
            bgcol = colors.get_color(bg)
            tp.SetBackgroundColor(bgcol)
            tp.SetBackgroundOpacity(alpha_bg)
            tp.SetFrameColor(bgcol)
            tp.FrameOn()

        tr = vtk.vtkTextRenderer()
        # GetConstrainedFontSize (const vtkUnicodeString &str,
        # vtkTextProperty(*tprop, int targetWidth, int targetHeight, int dpi)
        fs = tr.GetConstrainedFontSize(txt, tp, width, height, dpi)
        tp.SetFontSize(fs)

        img = vtk.vtkImageData()
        # img.SetOrigin(*pos,1)
        tr.RenderString(tp, txt, img, [width, height], dpi)
        # RenderString (vtkTextProperty *tprop, const vtkStdString &str,
        #   vtkImageData *data, int textDims[2], int dpi, int backend=Default)

        blf = vtk.vtkImageBlend()
        blf.AddInputData(self._data)
        blf.AddInputData(img)
        blf.SetOpacity(0, 1)
        blf.SetOpacity(1, alpha)
        blf.SetBlendModeToNormal()
        blf.Update()

        self._update(blf.GetOutput())
        self.pipeline = utils.OperationNode(
            "add_text", comment=f"{txt}", parents=[self], c="#f28482"
        )
        return self

    def modified(self):
        """Use in conjunction with ``tonumpy()`` to update any modifications to the picture array"""
        self._data.GetPointData().GetScalars().Modified()
        return self

    def write(self, filename):
        """Write picture to file as png or jpg."""
        vedo.file_io.write(self._data, filename)
        self.pipeline = utils.OperationNode(
            "write", comment=filename[:15], parents=[self], c="#8a817c", shape="cylinder"
        )
        return self
