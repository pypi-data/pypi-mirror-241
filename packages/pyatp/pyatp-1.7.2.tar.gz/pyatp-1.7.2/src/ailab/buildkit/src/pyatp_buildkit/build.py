def get_package_location():
    import ailab
    dir_name = os.path.dirname(os.path.dirname(ailab.__file__))
    return dir_name


import os
import shutil
def create_and_copy_directories(data, base_dir, wrapper_dir="wrappers"):
    for subcategory, subcategory_path in data.items():
        category_dir = os.path.join(base_dir, wrapper_dir)
        os.makedirs(category_dir, exist_ok=True)

        subcategory_before_path = get_package_location()
        subcategory_path = os.path.join(subcategory_before_path, subcategory_path)



        # Check for wrapper.py and wrapper_full.py
        wrapper_path = os.path.join(subcategory_path, "wrapper.py")
        wrapper_full_path = os.path.join(subcategory_path, "wrapper_full.py")

        if os.path.exists(wrapper_full_path):
            category_full_dir = os.path.join(category_dir, 'full')
            subcategory_full_dir = os.path.join(category_full_dir, subcategory)
            os.makedirs(subcategory_full_dir, exist_ok=True)
            # If wrapper_full.py exists, use it and rename to wrapper.py
            shutil.copy(wrapper_full_path, subcategory_full_dir)
            os.rename(os.path.join(subcategory_full_dir, "wrapper_full.py"), os.path.join(subcategory_full_dir, "wrapper.py"))
        if os.path.exists(wrapper_path):
            # If only wrapper.py exists, copy it
            category_lora_dir = os.path.join(category_dir, 'lora')
            subcategory_lora_dir = os.path.join(category_lora_dir, subcategory)
            os.makedirs(subcategory_lora_dir, exist_ok=True)
            shutil.copy(wrapper_path, subcategory_lora_dir)

            category_qlora_dir = os.path.join(category_dir, 'qlora')
            subcategory_qlora_dir = os.path.join(category_qlora_dir, subcategory)
            os.makedirs(subcategory_qlora_dir, exist_ok=True)

            shutil.copy(wrapper_path, subcategory_qlora_dir)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="An example script with command-line arguments.")
    parser.add_argument("--workdir", type=str, default=None)
    args = parser.parse_args()

    if not args.workdir:
        raise SystemExit(f"workdir cannot None")

    if not os.path.exists(args.workdir):
        # 如果目录不存在，则创建目录
        os.makedirs(args.workdir)

    import json
    json_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(json_path,"config.json")
    with open(json_path, "r") as json_file:
        json_data = json.load(json_file)
        create_and_copy_directories(json_data, args.workdir)