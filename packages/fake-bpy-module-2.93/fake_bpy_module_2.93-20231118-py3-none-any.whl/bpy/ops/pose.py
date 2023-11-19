import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def armature_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        selected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Apply the current pose as the new rest pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param selected: Selected Only, Only apply the selected bones (with propagation to children)
    :type selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def autoside_names(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        axis: typing.Optional[typing.Any] = 'XAXIS'):
    ''' Automatically renames the selected bones according to which side of the target axis they fall on

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param axis: Axis, Axis tag names with * ``XAXIS`` X-Axis, Left/Right. * ``YAXIS`` Y-Axis, Front/Back. * ``ZAXIS`` Z-Axis, Top/Bottom.
    :type axis: typing.Optional[typing.Any]
    '''

    pass


def bone_layers(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        layers: typing.Optional[
            typing.Union[typing.List[bool], typing.Any]] = (
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False,
                False, False, False, False, False)):
    ''' Change the layers that the selected bones belong to

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param layers: Layer, Armature layers that bone belongs to
    :type layers: typing.Optional[typing.Union[typing.List[bool], typing.Any]]
    '''

    pass


def breakdown(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.5,
        prev_frame: typing.Optional[typing.Any] = 0,
        next_frame: typing.Optional[typing.Any] = 0,
        channels: typing.Optional[typing.Any] = 'ALL',
        axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Create a suitable breakdown pose on the current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties, All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location, Location only. * ``ROT`` Rotation, Rotation only. * ``SIZE`` Scale, Scale only. * ``BBONE`` Bendy Bone, Bendy Bone shape properties. * ``CUSTOM`` Custom Properties, Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free, All axes are affected. * ``X`` X, Only X-axis transforms are affected. * ``Y`` Y, Only Y-axis transforms are affected. * ``Z`` Z, Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def constraint_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = ''):
    ''' Add a constraint to the active bone

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CAMERA_SOLVER`` Camera Solver. * ``FOLLOW_TRACK`` Follow Track. * ``OBJECT_SOLVER`` Object Solver. * ``COPY_LOCATION`` Copy Location, Copy the location of a target (with an optional offset), so that they move together. * ``COPY_ROTATION`` Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together. * ``COPY_SCALE`` Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount. * ``COPY_TRANSFORMS`` Copy Transforms, Copy all the transformations of a target, so that they move together. * ``LIMIT_DISTANCE`` Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only). * ``LIMIT_LOCATION`` Limit Location, Restrict movement along each axis within given ranges. * ``LIMIT_ROTATION`` Limit Rotation, Restrict rotation along each axis within given ranges. * ``LIMIT_SCALE`` Limit Scale, Restrict scaling along each axis with given ranges. * ``MAINTAIN_VOLUME`` Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes. * ``TRANSFORM`` Transformation, Use one transform property from target to control another (or same) property on owner. * ``TRANSFORM_CACHE`` Transform Cache, Look up the transformation matrix from an external file. * ``CLAMP_TO`` Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis. * ``DAMPED_TRACK`` Damped Track, Point towards a target by performing the smallest rotation necessary. * ``IK`` Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only). * ``LOCKED_TRACK`` Locked Track, Rotate around the specified ('locked') axis to point towards a target. * ``SPLINE_IK`` Spline IK, Align chain of bones along a curve (Bones only). * ``STRETCH_TO`` Stretch To, Stretch along Y-Axis to point towards a target. * ``TRACK_TO`` Track To, Legacy tracking constraint prone to twisting artifacts. * ``ACTION`` Action, Use transform property of target to look up pose for owner from an Action. * ``ARMATURE`` Armature, Apply weight-blended transformation from multiple bones like the Armature modifier. * ``CHILD_OF`` Child Of, Make target the 'detachable' parent of owner. * ``FLOOR`` Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross. * ``FOLLOW_PATH`` Follow Path, Use to animate an object/bone following a path. * ``PIVOT`` Pivot, Change pivot point for transforms (buggy). * ``SHRINKWRAP`` Shrinkwrap, Restrict movements to surface of target mesh.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def constraint_add_with_targets(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = ''):
    ''' Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CAMERA_SOLVER`` Camera Solver. * ``FOLLOW_TRACK`` Follow Track. * ``OBJECT_SOLVER`` Object Solver. * ``COPY_LOCATION`` Copy Location, Copy the location of a target (with an optional offset), so that they move together. * ``COPY_ROTATION`` Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together. * ``COPY_SCALE`` Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount. * ``COPY_TRANSFORMS`` Copy Transforms, Copy all the transformations of a target, so that they move together. * ``LIMIT_DISTANCE`` Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only). * ``LIMIT_LOCATION`` Limit Location, Restrict movement along each axis within given ranges. * ``LIMIT_ROTATION`` Limit Rotation, Restrict rotation along each axis within given ranges. * ``LIMIT_SCALE`` Limit Scale, Restrict scaling along each axis with given ranges. * ``MAINTAIN_VOLUME`` Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes. * ``TRANSFORM`` Transformation, Use one transform property from target to control another (or same) property on owner. * ``TRANSFORM_CACHE`` Transform Cache, Look up the transformation matrix from an external file. * ``CLAMP_TO`` Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis. * ``DAMPED_TRACK`` Damped Track, Point towards a target by performing the smallest rotation necessary. * ``IK`` Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only). * ``LOCKED_TRACK`` Locked Track, Rotate around the specified ('locked') axis to point towards a target. * ``SPLINE_IK`` Spline IK, Align chain of bones along a curve (Bones only). * ``STRETCH_TO`` Stretch To, Stretch along Y-Axis to point towards a target. * ``TRACK_TO`` Track To, Legacy tracking constraint prone to twisting artifacts. * ``ACTION`` Action, Use transform property of target to look up pose for owner from an Action. * ``ARMATURE`` Armature, Apply weight-blended transformation from multiple bones like the Armature modifier. * ``CHILD_OF`` Child Of, Make target the 'detachable' parent of owner. * ``FLOOR`` Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross. * ``FOLLOW_PATH`` Follow Path, Use to animate an object/bone following a path. * ``PIVOT`` Pivot, Change pivot point for transforms (buggy). * ``SHRINKWRAP`` Shrinkwrap, Restrict movements to surface of target mesh.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def constraints_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear all the constraints for the selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def constraints_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy constraints to other selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def copy(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None):
    ''' Copies the current pose of the selected bones to copy/paste buffer

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def flip_names(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        do_strip_numbers: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False):
    ''' Flips (and corrects) the axis suffixes of the names of selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names. Warning: May result in incoherent naming in some cases
    :type do_strip_numbers: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def group_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a new bone group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def group_assign(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 0):
    ''' Add selected bones to the chosen bone group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Bone Group Index
    :type type: typing.Optional[typing.Any]
    '''

    pass


