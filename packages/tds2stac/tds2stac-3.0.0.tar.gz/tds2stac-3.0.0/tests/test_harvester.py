# # SPDX-FileCopyrightText: 2023 Karlsruher Institut für Technologie
# #
# # SPDX-License-Identifier: CC0-1.0

# import sys

# from tds2stac.main_app import Harvester

# sys.path.append("../")


# def test_harvester_first_case_iso_without_lat_long_time():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/regional/seas5_bc/forecast_measures/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         web_service="iso",
#         limited_number=10,
#     )


# def test_harvester_first_case_iso_wit_manually_lat_long_time():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/regional/seas5_bc/forecast_measures/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         web_service="iso",
#         limited_number=10,
#         spatial_information=[0, 0, 0, 0],
#     )


# def test_harvester_first_case_iso():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/raster/global/era5/sfc/single/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         web_service="iso",
#         limited_number=10,
#     )


# def test_harvester_first_case_ncml():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/raster/global/era5/sfc/single/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         web_service="ncml",
#         limited_number=10,
#     )


# def test_harvester_first_case_wms():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/raster/global/era5/sfc/single/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         web_service="wms",
#         limited_number=10,
#     )


# def test_harvester_second_case():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/catalogues/sensor_catalog_ext.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#     )


# def test_harvester_third_case():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/raster/global/chirps/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#     )


# def test_harvester_fourth_case():
#     Harvester(
#         "https://thredds.atmohub.kit.edu/thredds/catalog/snowfogs/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#     )


# def test_harvester_fifth_case():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/climate/raster/global/chelsa/v1.2/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#     )


# def test_harvester_fifth_case_collection_thubmnail():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/climate/raster/global/chelsa/v1.2/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#         collection_thumbnail=True,
#     )


# def test_harvester_fifth_case_item_thubmnail():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/climate/raster/global/chelsa/v1.2/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#         item_thumbnail=True,
#     )


# def test_harvester_fifth_case_item_getminmax_thumbnail():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/climate/raster/global/chelsa/v1.2/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#         item_thumbnail=True,
#         item_getminmax_thumbnail=True,
#     )


# def test_harvester_sixth_case():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/raster/global/era5/sfc/single/daily/catalog.html?dataset=era5_sfc_0.25_single/daily/ERA5_daily_sp_1979.nc",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#     )


# def test_harvester_seventh_case():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/catalogues/climate_catalog_ext.html?dataset=gleam_v3.5a_daily_aggregated",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#     )


# def test_harvester_seventh_case_with_url():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/catalogues/climate_catalog_ext.html?dataset=gleam_v3.5a_daily_aggregated",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         aggregated_dataset_url="https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/raster/global/gleam/v3.5a/catalog.html",
#     )


# def test_harvester_eighth_case():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/catalogues/transfer.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#     )


# def test_harvester_ninth_case():
#     Harvester(
#         "https://thredds.imk-ifu.kit.edu/thredds/catalog/regclim/raster/global/hydrogfd/v3.0/catalog.html",
#         stac=True,
#         stac_id="id",
#         stac_description="description",
#         stac_dir="/Users/hadizadeh-m/stac/",
#         limited_number=10,
#     )
