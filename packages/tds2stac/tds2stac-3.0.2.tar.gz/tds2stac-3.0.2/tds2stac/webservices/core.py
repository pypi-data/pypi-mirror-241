# SPDX-FileCopyrightText: 2023 Karlsruher Institut für Technologie
#
# SPDX-License-Identifier: CC0-1.0


import json
import traceback
from typing import Any, List, Union

from lxml import etree

from .. import utils
from ..statics import constants


class ConfigFileWebServicesScraper(object):
    """
    A class for getting the list of webservices that used
    in the `tag_config.json` file.
    """

    def __init__(self, json_file: str):
        self.json_file = json_file
        self.values: list = []
        loaded_json = json.load(open(json_file))
        self.get_values(loaded_json, "tds2stac_webservice_analyser")

    def get_values(self, json_obj: Union[dict, list], key: str):
        """
        A function for getting the list of values of a
        specific key in a json file.
        """
        if isinstance(json_obj, dict):
            for k, v in json_obj.items():
                if k == key:
                    self.values.append(v)
                if isinstance(v, (dict, list)):
                    self.get_values(v, key)
        elif isinstance(json_obj, list):
            for item in json_obj:
                self.get_values(item, key)

        return self.values

    def aslist(self):
        """
        A function for returning the list of webservices
        """
        self.values = list(dict.fromkeys(self.values))
        return self.values

    def __iter__(self):
        """
        A function for returning the iterator of webservices
        """
        return iter(self.aslist())


class WebServiceListScraper(object):
    """
    A class for getting the list of available web services
    of a TDS catalogs.

        Args:
            url (str): The catalog URL from TDS to provide its web services
            auth (tuple, optional): Information for authentication of the TDS catalog
    """

    url: str
    """
    url is the url of the TDS catalog
    """
    auth: Union[tuple, None]
    """
    Authentication for TDS catalog e.g.('user', 'password') (optional)
    """

    def __init__(self, url: str, auth: Union[tuple, None] = None):
        ###############################################
        self.auth = auth
        self.webserivces = []
        url_xml, id_xml, xml = utils.xml_processing(url, self.auth)
        #################################
        # Getting the tree of the xml file
        #################################
        try:
            tree_data = etree.XML(xml)
        except Exception:
            print(
                "Web_Services class: The TDS Catalog URL does not provide any accessible services. Check it manually!"
            )
            # TODO: Add logger
            # self.logger.logger.error(
            #     "Web_Services class: The TDS Catalog URL does not provide any accessible services. Check it manually!"
            # )
            return
        else:
            try:
                ###############################################
                # Getting `dataset`, `catalog_url` and `catalog_id` of the data
                ###############################################
                dataset = tree_data.find("{%s}dataset" % constants.unidata)
                metadata = dataset.find("{%s}metadata" % constants.unidata)
                ########################################
                # Finding sevice tag in data tree element
                ########################################
                service_tag = dataset.find(
                    "{%s}serviceName" % constants.unidata
                )
                if service_tag is None and metadata is not None:
                    service_tag = metadata.find(
                        "{%s}serviceName" % constants.unidata
                    )
                if service_tag is None:
                    # Use services found in the file depends on the version of TDS 4 or 5
                    try:
                        services = tree_data.findall(
                            ".//{%s}service[@serviceType='Compound']"
                            % constants.unidata
                        )
                    except Exception:
                        services = tree_data.findall(
                            ".//{%s}service[@serviceType='compound']"
                            % constants.unidata
                        )
                else:
                    # Use specific named services
                    services = tree_data.findall(
                        ".//{%s}service[@name='%s']"
                        % (constants.unidata, service_tag.text)
                    )
                #############################################
                # Loop over all existing services in the data
                #############################################
                self.webserivces = [
                    s.get("name")
                    for i in services
                    for s in i.findall("{%s}service" % constants.unidata)
                    if (
                        i.get("serviceType") == "Compound"
                        or i.get("serviceType") == "compound"
                    )
                    # and s.get("name") in constants.supported_webservices
                ]
                self.webserivces = list(dict.fromkeys(self.webserivces))
                # TODO: Add logger
                # self.logger.logger.info(self.webserivces)
            except Exception:
                print(
                    "Web_Services class: The TDS Catalog URL does not provide any accessible services!"
                )
                # TODO: Add logger
                # self.logger.logger.error(
                #     "Web_Services class: The TDS Catalog URL does not provide any accessible services!"
                # )
                print(traceback.format_exc())
                return

    def aslist(self):
        return self.webserivces

    def __iter__(self):
        return iter(self.aslist())


