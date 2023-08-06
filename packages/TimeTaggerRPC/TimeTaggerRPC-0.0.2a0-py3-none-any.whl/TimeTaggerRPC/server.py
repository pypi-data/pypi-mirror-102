import inspect

import Pyro5.api
import TimeTagger as TT

from . import helper



EXCLUDED_LIBRARY_MEMBERS = [
    'TimeTaggerBase', 'TimeTaggerVirtual', 'createTimeTaggerVirtual', 
    'Iterator', 'IteratorBase',
    'CustomMeasurement', 'CustomMeasurementBase', 'FlimAbstract', 
    'TimeTagStream', 'FileReader', 
    'setLogger', 'setCustomBitFileName', 'hasTimeTaggerVirtualLicense',
    'flashLicense', 'extractLicenseInfo'
]

EXCLUDED_ITERATOR_ATTRIBUTES = [
    'waitUntilFinished',
]

EXCLUDED_TAGGER_ATTRIBUTES = [
    'factoryAccess'
]


def pyro_proxy2object(self, pyro_proxy):
    """Returns the Pyro object for a given proxy."""
    objectId = pyro_proxy._pyroUri.object
    return self._pyroDaemon.objectsById.get(objectId)


def make_module_function_proxy(func_name: str):

    func = getattr(TT, func_name)
    assert inspect.isfunction(func)

    def func_proxy(self, *args, **kwargs):
        return func(*args, **kwargs)

    func_proxy.__name__ = func.__name__
    func_proxy.__doc__ = func.__doc__
    func_proxy.__signature__ = inspect.signature(func)
    return func_proxy


def make_class_method_proxy(attrib: inspect.Attribute):
    """Creates a proxy methood for the wrapped method
         Copies name, signature and doc-string.
    """
    assert attrib.kind == 'method', 'Must be a class method'

    def method_proxy(self, *args, **kwargs):
        method_handle = getattr(self._obj, attrib.name)
        return method_handle(*args, **kwargs)

    method_proxy.__doc__ = attrib.object.__doc__
    method_proxy.__signature__ = inspect.signature(attrib.object)
    method_proxy.__name__ = attrib.name
    return method_proxy


def make_iterator_adapter_class(class_name: str):
    """Generates adapter class for the given Time Tagger iterator class 
        and exposes them with Pyro.
    """
    iterator_class = getattr(TT, class_name)
    assert issubclass(iterator_class, TT.IteratorBase), 'Must be a TT.Iterator object.'

    # Custom init method
    def __init__(self, tagger_adapter, *args, **kwargs):
        TTClass = getattr(TT, type(self).__name__)
        self._obj = TTClass(tagger_adapter._obj, *args, **kwargs)

    # Copy docstring adn signature
    __init__.__doc__ = iterator_class.__init__.__doc__
    __init__.__signature__ = inspect.signature(iterator_class.__init__)

    methods = {'__init__': __init__}

    # Iterate over all methods of the measurement and create proxy methods
    # print('iterator', class_name)
    for attrib in inspect.classify_class_attrs(iterator_class):
        if attrib.name in EXCLUDED_ITERATOR_ATTRIBUTES:
            continue
        if attrib.name.startswith('_'):
            continue
        if attrib.kind == 'method':
            # print('| --> ', attrib.name)
            methods[attrib.name] = make_class_method_proxy(attrib)
    
    # Expose class methods with Pyro
    IteratorAdapter = Pyro5.api.expose(type(class_name, (), methods))
    return IteratorAdapter


