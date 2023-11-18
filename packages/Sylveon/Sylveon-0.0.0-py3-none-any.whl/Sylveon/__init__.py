from .array_generator import ArrayGen
from .io_file import IOFile
from .graph_generator import GraphGen
from .string_generator import StringGen
from .graph import Graph
from .utils.rand import *

from random import randint, uniform, random, choices, sample

class Gen(ArrayGen, GraphGen, StringGen):
    pass