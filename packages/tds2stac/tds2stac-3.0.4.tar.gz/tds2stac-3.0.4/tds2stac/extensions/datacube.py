# SPDX-FileCopyrightText: 2023 Karlsruher Institut für Technologie
#
# SPDX-License-Identifier: CC0-1.0
# TODO: make the datacube configurable from outside
# TODO: make the datacube based on two other webservices: iso and wms

from pystac.extensions.datacube import (
    AdditionalDimension,
    DatacubeExtension,
    DimensionType,
    HorizontalSpatialDimension,
    TemporalDimension,
    Variable,
    VariableType,
    VerticalSpatialDimension,
)


class Datacube(object):
    def item_extension(self, item, harvesting_vars):
        variables = (
            {}
        )  # variables dictionary for gathering the Variable objects
        dimensions = (
            {}
        )  # dimensions dictionary for gathering the Dimension objects
        cube = DatacubeExtension.ext(item, add_if_missing=True)

        variable_dimensions = [
            elem.replace(" ", ",").split(",") if " " in elem else [elem]
            for elem in harvesting_vars["variable_dimensions"]
        ]
        if len(harvesting_vars["variable_ids"]) != len(variable_dimensions):
            # Another solution for this is to index each output element and find the None values to decide about them later
            raise ValueError(
                "The length of the variable list and the dimension list are not equal. Check your dataset in Thredds. WE SHOULD EXPLAIN THIS ERROR IN THE DOCUMENTATION"
            )
        else:
            for i, v in enumerate(harvesting_vars["variable_ids"]):
                variable_dict = dict()
                # forth case is when description is not available or is less than then variable ids or dimensions. It's not required then can be ignored
                # Usually every varialbe in ncML has name and shape attrs that it can be used as variable id and dimension.

                variable_dict["dimensions"] = variable_dimensions[i]
                variable_dict["type"] = VariableType.DATA.value
                if (
                    harvesting_vars["variable_description"] is not None
                    and len(harvesting_vars["variable_ids"])
                    == len(harvesting_vars["variable_description"])
                    and len(harvesting_vars["variable_description"])
                    != harvesting_vars["variable_description"].count(None)
                ):
                    if harvesting_vars["variable_description"][i] is not None:
                        variable_dict["description"] = harvesting_vars[
                            "variable_description"
                        ][i]
                variable_dict["dimensions"] = variable_dimensions[i]
                if (
                    harvesting_vars["variable_unit"] is not None
                    and len(harvesting_vars["variable_unit"])
                    == len(variable_dimensions)
                    and len(harvesting_vars["variable_unit"])
                    != harvesting_vars["variable_unit"].count(None)
                ):
                    if harvesting_vars["variable_unit"][i] is not None:
                        variable_dict["units"] = harvesting_vars[
                            "variable_unit"
                        ][i]
                variables[harvesting_vars["variable_ids"][i]] = Variable(
                    variable_dict
                )

        # Horizontal Spatial Dimension
        list_of_required_keys = [
            "horizontal_ids_lat",
            "horizontal_ids_lon",
            "horizontal_axis_x",
            "horizontal_axis_y",
            "horizontal_extent_lon_min",
            "horizontal_extent_lon_max",
            "horizontal_extent_lat_min",
            "horizontal_extent_lat_max",
        ]
        # TODO: check the possiblity of making the string values as float
        if all(
            harvesting_vars.get(key) is not None
            for key in list_of_required_keys
        ):
            print("test")
            horizontal_dict = dict()
            horizontal_dict = {
                "type": DimensionType.SPATIAL.value,
                "axis": harvesting_vars["horizontal_axis_x"],
                "description": harvesting_vars["horizontal_description_lon"],
                "extent": [
                    float(harvesting_vars["horizontal_extent_lon_min"]),
                    float(harvesting_vars["horizontal_extent_lon_max"]),
                ],
                "reference_system": harvesting_vars[
                    "horizontal_reference_system"
                ],
            }
            dimensions[
                harvesting_vars["horizontal_ids_lon"]
            ] = HorizontalSpatialDimension(horizontal_dict)
            horizontal_dict = dict()
            horizontal_dict = {
                "type": DimensionType.SPATIAL.value,
                "axis": harvesting_vars["horizontal_axis_y"],
                "description": harvesting_vars["horizontal_description_lat"],
                "extent": [
                    float(harvesting_vars["horizontal_extent_lat_min"]),
                    float(harvesting_vars["horizontal_extent_lat_max"]),
                ],
                "reference_system": harvesting_vars[
                    "horizontal_reference_system"
                ],
            }
            dimensions[
                harvesting_vars["horizontal_ids_lat"]
            ] = HorizontalSpatialDimension(horizontal_dict)
        else:
            print(
                "Required attributes are not involved in the output dictionary. Check your dataset in Thredds or config json file. WE SHOULD EXPLAIN THIS ERROR IN THE DOCUMENTATION"
            )

        # Vertical Spatial Dimension
        list_of_required_keys = [
            "vertical_id",
            "vertical_axis",
            "vertical_extent_upper",
            "vertical_extent_lower",
        ]
        if all(
            harvesting_vars.get(key) is not None and harvesting_vars[key] != []
            for key in list_of_required_keys
        ):
            vertical_dict = dict()
            vertical_dict = {
                "type": DimensionType.SPATIAL.value,
                "axis": harvesting_vars["vertical_axis"],
                "description": harvesting_vars["vertical_description"],
                "extent": [
                    float(harvesting_vars["vertical_extent_lower"]),
                    float(harvesting_vars["vertical_extent_upper"]),
                ],
            }
            dimensions[
                harvesting_vars["vertical_id"]
            ] = VerticalSpatialDimension(vertical_dict)
        else:
            print(
                "Required attributes are not involved in the output dictionary. Check your dataset in Thredds or config json file. WE SHOULD EXPLAIN THIS ERROR IN THE DOCUMENTATION"
            )

        # Temporal Dimension
        list_of_required_keys = [
            "temporal_id",
            "temporal_extent_start_datetime",
            "temporal_extent_end_datetime",
        ]
        if all(
            harvesting_vars.get(key) is not None
            for key in list_of_required_keys
        ):
            temporal_dict = dict()
            temporal_dict = {
                "type": DimensionType.TEMPORAL.value,
                "description": harvesting_vars["temporal_description"],
                "extent": [
                    harvesting_vars["temporal_extent_start_datetime"],
                    harvesting_vars["temporal_extent_end_datetime"],
                ],
            }
            dimensions[harvesting_vars["temporal_id"]] = TemporalDimension(
                temporal_dict
            )
        else:
            print(
                "Required attributes are not involved in the output dictionary. Check your dataset in Thredds or config json file. WE SHOULD EXPLAIN THIS ERROR IN THE DOCUMENTATION"
            )

        # Additional Dimensions
        anotherlist = [
            "x",
            "y",
            "time",
            "longitude",
            "latitude",
            "t",
            "z",
            "height",
        ]
        for id in harvesting_vars["additional_ids"]:
            if id.lower() not in [
                i.lower() for i in list(dimensions.keys()) + anotherlist
            ]:
                additional_dict = dict()
                additional_dict = {
                    "type": harvesting_vars["additional_type"],
                    "extent": [None, None],
                }
                dimensions[id] = AdditionalDimension(additional_dict)
        cube.apply(dimensions=dimensions, variables=variables)

    # def item(item, harvesting_vars):
    #     var = []
    #     dim = []
    #     variables = {}  # variables in a STAC-Item
    #     dimensions = {}  # dimensions in a STAC-Item
    #     cube = DatacubeExtension.ext(item, add_if_missing=True)
    #     # Creating dimension and varibles to datacube extension
    #     # TODO: temporary we add the following line to avoid error in STAC validation but we need to find a better solution
    #     # ISSUE #81
    #     # print('harvesting_vars["keyword"]', harvesting_vars["keyword"])
    #     # print('harvesting_vars["var_lists"]', harvesting_vars["var_lists"])
    #     # print('harvesting_vars["var_descs"]', harvesting_vars["var_descs"])
    #     # print('harvesting_vars["var_dims"]', harvesting_vars["var_dims"])
    #     DatacubeExtension.remove_from(item)
    #     for i, v in enumerate(harvesting_vars["var_lists"]):
    #         if harvesting_vars["keyword"] == []:
    #             var.append(
    #                 Variable(
    #                     dict(
    #                         type="data",
    #                         description=harvesting_vars["var_descs"][i],
    #                         dimensions=harvesting_vars["keyword"],
    #                     )
    #                 )
    #             )
    #         else:
    #             var.append(
    #                 Variable(
    #                     dict(
    #                         type="data",
    #                         description=harvesting_vars["var_descs"][i],
    #                         dimensions=harvesting_vars["keyword"][i],
    #                     )
    #                 )
    #             )

    #     for i, v in enumerate(harvesting_vars["var_lists"]):
    #         if harvesting_vars["var_lists"][i] not in harvesting_vars["var_dims"] and harvesting_vars["var_lists"][i] not in harvesting_vars["keyword"]:
    #             variables[v] = var[i]

    #     for i, v in enumerate(harvesting_vars["var_dims"]):
    #         if harvesting_vars["var_dims"][i] == "row" or "lon" in harvesting_vars["var_dims"][i]:
    #             extend_ = [
    #                 harvesting_vars["long_min"].replace(",", "."),
    #                 harvesting_vars["long_max"].replace(",", "."),
    #             ]
    #             type_ = DimensionType.SPATIAL.value
    #             description_ = "longitude"
    #             axis_ = "x"
    #         elif harvesting_vars["var_dims"][i] == "column" or "lat" in harvesting_vars["var_dims"][i]:
    #             extend_ = [
    #                 harvesting_vars["lat_min"].replace(",", "."),
    #                 harvesting_vars["lat_max"].replace(",", "."),
    #             ]
    #             type_ = DimensionType.SPATIAL.value
    #             description_ = "latitude"
    #             axis_ = "y"
    #         elif harvesting_vars["var_dims"][i] == "temporal" or "time" in harvesting_vars["var_dims"][i] or "t" in harvesting_vars["var_dims"][i]:
    #             extend_ = [
    #                 harvesting_vars["time_start"],
    #                 harvesting_vars["time_end"],
    #             ]
    #             type_ = DimensionType.TEMPORAL.value
    #             description_ = "time"
    #             axis_ = "time"
    #         else:
    #             extend_ = None
    #             type_ = DimensionType.SPATIAL.value
    #             description_ = harvesting_vars["var_dims"][i]
    #             axis_ = harvesting_vars["var_dims"][i]

    #         dim.append(
    #             HorizontalSpatialDimension(
    #                 properties=dict(
    #                     axis=axis_,
    #                     extent=extend_,
    #                     description=description_,
    #                     reference_system="epsg:4326",
    #                     type=type_,
    #                 )
    #             )
    #         )
    #     for i, v in enumerate(harvesting_vars["var_dims"]):
    #         dimensions[v] = dim[i]
    #     cube.apply(dimensions=dimensions, variables=variables)
