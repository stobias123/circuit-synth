"""
KiCad PCB API for creating and manipulating PCB files.

This module re-exports from kicad-pcb-api for compatibility.
NEW CODE SHOULD IMPORT DIRECTLY FROM kicad-pcb-api.
"""

from kicad_pcb_api import PCBBoard, PCBParser
from kicad_pcb_api.core.types import Footprint, Layer, Pad
from kicad_pcb_api.footprints.footprint_library import (
    FootprintInfo,
    FootprintLibraryCache,
    get_footprint_cache,
)

from .kicad_cli import DRCResult, KiCadCLI, KiCadCLIError, get_kicad_cli

__all__ = [
    "PCBBoard",
    "PCBParser",
    "Footprint",
    "Pad",
    "Layer",
    "KiCadCLI",
    "get_kicad_cli",
    "DRCResult",
    "KiCadCLIError",
    "FootprintLibraryCache",
    "FootprintInfo",
    "get_footprint_cache",
]
