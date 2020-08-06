import build
import os


def main():
    preset_args = [
        {'type': 'zip', 'resource': ['none'], 'hash': False, 'output': None},
        {'type': 'zip', 'resource': ['blue_ui'],
            'hash': False, 'output': None},
        {'type': 'zip', 'resource': [
            'bagify', 'observer_think', 'ore_highlight', 'trident_model'], 'hash': False, 'output': None},
        {'type': 'mcpack', 'resource': ['none'],
            'hash': False, 'output': None},
        {'type': 'mcpack', 'resource': ['blue_ui'],
            'hash': False, 'output': None},
        {'type': 'mcpack', 'resource': [
            'bagify', 'observer_think', 'ore_highlight', 'trident_model'], 'hash': False, 'output': None},
        {'type': 'zip', 'resource': ['all'], 'hash': False, 'output': None},
        {'type': 'mcpack', 'resource': ['all'], 'hash': False, 'output': None}
    ]
    preset_name = [
        "meme-resourcepack_noresource_noblueui.zip",
        "meme-resourcepack_noresource.zip",
        "meme-resourcepack_noblueui.zip",
        "meme-resourcepack_noresource_noblueui.mcpack",
        "meme-resourcepack_noresource.mcpack",
        "meme-resourcepack_noblueui.mcpack",
        "meme-resourcepack.zip",
        "meme-resourcepack.mcpack"
    ]
    pack_builder = build.builder()
    pack_counter = 0
    perfect_pack_counter = 0
    base_folder = "builds"
    if os.path.exists(base_folder) and not os.path.isdir(base_folder):
        os.remove(base_folder)
    if not os.path.exists(base_folder):
        os.mkdir(base_folder)
    for file in os.listdir(base_folder):
        os.remove(os.path.join(base_folder, file))
    for item, name in zip(preset_args, preset_name):
        pack_builder.set_args(item)
        pack_builder.build()
        if pack_builder.get_error_count() == 0:
            pack_counter += 1
            if pack_builder.get_warning_count() == 0:
                perfect_pack_counter += 1
            if name != "meme-resourcepack.zip" and name != "meme-resourcepack.mcpack":
                original_name = os.path.join(
                    base_folder, pack_builder.get_filename())
                os.rename(original_name,
                          os.path.join(base_folder, name))
            print(f"Renamed pack to {name}.")
        else:
            print(f"Failed to build pack {name}.")
    print(
        f"\nBuilt {pack_counter} packs with {perfect_pack_counter} pack(s) no warning.")


if __name__ == '__main__':
    main()