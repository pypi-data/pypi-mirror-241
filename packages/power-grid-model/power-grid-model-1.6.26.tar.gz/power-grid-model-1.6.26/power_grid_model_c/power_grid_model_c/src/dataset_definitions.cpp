// SPDX-FileCopyrightText: 2022 Contributors to the Power Grid Model project <dynamic.grid.calculation@alliander.com>
//
// SPDX-License-Identifier: MPL-2.0

// This header file is automatically generated. DO NOT modify it manually!

// clang-format off

#define PGM_DLL_EXPORTS
#include "forward_declarations.hpp"
#include "power_grid_model_c/dataset_definitions.h"
#include "power_grid_model_c/meta_data.h"

// dataset input
PGM_MetaDataset const* const PGM_def_input = PGM_meta_get_dataset_by_name(nullptr, "input");
// components of input
// component node
PGM_MetaComponent const* const PGM_def_input_node = PGM_meta_get_component_by_name(nullptr, "input", "node");
// attributes of input node
PGM_MetaAttribute const* const PGM_def_input_node_id = PGM_meta_get_attribute_by_name(nullptr, "input", "node", "id");
PGM_MetaAttribute const* const PGM_def_input_node_u_rated = PGM_meta_get_attribute_by_name(nullptr, "input", "node", "u_rated");
// component line
PGM_MetaComponent const* const PGM_def_input_line = PGM_meta_get_component_by_name(nullptr, "input", "line");
// attributes of input line
PGM_MetaAttribute const* const PGM_def_input_line_id = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "id");
PGM_MetaAttribute const* const PGM_def_input_line_from_node = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "from_node");
PGM_MetaAttribute const* const PGM_def_input_line_to_node = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "to_node");
PGM_MetaAttribute const* const PGM_def_input_line_from_status = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "from_status");
PGM_MetaAttribute const* const PGM_def_input_line_to_status = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "to_status");
PGM_MetaAttribute const* const PGM_def_input_line_r1 = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "r1");
PGM_MetaAttribute const* const PGM_def_input_line_x1 = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "x1");
PGM_MetaAttribute const* const PGM_def_input_line_c1 = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "c1");
PGM_MetaAttribute const* const PGM_def_input_line_tan1 = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "tan1");
PGM_MetaAttribute const* const PGM_def_input_line_r0 = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "r0");
PGM_MetaAttribute const* const PGM_def_input_line_x0 = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "x0");
PGM_MetaAttribute const* const PGM_def_input_line_c0 = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "c0");
PGM_MetaAttribute const* const PGM_def_input_line_tan0 = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "tan0");
PGM_MetaAttribute const* const PGM_def_input_line_i_n = PGM_meta_get_attribute_by_name(nullptr, "input", "line", "i_n");
// component link
PGM_MetaComponent const* const PGM_def_input_link = PGM_meta_get_component_by_name(nullptr, "input", "link");
// attributes of input link
PGM_MetaAttribute const* const PGM_def_input_link_id = PGM_meta_get_attribute_by_name(nullptr, "input", "link", "id");
PGM_MetaAttribute const* const PGM_def_input_link_from_node = PGM_meta_get_attribute_by_name(nullptr, "input", "link", "from_node");
PGM_MetaAttribute const* const PGM_def_input_link_to_node = PGM_meta_get_attribute_by_name(nullptr, "input", "link", "to_node");
PGM_MetaAttribute const* const PGM_def_input_link_from_status = PGM_meta_get_attribute_by_name(nullptr, "input", "link", "from_status");
PGM_MetaAttribute const* const PGM_def_input_link_to_status = PGM_meta_get_attribute_by_name(nullptr, "input", "link", "to_status");
// component transformer
PGM_MetaComponent const* const PGM_def_input_transformer = PGM_meta_get_component_by_name(nullptr, "input", "transformer");
// attributes of input transformer
PGM_MetaAttribute const* const PGM_def_input_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "id");
PGM_MetaAttribute const* const PGM_def_input_transformer_from_node = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "from_node");
PGM_MetaAttribute const* const PGM_def_input_transformer_to_node = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "to_node");
PGM_MetaAttribute const* const PGM_def_input_transformer_from_status = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "from_status");
PGM_MetaAttribute const* const PGM_def_input_transformer_to_status = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "to_status");
PGM_MetaAttribute const* const PGM_def_input_transformer_u1 = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "u1");
PGM_MetaAttribute const* const PGM_def_input_transformer_u2 = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "u2");
PGM_MetaAttribute const* const PGM_def_input_transformer_sn = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "sn");
PGM_MetaAttribute const* const PGM_def_input_transformer_uk = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "uk");
PGM_MetaAttribute const* const PGM_def_input_transformer_pk = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "pk");
PGM_MetaAttribute const* const PGM_def_input_transformer_i0 = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "i0");
PGM_MetaAttribute const* const PGM_def_input_transformer_p0 = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "p0");
PGM_MetaAttribute const* const PGM_def_input_transformer_winding_from = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "winding_from");
PGM_MetaAttribute const* const PGM_def_input_transformer_winding_to = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "winding_to");
PGM_MetaAttribute const* const PGM_def_input_transformer_clock = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "clock");
PGM_MetaAttribute const* const PGM_def_input_transformer_tap_side = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "tap_side");
PGM_MetaAttribute const* const PGM_def_input_transformer_tap_pos = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "tap_pos");
PGM_MetaAttribute const* const PGM_def_input_transformer_tap_min = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "tap_min");
PGM_MetaAttribute const* const PGM_def_input_transformer_tap_max = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "tap_max");
PGM_MetaAttribute const* const PGM_def_input_transformer_tap_nom = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "tap_nom");
PGM_MetaAttribute const* const PGM_def_input_transformer_tap_size = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "tap_size");
PGM_MetaAttribute const* const PGM_def_input_transformer_uk_min = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "uk_min");
PGM_MetaAttribute const* const PGM_def_input_transformer_uk_max = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "uk_max");
PGM_MetaAttribute const* const PGM_def_input_transformer_pk_min = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "pk_min");
PGM_MetaAttribute const* const PGM_def_input_transformer_pk_max = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "pk_max");
PGM_MetaAttribute const* const PGM_def_input_transformer_r_grounding_from = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "r_grounding_from");
PGM_MetaAttribute const* const PGM_def_input_transformer_x_grounding_from = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "x_grounding_from");
PGM_MetaAttribute const* const PGM_def_input_transformer_r_grounding_to = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "r_grounding_to");
PGM_MetaAttribute const* const PGM_def_input_transformer_x_grounding_to = PGM_meta_get_attribute_by_name(nullptr, "input", "transformer", "x_grounding_to");
// component three_winding_transformer
PGM_MetaComponent const* const PGM_def_input_three_winding_transformer = PGM_meta_get_component_by_name(nullptr, "input", "three_winding_transformer");
// attributes of input three_winding_transformer
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "id");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_node_1 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "node_1");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_node_2 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "node_2");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_node_3 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "node_3");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_status_1 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "status_1");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_status_2 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "status_2");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_status_3 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "status_3");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_u1 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "u1");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_u2 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "u2");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_u3 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "u3");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_sn_1 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "sn_1");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_sn_2 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "sn_2");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_sn_3 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "sn_3");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_12 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_12");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_13 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_13");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_23 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_23");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_12 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_12");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_13 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_13");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_23 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_23");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_i0 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "i0");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_p0 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "p0");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_winding_1 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "winding_1");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_winding_2 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "winding_2");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_winding_3 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "winding_3");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_clock_12 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "clock_12");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_clock_13 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "clock_13");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_tap_side = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "tap_side");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_tap_pos = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "tap_pos");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_tap_min = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "tap_min");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_tap_max = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "tap_max");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_tap_nom = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "tap_nom");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_tap_size = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "tap_size");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_12_min = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_12_min");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_12_max = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_12_max");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_13_min = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_13_min");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_13_max = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_13_max");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_23_min = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_23_min");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_uk_23_max = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "uk_23_max");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_12_min = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_12_min");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_12_max = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_12_max");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_13_min = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_13_min");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_13_max = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_13_max");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_23_min = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_23_min");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_pk_23_max = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "pk_23_max");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_r_grounding_1 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "r_grounding_1");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_x_grounding_1 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "x_grounding_1");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_r_grounding_2 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "r_grounding_2");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_x_grounding_2 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "x_grounding_2");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_r_grounding_3 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "r_grounding_3");
PGM_MetaAttribute const* const PGM_def_input_three_winding_transformer_x_grounding_3 = PGM_meta_get_attribute_by_name(nullptr, "input", "three_winding_transformer", "x_grounding_3");
// component sym_load
PGM_MetaComponent const* const PGM_def_input_sym_load = PGM_meta_get_component_by_name(nullptr, "input", "sym_load");
// attributes of input sym_load
PGM_MetaAttribute const* const PGM_def_input_sym_load_id = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_load", "id");
PGM_MetaAttribute const* const PGM_def_input_sym_load_node = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_load", "node");
PGM_MetaAttribute const* const PGM_def_input_sym_load_status = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_load", "status");
PGM_MetaAttribute const* const PGM_def_input_sym_load_type = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_load", "type");
PGM_MetaAttribute const* const PGM_def_input_sym_load_p_specified = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_load", "p_specified");
PGM_MetaAttribute const* const PGM_def_input_sym_load_q_specified = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_load", "q_specified");
// component sym_gen
PGM_MetaComponent const* const PGM_def_input_sym_gen = PGM_meta_get_component_by_name(nullptr, "input", "sym_gen");
// attributes of input sym_gen
PGM_MetaAttribute const* const PGM_def_input_sym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_gen", "id");
PGM_MetaAttribute const* const PGM_def_input_sym_gen_node = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_gen", "node");
PGM_MetaAttribute const* const PGM_def_input_sym_gen_status = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_gen", "status");
PGM_MetaAttribute const* const PGM_def_input_sym_gen_type = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_gen", "type");
PGM_MetaAttribute const* const PGM_def_input_sym_gen_p_specified = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_gen", "p_specified");
PGM_MetaAttribute const* const PGM_def_input_sym_gen_q_specified = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_gen", "q_specified");
// component asym_load
PGM_MetaComponent const* const PGM_def_input_asym_load = PGM_meta_get_component_by_name(nullptr, "input", "asym_load");
// attributes of input asym_load
PGM_MetaAttribute const* const PGM_def_input_asym_load_id = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_load", "id");
PGM_MetaAttribute const* const PGM_def_input_asym_load_node = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_load", "node");
PGM_MetaAttribute const* const PGM_def_input_asym_load_status = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_load", "status");
PGM_MetaAttribute const* const PGM_def_input_asym_load_type = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_load", "type");
PGM_MetaAttribute const* const PGM_def_input_asym_load_p_specified = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_load", "p_specified");
PGM_MetaAttribute const* const PGM_def_input_asym_load_q_specified = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_load", "q_specified");
// component asym_gen
PGM_MetaComponent const* const PGM_def_input_asym_gen = PGM_meta_get_component_by_name(nullptr, "input", "asym_gen");
// attributes of input asym_gen
PGM_MetaAttribute const* const PGM_def_input_asym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_gen", "id");
PGM_MetaAttribute const* const PGM_def_input_asym_gen_node = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_gen", "node");
PGM_MetaAttribute const* const PGM_def_input_asym_gen_status = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_gen", "status");
PGM_MetaAttribute const* const PGM_def_input_asym_gen_type = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_gen", "type");
PGM_MetaAttribute const* const PGM_def_input_asym_gen_p_specified = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_gen", "p_specified");
PGM_MetaAttribute const* const PGM_def_input_asym_gen_q_specified = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_gen", "q_specified");
// component shunt
PGM_MetaComponent const* const PGM_def_input_shunt = PGM_meta_get_component_by_name(nullptr, "input", "shunt");
// attributes of input shunt
PGM_MetaAttribute const* const PGM_def_input_shunt_id = PGM_meta_get_attribute_by_name(nullptr, "input", "shunt", "id");
PGM_MetaAttribute const* const PGM_def_input_shunt_node = PGM_meta_get_attribute_by_name(nullptr, "input", "shunt", "node");
PGM_MetaAttribute const* const PGM_def_input_shunt_status = PGM_meta_get_attribute_by_name(nullptr, "input", "shunt", "status");
PGM_MetaAttribute const* const PGM_def_input_shunt_g1 = PGM_meta_get_attribute_by_name(nullptr, "input", "shunt", "g1");
PGM_MetaAttribute const* const PGM_def_input_shunt_b1 = PGM_meta_get_attribute_by_name(nullptr, "input", "shunt", "b1");
PGM_MetaAttribute const* const PGM_def_input_shunt_g0 = PGM_meta_get_attribute_by_name(nullptr, "input", "shunt", "g0");
PGM_MetaAttribute const* const PGM_def_input_shunt_b0 = PGM_meta_get_attribute_by_name(nullptr, "input", "shunt", "b0");
// component source
PGM_MetaComponent const* const PGM_def_input_source = PGM_meta_get_component_by_name(nullptr, "input", "source");
// attributes of input source
PGM_MetaAttribute const* const PGM_def_input_source_id = PGM_meta_get_attribute_by_name(nullptr, "input", "source", "id");
PGM_MetaAttribute const* const PGM_def_input_source_node = PGM_meta_get_attribute_by_name(nullptr, "input", "source", "node");
PGM_MetaAttribute const* const PGM_def_input_source_status = PGM_meta_get_attribute_by_name(nullptr, "input", "source", "status");
PGM_MetaAttribute const* const PGM_def_input_source_u_ref = PGM_meta_get_attribute_by_name(nullptr, "input", "source", "u_ref");
PGM_MetaAttribute const* const PGM_def_input_source_u_ref_angle = PGM_meta_get_attribute_by_name(nullptr, "input", "source", "u_ref_angle");
PGM_MetaAttribute const* const PGM_def_input_source_sk = PGM_meta_get_attribute_by_name(nullptr, "input", "source", "sk");
PGM_MetaAttribute const* const PGM_def_input_source_rx_ratio = PGM_meta_get_attribute_by_name(nullptr, "input", "source", "rx_ratio");
PGM_MetaAttribute const* const PGM_def_input_source_z01_ratio = PGM_meta_get_attribute_by_name(nullptr, "input", "source", "z01_ratio");
// component sym_voltage_sensor
PGM_MetaComponent const* const PGM_def_input_sym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "input", "sym_voltage_sensor");
// attributes of input sym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_input_sym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_input_sym_voltage_sensor_measured_object = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_voltage_sensor", "measured_object");
PGM_MetaAttribute const* const PGM_def_input_sym_voltage_sensor_u_sigma = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_voltage_sensor", "u_sigma");
PGM_MetaAttribute const* const PGM_def_input_sym_voltage_sensor_u_measured = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_voltage_sensor", "u_measured");
PGM_MetaAttribute const* const PGM_def_input_sym_voltage_sensor_u_angle_measured = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_voltage_sensor", "u_angle_measured");
// component asym_voltage_sensor
PGM_MetaComponent const* const PGM_def_input_asym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "input", "asym_voltage_sensor");
// attributes of input asym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_input_asym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_input_asym_voltage_sensor_measured_object = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_voltage_sensor", "measured_object");
PGM_MetaAttribute const* const PGM_def_input_asym_voltage_sensor_u_sigma = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_voltage_sensor", "u_sigma");
PGM_MetaAttribute const* const PGM_def_input_asym_voltage_sensor_u_measured = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_voltage_sensor", "u_measured");
PGM_MetaAttribute const* const PGM_def_input_asym_voltage_sensor_u_angle_measured = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_voltage_sensor", "u_angle_measured");
// component sym_power_sensor
PGM_MetaComponent const* const PGM_def_input_sym_power_sensor = PGM_meta_get_component_by_name(nullptr, "input", "sym_power_sensor");
// attributes of input sym_power_sensor
PGM_MetaAttribute const* const PGM_def_input_sym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_input_sym_power_sensor_measured_object = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_power_sensor", "measured_object");
PGM_MetaAttribute const* const PGM_def_input_sym_power_sensor_measured_terminal_type = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_power_sensor", "measured_terminal_type");
PGM_MetaAttribute const* const PGM_def_input_sym_power_sensor_power_sigma = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_power_sensor", "power_sigma");
PGM_MetaAttribute const* const PGM_def_input_sym_power_sensor_p_measured = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_power_sensor", "p_measured");
PGM_MetaAttribute const* const PGM_def_input_sym_power_sensor_q_measured = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_power_sensor", "q_measured");
PGM_MetaAttribute const* const PGM_def_input_sym_power_sensor_p_sigma = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_power_sensor", "p_sigma");
PGM_MetaAttribute const* const PGM_def_input_sym_power_sensor_q_sigma = PGM_meta_get_attribute_by_name(nullptr, "input", "sym_power_sensor", "q_sigma");
// component asym_power_sensor
PGM_MetaComponent const* const PGM_def_input_asym_power_sensor = PGM_meta_get_component_by_name(nullptr, "input", "asym_power_sensor");
// attributes of input asym_power_sensor
PGM_MetaAttribute const* const PGM_def_input_asym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_input_asym_power_sensor_measured_object = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_power_sensor", "measured_object");
PGM_MetaAttribute const* const PGM_def_input_asym_power_sensor_measured_terminal_type = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_power_sensor", "measured_terminal_type");
PGM_MetaAttribute const* const PGM_def_input_asym_power_sensor_power_sigma = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_power_sensor", "power_sigma");
PGM_MetaAttribute const* const PGM_def_input_asym_power_sensor_p_measured = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_power_sensor", "p_measured");
PGM_MetaAttribute const* const PGM_def_input_asym_power_sensor_q_measured = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_power_sensor", "q_measured");
PGM_MetaAttribute const* const PGM_def_input_asym_power_sensor_p_sigma = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_power_sensor", "p_sigma");
PGM_MetaAttribute const* const PGM_def_input_asym_power_sensor_q_sigma = PGM_meta_get_attribute_by_name(nullptr, "input", "asym_power_sensor", "q_sigma");
// component fault
PGM_MetaComponent const* const PGM_def_input_fault = PGM_meta_get_component_by_name(nullptr, "input", "fault");
// attributes of input fault
PGM_MetaAttribute const* const PGM_def_input_fault_id = PGM_meta_get_attribute_by_name(nullptr, "input", "fault", "id");
PGM_MetaAttribute const* const PGM_def_input_fault_status = PGM_meta_get_attribute_by_name(nullptr, "input", "fault", "status");
PGM_MetaAttribute const* const PGM_def_input_fault_fault_type = PGM_meta_get_attribute_by_name(nullptr, "input", "fault", "fault_type");
PGM_MetaAttribute const* const PGM_def_input_fault_fault_phase = PGM_meta_get_attribute_by_name(nullptr, "input", "fault", "fault_phase");
PGM_MetaAttribute const* const PGM_def_input_fault_fault_object = PGM_meta_get_attribute_by_name(nullptr, "input", "fault", "fault_object");
PGM_MetaAttribute const* const PGM_def_input_fault_r_f = PGM_meta_get_attribute_by_name(nullptr, "input", "fault", "r_f");
PGM_MetaAttribute const* const PGM_def_input_fault_x_f = PGM_meta_get_attribute_by_name(nullptr, "input", "fault", "x_f");
// dataset sym_output
PGM_MetaDataset const* const PGM_def_sym_output = PGM_meta_get_dataset_by_name(nullptr, "sym_output");
// components of sym_output
// component node
PGM_MetaComponent const* const PGM_def_sym_output_node = PGM_meta_get_component_by_name(nullptr, "sym_output", "node");
// attributes of sym_output node
PGM_MetaAttribute const* const PGM_def_sym_output_node_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "node", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_node_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "node", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_node_u_pu = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "node", "u_pu");
PGM_MetaAttribute const* const PGM_def_sym_output_node_u = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "node", "u");
PGM_MetaAttribute const* const PGM_def_sym_output_node_u_angle = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "node", "u_angle");
PGM_MetaAttribute const* const PGM_def_sym_output_node_p = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "node", "p");
PGM_MetaAttribute const* const PGM_def_sym_output_node_q = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "node", "q");
// component line
PGM_MetaComponent const* const PGM_def_sym_output_line = PGM_meta_get_component_by_name(nullptr, "sym_output", "line");
// attributes of sym_output line
PGM_MetaAttribute const* const PGM_def_sym_output_line_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_line_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_line_loading = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "loading");
PGM_MetaAttribute const* const PGM_def_sym_output_line_p_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "p_from");
PGM_MetaAttribute const* const PGM_def_sym_output_line_q_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "q_from");
PGM_MetaAttribute const* const PGM_def_sym_output_line_i_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "i_from");
PGM_MetaAttribute const* const PGM_def_sym_output_line_s_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "s_from");
PGM_MetaAttribute const* const PGM_def_sym_output_line_p_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "p_to");
PGM_MetaAttribute const* const PGM_def_sym_output_line_q_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "q_to");
PGM_MetaAttribute const* const PGM_def_sym_output_line_i_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "i_to");
PGM_MetaAttribute const* const PGM_def_sym_output_line_s_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "line", "s_to");
// component link
PGM_MetaComponent const* const PGM_def_sym_output_link = PGM_meta_get_component_by_name(nullptr, "sym_output", "link");
// attributes of sym_output link
PGM_MetaAttribute const* const PGM_def_sym_output_link_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_link_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_link_loading = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "loading");
PGM_MetaAttribute const* const PGM_def_sym_output_link_p_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "p_from");
PGM_MetaAttribute const* const PGM_def_sym_output_link_q_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "q_from");
PGM_MetaAttribute const* const PGM_def_sym_output_link_i_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "i_from");
PGM_MetaAttribute const* const PGM_def_sym_output_link_s_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "s_from");
PGM_MetaAttribute const* const PGM_def_sym_output_link_p_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "p_to");
PGM_MetaAttribute const* const PGM_def_sym_output_link_q_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "q_to");
PGM_MetaAttribute const* const PGM_def_sym_output_link_i_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "i_to");
PGM_MetaAttribute const* const PGM_def_sym_output_link_s_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "link", "s_to");
// component transformer
PGM_MetaComponent const* const PGM_def_sym_output_transformer = PGM_meta_get_component_by_name(nullptr, "sym_output", "transformer");
// attributes of sym_output transformer
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_loading = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "loading");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_p_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "p_from");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_q_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "q_from");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_i_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "i_from");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_s_from = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "s_from");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_p_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "p_to");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_q_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "q_to");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_i_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "i_to");
PGM_MetaAttribute const* const PGM_def_sym_output_transformer_s_to = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "transformer", "s_to");
// component three_winding_transformer
PGM_MetaComponent const* const PGM_def_sym_output_three_winding_transformer = PGM_meta_get_component_by_name(nullptr, "sym_output", "three_winding_transformer");
// attributes of sym_output three_winding_transformer
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_loading = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "loading");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_p_1 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "p_1");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_q_1 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "q_1");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_i_1 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "i_1");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_s_1 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "s_1");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_p_2 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "p_2");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_q_2 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "q_2");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_i_2 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "i_2");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_s_2 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "s_2");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_p_3 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "p_3");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_q_3 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "q_3");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_i_3 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "i_3");
PGM_MetaAttribute const* const PGM_def_sym_output_three_winding_transformer_s_3 = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "three_winding_transformer", "s_3");
// component sym_load
PGM_MetaComponent const* const PGM_def_sym_output_sym_load = PGM_meta_get_component_by_name(nullptr, "sym_output", "sym_load");
// attributes of sym_output sym_load
PGM_MetaAttribute const* const PGM_def_sym_output_sym_load_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_load", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_load_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_load", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_load_p = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_load", "p");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_load_q = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_load", "q");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_load_i = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_load", "i");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_load_s = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_load", "s");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_load_pf = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_load", "pf");
// component sym_gen
PGM_MetaComponent const* const PGM_def_sym_output_sym_gen = PGM_meta_get_component_by_name(nullptr, "sym_output", "sym_gen");
// attributes of sym_output sym_gen
PGM_MetaAttribute const* const PGM_def_sym_output_sym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_gen", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_gen_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_gen", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_gen_p = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_gen", "p");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_gen_q = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_gen", "q");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_gen_i = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_gen", "i");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_gen_s = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_gen", "s");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_gen_pf = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_gen", "pf");
// component asym_load
PGM_MetaComponent const* const PGM_def_sym_output_asym_load = PGM_meta_get_component_by_name(nullptr, "sym_output", "asym_load");
// attributes of sym_output asym_load
PGM_MetaAttribute const* const PGM_def_sym_output_asym_load_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_load", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_load_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_load", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_load_p = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_load", "p");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_load_q = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_load", "q");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_load_i = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_load", "i");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_load_s = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_load", "s");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_load_pf = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_load", "pf");
// component asym_gen
PGM_MetaComponent const* const PGM_def_sym_output_asym_gen = PGM_meta_get_component_by_name(nullptr, "sym_output", "asym_gen");
// attributes of sym_output asym_gen
PGM_MetaAttribute const* const PGM_def_sym_output_asym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_gen", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_gen_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_gen", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_gen_p = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_gen", "p");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_gen_q = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_gen", "q");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_gen_i = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_gen", "i");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_gen_s = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_gen", "s");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_gen_pf = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_gen", "pf");
// component shunt
PGM_MetaComponent const* const PGM_def_sym_output_shunt = PGM_meta_get_component_by_name(nullptr, "sym_output", "shunt");
// attributes of sym_output shunt
PGM_MetaAttribute const* const PGM_def_sym_output_shunt_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "shunt", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_shunt_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "shunt", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_shunt_p = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "shunt", "p");
PGM_MetaAttribute const* const PGM_def_sym_output_shunt_q = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "shunt", "q");
PGM_MetaAttribute const* const PGM_def_sym_output_shunt_i = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "shunt", "i");
PGM_MetaAttribute const* const PGM_def_sym_output_shunt_s = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "shunt", "s");
PGM_MetaAttribute const* const PGM_def_sym_output_shunt_pf = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "shunt", "pf");
// component source
PGM_MetaComponent const* const PGM_def_sym_output_source = PGM_meta_get_component_by_name(nullptr, "sym_output", "source");
// attributes of sym_output source
PGM_MetaAttribute const* const PGM_def_sym_output_source_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "source", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_source_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "source", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_source_p = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "source", "p");
PGM_MetaAttribute const* const PGM_def_sym_output_source_q = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "source", "q");
PGM_MetaAttribute const* const PGM_def_sym_output_source_i = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "source", "i");
PGM_MetaAttribute const* const PGM_def_sym_output_source_s = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "source", "s");
PGM_MetaAttribute const* const PGM_def_sym_output_source_pf = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "source", "pf");
// component sym_voltage_sensor
PGM_MetaComponent const* const PGM_def_sym_output_sym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "sym_output", "sym_voltage_sensor");
// attributes of sym_output sym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_sym_output_sym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_voltage_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_voltage_sensor", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_voltage_sensor_u_residual = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_voltage_sensor", "u_residual");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_voltage_sensor_u_angle_residual = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_voltage_sensor", "u_angle_residual");
// component asym_voltage_sensor
PGM_MetaComponent const* const PGM_def_sym_output_asym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "sym_output", "asym_voltage_sensor");
// attributes of sym_output asym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_sym_output_asym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_voltage_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_voltage_sensor", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_voltage_sensor_u_residual = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_voltage_sensor", "u_residual");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_voltage_sensor_u_angle_residual = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_voltage_sensor", "u_angle_residual");
// component sym_power_sensor
PGM_MetaComponent const* const PGM_def_sym_output_sym_power_sensor = PGM_meta_get_component_by_name(nullptr, "sym_output", "sym_power_sensor");
// attributes of sym_output sym_power_sensor
PGM_MetaAttribute const* const PGM_def_sym_output_sym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_power_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_power_sensor", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_power_sensor_p_residual = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_power_sensor", "p_residual");
PGM_MetaAttribute const* const PGM_def_sym_output_sym_power_sensor_q_residual = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "sym_power_sensor", "q_residual");
// component asym_power_sensor
PGM_MetaComponent const* const PGM_def_sym_output_asym_power_sensor = PGM_meta_get_component_by_name(nullptr, "sym_output", "asym_power_sensor");
// attributes of sym_output asym_power_sensor
PGM_MetaAttribute const* const PGM_def_sym_output_asym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_power_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_power_sensor", "energized");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_power_sensor_p_residual = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_power_sensor", "p_residual");
PGM_MetaAttribute const* const PGM_def_sym_output_asym_power_sensor_q_residual = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "asym_power_sensor", "q_residual");
// component fault
PGM_MetaComponent const* const PGM_def_sym_output_fault = PGM_meta_get_component_by_name(nullptr, "sym_output", "fault");
// attributes of sym_output fault
PGM_MetaAttribute const* const PGM_def_sym_output_fault_id = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "fault", "id");
PGM_MetaAttribute const* const PGM_def_sym_output_fault_energized = PGM_meta_get_attribute_by_name(nullptr, "sym_output", "fault", "energized");
// dataset asym_output
PGM_MetaDataset const* const PGM_def_asym_output = PGM_meta_get_dataset_by_name(nullptr, "asym_output");
// components of asym_output
// component node
PGM_MetaComponent const* const PGM_def_asym_output_node = PGM_meta_get_component_by_name(nullptr, "asym_output", "node");
// attributes of asym_output node
PGM_MetaAttribute const* const PGM_def_asym_output_node_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "node", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_node_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "node", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_node_u_pu = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "node", "u_pu");
PGM_MetaAttribute const* const PGM_def_asym_output_node_u = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "node", "u");
PGM_MetaAttribute const* const PGM_def_asym_output_node_u_angle = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "node", "u_angle");
PGM_MetaAttribute const* const PGM_def_asym_output_node_p = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "node", "p");
PGM_MetaAttribute const* const PGM_def_asym_output_node_q = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "node", "q");
// component line
PGM_MetaComponent const* const PGM_def_asym_output_line = PGM_meta_get_component_by_name(nullptr, "asym_output", "line");
// attributes of asym_output line
PGM_MetaAttribute const* const PGM_def_asym_output_line_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_line_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_line_loading = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "loading");
PGM_MetaAttribute const* const PGM_def_asym_output_line_p_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "p_from");
PGM_MetaAttribute const* const PGM_def_asym_output_line_q_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "q_from");
PGM_MetaAttribute const* const PGM_def_asym_output_line_i_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "i_from");
PGM_MetaAttribute const* const PGM_def_asym_output_line_s_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "s_from");
PGM_MetaAttribute const* const PGM_def_asym_output_line_p_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "p_to");
PGM_MetaAttribute const* const PGM_def_asym_output_line_q_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "q_to");
PGM_MetaAttribute const* const PGM_def_asym_output_line_i_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "i_to");
PGM_MetaAttribute const* const PGM_def_asym_output_line_s_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "line", "s_to");
// component link
PGM_MetaComponent const* const PGM_def_asym_output_link = PGM_meta_get_component_by_name(nullptr, "asym_output", "link");
// attributes of asym_output link
PGM_MetaAttribute const* const PGM_def_asym_output_link_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_link_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_link_loading = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "loading");
PGM_MetaAttribute const* const PGM_def_asym_output_link_p_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "p_from");
PGM_MetaAttribute const* const PGM_def_asym_output_link_q_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "q_from");
PGM_MetaAttribute const* const PGM_def_asym_output_link_i_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "i_from");
PGM_MetaAttribute const* const PGM_def_asym_output_link_s_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "s_from");
PGM_MetaAttribute const* const PGM_def_asym_output_link_p_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "p_to");
PGM_MetaAttribute const* const PGM_def_asym_output_link_q_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "q_to");
PGM_MetaAttribute const* const PGM_def_asym_output_link_i_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "i_to");
PGM_MetaAttribute const* const PGM_def_asym_output_link_s_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "link", "s_to");
// component transformer
PGM_MetaComponent const* const PGM_def_asym_output_transformer = PGM_meta_get_component_by_name(nullptr, "asym_output", "transformer");
// attributes of asym_output transformer
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_loading = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "loading");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_p_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "p_from");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_q_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "q_from");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_i_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "i_from");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_s_from = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "s_from");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_p_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "p_to");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_q_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "q_to");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_i_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "i_to");
PGM_MetaAttribute const* const PGM_def_asym_output_transformer_s_to = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "transformer", "s_to");
// component three_winding_transformer
PGM_MetaComponent const* const PGM_def_asym_output_three_winding_transformer = PGM_meta_get_component_by_name(nullptr, "asym_output", "three_winding_transformer");
// attributes of asym_output three_winding_transformer
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_loading = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "loading");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_p_1 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "p_1");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_q_1 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "q_1");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_i_1 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "i_1");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_s_1 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "s_1");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_p_2 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "p_2");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_q_2 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "q_2");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_i_2 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "i_2");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_s_2 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "s_2");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_p_3 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "p_3");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_q_3 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "q_3");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_i_3 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "i_3");
PGM_MetaAttribute const* const PGM_def_asym_output_three_winding_transformer_s_3 = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "three_winding_transformer", "s_3");
// component sym_load
PGM_MetaComponent const* const PGM_def_asym_output_sym_load = PGM_meta_get_component_by_name(nullptr, "asym_output", "sym_load");
// attributes of asym_output sym_load
PGM_MetaAttribute const* const PGM_def_asym_output_sym_load_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_load", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_load_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_load", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_load_p = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_load", "p");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_load_q = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_load", "q");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_load_i = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_load", "i");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_load_s = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_load", "s");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_load_pf = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_load", "pf");
// component sym_gen
PGM_MetaComponent const* const PGM_def_asym_output_sym_gen = PGM_meta_get_component_by_name(nullptr, "asym_output", "sym_gen");
// attributes of asym_output sym_gen
PGM_MetaAttribute const* const PGM_def_asym_output_sym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_gen", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_gen_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_gen", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_gen_p = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_gen", "p");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_gen_q = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_gen", "q");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_gen_i = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_gen", "i");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_gen_s = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_gen", "s");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_gen_pf = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_gen", "pf");
// component asym_load
PGM_MetaComponent const* const PGM_def_asym_output_asym_load = PGM_meta_get_component_by_name(nullptr, "asym_output", "asym_load");
// attributes of asym_output asym_load
PGM_MetaAttribute const* const PGM_def_asym_output_asym_load_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_load", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_load_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_load", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_load_p = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_load", "p");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_load_q = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_load", "q");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_load_i = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_load", "i");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_load_s = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_load", "s");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_load_pf = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_load", "pf");
// component asym_gen
PGM_MetaComponent const* const PGM_def_asym_output_asym_gen = PGM_meta_get_component_by_name(nullptr, "asym_output", "asym_gen");
// attributes of asym_output asym_gen
PGM_MetaAttribute const* const PGM_def_asym_output_asym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_gen", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_gen_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_gen", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_gen_p = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_gen", "p");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_gen_q = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_gen", "q");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_gen_i = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_gen", "i");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_gen_s = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_gen", "s");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_gen_pf = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_gen", "pf");
// component shunt
PGM_MetaComponent const* const PGM_def_asym_output_shunt = PGM_meta_get_component_by_name(nullptr, "asym_output", "shunt");
// attributes of asym_output shunt
PGM_MetaAttribute const* const PGM_def_asym_output_shunt_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "shunt", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_shunt_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "shunt", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_shunt_p = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "shunt", "p");
PGM_MetaAttribute const* const PGM_def_asym_output_shunt_q = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "shunt", "q");
PGM_MetaAttribute const* const PGM_def_asym_output_shunt_i = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "shunt", "i");
PGM_MetaAttribute const* const PGM_def_asym_output_shunt_s = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "shunt", "s");
PGM_MetaAttribute const* const PGM_def_asym_output_shunt_pf = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "shunt", "pf");
// component source
PGM_MetaComponent const* const PGM_def_asym_output_source = PGM_meta_get_component_by_name(nullptr, "asym_output", "source");
// attributes of asym_output source
PGM_MetaAttribute const* const PGM_def_asym_output_source_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "source", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_source_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "source", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_source_p = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "source", "p");
PGM_MetaAttribute const* const PGM_def_asym_output_source_q = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "source", "q");
PGM_MetaAttribute const* const PGM_def_asym_output_source_i = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "source", "i");
PGM_MetaAttribute const* const PGM_def_asym_output_source_s = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "source", "s");
PGM_MetaAttribute const* const PGM_def_asym_output_source_pf = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "source", "pf");
// component sym_voltage_sensor
PGM_MetaComponent const* const PGM_def_asym_output_sym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "asym_output", "sym_voltage_sensor");
// attributes of asym_output sym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_asym_output_sym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_voltage_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_voltage_sensor", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_voltage_sensor_u_residual = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_voltage_sensor", "u_residual");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_voltage_sensor_u_angle_residual = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_voltage_sensor", "u_angle_residual");
// component asym_voltage_sensor
PGM_MetaComponent const* const PGM_def_asym_output_asym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "asym_output", "asym_voltage_sensor");
// attributes of asym_output asym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_asym_output_asym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_voltage_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_voltage_sensor", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_voltage_sensor_u_residual = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_voltage_sensor", "u_residual");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_voltage_sensor_u_angle_residual = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_voltage_sensor", "u_angle_residual");
// component sym_power_sensor
PGM_MetaComponent const* const PGM_def_asym_output_sym_power_sensor = PGM_meta_get_component_by_name(nullptr, "asym_output", "sym_power_sensor");
// attributes of asym_output sym_power_sensor
PGM_MetaAttribute const* const PGM_def_asym_output_sym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_power_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_power_sensor", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_power_sensor_p_residual = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_power_sensor", "p_residual");
PGM_MetaAttribute const* const PGM_def_asym_output_sym_power_sensor_q_residual = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "sym_power_sensor", "q_residual");
// component asym_power_sensor
PGM_MetaComponent const* const PGM_def_asym_output_asym_power_sensor = PGM_meta_get_component_by_name(nullptr, "asym_output", "asym_power_sensor");
// attributes of asym_output asym_power_sensor
PGM_MetaAttribute const* const PGM_def_asym_output_asym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_power_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_power_sensor", "energized");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_power_sensor_p_residual = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_power_sensor", "p_residual");
PGM_MetaAttribute const* const PGM_def_asym_output_asym_power_sensor_q_residual = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "asym_power_sensor", "q_residual");
// component fault
PGM_MetaComponent const* const PGM_def_asym_output_fault = PGM_meta_get_component_by_name(nullptr, "asym_output", "fault");
// attributes of asym_output fault
PGM_MetaAttribute const* const PGM_def_asym_output_fault_id = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "fault", "id");
PGM_MetaAttribute const* const PGM_def_asym_output_fault_energized = PGM_meta_get_attribute_by_name(nullptr, "asym_output", "fault", "energized");
// dataset update
PGM_MetaDataset const* const PGM_def_update = PGM_meta_get_dataset_by_name(nullptr, "update");
// components of update
// component node
PGM_MetaComponent const* const PGM_def_update_node = PGM_meta_get_component_by_name(nullptr, "update", "node");
// attributes of update node
PGM_MetaAttribute const* const PGM_def_update_node_id = PGM_meta_get_attribute_by_name(nullptr, "update", "node", "id");
// component line
PGM_MetaComponent const* const PGM_def_update_line = PGM_meta_get_component_by_name(nullptr, "update", "line");
// attributes of update line
PGM_MetaAttribute const* const PGM_def_update_line_id = PGM_meta_get_attribute_by_name(nullptr, "update", "line", "id");
PGM_MetaAttribute const* const PGM_def_update_line_from_status = PGM_meta_get_attribute_by_name(nullptr, "update", "line", "from_status");
PGM_MetaAttribute const* const PGM_def_update_line_to_status = PGM_meta_get_attribute_by_name(nullptr, "update", "line", "to_status");
// component link
PGM_MetaComponent const* const PGM_def_update_link = PGM_meta_get_component_by_name(nullptr, "update", "link");
// attributes of update link
PGM_MetaAttribute const* const PGM_def_update_link_id = PGM_meta_get_attribute_by_name(nullptr, "update", "link", "id");
PGM_MetaAttribute const* const PGM_def_update_link_from_status = PGM_meta_get_attribute_by_name(nullptr, "update", "link", "from_status");
PGM_MetaAttribute const* const PGM_def_update_link_to_status = PGM_meta_get_attribute_by_name(nullptr, "update", "link", "to_status");
// component transformer
PGM_MetaComponent const* const PGM_def_update_transformer = PGM_meta_get_component_by_name(nullptr, "update", "transformer");
// attributes of update transformer
PGM_MetaAttribute const* const PGM_def_update_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "update", "transformer", "id");
PGM_MetaAttribute const* const PGM_def_update_transformer_from_status = PGM_meta_get_attribute_by_name(nullptr, "update", "transformer", "from_status");
PGM_MetaAttribute const* const PGM_def_update_transformer_to_status = PGM_meta_get_attribute_by_name(nullptr, "update", "transformer", "to_status");
PGM_MetaAttribute const* const PGM_def_update_transformer_tap_pos = PGM_meta_get_attribute_by_name(nullptr, "update", "transformer", "tap_pos");
// component three_winding_transformer
PGM_MetaComponent const* const PGM_def_update_three_winding_transformer = PGM_meta_get_component_by_name(nullptr, "update", "three_winding_transformer");
// attributes of update three_winding_transformer
PGM_MetaAttribute const* const PGM_def_update_three_winding_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "update", "three_winding_transformer", "id");
PGM_MetaAttribute const* const PGM_def_update_three_winding_transformer_status_1 = PGM_meta_get_attribute_by_name(nullptr, "update", "three_winding_transformer", "status_1");
PGM_MetaAttribute const* const PGM_def_update_three_winding_transformer_status_2 = PGM_meta_get_attribute_by_name(nullptr, "update", "three_winding_transformer", "status_2");
PGM_MetaAttribute const* const PGM_def_update_three_winding_transformer_status_3 = PGM_meta_get_attribute_by_name(nullptr, "update", "three_winding_transformer", "status_3");
PGM_MetaAttribute const* const PGM_def_update_three_winding_transformer_tap_pos = PGM_meta_get_attribute_by_name(nullptr, "update", "three_winding_transformer", "tap_pos");
// component sym_load
PGM_MetaComponent const* const PGM_def_update_sym_load = PGM_meta_get_component_by_name(nullptr, "update", "sym_load");
// attributes of update sym_load
PGM_MetaAttribute const* const PGM_def_update_sym_load_id = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_load", "id");
PGM_MetaAttribute const* const PGM_def_update_sym_load_status = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_load", "status");
PGM_MetaAttribute const* const PGM_def_update_sym_load_p_specified = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_load", "p_specified");
PGM_MetaAttribute const* const PGM_def_update_sym_load_q_specified = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_load", "q_specified");
// component sym_gen
PGM_MetaComponent const* const PGM_def_update_sym_gen = PGM_meta_get_component_by_name(nullptr, "update", "sym_gen");
// attributes of update sym_gen
PGM_MetaAttribute const* const PGM_def_update_sym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_gen", "id");
PGM_MetaAttribute const* const PGM_def_update_sym_gen_status = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_gen", "status");
PGM_MetaAttribute const* const PGM_def_update_sym_gen_p_specified = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_gen", "p_specified");
PGM_MetaAttribute const* const PGM_def_update_sym_gen_q_specified = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_gen", "q_specified");
// component asym_load
PGM_MetaComponent const* const PGM_def_update_asym_load = PGM_meta_get_component_by_name(nullptr, "update", "asym_load");
// attributes of update asym_load
PGM_MetaAttribute const* const PGM_def_update_asym_load_id = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_load", "id");
PGM_MetaAttribute const* const PGM_def_update_asym_load_status = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_load", "status");
PGM_MetaAttribute const* const PGM_def_update_asym_load_p_specified = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_load", "p_specified");
PGM_MetaAttribute const* const PGM_def_update_asym_load_q_specified = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_load", "q_specified");
// component asym_gen
PGM_MetaComponent const* const PGM_def_update_asym_gen = PGM_meta_get_component_by_name(nullptr, "update", "asym_gen");
// attributes of update asym_gen
PGM_MetaAttribute const* const PGM_def_update_asym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_gen", "id");
PGM_MetaAttribute const* const PGM_def_update_asym_gen_status = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_gen", "status");
PGM_MetaAttribute const* const PGM_def_update_asym_gen_p_specified = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_gen", "p_specified");
PGM_MetaAttribute const* const PGM_def_update_asym_gen_q_specified = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_gen", "q_specified");
// component shunt
PGM_MetaComponent const* const PGM_def_update_shunt = PGM_meta_get_component_by_name(nullptr, "update", "shunt");
// attributes of update shunt
PGM_MetaAttribute const* const PGM_def_update_shunt_id = PGM_meta_get_attribute_by_name(nullptr, "update", "shunt", "id");
PGM_MetaAttribute const* const PGM_def_update_shunt_status = PGM_meta_get_attribute_by_name(nullptr, "update", "shunt", "status");
// component source
PGM_MetaComponent const* const PGM_def_update_source = PGM_meta_get_component_by_name(nullptr, "update", "source");
// attributes of update source
PGM_MetaAttribute const* const PGM_def_update_source_id = PGM_meta_get_attribute_by_name(nullptr, "update", "source", "id");
PGM_MetaAttribute const* const PGM_def_update_source_status = PGM_meta_get_attribute_by_name(nullptr, "update", "source", "status");
PGM_MetaAttribute const* const PGM_def_update_source_u_ref = PGM_meta_get_attribute_by_name(nullptr, "update", "source", "u_ref");
PGM_MetaAttribute const* const PGM_def_update_source_u_ref_angle = PGM_meta_get_attribute_by_name(nullptr, "update", "source", "u_ref_angle");
// component sym_voltage_sensor
PGM_MetaComponent const* const PGM_def_update_sym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "update", "sym_voltage_sensor");
// attributes of update sym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_update_sym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_update_sym_voltage_sensor_u_sigma = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_voltage_sensor", "u_sigma");
PGM_MetaAttribute const* const PGM_def_update_sym_voltage_sensor_u_measured = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_voltage_sensor", "u_measured");
PGM_MetaAttribute const* const PGM_def_update_sym_voltage_sensor_u_angle_measured = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_voltage_sensor", "u_angle_measured");
// component asym_voltage_sensor
PGM_MetaComponent const* const PGM_def_update_asym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "update", "asym_voltage_sensor");
// attributes of update asym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_update_asym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_update_asym_voltage_sensor_u_sigma = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_voltage_sensor", "u_sigma");
PGM_MetaAttribute const* const PGM_def_update_asym_voltage_sensor_u_measured = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_voltage_sensor", "u_measured");
PGM_MetaAttribute const* const PGM_def_update_asym_voltage_sensor_u_angle_measured = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_voltage_sensor", "u_angle_measured");
// component sym_power_sensor
PGM_MetaComponent const* const PGM_def_update_sym_power_sensor = PGM_meta_get_component_by_name(nullptr, "update", "sym_power_sensor");
// attributes of update sym_power_sensor
PGM_MetaAttribute const* const PGM_def_update_sym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_update_sym_power_sensor_power_sigma = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_power_sensor", "power_sigma");
PGM_MetaAttribute const* const PGM_def_update_sym_power_sensor_p_measured = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_power_sensor", "p_measured");
PGM_MetaAttribute const* const PGM_def_update_sym_power_sensor_q_measured = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_power_sensor", "q_measured");
PGM_MetaAttribute const* const PGM_def_update_sym_power_sensor_p_sigma = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_power_sensor", "p_sigma");
PGM_MetaAttribute const* const PGM_def_update_sym_power_sensor_q_sigma = PGM_meta_get_attribute_by_name(nullptr, "update", "sym_power_sensor", "q_sigma");
// component asym_power_sensor
PGM_MetaComponent const* const PGM_def_update_asym_power_sensor = PGM_meta_get_component_by_name(nullptr, "update", "asym_power_sensor");
// attributes of update asym_power_sensor
PGM_MetaAttribute const* const PGM_def_update_asym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_update_asym_power_sensor_power_sigma = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_power_sensor", "power_sigma");
PGM_MetaAttribute const* const PGM_def_update_asym_power_sensor_p_measured = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_power_sensor", "p_measured");
PGM_MetaAttribute const* const PGM_def_update_asym_power_sensor_q_measured = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_power_sensor", "q_measured");
PGM_MetaAttribute const* const PGM_def_update_asym_power_sensor_p_sigma = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_power_sensor", "p_sigma");
PGM_MetaAttribute const* const PGM_def_update_asym_power_sensor_q_sigma = PGM_meta_get_attribute_by_name(nullptr, "update", "asym_power_sensor", "q_sigma");
// component fault
PGM_MetaComponent const* const PGM_def_update_fault = PGM_meta_get_component_by_name(nullptr, "update", "fault");
// attributes of update fault
PGM_MetaAttribute const* const PGM_def_update_fault_id = PGM_meta_get_attribute_by_name(nullptr, "update", "fault", "id");
PGM_MetaAttribute const* const PGM_def_update_fault_status = PGM_meta_get_attribute_by_name(nullptr, "update", "fault", "status");
PGM_MetaAttribute const* const PGM_def_update_fault_fault_type = PGM_meta_get_attribute_by_name(nullptr, "update", "fault", "fault_type");
PGM_MetaAttribute const* const PGM_def_update_fault_fault_phase = PGM_meta_get_attribute_by_name(nullptr, "update", "fault", "fault_phase");
PGM_MetaAttribute const* const PGM_def_update_fault_fault_object = PGM_meta_get_attribute_by_name(nullptr, "update", "fault", "fault_object");
PGM_MetaAttribute const* const PGM_def_update_fault_r_f = PGM_meta_get_attribute_by_name(nullptr, "update", "fault", "r_f");
PGM_MetaAttribute const* const PGM_def_update_fault_x_f = PGM_meta_get_attribute_by_name(nullptr, "update", "fault", "x_f");
// dataset sc_output
PGM_MetaDataset const* const PGM_def_sc_output = PGM_meta_get_dataset_by_name(nullptr, "sc_output");
// components of sc_output
// component node
PGM_MetaComponent const* const PGM_def_sc_output_node = PGM_meta_get_component_by_name(nullptr, "sc_output", "node");
// attributes of sc_output node
PGM_MetaAttribute const* const PGM_def_sc_output_node_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "node", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_node_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "node", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_node_u_pu = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "node", "u_pu");
PGM_MetaAttribute const* const PGM_def_sc_output_node_u = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "node", "u");
PGM_MetaAttribute const* const PGM_def_sc_output_node_u_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "node", "u_angle");
// component line
PGM_MetaComponent const* const PGM_def_sc_output_line = PGM_meta_get_component_by_name(nullptr, "sc_output", "line");
// attributes of sc_output line
PGM_MetaAttribute const* const PGM_def_sc_output_line_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "line", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_line_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "line", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_line_i_from = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "line", "i_from");
PGM_MetaAttribute const* const PGM_def_sc_output_line_i_from_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "line", "i_from_angle");
PGM_MetaAttribute const* const PGM_def_sc_output_line_i_to = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "line", "i_to");
PGM_MetaAttribute const* const PGM_def_sc_output_line_i_to_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "line", "i_to_angle");
// component link
PGM_MetaComponent const* const PGM_def_sc_output_link = PGM_meta_get_component_by_name(nullptr, "sc_output", "link");
// attributes of sc_output link
PGM_MetaAttribute const* const PGM_def_sc_output_link_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "link", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_link_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "link", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_link_i_from = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "link", "i_from");
PGM_MetaAttribute const* const PGM_def_sc_output_link_i_from_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "link", "i_from_angle");
PGM_MetaAttribute const* const PGM_def_sc_output_link_i_to = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "link", "i_to");
PGM_MetaAttribute const* const PGM_def_sc_output_link_i_to_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "link", "i_to_angle");
// component transformer
PGM_MetaComponent const* const PGM_def_sc_output_transformer = PGM_meta_get_component_by_name(nullptr, "sc_output", "transformer");
// attributes of sc_output transformer
PGM_MetaAttribute const* const PGM_def_sc_output_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "transformer", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_transformer_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "transformer", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_transformer_i_from = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "transformer", "i_from");
PGM_MetaAttribute const* const PGM_def_sc_output_transformer_i_from_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "transformer", "i_from_angle");
PGM_MetaAttribute const* const PGM_def_sc_output_transformer_i_to = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "transformer", "i_to");
PGM_MetaAttribute const* const PGM_def_sc_output_transformer_i_to_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "transformer", "i_to_angle");
// component three_winding_transformer
PGM_MetaComponent const* const PGM_def_sc_output_three_winding_transformer = PGM_meta_get_component_by_name(nullptr, "sc_output", "three_winding_transformer");
// attributes of sc_output three_winding_transformer
PGM_MetaAttribute const* const PGM_def_sc_output_three_winding_transformer_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "three_winding_transformer", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_three_winding_transformer_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "three_winding_transformer", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_three_winding_transformer_i_1 = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "three_winding_transformer", "i_1");
PGM_MetaAttribute const* const PGM_def_sc_output_three_winding_transformer_i_1_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "three_winding_transformer", "i_1_angle");
PGM_MetaAttribute const* const PGM_def_sc_output_three_winding_transformer_i_2 = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "three_winding_transformer", "i_2");
PGM_MetaAttribute const* const PGM_def_sc_output_three_winding_transformer_i_2_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "three_winding_transformer", "i_2_angle");
PGM_MetaAttribute const* const PGM_def_sc_output_three_winding_transformer_i_3 = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "three_winding_transformer", "i_3");
PGM_MetaAttribute const* const PGM_def_sc_output_three_winding_transformer_i_3_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "three_winding_transformer", "i_3_angle");
// component sym_load
PGM_MetaComponent const* const PGM_def_sc_output_sym_load = PGM_meta_get_component_by_name(nullptr, "sc_output", "sym_load");
// attributes of sc_output sym_load
PGM_MetaAttribute const* const PGM_def_sc_output_sym_load_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_load", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_sym_load_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_load", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_sym_load_i = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_load", "i");
PGM_MetaAttribute const* const PGM_def_sc_output_sym_load_i_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_load", "i_angle");
// component sym_gen
PGM_MetaComponent const* const PGM_def_sc_output_sym_gen = PGM_meta_get_component_by_name(nullptr, "sc_output", "sym_gen");
// attributes of sc_output sym_gen
PGM_MetaAttribute const* const PGM_def_sc_output_sym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_gen", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_sym_gen_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_gen", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_sym_gen_i = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_gen", "i");
PGM_MetaAttribute const* const PGM_def_sc_output_sym_gen_i_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_gen", "i_angle");
// component asym_load
PGM_MetaComponent const* const PGM_def_sc_output_asym_load = PGM_meta_get_component_by_name(nullptr, "sc_output", "asym_load");
// attributes of sc_output asym_load
PGM_MetaAttribute const* const PGM_def_sc_output_asym_load_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_load", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_asym_load_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_load", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_asym_load_i = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_load", "i");
PGM_MetaAttribute const* const PGM_def_sc_output_asym_load_i_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_load", "i_angle");
// component asym_gen
PGM_MetaComponent const* const PGM_def_sc_output_asym_gen = PGM_meta_get_component_by_name(nullptr, "sc_output", "asym_gen");
// attributes of sc_output asym_gen
PGM_MetaAttribute const* const PGM_def_sc_output_asym_gen_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_gen", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_asym_gen_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_gen", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_asym_gen_i = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_gen", "i");
PGM_MetaAttribute const* const PGM_def_sc_output_asym_gen_i_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_gen", "i_angle");
// component shunt
PGM_MetaComponent const* const PGM_def_sc_output_shunt = PGM_meta_get_component_by_name(nullptr, "sc_output", "shunt");
// attributes of sc_output shunt
PGM_MetaAttribute const* const PGM_def_sc_output_shunt_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "shunt", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_shunt_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "shunt", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_shunt_i = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "shunt", "i");
PGM_MetaAttribute const* const PGM_def_sc_output_shunt_i_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "shunt", "i_angle");
// component source
PGM_MetaComponent const* const PGM_def_sc_output_source = PGM_meta_get_component_by_name(nullptr, "sc_output", "source");
// attributes of sc_output source
PGM_MetaAttribute const* const PGM_def_sc_output_source_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "source", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_source_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "source", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_source_i = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "source", "i");
PGM_MetaAttribute const* const PGM_def_sc_output_source_i_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "source", "i_angle");
// component sym_voltage_sensor
PGM_MetaComponent const* const PGM_def_sc_output_sym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "sc_output", "sym_voltage_sensor");
// attributes of sc_output sym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_sc_output_sym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_sym_voltage_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_voltage_sensor", "energized");
// component asym_voltage_sensor
PGM_MetaComponent const* const PGM_def_sc_output_asym_voltage_sensor = PGM_meta_get_component_by_name(nullptr, "sc_output", "asym_voltage_sensor");
// attributes of sc_output asym_voltage_sensor
PGM_MetaAttribute const* const PGM_def_sc_output_asym_voltage_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_voltage_sensor", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_asym_voltage_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_voltage_sensor", "energized");
// component sym_power_sensor
PGM_MetaComponent const* const PGM_def_sc_output_sym_power_sensor = PGM_meta_get_component_by_name(nullptr, "sc_output", "sym_power_sensor");
// attributes of sc_output sym_power_sensor
PGM_MetaAttribute const* const PGM_def_sc_output_sym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_sym_power_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "sym_power_sensor", "energized");
// component asym_power_sensor
PGM_MetaComponent const* const PGM_def_sc_output_asym_power_sensor = PGM_meta_get_component_by_name(nullptr, "sc_output", "asym_power_sensor");
// attributes of sc_output asym_power_sensor
PGM_MetaAttribute const* const PGM_def_sc_output_asym_power_sensor_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_power_sensor", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_asym_power_sensor_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "asym_power_sensor", "energized");
// component fault
PGM_MetaComponent const* const PGM_def_sc_output_fault = PGM_meta_get_component_by_name(nullptr, "sc_output", "fault");
// attributes of sc_output fault
PGM_MetaAttribute const* const PGM_def_sc_output_fault_id = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "fault", "id");
PGM_MetaAttribute const* const PGM_def_sc_output_fault_energized = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "fault", "energized");
PGM_MetaAttribute const* const PGM_def_sc_output_fault_i_f = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "fault", "i_f");
PGM_MetaAttribute const* const PGM_def_sc_output_fault_i_f_angle = PGM_meta_get_attribute_by_name(nullptr, "sc_output", "fault", "i_f_angle");
//

// clang-format on
