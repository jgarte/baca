.. _baca--segmentmaker:

segmentmaker
============

.. automodule:: baca.segmentmaker

.. currentmodule:: baca.segmentmaker

.. container:: svg-container

   .. inheritance-diagram:: baca
      :lineage: baca.segmentmaker

.. raw:: html

   <hr/>

.. rubric:: Classes
   :class: section-header

.. autosummary::
   :nosignatures:

   ~SegmentMaker

.. autoclass:: SegmentMaker

   .. raw:: html

      <hr/>

   .. rubric:: Attributes Summary
      :class: class-header

   .. autosummary::
      :nosignatures:

      __call__
      activate
      allow_empty_selections
      breaks
      check_all_are_pitched
      clock_time_extra_offset
      clock_time_override
      color_octaves
      commands
      deactivate
      do_not_check_beamed_long_notes
      do_not_check_out_of_range_pitches
      do_not_check_persistence
      do_not_check_wellformedness
      do_not_force_nonnatural_accidentals
      do_not_include_layout_ly
      fermata_measure_empty_overrides
      final_segment
      first_measure_number
      first_segment
      ignore_repeat_pitch_classes
      includes
      instruments
      lilypond_file
      local_measure_number_extra_offset
      magnify_staves
      manifests
      margin_markups
      measure_count
      measure_number_extra_offset
      metadata
      metronome_marks
      midi
      parts_metric_modulation_multiplier
      persist
      previous_metadata
      previous_persist
      remove_phantom_measure
      run
      score_template
      skips_instead_of_rests
      spacing
      spacing_extra_offset
      stage_markup
      stage_number_extra_offset
      test_container_identifiers
      time_signatures
      transpose_score
      validate_measure_count
      voice_metadata

   .. raw:: html

      <hr/>

   .. rubric:: Special methods
      :class: class-header

   .. automethod:: SegmentMaker.__call__

   .. container:: inherited

      .. automethod:: SegmentMaker.__eq__

   .. container:: inherited

      .. automethod:: SegmentMaker.__hash__

   .. container:: inherited

      .. automethod:: SegmentMaker.__illustrate__

   .. container:: inherited

      .. automethod:: SegmentMaker.__repr__

   .. raw:: html

      <hr/>

   .. rubric:: Methods
      :class: class-header

   .. automethod:: SegmentMaker.run

   .. raw:: html

      <hr/>

   .. rubric:: Class & static methods
      :class: class-header

   .. container:: inherited

      .. automethod:: SegmentMaker.comment_measure_numbers

   .. raw:: html

      <hr/>

   .. rubric:: Read-only properties
      :class: class-header

   .. autoattribute:: SegmentMaker.activate

   .. autoattribute:: SegmentMaker.allow_empty_selections

   .. autoattribute:: SegmentMaker.breaks

   .. autoattribute:: SegmentMaker.check_all_are_pitched

   .. autoattribute:: SegmentMaker.clock_time_extra_offset

   .. autoattribute:: SegmentMaker.clock_time_override

   .. autoattribute:: SegmentMaker.color_octaves

   .. autoattribute:: SegmentMaker.commands

   .. autoattribute:: SegmentMaker.deactivate

   .. autoattribute:: SegmentMaker.do_not_check_beamed_long_notes

   .. autoattribute:: SegmentMaker.do_not_check_out_of_range_pitches

   .. autoattribute:: SegmentMaker.do_not_check_persistence

   .. autoattribute:: SegmentMaker.do_not_check_wellformedness

   .. autoattribute:: SegmentMaker.do_not_force_nonnatural_accidentals

   .. autoattribute:: SegmentMaker.do_not_include_layout_ly

   .. container:: inherited

      .. autoattribute:: SegmentMaker.environment

   .. autoattribute:: SegmentMaker.fermata_measure_empty_overrides

   .. autoattribute:: SegmentMaker.final_segment

   .. autoattribute:: SegmentMaker.first_measure_number

   .. autoattribute:: SegmentMaker.first_segment

   .. autoattribute:: SegmentMaker.ignore_repeat_pitch_classes

   .. autoattribute:: SegmentMaker.includes

   .. autoattribute:: SegmentMaker.instruments

   .. autoattribute:: SegmentMaker.lilypond_file

   .. autoattribute:: SegmentMaker.local_measure_number_extra_offset

   .. autoattribute:: SegmentMaker.magnify_staves

   .. autoattribute:: SegmentMaker.manifests

   .. autoattribute:: SegmentMaker.margin_markups

   .. autoattribute:: SegmentMaker.measure_count

   .. autoattribute:: SegmentMaker.measure_number_extra_offset

   .. autoattribute:: SegmentMaker.metadata

   .. autoattribute:: SegmentMaker.metronome_marks

   .. autoattribute:: SegmentMaker.midi

   .. autoattribute:: SegmentMaker.parts_metric_modulation_multiplier

   .. autoattribute:: SegmentMaker.persist

   .. autoattribute:: SegmentMaker.previous_metadata

   .. autoattribute:: SegmentMaker.previous_persist

   .. autoattribute:: SegmentMaker.remove_phantom_measure

   .. container:: inherited

      .. autoattribute:: SegmentMaker.score

   .. autoattribute:: SegmentMaker.score_template

   .. container:: inherited

      .. autoattribute:: SegmentMaker.segment_directory

   .. container:: inherited

      .. autoattribute:: SegmentMaker.segment_name

   .. autoattribute:: SegmentMaker.skips_instead_of_rests

   .. autoattribute:: SegmentMaker.spacing

   .. autoattribute:: SegmentMaker.spacing_extra_offset

   .. autoattribute:: SegmentMaker.stage_markup

   .. autoattribute:: SegmentMaker.stage_number_extra_offset

   .. autoattribute:: SegmentMaker.test_container_identifiers

   .. autoattribute:: SegmentMaker.time_signatures

   .. autoattribute:: SegmentMaker.transpose_score

   .. autoattribute:: SegmentMaker.validate_measure_count

   .. autoattribute:: SegmentMaker.voice_metadata