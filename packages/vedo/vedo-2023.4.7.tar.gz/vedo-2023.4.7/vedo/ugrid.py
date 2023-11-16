import numpy as np

try:
    import vedo.vtkclasses as vtk
except ImportError:
    import vtkmodules.all as vtk

import vedo
from vedo import settings
from vedo import colors
from vedo import utils
from vedo.base import BaseGrid
from vedo.file_io import download, loadUnStructuredGrid


__docformat__ = "google"

__doc__ = """
Work with unstructured grid datasets
"""

__all__ = ["UGrid"]

#########################################################################
class UGrid(BaseGrid, vtk.vtkActor):
    """Support for UnstructuredGrid objects."""

    def __init__(self, inputobj=None):
        """
        Support for UnstructuredGrid objects.

        Arguments:
            inputobj : (list, vtkUnstructuredGrid, str)
                A list in the form `[points, cells, celltypes]`,
                or a vtkUnstructuredGrid object, or a filename

        Celltypes are identified by the following convention:
            - VTK_TETRA = 10
            - VTK_VOXEL = 11
            - VTK_HEXAHEDRON = 12
            - VTK_WEDGE = 13
            - VTK_PYRAMID = 14
            - VTK_HEXAGONAL_PRISM = 15
            - VTK_PENTAGONAL_PRISM = 16
        """

        vtk.vtkActor.__init__(self)
        BaseGrid.__init__(self)

        inputtype = str(type(inputobj))
        self._data = None
        self._polydata = None
        self._bfprop = None
        self.name = "UGrid"

        ###################
        if inputobj is None:
            self._data = vtk.vtkUnstructuredGrid()

        elif utils.is_sequence(inputobj):

            pts, cells, celltypes = inputobj

            self._data = vtk.vtkUnstructuredGrid()

            if not utils.is_sequence(cells[0]):
                tets = []
                nf = cells[0] + 1
                for i, cl in enumerate(cells):
                    if i in (nf, 0):
                        k = i + 1
                        nf = cl + k
                        cell = [cells[j + k] for j in range(cl)]
                        tets.append(cell)
                cells = tets

            # This would fill the points and use those to define orientation
            vpts = utils.numpy2vtk(pts, dtype=np.float32)
            points = vtk.vtkPoints()
            points.SetData(vpts)
            self._data.SetPoints(points)

            # This fill the points and use cells to define orientation
            # points = vtk.vtkPoints()
            # for c in cells:
            #       for pid in c:
            #           points.InsertNextPoint(pts[pid])
            # self._data.SetPoints(points)

            # Fill cells
            # https://vtk.org/doc/nightly/html/vtkCellType_8h_source.html
            for i, ct in enumerate(celltypes):
                cell_conn = cells[i]
                if ct == vtk.VTK_HEXAHEDRON:
                    cell = vtk.vtkHexahedron()
                elif ct == vtk.VTK_TETRA:
                    cell = vtk.vtkTetra()
                elif ct == vtk.VTK_VOXEL:
                    cell = vtk.vtkVoxel()
                elif ct == vtk.VTK_WEDGE:
                    cell = vtk.vtkWedge()
                elif ct == vtk.VTK_PYRAMID:
                    cell = vtk.vtkPyramid()
                elif ct == vtk.VTK_HEXAGONAL_PRISM:
                    cell = vtk.vtkHexagonalPrism()
                elif ct == vtk.VTK_PENTAGONAL_PRISM:
                    cell = vtk.vtkPentagonalPrism()
                else:
                    print("UGrid: cell type", ct, "not implemented. Skip.")
                    continue
                cpids = cell.GetPointIds()
                for j, pid in enumerate(cell_conn):
                    cpids.SetId(j, pid)
                self._data.InsertNextCell(ct, cpids)

        elif "UnstructuredGrid" in inputtype:
            self._data = inputobj

        elif isinstance(inputobj, str):
            if "https://" in inputobj:
                inputobj = download(inputobj, verbose=False)
            self._data = loadUnStructuredGrid(inputobj)
            self.filename = inputobj

        else:
            vedo.logger.error(f"cannot understand input type {inputtype}")
            return

        # self._mapper = vtk.vtkDataSetMapper()
        self._mapper = vtk.vtkPolyDataMapper()
        self._mapper.SetInterpolateScalarsBeforeMapping(settings.interpolate_scalars_before_mapping)

        if settings.use_polygon_offset:
            self._mapper.SetResolveCoincidentTopologyToPolygonOffset()
            pof, pou = settings.polygon_offset_factor, settings.polygon_offset_units
            self._mapper.SetResolveCoincidentTopologyPolygonOffsetParameters(pof, pou)
        self.GetProperty().SetInterpolationToFlat()

        if not self._data:
            return

        # now fill the representation of the vtk unstr grid
        sf = vtk.vtkShrinkFilter()
        sf.SetInputData(self._data)
        sf.SetShrinkFactor(1.0)
        sf.Update()
        gf = vtk.vtkGeometryFilter()
        gf.SetInputData(sf.GetOutput())
        gf.Update()
        self._polydata = gf.GetOutput()

        self._mapper.SetInputData(self._polydata)
        sc = None
        if self.useCells:
            sc = self._polydata.GetCellData().GetScalars()
        else:
            sc = self._polydata.GetPointData().GetScalars()
        if sc:
            self._mapper.SetScalarRange(sc.GetRange())

        self.SetMapper(self._mapper)
        self.property = self.GetProperty()

        self.pipeline = utils.OperationNode(
            self, comment=f"#cells {self._data.GetNumberOfCells()}",
            c="#4cc9f0",
        )
    # ------------------------------------------------------------------

    def _repr_html_(self):
        """
        HTML representation of the UGrid object for Jupyter Notebooks.

        Returns:
            HTML text with the image and some properties.
        """
        import io
        import base64
        from PIL import Image

        library_name = "vedo.ugrid.UGrid"
        help_url = "https://vedo.embl.es/docs/vedo/ugrid.html"

        arr = self.thumbnail()
        im = Image.fromarray(arr)
        buffered = io.BytesIO()
        im.save(buffered, format="PNG", quality=100)
        encoded = base64.b64encode(buffered.getvalue()).decode("utf-8")
        url = "data:image/png;base64," + encoded
        image = f"<img src='{url}'></img>"

        bounds = "<br/>".join(
            [
                utils.precision(min_x,4) + " ... " + utils.precision(max_x,4)
                for min_x, max_x in zip(self.bounds()[::2], self.bounds()[1::2])
            ]
        )

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
                cdata = "<tr><td><b> cell data array </b></td><td>" + name + "</td></tr>"

        pts = self.points()
        cm = np.mean(pts, axis=0)

        all = [
            "<table>",
            "<tr>",
            "<td>", image, "</td>",
            "<td style='text-align: center; vertical-align: center;'><br/>", help_text,
            "<table>",
            "<tr><td><b> bounds </b> <br/> (x/y/z) </td><td>" + str(bounds) + "</td></tr>",
            "<tr><td><b> center of mass </b></td><td>" + utils.precision(cm,3) + "</td></tr>",
            # "<tr><td><b> average size </b></td><td>" + str(average_size) + "</td></tr>",
            "<tr><td><b> nr. points&nbsp/&nbspcells </b></td><td>"
            + str(self.npoints) + "&nbsp/&nbsp" + str(self.ncells) + "</td></tr>",
            pdata,
            cdata,
            "</table>",
            "</table>",
        ]
        return "\n".join(all)

    def clone(self):
        """Clone the UGrid object to yield an exact copy."""
        ugCopy = vtk.vtkUnstructuredGrid()
        ugCopy.DeepCopy(self._data)

        cloned = UGrid(ugCopy)
        pr = self.GetProperty()
        if isinstance(pr, vtk.vtkVolumeProperty):
            prv = vtk.vtkVolumeProperty()
        else:
            prv = vtk.vtkProperty()
        prv.DeepCopy(pr)
        cloned.SetProperty(prv)
        cloned.property = prv

        # assign the same transformation to the copy
        cloned.SetOrigin(self.GetOrigin())
        cloned.SetScale(self.GetScale())
        cloned.SetOrientation(self.GetOrientation())
        cloned.SetPosition(self.GetPosition())
        cloned.name = self.name

        cloned.pipeline = utils.OperationNode(
            "clone", parents=[self], shape='diamond', c='#bbe1ed',
        )
        return cloned

    def color(self, c=False, alpha=None):
        """
        Set/get UGrid color.
        If None is passed as input, will use colors from active scalars.
        Same as `ugrid.c()`.
        """
        if c is False:
            return np.array(self.GetProperty().GetColor())
        if c is None:
            self._mapper.ScalarVisibilityOn()
            return self
        self._mapper.ScalarVisibilityOff()
        cc = colors.get_color(c)
        self.property.SetColor(cc)
        if self.trail:
            self.trail.GetProperty().SetColor(cc)
        if alpha is not None:
            self.alpha(alpha)
        return self

    def alpha(self, opacity=None):
        """Set/get mesh's transparency. Same as `mesh.opacity()`."""
        if opacity is None:
            return self.property.GetOpacity()

        self.property.SetOpacity(opacity)
        bfp = self.GetBackfaceProperty()
        if bfp:
            if opacity < 1:
                self._bfprop = bfp
                self.SetBackfaceProperty(None)
            else:
                self.SetBackfaceProperty(self._bfprop)
        return self

    def opacity(self, alpha=None):
        """Set/get mesh's transparency. Same as `mesh.alpha()`."""
        return self.alpha(alpha)

    def wireframe(self, value=True):
        """Set mesh's representation as wireframe or solid surface.
        Same as `mesh.wireframe()`."""
        if value:
            self.property.SetRepresentationToWireframe()
        else:
            self.property.SetRepresentationToSurface()
        return self

    def linewidth(self, lw=None):
        """Set/get width of mesh edges. Same as `lw()`."""
        if lw is not None:
            if lw == 0:
                self.property.EdgeVisibilityOff()
                self.property.SetRepresentationToSurface()
                return self
            self.property.EdgeVisibilityOn()
            self.property.SetLineWidth(lw)
        else:
            return self.property.GetLineWidth()
        return self

    def lw(self, linewidth=None):
        """Set/get width of mesh edges. Same as `linewidth()`."""
        return self.linewidth(linewidth)

    def linecolor(self, lc=None):
        """Set/get color of mesh edges. Same as `lc()`."""
        if lc is not None:
            if "ireframe" in self.property.GetRepresentationAsString():
                self.property.EdgeVisibilityOff()
                self.color(lc)
                return self
            self.property.EdgeVisibilityOn()
            self.property.SetEdgeColor(colors.get_color(lc))
        else:
            return self.property.GetEdgeColor()
        return self

    def lc(self, linecolor=None):
        """Set/get color of mesh edges. Same as `linecolor()`."""
        return self.linecolor(linecolor)

    def extract_cell_type(self, ctype):
        """Extract a specific cell type and return a new `UGrid`."""
        uarr = self._data.GetCellTypesArray()
        ctarrtyp = np.where(utils.vtk2numpy(uarr) == ctype)[0]
        uarrtyp = utils.numpy2vtk(ctarrtyp, deep=False, dtype="id")
        selection_node = vtk.vtkSelectionNode()
        selection_node.SetFieldType(vtk.vtkSelectionNode.CELL)
        selection_node.SetContentType(vtk.vtkSelectionNode.INDICES)
        selection_node.SetSelectionList(uarrtyp)
        selection = vtk.vtkSelection()
        selection.AddNode(selection_node)
        es = vtk.vtkExtractSelection()
        es.SetInputData(0, self._data)
        es.SetInputData(1, selection)
        es.Update()
        ug = UGrid(es.GetOutput())

        ug.pipeline = utils.OperationNode(
            "extract_cell_type", comment=f"type {ctype}",
            c="#edabab", parents=[self],
        )
        return ug