class WebServiceContentScraper(object):
    """
    The functionality of the existing class is dependent on the settings
    specified in the `tag_config.json` file in order to harvest targeted
    information from a selected web service. For comprehensive instructions
    on configuring the `tag_config.json` file, refer to the following link:
    :ref:`tag-config`.

        Args:
            root (etree._Element): The root of the XML-based web service
            json_file (str): The path to the `tag_config.json` file
            extensions_list (list): The list of extensions to be harvested
                from the web service (main keys in the `tag_config.json` file)
            harvesting_vars (dict, optional): The dictionary of harvesting variables
    """

    root: etree._Element
    """
    Etree root object of the XML-based web service
    """
    json_file: str
    """
    The path to the `tag_config.json` file
    """
    extensions_list: list
    """
    The list of extensions to be harvested from the web service.
    Main keys in the `tag_config.json` file. For example `item_datacube_extension`
    and so on.
    """
    harvesting_vars: Union[dict, None]
    """
    It's a dictionary that keys are variable names and values are the result of harvesting.
    """

    def __init__(
        self,
        root: etree._Element,
        json_file: str,
        extensions_list: list,
        harvesting_vars: Union[dict, None] = None,
    ):
        ncml_json = json.load(open(json_file))
        self.list_of_all_tags: List[Any] = []
        for extention in extensions_list:
            self.harvester(root, ncml_json, extention, harvesting_vars)

    def harvester(self, root, json_file, ext_name, harvesting_vars=None):
        for k, v in json_file[ext_name].items():
            xpath_string_schema = ""
            namespaces_ = dict()
            action_type = []
            values_with_none_ = []
            list_of_all_tags_with_none = []
            if v is not None and isinstance(v, dict):
                # Main function starts from this point. because it finds the attrs of a tag
                if v["tds2stac_mode_analyser"] == "str":
                    harvesting_vars[k] = v["tds2stac_manual_variable"]
                    # print (k, v["tds2stac_manual_variable"], type(v["tds2stac_manual_variable"]))
                elif v["tds2stac_mode_analyser"] == "list":
                    # TODO: Add a warning to check the list is not empty or in a right format
                    harvesting_vars[k] = (
                        v["tds2stac_manual_variable"].strip("][").split(", ")
                    )
                elif v["tds2stac_mode_analyser"] == "get":
                    # make a function to make a string to input to the xpath function
                    if v.get("tds2stac_reference_key") is not None:
                        # TODO: add warning: if you want to use this feature, it highly recomend to not add more than one null attribute to the nested key
                        for k1, v1 in v.items():
                            if k not in constants.static_list_webservices:
                                # A condition specifically for ISO 19115-2 XML files

                                if isinstance(v1, dict):
                                    # This condition is for finding which method should
                                    # be used to get the result data. For example, if
                                    # all attributed were field, it means we should use
                                    # `tag.text` method to get the result data. If one of
                                    # the attributes were None, it means we should use
                                    # tag.get(attr) method to get the result data.
                                    if v1 == list(v.values())[-1]:
                                        if list(v1.values()).count(None) == 0:
                                            values_with_none_.append(
                                                "text_of_tag"
                                            )
                                            action_type.append("text_of_tag")
                                        elif (
                                            list(v1.values()).count(None) == 1
                                        ):
                                            values_with_none_.extend(
                                                list(v1.values())
                                            )
                                            action_type.append(
                                                list(v1.keys())[
                                                    list(v1.values()).index(
                                                        None
                                                    )
                                                ]
                                            )
                                        elif list(v1.values()).count(None) > 1:
                                            list_of_more_than_one_None = [
                                                v
                                                for i, v in enumerate(
                                                    list(v1.values())
                                                )
                                                if v is None
                                            ]
                                            values_with_none_.extend(
                                                list_of_more_than_one_None
                                            )
                                            list_of_more_than_one_None = [
                                                list(v1.keys())[i]
                                                for i, v in enumerate(
                                                    list(v1.values())
                                                )
                                                if v is None
                                            ]
                                            action_type.extend(
                                                list_of_more_than_one_None
                                            )

                        k_ref = v["tds2stac_reference_key"]
                        v_ref = json_file[ext_name][
                            v["tds2stac_reference_key"]
                        ]
                        for k1, v1 in v_ref.items():
                            if k_ref not in constants.static_list_webservices:
                                # A condition specifically for ISO 19115-2 XML files
                                if ":" in k1:
                                    schema = k1.split(":")[0]
                                    localname = k1.split(":")[1]
                                else:
                                    schema = v_ref[
                                        "tds2stac_webservice_analyser"
                                    ]
                                    localname = k1
                                # In this condition we don't add any attribute to the xpath string
                                if v1 is None:
                                    xpath_string_schema += "/%s:%s" % (
                                        schema,
                                        localname,
                                    )
                                    namespaces_[
                                        schema
                                    ] = constants.schemas_dicts[schema]
                                elif isinstance(v1, dict):
                                    # This condition is for finding which method should
                                    # be used to get the result data. For example, if
                                    # all attributed were field, it means we should use
                                    # tag.text method to get the result data. If one of
                                    # the attributes were None, it means we should use
                                    # tag.get(attr) method to get the result data.

                                    attribute_str = ""  # defining an empty string for collecting all tag elements and attributes for xpath search in the following loop
                                    for k2, v2 in v1.items():
                                        if v2 is not None:
                                            attribute_str += '[@%s="%s"]' % (
                                                k2,
                                                v2,
                                            )
                                        # this condition defined for times that we have need to get one of the attributes of a tag
                                        elif (
                                            v2 is None
                                            and list(v1.values()).count(None)
                                            == 1
                                        ):
                                            attribute_str += "[@%s]" % (k2)
                                        # TODO: For this condition we have to triger (because it's within a loop
                                        # and might issue more than one log) a warning to inform the user that he/she
                                        #  should choose one of the attributes of a tag to restrict the search to the desirable tag attribute
                                        #  otherwise it will return a nested list.of elements that each list in the nested list
                                        #  is content of getting attribute of a tag.
                                        # For example if we define like {'name': null, 'value': null} it will return a nested list
                                        # like  [[... ,... ], [... ,... ]].
                                        elif (
                                            v2 is None
                                            and list(v1.values()).count(None)
                                            > 1
                                        ):
                                            # TODO:we have to define a Logger for this warning

                                            attribute_str += "[@%s]" % (k2)
                                            print(
                                                "Error: It contains more than one null in the nested dict and you have to choose one of them. Revise your json file."
                                            )

                                    xpath_string_schema += "/%s:%s%s" % (
                                        schema,
                                        localname,
                                        attribute_str,
                                    )
                                    namespaces_[
                                        schema
                                    ] = constants.schemas_dicts[schema]

                        if namespaces_ != {}:
                            self.list_of_all_tags = root.xpath(
                                xpath_string_schema, namespaces=namespaces_
                            )
                            if self.list_of_all_tags != []:
                                for a in self.list_of_all_tags:
                                    if a.xpath(".//*") != []:
                                        list_of_all_tags_with_none_temp = []
                                        for xx in a.xpath(".//*"):
                                            if (
                                                values_with_none_[0]
                                                in xx.attrib.values()
                                            ):
                                                list_of_all_tags_with_none_temp.append(
                                                    xx
                                                )
                                            else:
                                                continue
                                        list_of_all_tags_with_none.extend(
                                            list_of_all_tags_with_none_temp
                                        )
                                        if (
                                            list_of_all_tags_with_none_temp
                                            == []
                                        ):
                                            list_of_all_tags_with_none.append(
                                                None
                                            )
                                    else:
                                        list_of_all_tags_with_none.append(None)

                            if len(list_of_all_tags_with_none) == 0:
                                continue
                                # TODO: logger
                                # print("Error: It couldn't find any tag for the considered tag element. It means you should check the tag element name in the json file.")
                            elif (
                                len(list_of_all_tags_with_none) == 1
                                and action_type != []
                            ):
                                if action_type[0] == "text_of_tag":
                                    harvesting_vars[
                                        k
                                    ] = list_of_all_tags_with_none[0].text
                                else:
                                    harvesting_vars[
                                        k
                                    ] = list_of_all_tags_with_none[0].get(
                                        action_type[0]
                                    )
                            elif len(list_of_all_tags_with_none) > 1:
                                if action_type[0] == "text_of_tag":
                                    harvesting_vars[k] = [
                                        a.text if a is not None else None
                                        for a in list_of_all_tags_with_none
                                    ]
                                else:
                                    harvesting_vars[k] = [
                                        a.get(action_type[b])
                                        if a is not None
                                        else None
                                        for b in range(len(action_type))
                                        for a in list_of_all_tags_with_none
                                    ]
                    else:
                        for k1, v1 in v.items():
                            if k not in constants.static_list_webservices:
                                # A condition specifically for ISO 19115-2 XML files
                                if ":" in k1:
                                    schema = k1.split(":")[0]
                                    localname = k1.split(":")[1]
                                else:
                                    schema = v["tds2stac_webservice_analyser"]
                                    localname = k1
                                # In this condition we don't add any attribute to the xpath string
                                if v1 is None:
                                    xpath_string_schema += "/%s:%s" % (
                                        schema,
                                        localname,
                                    )
                                    namespaces_[
                                        schema
                                    ] = constants.schemas_dicts[schema]
                                elif isinstance(v1, dict):
                                    # This condition is for finding which method should
                                    # be used to get the result data. For example, if
                                    # all attributed were field, it means we should use
                                    # tag.text method to get the result data. If one of
                                    # the attributes were None, it means we should use
                                    # tag.get(attr) method to get the result data.
                                    if v1 == list(v.values())[-1]:
                                        if list(v1.values()).count(None) == 0:
                                            action_type.append("text_of_tag")
                                        elif (
                                            list(v1.values()).count(None) == 1
                                        ):
                                            action_type.append(
                                                list(v1.keys())[
                                                    list(v1.values()).index(
                                                        None
                                                    )
                                                ]
                                            )
                                        elif list(v1.values()).count(None) > 1:
                                            list_of_more_than_one_None = [
                                                list(v1.keys())[i]
                                                for i, v in enumerate(
                                                    list(v1.values())
                                                )
                                                if v is None
                                            ]
                                            action_type.extend(
                                                list_of_more_than_one_None
                                            )
                                    attribute_str = ""  # defining an empty string for collecting all tag elements and attributes for xpath search in the following loop
                                    for k2, v2 in v1.items():
                                        if v2 is not None:
                                            attribute_str += '[@%s="%s"]' % (
                                                k2,
                                                v2,
                                            )
                                        # this condition defined for times that we have need to get one of the attributes of a tag
                                        elif (
                                            v2 is None
                                            and list(v1.values()).count(None)
                                            == 1
                                        ):
                                            attribute_str += "[@%s]" % (k2)
                                        # TODO: For this condition we have to triger (because it's within a loop
                                        # and might issue more than one log) a warning to inform the user that he/she
                                        #  should choose one of the attributes of a tag to restrict the search to the desirable tag attribute
                                        #  otherwise it will return a nested list.of elements that each list in the nested list
                                        #  is content of getting attribute of a tag.
                                        # For example if we define like {'name': null, 'value': null} it will return a nested list
                                        # like  [[... ,... ], [... ,... ]].
                                        elif (
                                            v2 is None
                                            and list(v1.values()).count(None)
                                            > 1
                                        ):
                                            # we have to define a Logger for this warning

                                            attribute_str += "[@%s]" % (k2)
                                            # TODO: logger
                                            # print("Error: It contains more than one null in the nested dict and you have to choose one of them. Revise your json file.")

                                    xpath_string_schema += "/%s:%s%s" % (
                                        schema,
                                        localname,
                                        attribute_str,
                                    )
                                    namespaces_[
                                        schema
                                    ] = constants.schemas_dicts[schema]

                        if namespaces_ != {}:
                            self.list_of_all_tags = root.xpath(
                                xpath_string_schema, namespaces=namespaces_
                            )

                            if len(self.list_of_all_tags) == 0:
                                # TODO logger print("Error: It couldn't find any tag for the considered tag element. It means you should check the tag element name in the json file.")
                                continue
                            elif (
                                len(self.list_of_all_tags) == 1
                                and action_type != []
                            ):
                                if action_type[0] == "text_of_tag":
                                    harvesting_vars[k] = self.list_of_all_tags[
                                        0
                                    ].text
                                else:
                                    harvesting_vars[k] = self.list_of_all_tags[
                                        0
                                    ].get(action_type[0])
                            elif len(self.list_of_all_tags) > 1:
                                if action_type[0] == "text_of_tag":
                                    harvesting_vars[k] = [
                                        a.text for a in self.list_of_all_tags
                                    ]
                                else:
                                    harvesting_vars[k] = [
                                        a.get(action_type[b])
                                        for b in range(len(action_type))
                                        for a in self.list_of_all_tags
                                    ]
                elif v["tds2stac_mode_analyser"] == "check":
                    # make a function to make a string to input to the xpath function
                    for k1, v1 in v.items():
                        if k not in constants.static_list_webservices:
                            if ":" in k1:
                                schema = k1.split(":")[0]
                                localname = k1.split(":")[1]
                            else:
                                schema = v["tds2stac_webservice_analyser"]
                                localname = k1
                            if v1 is None:
                                xpath_string_schema += "/%s:%s" % (
                                    schema,
                                    localname,
                                )
                                namespaces_[schema] = constants.schemas_dicts[
                                    schema
                                ]
                            elif isinstance(v1, dict):
                                attribute_str = ""
                                for k2, v2 in v1.items():
                                    if v2 is not None:
                                        attribute_str += '[@%s="%s"]' % (
                                            k2,
                                            v2,
                                        )
                                    elif (
                                        v2 is None
                                        and list(v1.values()).count(None) == 1
                                    ):
                                        attribute_str += "[@%s]" % (k2)
                                    elif (
                                        v2 is None
                                        and v1.values().count(None) > 1
                                    ):
                                        attribute_str += "[@%s]" % (k2)
                                        print(
                                            "Error: It contains more than one null in the nested dict and you have to choose one of them. Revise your json file."
                                        )

                                xpath_string_schema += "/%s:%s%s" % (
                                    schema,
                                    localname,
                                    attribute_str,
                                )
                                namespaces_[schema] = constants.schemas_dicts[
                                    schema
                                ]
                    if namespaces_ != {}:
                        self.list_of_all_tags = root.xpath(
                            xpath_string_schema, namespaces=namespaces_
                        )
                        if len(self.list_of_all_tags) == 0:
                            continue
                            # TODO: logger
                            # print("Error: It couldn't find any tag for the considered tag element. It means you should check the tag element name in the json file.")
                        elif len(self.list_of_all_tags) >= 1:
                            harvesting_vars[k] = v["tds2stac_manual_variable"]
