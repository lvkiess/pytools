import os
from pprint import pprint

import unreal
from collections import OrderedDict

print("test by ccy")
# info = dir(unreal)
# for i in info:
#     unreal.log(i)
asset_paths = unreal.EditorAssetLibrary.list_assets('/Game/ArkGame/Character/Hero/Brother/Brother_Skin_Orange_03/',
                                                    include_folder=True)

load_assets = []
for asset_path in asset_paths:
    if asset_path[-1] != '/':
        # print(asset_path)
        load_asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        load_assets.append(load_asset)
        asset_type = type(load_asset)
        # if "DT_PVPSpawnPatternPool" == str(load_asset.get_name()):
        # print("get_full_name:" + str(load_asset.get_full_name()))
        if "DataTableeeeeeee" == asset_type.__name__:
            # print("Loaded asset type:" + str(asset_type))
            # print("Loaded asset type name:" + asset_type.__name__)
            # print("get_fname:" + str(load_asset.get_fname()))
            print("get_full_name:" + str(load_asset.get_full_name()))
            # print("get_name:" + str(load_asset.get_name()))
            # print("get_path_name:" + str(load_asset.get_path_name()))
            # print("get_class:" + str(load_asset.get_class()))

# skeletal_mesh_objets = unreal.EditorFilterLibrary.by_class(load_assets,unreal.SkeletalMesh.static_class())
# print(skeletal_mesh_objets)


# datatable

print("--------datatable begin--------")

dt = unreal.EditorAssetLibrary.load_asset("/Game/ArkGame/Config/RangeWeapon/RangeWeaponCfg")
print(dt.get_name())
if "DataTableeeeee" == type(dt).__name__:
    print("Loaded asset type:" + str(type(dt)))
    print("Loaded asset type name:" + type(dt).__name__)

    dt_function = unreal.DataTableFunctionLibrary()
    row_names = dt_function.get_data_table_row_names(dt)
    print(row_names)

    weapon_hit_damage_column = "hitdamage"
    weapon_ammo_column = "ammopermag"
    weapon_hit_damage_column = dt_function.get_data_table_column_as_string(dt, weapon_hit_damage_column)
    weapon_ammo = dt_function.get_data_table_column_as_string(dt, weapon_ammo_column)

    all_columns = unreal.ZFunction.get_data_table_column_names(dt)

    for index, row_name in enumerate(row_names):
        print(str(row_name) + " hit player damage: " + str(weapon_hit_damage_column[index]))
    for column in all_columns:
        print(column)

print("--------datatable over--------")
print("--------blueprinter begin--------")

weapon_bp_path_disk = 'H:/_ark_h_H/Trunk/ArkGame/Content/ArkGame/Gameplay/Pickup/Weapon/WeaponPickupAK47.uasset'
ak_bp_path = '/Game/ArkGame/Gameplay/Pickup/Weapon/WeaponPickupAK47'
ak_bp = unreal.EditorAssetLibrary.load_asset(ak_bp_path)

if "Blueprinttttttttttt" == type(ak_bp).__name__:

    keys_list, values_list = unreal.ZFunction.get_default_values_for_blueprint_class(ak_bp_path)
    class_default_dic = OrderedDict(zip(keys_list, values_list))
    for key, value in class_default_dic.items():
        print("Key: {}, Value: {}".format(key, value))

print("--------blueprinter over--------")
print("--------SK begin--------")

bro_disk = 'H:/_ark_h_H/Trunk/ArkGame/Content/ArkGame/Character/Hero/Brother/Brother_Skin_Orange_03/SK_Brother_Skin_Orange_03.uasset'
bro_sk_path = '/Game/ArkGame/Character/Hero/Brother/Brother_Skin_Orange_03/SK_Brother_Skin_Orange_03'

bro_sk = unreal.EditorAssetLibrary.load_asset(bro_sk_path)

print("Loaded asset type name:" + type(bro_sk).__name__)
print(type(bro_sk.get_all_morph_target_names()))
print(bro_sk.get_all_morph_target_names())

lod_info = bro_sk.get_editor_property('lod_info')
print(lod_info)

# info = dir(bro_sk)
# for i in info:
#     unreal.log(i)

print(bro_sk.get_lod_count())
print(bro_sk.get_lod_material_slot(1, 1))
print(bro_sk.get_num_sections(1))

# print(bro_sk.get_lod_build_settings(0))

# info = dir(unreal.EditorStaticMeshLibrary)
# for i in info:
#     unreal.log(i)

# info = dir(unreal.EditorSkeletalMeshLibrary)
# for i in info:
#     unreal.log(i)

# keys_list, values_list = unreal.EditorSkeletalMeshLibrary(bro_sk)
# class_default_dic = OrderedDict(zip(keys_list, values_list))
# for key, value in class_default_dic.items():
#     print("Key: {}, Value: {}".format(key, value))

print("--------SK end--------")
print("--------dep and ref begin--------")

asset_reg = unreal.AssetRegistryHelpers.get_asset_registry()
deps = asset_reg.get_referencers(bro_sk_path, unreal.AssetRegistryDependencyOptions(True, True))
for dep in deps:
    print(dep)
print("==========================")
refs = asset_reg.get_dependencies(bro_sk_path, unreal.AssetRegistryDependencyOptions(True, True))
for ref in refs:
    print(ref)
print("==========================")

referenced_assets = set()
asset = unreal.load_asset(bro_sk_path)

# 使用find_package_referencers_for_asset方法查找引用该资产的所有包
referencers = unreal.EditorAssetLibrary.find_package_referencers_for_asset(bro_sk_path)

# 使用pprint模块打印引用该资产的所有包
pprint(referencers)
for referencer in referencers:
    print(referencer)