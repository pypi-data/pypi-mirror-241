# # SPDX-FileCopyrightText: 2023 Karlsruher Institut für Technologie
# #
# # SPDX-License-Identifier: CC0-1.0

# import os
# import shutil

# from tds2stac.main_app import Existance_checker


# def test_existance_checker_true():
#     current_dir = os.getcwd()
#     if not os.path.exists(current_dir + "/stac/"):
#         os.mkdir(current_dir + "/stac/")
#     os.chdir(current_dir + "/stac/")

#     f = open("catalog.json", "w")
#     f.write("Now the file has more content!")
#     f.close()
#     Existance_checker(current_dir)
#     shutil.rmtree(current_dir + "/stac/")


# def test_existance_checker_false():
#     Existance_checker("/Users/PycharmProjects/tds2stac/")
