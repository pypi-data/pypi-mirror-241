# coding: utf-8
import ctypes
import numpy as np
from pathlib import Path
import platform

try: from . import conlib
except: import conlib

# coding: utf-8
import ctypes
import numpy as np
from pathlib import Path
import platform

try: from . import conlib
except: import conlib

_dll_map = {"Linux":"libort.so", "Windows": "libort.dll", "Darwin": None}
dll_path=str(Path(__file__).parent.joinpath(_dll_map.get(platform.system())).resolve())
print(dll_path)
assert Path(dll_path).exists()
_libc = ctypes.cdll.LoadLibrary(dll_path)
assert _libc is not None

SHAPE_T = ctypes.c_int*8
class CTENSOR(ctypes.Structure):
    _fields_ = [
        ("buffer", ctypes.c_void_p),
        ("shape", SHAPE_T),
        ("ndim", ctypes.c_int),
        ("kind", ctypes.c_int),
        ("itemsize", ctypes.c_int),
        ("alloc", ctypes.c_int),
    ]

_libc.ctensor_free.argtypes = (
    ctypes.POINTER(CTENSOR),
)

_libc.ort_init.argtypes = (
    ctypes.POINTER(ctypes.c_char),
)
_libc.ort_init.restype = ctypes.c_void_p

_libc.ort_release.argtypes = (
    ctypes.c_void_p,
)
_libc.ort_release.restype = ctypes.c_int

_libc.ort_run.argtypes = (
    ctypes.c_void_p,
    ctypes.POINTER(CTENSOR),
    ctypes.POINTER(CTENSOR),
)
_libc.ort_run.restype = ctypes.c_int

def ndarray2ctensor(*args):
    t = (CTENSOR*len(args))()
    for i, arr in enumerate(args):
        assert arr.flags['C_CONTIGUOUS']
        t[i].buffer = ctypes.cast(np.ctypeslib.as_ctypes(arr), ctypes.c_void_p)
        t[i].kind = int(ord(arr.dtype.kind))
        t[i].itemsize = int(arr.dtype.itemsize)
        t[i].alloc = 0
        t[i].ndim = arr.ndim
        t[i].shape = SHAPE_T(*arr.shape)  
    return t

def str2ctensor(s):
    t = (CTENSOR*1)()
    i = 0
    s = s.encode()
    t[i].buffer = ctypes.cast(ctypes.create_string_buffer(s), ctypes.c_void_p) 
    t[i].kind = int(ord('u'))
    t[i].itemsize = 1
    t[i].alloc = 0
    t[i].ndim = 1
    t[i].shape = SHAPE_T(len(s)+1)
    return t  

def ctensor2ndarray(t, deepcopy=False):
    if t.ndim <= 0: return None
    if t.kind == ord('u') and t.itemsize == 1:
        buffer = ctypes.cast(t.buffer, ctypes.POINTER(ctypes.c_uint8))
    elif t.kind == ord('i') and t.itemsize == 4:
        buffer = ctypes.cast(t.buffer, ctypes.POINTER(ctypes.c_int32))
    elif t.kind == ord('i') and t.itemsize == 8:
        buffer = ctypes.cast(t.buffer, ctypes.POINTER(ctypes.c_int64))
    elif t.kind == ord('f') and t.itemsize == 4:
        buffer = ctypes.cast(t.buffer, ctypes.POINTER(ctypes.c_float))
    elif t.kind == ord('f') and t.itemsize == 8:
        buffer = ctypes.cast(t.buffer, ctypes.POINTER(ctypes.c_double))
    else:
        print(chr(t.kind), t.itemsize, t.kind == ord('i') and t.itemsize == 4)
        raise NotImplementedError(f"{chr(t.kind)} {t.itemsize} {t.kind == ord('i') and t.itemsize == 4}")
    shape = []
    for _ in range(t.ndim):
        shape.append(t.shape[_])
    arr = np.ctypeslib.as_array(buffer, shape=shape)    
    if deepcopy: return arr.copy()
    return arr


class Ort(object):
    def __init__(self, **kwargs) -> None:
        self.model_path = str(kwargs["model_path"])
        self.input_names = kwargs.get("input_names", [])
        self.output_names = kwargs.get("output_names", [])

        self._model = _libc.ort_init(conlib.dumps(dict(
            model_path=self.model_path,
            input_names=self.input_names,
            output_names=self.output_names,
        )).encode("utf-8"))   

    def __del__(self):
        _libc.ort_release(self._model)

    def run(self, inputs):
        assert len(inputs) == len(self.input_names)
        cinputs  = ndarray2ctensor(*inputs) 
        coutputs = (CTENSOR*len(self.output_names))()
        _libc.ort_run(self._model, cinputs, coutputs)

        outputs = []
        for _ in range(len(self.output_names)):
            outputs.append(ctensor2ndarray(coutputs[_], True))

        return outputs