def make_synchronized_measurements_adaptor_class():
    """Generates adapter class for the given Time Tagger iterator class 
        and exposes them with Pyro.
    """
    Cls = TT.SynchronizedMeasurements
    class_name = Cls.__name__

    # Custom methods method
    def __init__(self, tagger_adaptor):
        self._obj = TT.SynchronizedMeasurements(tagger_adaptor._obj)

    def registerMeasurement(self, measurement_proxy):
        iterator_adaptor = pyro_proxy2object(self, measurement_proxy)
        return self._obj.registerMeasurement(iterator_adaptor._obj)

    def unregisterMeasurement(self, measurement_proxy):
        iterator_adaptor = pyro_proxy2object(self, measurement_proxy)
        return self._obj.unregisterMeasurement(iterator_adaptor._obj)

    # Possible but does not work yet
    # def getTagger(self):
    #     tagger = self._obj.getTagger()
    #     # Requires separate adaptor generator
    #     # TimeTaggerAdaptor = make_timetagger_adapter_class(type(tagger).__name__)
    #     tagger_adaptor = TimeTaggerAdaptor(tagger)
    #     self._pyroDaemon.register(tagger_adaptor)
    #     return tagger_adaptor

    # Copy docstring adn signature
    __init__.__doc__ = Cls.__init__.__doc__
    __init__.__signature__ = inspect.signature(Cls.__init__)

    methods = {
        '__init__': __init__,
        'registerMeasurement': registerMeasurement,
        'unregisterMeasurement': unregisterMeasurement,
        # 'getTagger': getTagger,
        }

    # Iterate over all methods of the measurement and create proxy methods
    # print('object', class_name)
    for attrib in inspect.classify_class_attrs(Cls):
        if attrib.name in methods:
            continue
        if attrib.name in EXCLUDED_ITERATOR_ATTRIBUTES + ['getTagger']:
            continue
        if attrib.name.startswith('_'):
            continue
        if attrib.kind == 'method':
            # print(' --> ', attrib.name)
            methods[attrib.name] = make_class_method_proxy(attrib)
    
    # Expose class methods with Pyro
    IteratorAdapter = Pyro5.api.expose(type(class_name, (), methods))
    return IteratorAdapter


def make_timetagger_adapter_class(class_name: str):

    tagger_class = getattr(TT, class_name)
    assert issubclass(tagger_class, TT.TimeTaggerBase), 'Must be a TT.TimeTaggerBase object.'

    # Custom init method
    def __init__(self, *args, **kwargs):
        TimeTaggerCreator = getattr(TT, 'create'+class_name)
        self._obj = TimeTaggerCreator(*args, **kwargs)

    # Copy docstring adn signature
    __init__.__doc__ = tagger_class.__init__.__doc__
    __init__.__signature__ = inspect.signature(tagger_class.__init__)

    methods = {'__init__': __init__}

    # Iterate over all methods of the measurement and create proxy methods
    # print('tagger', class_name)
    for attrib in inspect.classify_class_attrs(tagger_class):
        if attrib.name in EXCLUDED_TAGGER_ATTRIBUTES:
            continue
        if attrib.name.startswith('_'):
            continue
        if attrib.kind == 'method':
            # print(' --> ', attrib.name)
            methods[attrib.name] = make_class_method_proxy(attrib)

    # Expose class methods with Pyro
    TaggerAdapterClass = Pyro5.api.expose(type(class_name, (), methods))
    return TaggerAdapterClass


def make_iterator_constructor(iterator_name: str):
    """Creates a method that constructs the Time Tagger Iterator object and its adaptor.
        The constructor method will be exposed via Pyro and allows creation of the measurements 
        and virtual channels via the TimeTaggerRPC interface.
    """

    AdapterClass = make_iterator_adapter_class(iterator_name)

    def constructor(self, tagger_proxy, *args, **kwargs): 
        tagger_adapter = pyro_proxy2object(self, tagger_proxy)
        pyro_obj = AdapterClass(tagger_adapter, *args, **kwargs)
        self._pyroDaemon.register(pyro_obj)
        return pyro_obj
    constructor.__name__ = AdapterClass.__name__
    constructor.__doc__ = AdapterClass.__doc__
    constructor.__signature__ = inspect.signature(AdapterClass.__init__)
    return constructor


