from . import com

class Application:
    def show(self):
        pass

    def maximise(self):
        pass

    def minimise(self):
        pass

    def close(self):
        pass

    @property
    def borehole_documents(self):
        """ A collection of borehole documents open in the application. """
        pass

    def open_borehole_document(self, filename):
        """ Opens a borehole document in the application and returns it. """
        pass

    def new_borehole_document(self):
        """ Creates a new borehole document and returns it. """
        pass
    
    @property
    def version(self):
        """ The version number of the running WellCAD application. """
        pass

    """ ????
    def minimise_borehole_document(self, document):
        pass

    def cascade_borehole_documents(self):
        pass
    """

class BoreholeDocumentCollection:
    def append(self):
        """ Adds a borehole document to the collection. """
    
    def remove(self, name):
        """ Removes a borehole document from this collection by name or index. """
    
    def __iter__(self):
        """ Iterate over the collection. """
    
    def __getitem__(self, name):
        """ Returns a borehole document by name or index. """


""" File Writers"""
class LasWriter:
    pass


class DlisWriter:
    pass


class TextWriter:
    pass
""" /end File Writers """


class Range:
    """ Represents a range. """

    @property
    def max(self):
        pass

    @property
    def min(self):
        pass


class BoreholeDocument:
    def __init__(self, filename=None, template=None):
        """ Opens or constructs a new borehole document. """
        pass

    @property
    def name(self):
        """ Returns the name of the borehole document. """
    
    @name.setter
    def name(self, value):
        pass

    def save(self, filename, version=None):
        pass

    def export_file(self, filename, writer=None):
        """ Exports a file using the specified writer. If no writer is specified, autodetect based on file extension. """
        pass

    def import_file(self, filename, reader=None):
        """ Imports a file using the specified reader. If no reader is specified, autodetect based on file extension. """
        pass

    @property
    def range(self):
        """ The depth or time range for this borehole document. """
        pass

    """ Where should the borehole document visibility and application view go? Stuff like minimise(), maximise(), ... Application? """

    # Big questions about this one below. If every log has its own reference, what does the master log do? Is it
    # only for display?
    @property
    def reference(self):
        """ The depth or time or other reference log. """
        pass

    @property
    def logs(self):
        """ Return a collection of logs in the borehole document. """
        pass

    @property
    def headers(self):
        """ Returns a collection of borehole headers. """
        pass

    @property
    def trailers(self):
        """ Returns a collection of borehole trailers. """
        pass

    @property
    def workspaces(self):
        """ Returns a collection of workspaces in the borehole document.
        
        Big question here about whether workspaces should be in a borehole document. """
        pass

    @property
    def charts(self):
        """ Returns a collection of charts (crossplot, deviation, polar and rose).
        
        Big question here about whether charts should be in a borehole document. And are they really just workspaces with another name? """
        pass

    @property
    def annotation_layers(self):
        """ Returns a collection of annotation layers. """
        pass

    @property
    def metadata(self):
        """ Returns metadata for the borehole document. """


class Log:
    def __init__(self):
        pass


class ArrayAxis:
    @property
    def units(self):
        """ The units for this axis. """
        pass

    @property
    def values(self):
        """ Values for this axis. """
        pass

    @property
    def evenly_spaced(self):
        """ Whether or not this axis is evenly spaced. """
        pass

    @property
    def wrapped(self):
        """ Whether this axis wraps (like an azimuth). """
        pass

    @property
    def monotonic(self):
        """ Whether this axis is monotonic.
        
        Big question about whether WellCAD should allow non-monotonic logs. """
        pass
    
    @property
    def range(self):
        """ The range (max and min) of this axis. """
        pass

class ConstantSampledArrayAxis(ArrayAxis):
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
    
    @property
    def values(self):
        return np.arange(self.start, self.stop, self.step)
    
    @property
    def monotonic(self):
        return True
    
    @property
    def evenly_spaced(self):
        return True


class ArrayLog:
    @property
    def axes(self):
        """ Returns a list of reference axes.
        
        For example, if this is a 1D array, this will return all depths or times for each "row":
        [ArrayAxis()]

        If this is a 2D array, it will return all depths/times, and all azimuths.
        [ArrayAxis(), ArrayAxis()]
        """
        pass
    
    @property
    def values(self):
        """ Returns a numpy array representing the values for this log.

        Allows editing of data live (this is a huge task).
        """
        pass

    @property
    def units(self):
        """ Returns the units of this log. """
        pass

    @property
    def shape(self):
        """ Returns the shape of the array this log represents. """
        pass

    @property
    def dtype(self):
        """ Returns the datatype of the values in this array. """
        pass

    @property
    def ndims(self):
        """ Returns the number of dimensions for this array. """
        pass


log = ArrayLog()
# Allowed
log.values[10:50] *= 2
# Forbidden, unless shapes match.
log.values = np.random(10, 20)

app = Application()
bh = BoreholeDocument("some_file.wcl")
app.borehole_documents.append(bh)

bh = BoreholeDocument("file.wcl")
bh.export("output.las")