def group_deselect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Deselect bones of active Bone Group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def group_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'UP'):
    ''' Change position of active Bone Group in list of Bone Groups

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to move the active Bone Group towards
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def group_remove(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove the active bone group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def group_select(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select bones in active Bone Group

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def group_sort(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Sort Bone Groups by their names in ascending order

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def group_unassign(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Remove selected bones from all bone groups

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def hide(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Tag selected bones to not be visible in Pose Mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def ik_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        with_targets: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Add IK Constraint to the active Bone

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
    :type with_targets: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def ik_clear(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None):
    ''' Remove all IK Constraints from selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def loc_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset locations of selected bones to their default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def paste(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          flipped: typing.Optional[typing.Union[bool, typing.Any]] = False,
          selected_mask: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False):
    ''' Paste the stored pose on to the current pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
    :type flipped: typing.Optional[typing.Union[bool, typing.Any]]
    :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
    :type selected_mask: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def paths_calculate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        start_frame: typing.Optional[typing.Any] = 1,
        end_frame: typing.Optional[typing.Any] = 250,
        bake_location: typing.Optional[typing.Any] = 'HEADS'):
    ''' Calculate paths for the selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param start_frame: Start, First frame to calculate bone paths on
    :type start_frame: typing.Optional[typing.Any]
    :param end_frame: End, Last frame to calculate bone paths on
    :type end_frame: typing.Optional[typing.Any]
    :param bake_location: Bake Location, Which point on the bones is used when calculating paths * ``HEADS`` Heads, Calculate bone paths from heads. * ``TAILS`` Tails, Calculate bone paths from tails.
    :type bake_location: typing.Optional[typing.Any]
    '''

    pass


def paths_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_selected: typing.Optional[typing.Union[bool, typing.
                                                    Any]] = False):
    ''' Clear path caches for all bones, hold Shift key for selected bones only

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_selected: Only Selected, Only clear paths from selected bones
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def paths_range_update(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Update frame range for motion paths from the Scene's current frame range

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def paths_update(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Recalculate paths for bones that already have them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def propagate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'WHILE_HELD',
        end_frame: typing.Optional[typing.Any] = 250.0):
    ''' Copy selected aspects of the current pose to subsequent poses already keyframed

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes * ``WHILE_HELD`` While Held, Propagate pose to all keyframes after current frame that don't change (Default behavior). * ``NEXT_KEY`` To Next Keyframe, Propagate pose to first keyframe following the current frame only. * ``LAST_KEY`` To Last Keyframe, Propagate pose to the last keyframe only (i.e. making action cyclic). * ``BEFORE_FRAME`` Before Frame, Propagate pose to all keyframes between current frame and 'Frame' property. * ``BEFORE_END`` Before Last Keyframe, Propagate pose to all keyframes from current frame until no more are found. * ``SELECTED_KEYS`` On Selected Keyframes, Propagate pose to all selected keyframes. * ``SELECTED_MARKERS`` On Selected Markers, Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
    :type mode: typing.Optional[typing.Any]
    :param end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode)
    :type end_frame: typing.Optional[typing.Any]
    '''

    pass


def push(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         factor: typing.Optional[typing.Any] = 0.5,
         prev_frame: typing.Optional[typing.Any] = 0,
         next_frame: typing.Optional[typing.Any] = 0,
         channels: typing.Optional[typing.Any] = 'ALL',
         axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Exaggerate the current pose in regards to the breakdown pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties, All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location, Location only. * ``ROT`` Rotation, Rotation only. * ``SIZE`` Scale, Scale only. * ``BBONE`` Bendy Bone, Bendy Bone shape properties. * ``CUSTOM`` Custom Properties, Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free, All axes are affected. * ``X`` X, Only X-axis transforms are affected. * ``Y`` Y, Only Y-axis transforms are affected. * ``Z`` Z, Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def push_rest(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.5,
        prev_frame: typing.Optional[typing.Any] = 0,
        next_frame: typing.Optional[typing.Any] = 0,
        channels: typing.Optional[typing.Any] = 'ALL',
        axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Push the current pose further away from the rest pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties, All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location, Location only. * ``ROT`` Rotation, Rotation only. * ``SIZE`` Scale, Scale only. * ``BBONE`` Bendy Bone, Bendy Bone shape properties. * ``CUSTOM`` Custom Properties, Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free, All axes are affected. * ``X`` X, Only X-axis transforms are affected. * ``Y`` Y, Only Y-axis transforms are affected. * ``Z`` Z, Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def quaternions_flip(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Flip quaternion values to achieve desired rotations, while maintaining the same orientations

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def relax(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          factor: typing.Optional[typing.Any] = 0.5,
          prev_frame: typing.Optional[typing.Any] = 0,
          next_frame: typing.Optional[typing.Any] = 0,
          channels: typing.Optional[typing.Any] = 'ALL',
          axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Make the current pose more similar to its breakdown pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties, All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location, Location only. * ``ROT`` Rotation, Rotation only. * ``SIZE`` Scale, Scale only. * ``BBONE`` Bendy Bone, Bendy Bone shape properties. * ``CUSTOM`` Custom Properties, Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free, All axes are affected. * ``X`` X, Only X-axis transforms are affected. * ``Y`` Y, Only Y-axis transforms are affected. * ``Z`` Z, Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def relax_rest(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.5,
        prev_frame: typing.Optional[typing.Any] = 0,
        next_frame: typing.Optional[typing.Any] = 0,
        channels: typing.Optional[typing.Any] = 'ALL',
        axis_lock: typing.Optional[typing.Any] = 'FREE'):
    ''' Make the current pose more similar to the rest pose

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Weighting factor for which keyframe is favored more
    :type factor: typing.Optional[typing.Any]
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
    :type prev_frame: typing.Optional[typing.Any]
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
    :type next_frame: typing.Optional[typing.Any]
    :param channels: Channels, Set of properties that are affected * ``ALL`` All Properties, All properties, including transforms, bendy bone shape, and custom properties. * ``LOC`` Location, Location only. * ``ROT`` Rotation, Rotation only. * ``SIZE`` Scale, Scale only. * ``BBONE`` Bendy Bone, Bendy Bone shape properties. * ``CUSTOM`` Custom Properties, Custom properties.
    :type channels: typing.Optional[typing.Any]
    :param axis_lock: Axis Lock, Transform axis to restrict effects to * ``FREE`` Free, All axes are affected. * ``X`` X, Only X-axis transforms are affected. * ``Y`` Y, Only Y-axis transforms are affected. * ``Z`` Z, Only Z-axis transforms are affected.
    :type axis_lock: typing.Optional[typing.Any]
    '''

    pass


def reveal(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           select: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Reveal all bones hidden in Pose Mode

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def rot_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset rotations of selected bones to their default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def rotation_mode_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'QUATERNION'):
    ''' Set the rotation representation used by selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Rotation Mode * ``QUATERNION`` Quaternion (WXYZ), No Gimbal Lock. * ``XYZ`` XYZ Euler, XYZ Rotation Order - prone to Gimbal Lock (default). * ``XZY`` XZY Euler, XZY Rotation Order - prone to Gimbal Lock. * ``YXZ`` YXZ Euler, YXZ Rotation Order - prone to Gimbal Lock. * ``YZX`` YZX Euler, YZX Rotation Order - prone to Gimbal Lock. * ``ZXY`` ZXY Euler, ZXY Rotation Order - prone to Gimbal Lock. * ``ZYX`` ZYX Euler, ZYX Rotation Order - prone to Gimbal Lock. * ``AXIS_ANGLE`` Axis Angle, Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def scale_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset scaling of selected bones to their default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Toggle selection status of all bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle, Toggle selection for all elements. * ``SELECT`` Select, Select all elements. * ``DESELECT`` Deselect, Deselect all elements. * ``INVERT`` Invert, Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_constraint_target(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select bones used as targets for the currently selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_grouped(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        type: typing.Optional[typing.Any] = 'LAYER'):
    ''' Select all visible bones grouped by similar properties

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param type: Type * ``LAYER`` Layer, Shared layers. * ``GROUP`` Group, Shared group. * ``KEYINGSET`` Keying Set, All bones affected by active Keying Set.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select_hierarchy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'PARENT',
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select immediate parent/children of selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param direction: Direction
    :type direction: typing.Optional[typing.Any]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_linked(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select all bones linked by parent/child connections to the current selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked_pick(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select bones linked by parent/child connections under the mouse cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_mirror(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_active: typing.Optional[typing.Union[bool, typing.Any]] = False,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Mirror the bone selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_active: Active Only, Only operate on the active bone
    :type only_active: typing.Optional[typing.Union[bool, typing.Any]]
    :param extend: Extend, Extend the selection
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_parent(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select bones that are parents of the currently selected bones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def transforms_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset location, rotation, and scaling of selected bones to their default values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def user_transforms_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_selected: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Reset pose bone transforms to keyframed state

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_selected: Only Selected, Only visible/selected bones
    :type only_selected: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def visual_transform_apply(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Apply final constrained position of pose bones to their transform

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
