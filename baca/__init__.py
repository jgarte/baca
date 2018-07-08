import abjad
from .library import *
from .divisionlib import *
from .dynamiclib import *
from .indicatorlib import *
from .markuplib import Markup
from .overridelib import *
from .pitcharraylib import *
from .pitchlib import *
from .registerlib import *
from .rhythmlib import *
from .settinglib import *
from .spannerlib import *
from .templatelib import *
from . import markuplib

# classes
from .AccidentalAdjustmentCommand import AccidentalAdjustmentCommand
from .AnchorSpecifier import AnchorSpecifier
from .BCPCommand import BCPCommand
from .BreakMeasureMap import BreakMeasureMap
from .ClusterCommand import ClusterCommand
from .Coat import Coat
from .ColorCommand import ColorCommand
from .ColorFingeringCommand import ColorFingeringCommand
from .Command import Command
from .Command import Map
from .Command import Suite
from .CommandWrapper import CommandWrapper
from .ContainerCommand import ContainerCommand
from .Counter import Counter
from .Cursor import Cursor
from .DesignMaker import DesignMaker
from .DiatonicClusterCommand import DiatonicClusterCommand
from .IndicatorBundle import IndicatorBundle
from .Expression import Expression
from .ExpressionGallery import ExpressionGallery
from .GlobalFermataCommand import GlobalFermataCommand
from .HarmonicSeries import HarmonicSeries
from .HorizontalSpacingSpecifier import HorizontalSpacingSpecifier
from .ImbricationCommand import ImbricationCommand
from .IndicatorCommand import IndicatorCommand
from .InstrumentChangeCommand import InstrumentChangeCommand
from .Interpolator import Interpolator
from .LMRSpecifier import LMRSpecifier
from .LabelCommand import LabelCommand
from .Loop import Loop
from .MeasureWrapper import MeasureWrapper
from .MetronomeMarkCommand import MetronomeMarkCommand
from .MetronomeMarkMeasureMap import MetronomeMarkMeasureMap
from .MicrotoneDeviationCommand import MicrotoneDeviationCommand
from .MusicAccumulator import MusicAccumulator
from .MusicContribution import MusicContribution
from .MusicMaker import MusicMaker
from .NestingCommand import NestingCommand
from .OctaveDisplacementCommand import OctaveDisplacementCommand
from .PaddedTuple import PaddedTuple
from .PageSpecifier import PageSpecifier
from .PartAssignmentCommand import PartAssignmentCommand
from .Partial import Partial
from .PersistentIndicatorTests import PersistentIndicatorTests
from .PiecewiseIndicatorCommand import PiecewiseIndicatorCommand
from .PitchCommand import PitchCommand
from .PitchSpecifier import PitchSpecifier
from .RestAffixSpecifier import RestAffixSpecifier
from .SchemeManifest import SchemeManifest
from .Scope import Scope
from .SegmentMaker import SegmentMaker
from .Selection import Selection
from .Sequence import Sequence
from .SpacingIndication import SpacingIndication
from .SpacingSection import SpacingSection
from .StaffPositionCommand import StaffPositionCommand
from .StaffPositionInterpolationCommand import \
    StaffPositionInterpolationCommand
from .StageMeasureMap import StageMeasureMap
from .SystemSpecifier import SystemSpecifier
from .TieCorrectionCommand import TieCorrectionCommand
from .TimeSignatureGroups import TimeSignatureGroups
from .TimeSignatureMaker import TimeSignatureMaker
from .TimelineScope import TimelineScope
from .Tree import Tree
from .VoltaCommand import VoltaCommand
from .WellformednessManager import WellformednessManager

# expression constructors
from .pitchlib import _pitch_class_segment as pitch_class_segment
from .pitchlib import _pitch_class_set as pitch_class_set
from .pitchlib import _pitch_set as pitch_set
from .pitchlib import _pitch_segment as pitch_segment
from .Selection import _select as select
from .Sequence import _sequence as sequence

def _publish_selectors(class_):
    for name in dir(class_):
        if name.startswith('_'):
            continue
        if name in ('map',):
            continue
        statement = f"""def {name}(*arguments, **keywords):
            return select().{name}(*arguments, **keywords)"""
        exec(statement, globals())

from .LibraryAF import *
from .LibraryGM import *
from .LibraryNS import *
from .LibraryTZ import *

_publish_selectors(Selection)