def make_synchronized_measurement_constructor():
    """Creates a method that constructs the SynchronizedMeasurements object and its adaptor.
        The constructor method will be exposed via Pyro and allows creation of the measurements 
        and virtual channels via the TimeTaggerRPC interface.
    """

    AdapterClass = make_synchronized_measurements_adaptor_class()

    def constructor(self, tagger_proxy, *args, **kwargs): 
        tagger_adapter = pyro_proxy2object(self, tagger_proxy)
        pyro_obj = AdapterClass(tagger_adapter)
        self._pyroDaemon.register(pyro_obj)
        return pyro_obj
    constructor.__name__ = AdapterClass.__name__
    constructor.__doc__ = AdapterClass.__doc__
    constructor.__signature__ = inspect.signature(AdapterClass.__init__)
    return constructor


def make_tagger_constructor(class_name: str):
    """Creates a method that constructs the Time Tagger object and its adaptor.
        The constructor method will be exposed via Pyro and allows creation 
        of time taggers via the TimeTaggerRPC interface.
    """
    TimeTaggerAdaptor = make_timetagger_adapter_class(class_name)

    def constructor(self, *args, **kwargs):
        pyro_obj = TimeTaggerAdaptor(*args, **kwargs)
        self._pyroDaemon.register(pyro_obj)
        return pyro_obj
    constructor.__name__ = 'create'+TimeTaggerAdaptor.__name__
    constructor.__doc__ = TimeTaggerAdaptor.__init__.__doc__
    constructor.__signature__ = inspect.signature(TimeTaggerAdaptor.__init__)
    return constructor


def make_timetagger_library_adapter():
    """Creates an adapter class for the Time Tagger library and exposes it with Pyro.
        This class is an entry point for remote connections.
    """

    # Manually defined functions and helpers
    def freeTimeTagger(self, tagger_proxy):
        tagger_adapter = pyro_proxy2object(self, tagger_proxy)
        self._pyroDaemon.unregister(tagger_adapter)
        return TT.freeTimeTagger(tagger_adapter._obj)

    TimeTaggerRPC_methods = {
        "freeTimeTagger": freeTimeTagger,
    }

    # Create classes
    for name, Cls in inspect.getmembers(TT, predicate=inspect.isclass):
        if name in EXCLUDED_LIBRARY_MEMBERS:
            continue
        if name.startswith('_'):
            continue
        if issubclass(Cls, TT.IteratorBase):
            TimeTaggerRPC_methods[name] = make_iterator_constructor(name)
        elif issubclass(Cls, TT.TimeTaggerBase):
            TimeTaggerRPC_methods['create'+name] = make_tagger_constructor(name)
        elif issubclass(Cls, TT.SynchronizedMeasurements):
            TimeTaggerRPC_methods[name] = make_synchronized_measurement_constructor()

    # Create module level functions
    for name, func in inspect.getmembers(TT, predicate=inspect.isfunction):
        if name in TimeTaggerRPC_methods:
            continue
        if name in EXCLUDED_LIBRARY_MEMBERS:
            continue
        if name.startswith('_'):
            continue
        # print('function', name)
        TimeTaggerRPC_methods[name] = make_module_function_proxy(name)

    # Construct and expose the final RPC adapter class
    TimeTaggerRPC = Pyro5.api.expose(type("TimeTaggerRPC", (), TimeTaggerRPC_methods))
    return TimeTaggerRPC


def start_server(host='localhost', port=23000, use_ns=False, start_ns=False):
    """This method start the Pyro server eventloop and processes client requests."""

    # Start Pyro nameserver in a subprocess
    if start_ns:
        import subprocess
        ns_proc = subprocess.Popen(
            ['python', '-m', 'Pyro5.nameserver', '-n', host])

    try:
        with Pyro5.api.Daemon(host=host, port=port) as daemon:
            # register native numpy arrays
            helper.register_numpy_handler()

            # register the Pyro class
            TimeTaggerRPC = make_timetagger_library_adapter()
            uri = daemon.register(TimeTaggerRPC, 'TimeTagger')
            print('Server URI=', uri)
            if use_ns:
                ns = Pyro5.api.locate_ns()         # find the name server
                # register the object with a name in the name server
                ns.register("TimeTagger", uri)
            # start the event loop of the server to wait for calls
            daemon.requestLoop()
    except KeyboardInterrupt:
        pass
    finally:
        if start_ns:
            ns_proc.terminate()


if __name__ == "__main__":
    start_server()
    pass
