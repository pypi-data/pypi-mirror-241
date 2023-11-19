import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def active_frame_delete(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Delete the active frame for the active Grease Pencil Layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def active_frames_delete_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Delete the active frame(s) of all editable Grease Pencil layers

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def annotate(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             mode: typing.Optional[typing.Any] = 'DRAW',
             arrowstyle_start: typing.Optional[typing.Any] = 'NONE',
             arrowstyle_end: typing.Optional[typing.Any] = 'NONE',
             use_stabilizer: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
             stabilizer_factor: typing.Optional[typing.Any] = 0.75,
             stabilizer_radius: typing.Optional[typing.Any] = 35,
             stroke: typing.Optional[bpy.types.bpy_prop_collection[
                 'bpy.types.OperatorStrokeElement']] = None,
             wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True):
    ''' Make annotations on the active data

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Way to interpret mouse movements * ``DRAW`` Draw Freehand, Draw freehand stroke(s). * ``DRAW_STRAIGHT`` Draw Straight Lines, Draw straight line segment(s). * ``DRAW_POLY`` Draw Poly Line, Click to place endpoints of straight line segments (connected). * ``ERASER`` Eraser, Erase Annotation strokes.
    :type mode: typing.Optional[typing.Any]
    :param arrowstyle_start: Start Arrow Style, Stroke start style * ``NONE`` None, Don't use any arrow/style in corner. * ``ARROW`` Arrow, Use closed arrow style. * ``ARROW_OPEN`` Open Arrow, Use open arrow style. * ``ARROW_OPEN_INVERTED`` Segment, Use perpendicular segment style. * ``DIAMOND`` Square, Use square style.
    :type arrowstyle_start: typing.Optional[typing.Any]
    :param arrowstyle_end: End Arrow Style, Stroke end style * ``NONE`` None, Don't use any arrow/style in corner. * ``ARROW`` Arrow, Use closed arrow style. * ``ARROW_OPEN`` Open Arrow, Use open arrow style. * ``ARROW_OPEN_INVERTED`` Segment, Use perpendicular segment style. * ``DIAMOND`` Square, Use square style.
    :type arrowstyle_end: typing.Optional[typing.Any]
    :param use_stabilizer: Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active)
    :type use_stabilizer: typing.Optional[typing.Union[bool, typing.Any]]
    :param stabilizer_factor: Stabilizer Stroke Factor, Higher values gives a smoother stroke
    :type stabilizer_factor: typing.Optional[typing.Any]
    :param stabilizer_radius: Stabilizer Stroke Radius, Minimum distance from last point before stroke continues
    :type stabilizer_radius: typing.Optional[typing.Any]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def annotation_active_frame_delete(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Delete the active frame for the active Annotation Layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def annotation_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add new Annotation data-block

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def bake_mesh_animation(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        target: typing.Optional[typing.Any] = 'NEW',
        frame_start: typing.Optional[typing.Any] = 1,
        frame_end: typing.Optional[typing.Any] = 250,
        step: typing.Optional[typing.Any] = 1,
        thickness: typing.Optional[typing.Any] = 1,
        angle: typing.Optional[typing.Any] = 1.22173,
        offset: typing.Optional[typing.Any] = 0.001,
        seams: typing.Optional[typing.Union[bool, typing.Any]] = False,
        faces: typing.Optional[typing.Union[bool, typing.Any]] = True,
        only_selected: typing.Optional[typing.Union[bool, typing.Any]] = False,
        frame_target: typing.Optional[typing.Any] = 1,
        project_type: typing.Optional[typing.Any] = 'VIEW'):
    ''' Bake mesh animation to grease pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param target: Target Object, Target grease pencil
    :type target: typing.Optional[typing.Any]
    :param frame_start: Start Frame, The start frame
    :type frame_start: typing.Optional[typing.Any]
    :param frame_end: End Frame, The end frame of animation
    :type frame_end: typing.Optional[typing.Any]
    :param step: Step, Step between generated frames
    :type step: typing.Optional[typing.Any]
    :param thickness: Thickness
    :type thickness: typing.Optional[typing.Any]
    :param angle: Threshold Angle, Threshold to determine ends of the strokes
    :type angle: typing.Optional[typing.Any]
    :param offset: Stroke Offset, Offset strokes from fill
    :type offset: typing.Optional[typing.Any]
    :param seams: Only Seam Edges, Convert only seam edges
    :type seams: typing.Optional[typing.Union[bool, typing.Any]]
    :param faces: Export Faces, Export faces as filled strokes
    :type faces: typing.Optional[typing.Union[bool, typing.Any]]
    :param only_selected: Only Selected Keyframes, Convert only selected keyframes
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param frame_target: Target Frame, Destination frame
    :type frame_target: typing.Optional[typing.Any]
    :param project_type: Projection Type * ``KEEP`` No Reproject. * ``FRONT`` Front, Reproject the strokes using the X-Z plane. * ``SIDE`` Side, Reproject the strokes using the Y-Z plane. * ``TOP`` Top, Reproject the strokes using the X-Y plane. * ``VIEW`` View, Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement. * ``CURSOR`` Cursor, Reproject the strokes using the orientation of 3D cursor.
    :type project_type: typing.Optional[typing.Any]
    '''

    pass


def blank_frame_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        all_layers: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Insert a blank frame on the current frame (all subsequently existing frames, if any, are shifted right by one frame)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param all_layers: All Layers, Create blank frame in all layers, not only active
    :type all_layers: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def brush_reset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset brush to default parameters

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def brush_reset_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Delete all mode brushes and recreate a default set

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def convert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'PATH',
        bevel_depth: typing.Optional[typing.Any] = 0.0,
        bevel_resolution: typing.Optional[typing.Any] = 0,
        use_normalize_weights: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = True,
        radius_multiplier: typing.Optional[typing.Any] = 1.0,
        use_link_strokes: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        timing_mode: typing.Optional[typing.Any] = 'FULL',
        frame_range: typing.Optional[typing.Any] = 100,
        start_frame: typing.Optional[typing.Any] = 1,
        use_realtime: typing.Optional[typing.Union[bool, typing.Any]] = False,
        end_frame: typing.Optional[typing.Any] = 250,
        gap_duration: typing.Optional[typing.Any] = 0.0,
        gap_randomness: typing.Optional[typing.Any] = 0.0,
        seed: typing.Optional[typing.Any] = 0,
        use_timing_data: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Convert the active Grease Pencil layer to a new Curve Object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Which type of curve to convert to * ``PATH`` Path, Animation path. * ``CURVE`` Bezier Curve, Smooth Bezier curve. * ``POLY`` Polygon Curve, Bezier curve with straight-line segments (vector handles).
    :type type: typing.Optional[typing.Any]
    :param bevel_depth: Bevel Depth
    :type bevel_depth: typing.Optional[typing.Any]
    :param bevel_resolution: Bevel Resolution, Bevel resolution when depth is non-zero
    :type bevel_resolution: typing.Optional[typing.Any]
    :param use_normalize_weights: Normalize Weight, Normalize weight (set from stroke width)
    :type use_normalize_weights: typing.Optional[typing.Union[bool, typing.Any]]
    :param radius_multiplier: Radius Factor, Multiplier for the points' radii (set from stroke width)
    :type radius_multiplier: typing.Optional[typing.Any]
    :param use_link_strokes: Link Strokes, Whether to link strokes with zero-radius sections of curves
    :type use_link_strokes: typing.Optional[typing.Union[bool, typing.Any]]
    :param timing_mode: Timing Mode, How to use timing data stored in strokes * ``NONE`` No Timing, Ignore timing. * ``LINEAR`` Linear, Simple linear timing. * ``FULL`` Original, Use the original timing, gaps included. * ``CUSTOMGAP`` Custom Gaps, Use the original timing, but with custom gap lengths (in frames).
    :type timing_mode: typing.Optional[typing.Any]
    :param frame_range: Frame Range, The duration of evaluation of the path control curve
    :type frame_range: typing.Optional[typing.Any]
    :param start_frame: Start Frame, The start frame of the path control curve
    :type start_frame: typing.Optional[typing.Any]
    :param use_realtime: Realtime, Whether the path control curve reproduces the drawing in realtime, starting from Start Frame
    :type use_realtime: typing.Optional[typing.Union[bool, typing.Any]]
    :param end_frame: End Frame, The end frame of the path control curve (if Realtime is not set)
    :type end_frame: typing.Optional[typing.Any]
    :param gap_duration: Gap Duration, Custom Gap mode: (Average) length of gaps, in frames (Note: Realtime value, will be scaled if Realtime is not set)
    :type gap_duration: typing.Optional[typing.Any]
    :param gap_randomness: Gap Randomness, Custom Gap mode: Number of frames that gap lengths can vary
    :type gap_randomness: typing.Optional[typing.Any]
    :param seed: Random Seed, Custom Gap mode: Random generator seed
    :type seed: typing.Optional[typing.Any]
    :param use_timing_data: Has Valid Timing, Whether the converted Grease Pencil layer has valid timing data (internal use)
    :type use_timing_data: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def convert_old_files(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        annotation: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Convert 2.7x grease pencil files to 2.80

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param annotation: Annotation, Convert to Annotations
    :type annotation: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def copy(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None):
    ''' Copy selected Grease Pencil points and strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def data_unlink(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Unlink active Annotation data-block

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def delete(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           type: typing.Optional[typing.Any] = 'POINTS'):
    ''' Delete selected Grease Pencil strokes, vertices, or frames

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Method used for deleting Grease Pencil data * ``POINTS`` Points, Delete selected points and split strokes into segments. * ``STROKES`` Strokes, Delete selected strokes. * ``FRAME`` Frame, Delete active frame.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def dissolve(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             type: typing.Optional[typing.Any] = 'POINTS'):
    ''' Delete selected points without splitting strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Method used for dissolving stroke points * ``POINTS`` Dissolve, Dissolve selected points. * ``BETWEEN`` Dissolve Between, Dissolve points between selected points. * ``UNSELECT`` Dissolve Unselect, Dissolve all unselected points.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def draw(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'DRAW',
        stroke: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        disable_straight: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        disable_fill: typing.Optional[typing.Union[bool, typing.Any]] = False,
        disable_stabilizer: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False,
        guide_last_angle: typing.Optional[typing.Any] = 0.0):
    ''' Draw a new stroke in the active Grease Pencil object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Way to interpret mouse movements * ``DRAW`` Draw Freehand, Draw freehand stroke(s). * ``DRAW_STRAIGHT`` Draw Straight Lines, Draw straight line segment(s). * ``ERASER`` Eraser, Erase Grease Pencil strokes.
    :type mode: typing.Optional[typing.Any]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    :param disable_straight: No Straight lines, Disable key for straight lines
    :type disable_straight: typing.Optional[typing.Union[bool, typing.Any]]
    :param disable_fill: No Fill Areas, Disable fill to use stroke as fill boundary
    :type disable_fill: typing.Optional[typing.Union[bool, typing.Any]]
    :param disable_stabilizer: No Stabilizer
    :type disable_stabilizer: typing.Optional[typing.Union[bool, typing.Any]]
    :param guide_last_angle: Angle, Speed guide angle
    :type guide_last_angle: typing.Optional[typing.Any]
    '''

    pass


def duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Duplicate the selected Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def duplicate_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        GPENCIL_OT_duplicate: typing.Optional['duplicate'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Make copies of the selected Grease Pencil strokes and move them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param GPENCIL_OT_duplicate: Duplicate Strokes, Duplicate the selected Grease Pencil strokes
    :type GPENCIL_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def editmode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        back: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Enter/Exit edit mode for Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param back: Return to Previous Mode, Return to previous mode
    :type back: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def extract_palette_vertex(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False,
        threshold: typing.Optional[typing.Any] = 1):
    ''' Extract all colors used in Grease Pencil Vertex and create a Palette

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param selected: Only Selected, Convert only selected strokes
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param threshold: Threshold
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def extrude(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
            execution_context: typing.Optional[typing.Union[str, int]] = None,
            undo: typing.Optional[bool] = None):
    ''' Extrude the selected Grease Pencil points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def extrude_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        GPENCIL_OT_extrude: typing.Optional['extrude'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Extrude selected points and move them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param GPENCIL_OT_extrude: Extrude Stroke Points, Extrude the selected Grease Pencil points
    :type GPENCIL_OT_extrude: typing.Optional['extrude']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def fill(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         on_back: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Fill with color the shape formed by strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param on_back: Draw on Back, Send new stroke to back
    :type on_back: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def frame_clean_duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'ALL'):
    ''' Remove any duplicated frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def frame_clean_fill(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'ACTIVE'):
    ''' Remove 'no fill' boundary strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``ACTIVE`` Active Frame Only, Clean active frame only. * ``ALL`` All Frames, Clean all frames in all layers.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def frame_clean_loose(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        limit: typing.Optional[typing.Any] = 1):
    ''' Remove loose points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param limit: Limit, Number of points to consider stroke as loose
    :type limit: typing.Optional[typing.Any]
    '''

    pass


def frame_duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'ACTIVE'):
    ''' Make a copy of the active Grease Pencil Frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``ACTIVE`` Active, Duplicate frame in active layer only. * ``ALL`` All, Duplicate active frames in all layers.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def generate_weights(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'NAME',
        armature: typing.Optional[typing.Union[str, int, typing.
                                               Any]] = 'DEFAULT',
        ratio: typing.Optional[typing.Any] = 0.1,
        decay: typing.Optional[typing.Any] = 0.8):
    ''' Generate automatic weights for armatures (requires armature modifier)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param armature: Armature, Armature to use
    :type armature: typing.Optional[typing.Union[str, int, typing.Any]]
    :param ratio: Ratio, Ratio between bone length and influence radius
    :type ratio: typing.Optional[typing.Any]
    :param decay: Decay, Factor to reduce influence depending of distance to bone axis
    :type decay: typing.Optional[typing.Any]
    '''

    pass


def guide_rotate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        increment: typing.Optional[typing.Union[bool, typing.Any]] = True,
        angle: typing.Optional[typing.Any] = 0.0):
    ''' Rotate guide angle

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param increment: Increment, Increment angle
    :type increment: typing.Optional[typing.Union[bool, typing.Any]]
    :param angle: Angle, Guide angle
    :type angle: typing.Optional[typing.Any]
    '''

    pass


def hide(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Hide selected/unselected Grease Pencil layers

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected layers
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def image_to_grease_pencil(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        size: typing.Optional[typing.Any] = 0.005,
        mask: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Generate a Grease Pencil Object using Image as source

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param size: Point Size, Size used for grease pencil points
    :type size: typing.Optional[typing.Any]
    :param mask: Generate Mask, Create an inverted image for masking using alpha channel
    :type mask: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def interpolate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        shift: typing.Optional[typing.Any] = 0.0):
    ''' Interpolate grease pencil strokes between frames

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param shift: Shift, Bias factor for which frame has more influence on the interpolated strokes
    :type shift: typing.Optional[typing.Any]
    '''

    pass


def interpolate_reverse(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove breakdown frames generated by interpolating between two Grease Pencil frames

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def interpolate_sequence(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Generate 'in-betweens' to smoothly interpolate between Grease Pencil frames

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_active(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        layer: typing.Optional[typing.Any] = 0):
    ''' Active Grease Pencil layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param layer: Grease Pencil Layer
    :type layer: typing.Optional[typing.Any]
    '''

    pass


def layer_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add new layer or note for the active data-block

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_annotation_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add new Annotation layer or note for the active data-block

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_annotation_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active Annotation layer up/down in the list

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def layer_annotation_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove active Annotation layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_change(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        layer: typing.Optional[typing.Union[str, int, typing.
                                            Any]] = 'DEFAULT'):
    ''' Change active Grease Pencil layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param layer: Grease Pencil Layer
    :type layer: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def layer_duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Make a copy of the active Grease Pencil layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_duplicate_object(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        object: typing.Union[str, typing.Any] = "",
        mode: typing.Optional[typing.Any] = 'ALL'):
    ''' Make a copy of the active Grease Pencil layer to new object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param object: Object, Name of the destination object
    :type object: typing.Union[str, typing.Any]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def layer_isolate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        affect_visibility: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False):
    ''' Toggle whether the active layer is the only one that can be edited and/or visible

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def layer_mask_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = ""):
    ''' Add new layer as masking

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param name: Layer, Name of the layer
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def layer_mask_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove Layer Mask

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_merge(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Merge the current layer with the layer below

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active Grease Pencil layer up/down in the list

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def layer_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove active Grease Pencil layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def lock_all(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None):
    ''' Lock all Grease Pencil layers to prevent them from being accidentally modified

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def lock_layer(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Lock and hide any color not used in any layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_hide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Hide selected/unselected Grease Pencil materials

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected colors
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def material_isolate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        affect_visibility: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False):
    ''' Toggle whether the active material is the only one that is editable and/or visible

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def material_lock_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Lock all Grease Pencil materials to prevent them from being accidentally modified

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_lock_unused(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Lock any material not used in any selected stroke

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_reveal(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Unhide all hidden Grease Pencil materials

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        deselect: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select/Deselect all Grease Pencil strokes using current material

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param deselect: Deselect, Unselect strokes
    :type deselect: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def material_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        slot: typing.Optional[typing.Union[str, int, typing.Any]] = 'DEFAULT'):
    ''' Set active material

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param slot: Material Slot
    :type slot: typing.Optional[typing.Union[str, int, typing.Any]]
    '''

    pass


def material_to_vertex_color(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        remove: typing.Optional[typing.Union[bool, typing.Any]] = True,
        palette: typing.Optional[typing.Union[bool, typing.Any]] = True,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False,
        threshold: typing.Optional[typing.Any] = 3):
    ''' Replace materials in strokes with Vertex Color

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param remove: Remove Unused Materials, Remove any unused material after the conversion
    :type remove: typing.Optional[typing.Union[bool, typing.Any]]
    :param palette: Create Palette, Create a new palette with colors
    :type palette: typing.Optional[typing.Union[bool, typing.Any]]
    :param selected: Only Selected, Convert only selected strokes
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param threshold: Threshold
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def material_unlock_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Unlock all Grease Pencil materials so that they can be edited

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def move_to_layer(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        layer: typing.Optional[typing.Any] = 0):
    ''' Move selected strokes to another layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param layer: Grease Pencil Layer
    :type layer: typing.Optional[typing.Any]
    '''

    pass


def paintmode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        back: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Enter/Exit paint mode for Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param back: Return to Previous Mode, Return to previous mode
    :type back: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def paste(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          type: typing.Optional[typing.Any] = 'ACTIVE',
          paste_back: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Paste previously copied strokes to active layer or to original layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param paste_back: Paste on Back, Add pasted strokes behind all strokes
    :type paste_back: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def primitive_box(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        subdivision: typing.Optional[typing.Any] = 3,
        edges: typing.Optional[typing.Any] = 2,
        type: typing.Optional[typing.Any] = 'BOX',
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Create predefined grease pencil stroke box shapes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: typing.Optional[typing.Any]
    :param edges: Edges, Number of points by edge
    :type edges: typing.Optional[typing.Any]
    :param type: Type, Type of shape
    :type type: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def primitive_circle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        subdivision: typing.Optional[typing.Any] = 94,
        edges: typing.Optional[typing.Any] = 2,
        type: typing.Optional[typing.Any] = 'CIRCLE',
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Create predefined grease pencil stroke circle shapes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: typing.Optional[typing.Any]
    :param edges: Edges, Number of points by edge
    :type edges: typing.Optional[typing.Any]
    :param type: Type, Type of shape
    :type type: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def primitive_curve(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        subdivision: typing.Optional[typing.Any] = 62,
        edges: typing.Optional[typing.Any] = 2,
        type: typing.Optional[typing.Any] = 'CURVE',
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Create predefined grease pencil stroke curve shapes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: typing.Optional[typing.Any]
    :param edges: Edges, Number of points by edge
    :type edges: typing.Optional[typing.Any]
    :param type: Type, Type of shape
    :type type: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def primitive_line(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        subdivision: typing.Optional[typing.Any] = 6,
        edges: typing.Optional[typing.Any] = 2,
        type: typing.Optional[typing.Any] = 'LINE',
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Create predefined grease pencil stroke lines

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: typing.Optional[typing.Any]
    :param edges: Edges, Number of points by edge
    :type edges: typing.Optional[typing.Any]
    :param type: Type, Type of shape
    :type type: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def primitive_polyline(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        subdivision: typing.Optional[typing.Any] = 6,
        edges: typing.Optional[typing.Any] = 2,
        type: typing.Optional[typing.Any] = 'POLYLINE',
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Create predefined grease pencil stroke polylines

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param subdivision: Subdivisions, Number of subdivision by edges
    :type subdivision: typing.Optional[typing.Any]
    :param edges: Edges, Number of points by edge
    :type edges: typing.Optional[typing.Any]
    :param type: Type, Type of shape
    :type type: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def recalc_geometry(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Update all internal geometry data

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def reproject(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'VIEW',
        keep_original: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Projection Type * ``FRONT`` Front, Reproject the strokes using the X-Z plane. * ``SIDE`` Side, Reproject the strokes using the Y-Z plane. * ``TOP`` Top, Reproject the strokes using the X-Y plane. * ``VIEW`` View, Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using 'Cursor' Stroke Placement. * ``SURFACE`` Surface, Reproject the strokes on to the scene geometry, as if drawn using 'Surface' placement. * ``CURSOR`` Cursor, Reproject the strokes using the orientation of 3D cursor.
    :type type: typing.Optional[typing.Any]
    :param keep_original: Keep Original, Keep original strokes and create a copy before reprojecting instead of reproject them
    :type keep_original: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def reset_transform_fill(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'ALL'):
    ''' Reset any UV transformation and back to default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def reveal(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           select: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Show all Grease Pencil layers

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def sculpt_paint(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        stroke: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Apply tweaks to strokes by painting over the strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param wait_for_input: Wait for Input, Enter a mini 'sculpt-mode' if enabled, otherwise, exit after drawing a single stroke
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def sculptmode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        back: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Enter/Exit sculpt mode for Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param back: Return to Previous Mode, Return to previous mode
    :type back: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect: typing.Optional[typing.Union[bool, typing.Any]] = False,
        toggle: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect_all: typing.Optional[typing.Union[bool, typing.Any]] = False,
        entire_strokes: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        location: typing.Optional[typing.Any] = (0, 0),
        use_shift_extend: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False):
    ''' Select Grease Pencil strokes and/or stroke points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect: Deselect, Remove from selection
    :type deselect: typing.Optional[typing.Union[bool, typing.Any]]
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: typing.Optional[typing.Union[bool, typing.Any]]
    :param entire_strokes: Entire Strokes, Select entire strokes instead of just the nearest stroke vertex
    :type entire_strokes: typing.Optional[typing.Union[bool, typing.Any]]
    :param location: Location, Mouse location
    :type location: typing.Optional[typing.Any]
    :param use_shift_extend: Extend
    :type use_shift_extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection of all Grease Pencil strokes currently visible

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle, Toggle selection for all elements. * ``SELECT`` Select, Select all elements. * ``DESELECT`` Deselect, Deselect all elements. * ``INVERT`` Invert, Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_alternate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        unselect_ends: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Select alternative points in same strokes as already selected points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselect_ends: Unselect Ends, Do not select the first and last point of the stroke
    :type unselect_ends: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_box(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        xmin: typing.Optional[typing.Any] = 0,
        xmax: typing.Optional[typing.Any] = 0,
        ymin: typing.Optional[typing.Any] = 0,
        ymax: typing.Optional[typing.Any] = 0,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mode: typing.Optional[typing.Any] = 'SET'):
    ''' Select Grease Pencil strokes within a rectangular region

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    :param mode: Mode * ``SET`` Set, Set a new selection. * ``ADD`` Extend, Extend existing selection. * ``SUB`` Subtract, Subtract existing selection. * ``XOR`` Difference, Inverts existing selection. * ``AND`` Intersect, Intersect existing selection.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def select_circle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        x: typing.Optional[typing.Any] = 0,
        y: typing.Optional[typing.Any] = 0,
        radius: typing.Optional[typing.Any] = 25,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mode: typing.Optional[typing.Any] = 'SET'):
    ''' Select Grease Pencil strokes using brush selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param x: X
    :type x: typing.Optional[typing.Any]
    :param y: Y
    :type y: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    :param mode: Mode * ``SET`` Set, Set a new selection. * ``ADD`` Extend, Extend existing selection. * ``SUB`` Subtract, Subtract existing selection.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def select_first(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_selected_strokes: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select first point in Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_selected_strokes: Selected Strokes Only, Only select the first point of strokes that already have points selected
    :type only_selected_strokes: typing.Optional[typing.Union[bool, typing.Any]]
    :param extend: Extend, Extend selection instead of deselecting all other selected points
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_grouped(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'LAYER'):
    ''' Select all strokes with similar characteristics

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``LAYER`` Layer, Shared layers. * ``MATERIAL`` Material, Shared materials.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select_lasso(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'SET',
        path: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorMousePath']] = None):
    ''' Select Grease Pencil strokes using lasso selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``SET`` Set, Set a new selection. * ``ADD`` Extend, Extend existing selection. * ``SUB`` Subtract, Subtract existing selection. * ``XOR`` Difference, Inverts existing selection. * ``AND`` Intersect, Intersect existing selection.
    :type mode: typing.Optional[typing.Any]
    :param path: Path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    '''

    pass


def select_last(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_selected_strokes: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select last point in Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_selected_strokes: Selected Strokes Only, Only select the last point of strokes that already have points selected
    :type only_selected_strokes: typing.Optional[typing.Union[bool, typing.Any]]
    :param extend: Extend, Extend selection instead of deselecting all other selected points
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_less(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Shrink sets of selected Grease Pencil points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all points in same strokes as already selected points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_more(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Grow sets of selected Grease Pencil points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_vertex_color(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        threshold: typing.Optional[typing.Any] = 0):
    ''' Select all points with similar vertex color of current selected

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param threshold: Threshold, Tolerance of the selection. Higher values select a wider range of similar colors
    :type threshold: typing.Optional[typing.Any]
    '''

    pass


def selection_opacity_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Hide/Unhide selected points for Grease Pencil strokes setting alpha factor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def selectmode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 0):
    ''' Set selection mode for Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Select Mode, Select mode
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def set_active_material(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set the selected stroke material as the active material

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def snap_cursor_to_selected(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Snap cursor to center of selected points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def snap_to_cursor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_offset: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Snap selected points/strokes to the cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_offset: With Offset, Offset the entire stroke instead of selected points only
    :type use_offset: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def snap_to_grid(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Snap selected points to the nearest grid points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def stroke_apply_thickness(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Apply the thickness change of the layer to its strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def stroke_arrange(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'UP'):
    ''' Arrange selected strokes up/down in the drawing order of the active layer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def stroke_caps_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change stroke caps mode (rounded or flat)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``TOGGLE`` Both. * ``START`` Start. * ``END`` End. * ``TOGGLE`` Default, Set as default rounded.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def stroke_change_color(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        material: typing.Union[str, typing.Any] = ""):
    ''' Move selected strokes to active material

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param material: Material, Name of the material
    :type material: typing.Union[str, typing.Any]
    '''

    pass


def stroke_cutter(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        path: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorMousePath']] = None,
        flat_caps: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select section and cut

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param path: Path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    :param flat_caps: Flat Caps
    :type flat_caps: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stroke_cyclical_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'TOGGLE',
        geometry: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Close or open the selected stroke adding an edge from last to first point

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param geometry: Create Geometry, Create new geometry for closing stroke
    :type geometry: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stroke_editcurve_set_handle_type(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'AUTOMATIC'):
    ''' Set the type of a edit curve handle

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type, Spline type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def stroke_enter_editcurve_mode(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        error_threshold: typing.Optional[typing.Any] = 0.1):
    ''' Called to transform a stroke into a curve

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param error_threshold: Error Threshold, Threshold on the maximum deviation from the actual stroke
    :type error_threshold: typing.Optional[typing.Any]
    '''

    pass


def stroke_flip(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Change direction of the points of the selected strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def stroke_join(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'JOIN',
        leave_gaps: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Join selected strokes (optionally as new stroke)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param leave_gaps: Leave Gaps, Leave gaps between joined strokes instead of linking them
    :type leave_gaps: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stroke_merge(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'STROKE',
        back: typing.Optional[typing.Union[bool, typing.Any]] = False,
        additive: typing.Optional[typing.Union[bool, typing.Any]] = False,
        cyclic: typing.Optional[typing.Union[bool, typing.Any]] = False,
        clear_point: typing.Optional[typing.Union[bool, typing.Any]] = False,
        clear_stroke: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Create a new stroke with the selected stroke points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param back: Draw on Back, Draw new stroke below all previous strokes
    :type back: typing.Optional[typing.Union[bool, typing.Any]]
    :param additive: Additive Drawing, Add to previous drawing
    :type additive: typing.Optional[typing.Union[bool, typing.Any]]
    :param cyclic: Cyclic, Close new stroke
    :type cyclic: typing.Optional[typing.Union[bool, typing.Any]]
    :param clear_point: Dissolve Points, Dissolve old selected points
    :type clear_point: typing.Optional[typing.Union[bool, typing.Any]]
    :param clear_stroke: Delete Strokes, Delete old selected strokes
    :type clear_stroke: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stroke_merge_by_distance(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        threshold: typing.Optional[typing.Any] = 0.001,
        use_unselected: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False):
    ''' Merge points by distance

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param threshold: Threshold
    :type threshold: typing.Optional[typing.Any]
    :param use_unselected: Unselected, Use whole stroke, not only selected points
    :type use_unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stroke_merge_material(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        hue_threshold: typing.Optional[typing.Any] = 0.001,
        sat_threshold: typing.Optional[typing.Any] = 0.001,
        val_threshold: typing.Optional[typing.Any] = 0.001):
    ''' Replace materials in strokes merging similar

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param hue_threshold: Hue Threshold
    :type hue_threshold: typing.Optional[typing.Any]
    :param sat_threshold: Saturation Threshold
    :type sat_threshold: typing.Optional[typing.Any]
    :param val_threshold: Value Threshold
    :type val_threshold: typing.Optional[typing.Any]
    '''

    pass


def stroke_reset_vertex_color(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'BOTH'):
    ''' Reset vertex color for all or selected strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``STROKE`` Stroke, Reset Vertex Color to Stroke only. * ``FILL`` Fill, Reset Vertex Color to Fill only. * ``BOTH`` Stroke and Fill, Reset Vertex Color to Stroke and Fill.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def stroke_sample(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        length: typing.Optional[typing.Any] = 0.1):
    ''' Sample stroke points to predefined segment length

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param length: Length
    :type length: typing.Optional[typing.Any]
    '''

    pass


def stroke_separate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'POINT'):
    ''' Separate the selected strokes or layer in a new grease pencil object

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``POINT`` Selected Points, Separate the selected points. * ``STROKE`` Selected Strokes, Separate the selected strokes. * ``LAYER`` Active Layer, Separate the strokes of the current layer.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def stroke_simplify(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.0):
    ''' Simplify selected stroked reducing number of points

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def stroke_simplify_fixed(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        step: typing.Optional[typing.Any] = 1):
    ''' Simplify selected stroked reducing number of points using fixed algorithm

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param step: Steps, Number of simplify steps
    :type step: typing.Optional[typing.Any]
    '''

    pass


def stroke_smooth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        repeat: typing.Optional[typing.Any] = 1,
        factor: typing.Optional[typing.Any] = 0.5,
        only_selected: typing.Optional[typing.Union[bool, typing.Any]] = True,
        smooth_position: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        smooth_thickness: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        smooth_strength: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        smooth_uv: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Smooth selected strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param repeat: Repeat
    :type repeat: typing.Optional[typing.Any]
    :param factor: Factor
    :type factor: typing.Optional[typing.Any]
    :param only_selected: Selected Points, Smooth only selected points in the stroke
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_position: Position
    :type smooth_position: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_thickness: Thickness
    :type smooth_thickness: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_strength: Strength
    :type smooth_strength: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_uv: UV
    :type smooth_uv: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stroke_split(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Split selected points as new stroke on same frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def stroke_subdivide(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        number_cuts: typing.Optional[typing.Any] = 1,
        factor: typing.Optional[typing.Any] = 0.0,
        repeat: typing.Optional[typing.Any] = 1,
        only_selected: typing.Optional[typing.Union[bool, typing.Any]] = True,
        smooth_position: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        smooth_thickness: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        smooth_strength: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        smooth_uv: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Subdivide between continuous selected points of the stroke adding a point half way between them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param number_cuts: Number of Cuts
    :type number_cuts: typing.Optional[typing.Any]
    :param factor: Smooth
    :type factor: typing.Optional[typing.Any]
    :param repeat: Repeat
    :type repeat: typing.Optional[typing.Any]
    :param only_selected: Selected Points, Smooth only selected points in the stroke
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_position: Position
    :type smooth_position: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_thickness: Thickness
    :type smooth_thickness: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_strength: Strength
    :type smooth_strength: typing.Optional[typing.Union[bool, typing.Any]]
    :param smooth_uv: UV
    :type smooth_uv: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stroke_trim(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Trim selected stroke to first loop or intersection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def tint_flip(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Switch tint colors :file: `startup/bl_ui/properties_grease_pencil_common.py\:872 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_ui/properties_grease_pencil_common.py$872>`_

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def trace_image(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        target: typing.Optional[typing.Any] = 'NEW',
        thickness: typing.Optional[typing.Any] = 10,
        resolution: typing.Optional[typing.Any] = 5,
        scale: typing.Optional[typing.Any] = 1.0,
        sample: typing.Optional[typing.Any] = 0.0,
        threshold: typing.Optional[typing.Any] = 0.5,
        turnpolicy: typing.Optional[typing.Any] = 'MINORITY',
        mode: typing.Optional[typing.Any] = 'SINGLE'):
    ''' Extract Grease Pencil strokes from image

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param target: Target Object, Target grease pencil
    :type target: typing.Optional[typing.Any]
    :param thickness: Thickness
    :type thickness: typing.Optional[typing.Any]
    :param resolution: Resolution, Resolution of the generated curves
    :type resolution: typing.Optional[typing.Any]
    :param scale: Scale, Scale of the final stroke
    :type scale: typing.Optional[typing.Any]
    :param sample: Sample, Distance to sample points, zero to disable
    :type sample: typing.Optional[typing.Any]
    :param threshold: Color Threshold, Determine the lightness threshold above which strokes are generated
    :type threshold: typing.Optional[typing.Any]
    :param turnpolicy: Turn Policy, Determines how to resolve ambiguities during decomposition of bitmaps into paths * ``BLACK`` Black, Prefers to connect black (foreground) components. * ``WHITE`` White, Prefers to connect white (background) components. * ``LEFT`` Left, Always take a left turn. * ``RIGHT`` Right, Always take a right turn. * ``MINORITY`` Minority, Prefers to connect the color (black or white) that occurs least frequently in the local neighborhood of the current position. * ``MAJORITY`` Majority, Prefers to connect the color (black or white) that occurs most frequently in the local neighborhood of the current position. * ``RANDOM`` Random, Choose pseudo-randomly.
    :type turnpolicy: typing.Optional[typing.Any]
    :param mode: Mode, Determines if trace simple image or full sequence * ``SINGLE`` Single, Trace the current frame of the image. * ``SEQUENCE`` Sequence, Trace full sequence.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def transform_fill(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'ROTATE',
        location: typing.Optional[typing.Any] = (0.0, 0.0),
        rotation: typing.Optional[typing.Any] = 0.0,
        scale: typing.Optional[typing.Any] = 0.0,
        release_confirm: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Transform grease pencil stroke fill

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param location: Location
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation
    :type rotation: typing.Optional[typing.Any]
    :param scale: Scale
    :type scale: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release
    :type release_confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def unlock_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Unlock all Grease Pencil layers so that they can be edited

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_color_brightness_contrast(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'BOTH',
        brightness: typing.Optional[typing.Any] = 0.0,
        contrast: typing.Optional[typing.Any] = 0.0):
    ''' Adjust vertex color brightness/contrast

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param brightness: Brightness
    :type brightness: typing.Optional[typing.Any]
    :param contrast: Contrast
    :type contrast: typing.Optional[typing.Any]
    '''

    pass


def vertex_color_hsv(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'BOTH',
        h: typing.Optional[typing.Any] = 0.5,
        s: typing.Optional[typing.Any] = 1.0,
        v: typing.Optional[typing.Any] = 1.0):
    ''' Adjust vertex color HSV values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param h: Hue
    :type h: typing.Optional[typing.Any]
    :param s: Saturation
    :type s: typing.Optional[typing.Any]
    :param v: Value
    :type v: typing.Optional[typing.Any]
    '''

    pass


def vertex_color_invert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'BOTH'):
    ''' Invert RGB values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def vertex_color_levels(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'BOTH',
        offset: typing.Optional[typing.Any] = 0.0,
        gain: typing.Optional[typing.Any] = 1.0):
    ''' Adjust levels of vertex colors

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param offset: Offset, Value to add to colors
    :type offset: typing.Optional[typing.Any]
    :param gain: Gain, Value to multiply colors by
    :type gain: typing.Optional[typing.Any]
    '''

    pass


def vertex_color_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'BOTH',
        factor: typing.Optional[typing.Any] = 1.0):
    ''' Set active color to all selected vertex

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param factor: Factor, Mix Factor
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_assign(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Assign the selected vertices to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_deselect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Deselect all selected vertices assigned to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_invert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Invert weights to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_normalize(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Normalize weights to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_normalize_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        lock_active: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertex_group_remove_from(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove the selected vertices from active or all vertex group(s)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all the vertices assigned to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_smooth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.5,
        repeat: typing.Optional[typing.Any] = 1):
    ''' Smooth weights to the active vertex group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor
    :type factor: typing.Optional[typing.Any]
    :param repeat: Iterations
    :type repeat: typing.Optional[typing.Any]
    '''

    pass


def vertex_paint(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        stroke: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Paint stroke points with a color

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def vertexmode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        back: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Enter/Exit vertex paint mode for Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param back: Return to Previous Mode, Return to previous mode
    :type back: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def weight_paint(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        stroke: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        wait_for_input: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = True):
    ''' Paint stroke points with a color

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def weightmode_toggle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        back: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Enter/Exit weight paint mode for Grease Pencil strokes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param back: Return to Previous Mode, Return to previous mode
    :type back: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass
