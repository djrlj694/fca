# -*- coding: utf-8 -*-
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(name             = "fca",
      version          = "0.0.1",
      author           = "Nikita Romashkin",
      author_email     = "romashkin.nikita@gmail.com",
      description      = "Python package for formal concept analysis",
      keywords         = ["FCA", "Concept mining", "Mathematics", "lattice theory"],
      license          = "LGPL",
      platforms        = ["Linux", "Mac OS X", "Windows XP/2000/NT"],
)