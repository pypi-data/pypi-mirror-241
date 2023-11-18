# SPDX-FileCopyrightText: 2023 Karlsruher Institut für Technologie
#
# SPDX-License-Identifier: EUPL-1.2

"""Test file for imports."""


def test_package_import():
    """Test the import of the main package."""
    import tds2stac  # noqa: F401


# # nested depth = 0
# def test_cc():
#     TDS2STACIntegrator(
#         "http://localhost:8080/thredds/catalog/testAll/catalog.html?dataset=testDatasetScan/2004050412_eta_211.nc",
#         stac_dir="stac/",
#     )
