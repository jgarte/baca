from abjad.tools import measuretools
from abjad.tools import notetools
import baca
import py


def test_MaterialPackageProxy_read_only_attributes_01():
    '''Data-only package.
    '''
    
    mpp = baca.scf.MaterialPackageProxy('baca.materials.red_numbers')
    assert     mpp.breadcrumb == 'red numbers'
    assert not mpp.has_illustration_builder_module
    assert not mpp.has_illustration_ly
    assert not mpp.has_illustration_pdf
    assert     mpp.has_material_definition
    assert     mpp.has_material_definition_module
    assert not mpp.has_material_package_maker
    assert     mpp.has_output_material
    assert     mpp.has_output_material_module
    assert not mpp.has_user_input_module
    assert not mpp.has_user_input_wrapper_on_disk
    assert     mpp.illustration is None
    assert     mpp.illustration_builder_module_file_name is None
    assert     mpp.illustration_builder_module_importable_name is None
    assert     mpp.illustration_builder_module_proxy is None
    assert     mpp.illustration_ly_file_name is None
    assert     mpp.illustration_ly_file_proxy is None
    assert     mpp.illustration_pdf_file_name is None
    assert     mpp.illustration_pdf_file_proxy is None
    # TODO:
    #assert not mpp.is_changed   
    assert     mpp.is_data_only
    assert     mpp.is_handmade
    assert     mpp.material_definition == [1, 2, 3, 4, 5]
    assert     mpp.material_definition_module_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_numbers/material_definition.py'
    assert     mpp.material_definition_module_importable_name == \
        'baca.materials.red_numbers.material_definition' 
    assert     mpp.material_definition_module_proxy is not None
    assert     mpp.material_package_directory == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_numbers'
    assert     mpp.material_package_maker is None
    assert     mpp.material_package_maker_class_name is None
    assert     mpp.material_package_short_name == 'red_numbers'
    assert     mpp.material_spaced_name == 'red numbers'
    assert     mpp.material_underscored_name == 'red_numbers'
    assert     mpp.materials_directory_name == \
        '/Users/trevorbaca/Documents/other/baca/materials'
    assert     mpp.materials_package_importable_name == 'baca.materials'
    assert     mpp.output_material == [1, 2, 3, 4, 5]
    assert     mpp.output_material_module_body_lines == ['red_numbers = [1, 2, 3, 4, 5]']
    assert     mpp.output_material_module_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_numbers/output_material.py'
    assert     mpp.output_material_module_importable_name == \
        'baca.materials.red_numbers.output_material'
    assert      mpp.output_material_module_proxy is not None
    assert not  mpp.should_have_illustration
    assert not  mpp.should_have_illustration_builder_module
    assert not  mpp.should_have_illustration_ly
    assert not  mpp.should_have_illustration_pdf
    assert      mpp.should_have_material_definition_module
    assert      mpp.should_have_output_material_module
    assert not  mpp.should_have_user_input_module
    assert      mpp.stylesheet_file_name_on_disk is None
    assert      mpp.stylesheet_file_proxy is None
    assert      mpp.user_input_module_file_name is None
    assert      mpp.user_input_module_importable_name is None
    assert      mpp.user_input_module_proxy is None


def test_MaterialPackageProxy_read_only_attributes_02():
    '''Makermade material.
    '''

    mpp = baca.scf.materialpackagemakers.SargassoMeasureMaterialPackageMaker('baca.materials.red_sargasso')
    assert     mpp.breadcrumb == 'red sargasso'
    assert not mpp.has_illustration_builder_module
    assert     mpp.has_illustration_ly
    assert     mpp.has_illustration_pdf
    assert not mpp.has_material_definition
    assert not mpp.has_material_definition_module
    assert     mpp.has_material_package_maker
    assert     mpp.has_output_material
    assert     mpp.has_output_material_module
    assert     mpp.has_user_input_module
    assert     mpp.has_user_input_wrapper_on_disk        
    assert     mpp.has_user_input_wrapper_in_memory
    assert     mpp.illustration is not None
    assert     mpp.illustration_builder_module_file_name is None
    assert     mpp.illustration_builder_module_importable_name is None
    assert     mpp.illustration_builder_module_proxy is None
    assert     mpp.illustration_ly_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_sargasso/illustration.ly'
    assert     mpp.illustration_ly_file_proxy is not None
    assert     mpp.illustration_pdf_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_sargasso/illustration.pdf'
    assert     mpp.illustration_pdf_file_proxy is not None
    # TODO:
    #assert not mpp.is_changed   
    assert not mpp.is_data_only
    assert not mpp.is_handmade
    assert     mpp.is_makermade
    assert     mpp.material_definition_module_file_name is None
    assert     mpp.material_definition_module_importable_name is None
    assert     mpp.material_definition_module_proxy is None
    assert     mpp.material_package_directory == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_sargasso'
    assert     mpp.material_package_maker is baca.scf.materialpackagemakers.SargassoMeasureMaterialPackageMaker
    assert     mpp.material_package_maker_class_name == 'SargassoMeasureMaterialPackageMaker'
    assert     mpp.material_package_short_name == 'red_sargasso'
    assert     mpp.material_spaced_name == 'red sargasso'
    assert     mpp.material_underscored_name == 'red_sargasso'
    assert     mpp.materials_directory_name == \
        '/Users/trevorbaca/Documents/other/baca/materials'
    assert     mpp.materials_package_importable_name == 'baca.materials'
    assert     measuretools.all_are_measures(mpp.output_material)
    assert     mpp.output_material_module_body_lines is None
    assert     mpp.output_material_module_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_sargasso/output_material.py'
    assert     mpp.output_material_module_importable_name == \
        'baca.materials.red_sargasso.output_material'
    assert      mpp.output_material_module_proxy is not None
    assert      mpp.should_have_illustration
    assert not  mpp.should_have_illustration_builder_module
    assert      mpp.should_have_illustration_ly
    assert      mpp.should_have_illustration_pdf
    assert not  mpp.should_have_material_definition_module
    assert      mpp.should_have_output_material_module
    assert      mpp.should_have_user_input_module
    # TODO:
    #assert      mpp.stylesheet_file_name_on_disk is None
    #assert      mpp.stylesheet_file_proxy is None
    assert      mpp.user_input_module_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_sargasso/user_input.py'
    assert      mpp.user_input_module_importable_name == \
        'baca.materials.red_sargasso.user_input'
    assert      mpp.user_input_module_proxy is not None


