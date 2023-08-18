import unreal


sound_wav = "D:/Documents/Resources/Audios/SFX/FastSound_01.wav"
skeletal_mesh_fbx = "C:/Users/PC/Desktop/Walk_WP.fbx"


def importMyAssets():
    folder = "/Game/Cinematic/Developers/Stephen/Test"
    # soundTask = buildImportTask(sound_wav, folder)
    # SKMeshTask = buildImportTask(skeletal_mesh_fbx, folder, options=buildSkeletalMeshImportOptions())
    animationTask = buildImportTask(
        skeletal_mesh_fbx, folder, 
        options=buildAnimationImportOptions("/Game/Characters/Mannequins/Meshes/SK_Mannequin"))
    
    executeImportTasks([animationTask])


def buildImportTask(filename, destination_path, destination_name="", options=None):
    task = unreal.AssetImportTask()
    task.filename = filename
    task.destination_path = destination_path
    task.destination_name = destination_name
    task.automated = True
    task.replace_existing = True
    task.save = False
    task.options = options
    
    return task


def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    
    
def buildStaticMeshimportOptions():
    options = unreal.FbxImportUI()
    options.set_editor_property("import_mesh", True)
    options.set_editor_property("import_textures", False)
    options.set_editor_property("import_materials", False)
    options.set_editor_property("import_as_skeletal", False)
    options.set_editor_property("import_animations", False)
    options.set_editor_property("import_rigid_mesh", True)
    options.set_editor_property("import_mesh_lods", False)
    options.set_editor_property("import_material_slots_as_imported", True)
    options.set_editor_property("import_meshes_in_bone_hierarchy", False)
    options.set_editor_property("import_mesh_normals", True)
    options.set_editor_property("import_mesh_vertex_colors", False)
    options.set_editor_property("import_mesh_smoothing", True)
    options.set_editor_property("import_mesh_vertex_color_mode", unreal.VertexColorImportOption.IGNORE)
    options.set_editor_property("import_translation", unreal.Vector(0.0, 0.0, 0.0))
    options.set_editor_property("import_rotation", unreal.Rotator(0.0, 0.0, 0.0))
    options.set_editor_property("import_uniform_scale", 1.0)
    options.set_editor_property("convert_scene", False)
    options.set_editor_property("force_front_x_axis", False)
    options.set_editor_property("convert_scene_unit", unreal.FBXImportType.METERS)
    options.set_editor_property("automatic_import_lods", False)
    options.set_editor_property("import_mesh_bone_weights", True)

    return options


def buildSkeletalMeshImportOptions():
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property("import_mesh", True)
    options.set_editor_property("import_textures", False)
    options.set_editor_property("import_materials", False)
    options.set_editor_property("import_as_skeletal", True)
    # unreal.FbxMeshImportData
    options.skeletal_mesh_import_data.set_editor_property("import_translation", unreal.Vector(0.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property("import_rotation", unreal.Rotator(0.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property("import_uniform_scale", 1.0)
    # unreal.FbxSkeletalMeshImportData
    options.skeletal_mesh_import_data.set_editor_property("import_morph_targets", True)
    options.skeletal_mesh_import_data.set_editor_property("update_skeleton_reference_pose", False)

    return options


def buildAnimationImportOptions(skeleton_path):
    options = unreal.FbxImportUI()
    # unreal.FbxImportUI
    options.set_editor_property("import_as_skeletal", True)
    options.set_editor_property("import_animations", True)
    options.set_editor_property("import_mesh", False)
    options.set_editor_property("import_materials", False)
    options.set_editor_property("create_physics_asset", False)
    options.skeleton = unreal.load_asset(skeleton_path)
    # only Animation Sequence
    options.set_editor_property("automated_import_should_detect_type", False)
    options.set_editor_property("original_import_type", unreal.FBXImportType.FBXIT_SKELETAL_MESH)
    options.set_editor_property("mesh_type_to_import", unreal.FBXImportType.FBXIT_ANIMATION)
    # unreal.FbxMeshImportData
    options.anim_sequence_import_data.set_editor_property("import_translation", unreal.Vector(0.0, 0.0, 0.0))
    options.anim_sequence_import_data.set_editor_property("import_rotation", unreal.Rotator(0.0, 0.0, 0.0))
    options.anim_sequence_import_data.set_editor_property("import_uniform_scale", 1.0)
    # unreal.FbxAnimSequenceImportData
    options.anim_sequence_import_data.set_editor_property("animation_length", unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME)
    options.anim_sequence_import_data.set_editor_property("remove_redundant_keys", True)
    
    return options


# add a animation track to sequencer
def addAnimationTrackToSequencer():
    # EditorLevelLibrary has DeprecationWarning
    # accessing the proper subsystem
    # https://docs.unrealengine.com/4.27/en-US/ProgrammingAndScripting/Subsystems
    editorSubsystem = unreal.get_editor_subsystem(unreal.EditorSubsystem)
    unreal.log(f'{dir(editorSubsystem)}')
    # get the level
    currentLevel = editorSubsystem.get_current_level()
    unreal.log(f'{currentLevel}')
    # get the sequencer
    sequencer = unreal.find_asset('/Game/Cinematic/Developers/Stephen/LS_TEST')
    unreal.log(f'{sequencer}')

    # https://docs.unrealengine.com/5.0/en-US/python-scripting-in-sequencer-in-unreal-engine/
    # Adding Actors.
    actor_system = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    try:
        # To add an actor from your current Level for Sequencer to possess.
        # try:
        #     actor_selected = actor_system.get_selected_level_actors()[0]
        #     unreal.log(f'selected actor: {actor_selected}')
        #     actor_binding = sequencer.add_possessable(actor_selected)
        #     unreal.log(f'actor_binding: {actor_binding}')
        # except IndexError:
        #     unreal.log('no actor selected')
        #     actor_selected = None

        # Instead of possessing a current actor from your Level, Sequencer can spawn new ones for the duration of the sequence.
        actor_selected = actor_system.get_selected_level_actors()[0]
        unreal.log(f'selected actor: {actor_selected}')
        actor_binding = sequencer.add_spawnable_from_instance(actor_selected)
        unreal.log(f'actor_binding: {actor_binding}')

        # Create Tracks and Sections.
        # Use the binding to add tracks into sequencer.
        transform_track = actor_binding.add_track(unreal.MovieScene3DTransformTrack)
        anim_track = actor_binding.add_track(unreal.MovieSceneSkeletalAnimationTrack)
        # add section to track to be able to manipulate range, parameters, or properties.
        transform_section = transform_track.add_section()
        anim_section = anim_track.add_section()
        # get level sequence start and end frame
        start_frame = sequencer.get_playback_start()
        end_frame = sequencer.get_playback_end()
        unreal.log(f'start_frame: {start_frame}')
        unreal.log(f'end_frame: {end_frame}')
        # set section range to level sequence start and end frame
        transform_section.set_range(start_frame, end_frame)
        anim_section.set_range(start_frame, end_frame)
        # set animation parameters
        anim_section.params.animation = unreal.find_asset('/Game/Cinematic/Developers/Stephen/Test/Walk_WP')
    except IndexError:
        unreal.log('no actor selected')
        actor_selected = None
        
    # refresh the sequencer
    unreal.LevelSequenceEditorBlueprintLibrary.refresh_current_level_sequence()
    
    
if __name__ == '__main__':    
    # importMyAssets()
    addAnimationTrackToSequencer()
        
    unreal.log('Done.')