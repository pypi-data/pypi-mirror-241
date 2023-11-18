# SPDX-FileCopyrightText: 2023 Karlsruher Institut für Technologie
#
# SPDX-License-Identifier: CC0-1.0

import json

# from ..statics import constants


class Verifier(object):  # type: ignore
    def webservice_properties(
        self,
        webservice_properties: dict,
    ):
        if webservice_properties is None:
            # webservice_properties["webservice"] = "all"
            webservice_properties["web_service_config_file"] = "default"
        # elif "webservice" not in webservice_properties.keys():
        #     # TODO: defining a warning, because webservice attribute is mandatory and you didnt define it there we will pu it as all
        #     webservice_properties["webservice"] = "all"
        # elif not any(webservice_properties["webservice"] in str(ws) for ws in constants.supported_webservices):
        #     # TODO: issue a warning that the webservice is not valid and we will put it as all
        #     webservice_properties["webservice"] = "all"
        elif "web_service_config_file" not in webservice_properties.keys():
            # TODO: adding another warning logger here
            webservice_properties["web_service_config_file"] = "default"
        elif "web_service_config_file" in webservice_properties.keys():
            try:
                json.load(
                    open(webservice_properties["web_service_config_file"])
                )
            except Exception:
                # TODO: adding another warning logger here
                print(
                    "The json file is not valid. Check the json file address and try again. For this case we set the `web_service_config_file` to `default`"
                )
                webservice_properties["web_service_config_file"] = "default"

    def extension_properties(
        self,
        extension_properties: dict,
    ):
        List_of_extension_keys = [
            "item_datacube",
            "item_common_metadata",
            "item_scientific",
            "collection_scientific",
            "custom_extension_name",
            "custom_extension_script",
        ]
        custom_extension_keys = [
            "custom_extension_name",
            "custom_extension_script",
        ]
        if extension_properties is None or extension_properties == {}:
            extension_properties["item_datacube"] = False
            extension_properties["item_common_metadata"] = False
            extension_properties["item_scientific"] = False
            extension_properties["collection_scientific"] = False
            extension_properties["custom_extension_name"] = None
            extension_properties["custom_extension_script"] = None

        elif extension_properties is not None or extension_properties != {}:
            for i in List_of_extension_keys:
                if i not in extension_properties.keys():
                    if i not in custom_extension_keys:
                        extension_properties[i] = False
                    else:
                        extension_properties[i] = None

    def asset_properties(
        self,
        asset_properties: dict,
    ):
        asset_properties_list = [
            "item_thumbnail",
            "item_overview",
            "item_getminmax_thumbnail",
            "collection_thumbnail",
            "collection_overview",
            "collection_thumbnail_link",
            "item_assets_list_allowed",
            "item_assets_list_avoided",
            "collection_assets_list_allowed",
            "collection_assets_list_avoided",
            "item_scientific",
            "explore_data",
            "check_get_metadata",
            "jupyter_notebook",
        ]
        none_false_asset_properties = [
            "collection_thumbnail_link",
            "collection_overview",
            "collection_thumbnail",
            "item_assets_list_allowed",
            "item_assets_list_avoided",
            "collection_assets_list_allowed",
            "collection_assets_list_avoided",
        ]
        if asset_properties is None:
            asset_properties["item_thumbnail"] = False
            asset_properties["item_overview"] = False
            asset_properties["item_getminmax_thumbnail"] = False
            asset_properties["collection_thumbnail"] = None
            asset_properties["collection_overview"] = None
            asset_properties["collection_thumbnail_link"] = None
            asset_properties["item_scientific"] = False
            asset_properties["item_assets_list_allowed"] = None
            asset_properties["item_assets_list_avoided"] = None
            asset_properties["collection_assets_list_allowed"] = None
            asset_properties["collection_assets_list_avoided"] = None
            asset_properties["explore_data"] = False
            asset_properties["check_get_metadata"] = False
            asset_properties["jupyter_notebook"] = False

        elif asset_properties is not None:
            for i in asset_properties_list:
                if i not in asset_properties.keys():
                    if i not in none_false_asset_properties:
                        asset_properties[i] = False
                    else:
                        asset_properties[i] = None

    def logger_properties(
        self,
        logger_properties: dict,
    ) -> dict:
        if logger_properties == {}:
            logger_properties["logger_handler"] = "NullHandler"
        return logger_properties