def test_MaterialPackageProxy_read_only_attributes_03():
    '''Handmade material.
    '''

    mpp = baca.scf.MaterialPackageProxy('baca.materials.red_notes')
    assert     mpp.breadcrumb == 'red notes'
    assert     mpp.has_illustration_builder_module
    assert     mpp.has_illustration_ly
    assert     mpp.has_illustration_pdf
    assert     mpp.has_material_definition
    assert     mpp.has_material_definition_module
    assert not mpp.has_material_package_maker
    assert     mpp.has_output_material
    assert     mpp.has_output_material_module
    assert not mpp.has_user_input_module
    assert not mpp.has_user_input_wrapper_on_disk
    assert     mpp.illustration is not None
    assert     mpp.illustration_builder_module_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_notes/illustration_builder.py'
    assert     mpp.illustration_builder_module_importable_name == \
        'baca.materials.red_notes.illustration_builder'
    assert     mpp.illustration_builder_module_proxy is not None
    assert     mpp.illustration_ly_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_notes/illustration.ly'
    assert     mpp.illustration_ly_file_proxy is not None
    assert     mpp.illustration_pdf_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_notes/illustration.pdf'
    assert     mpp.illustration_pdf_file_proxy is not None
    # TODO:
    #assert not mpp.is_changed   
    assert not mpp.is_data_only
    assert     mpp.is_handmade
    assert not mpp.is_makermade
    assert     mpp.material_definition_module_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_notes/material_definition.py'
    assert     mpp.material_definition_module_importable_name == \
        'baca.materials.red_notes.material_definition'
    assert     mpp.material_definition_module_proxy is not None
    assert     mpp.material_package_directory == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_notes'
    assert     mpp.material_package_maker is None
    assert     mpp.material_package_maker_class_name is None
    assert     mpp.material_package_short_name == 'red_notes'
    assert     mpp.material_spaced_name == 'red notes'
    assert     mpp.material_underscored_name == 'red_notes'
    assert     mpp.materials_directory_name == \
        '/Users/trevorbaca/Documents/other/baca/materials'
    assert     mpp.materials_package_importable_name == 'baca.materials'
    assert     notetools.all_are_notes(mpp.material_definition)
    assert     mpp.output_material_module_body_lines is not None
    assert     mpp.output_material_module_file_name == \
        '/Users/trevorbaca/Documents/other/baca/materials/red_notes/output_material.py'
    assert     mpp.output_material_module_importable_name == \
        'baca.materials.red_notes.output_material'
    assert      mpp.output_material_module_proxy is not None
    assert      mpp.should_have_illustration
    assert      mpp.should_have_illustration_builder_module
    assert      mpp.should_have_illustration_ly
    assert      mpp.should_have_illustration_pdf
    assert      mpp.should_have_material_definition_module
    assert      mpp.should_have_output_material_module
    assert not  mpp.should_have_user_input_module
    assert      mpp.stylesheet_file_name_on_disk == '/Users/trevorbaca/Documents/other/baca/scf/stylesheets/clean_letter_14.ly'
    # TODO:
    #assert      mpp.stylesheet_file_proxy is not None
    assert      mpp.user_input_module_file_name is None
    assert      mpp.user_input_module_importable_name is None
    assert      mpp.user_input_module_proxy is None
