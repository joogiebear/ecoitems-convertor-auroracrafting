import os
import yaml
from textwrap import dedent

def convert_file(input_file, skipped_files):
    with open(input_file, 'r') as file:
        old_config = yaml.safe_load(file)

    if not isinstance(old_config, dict) or 'item' not in old_config:
        print(f"⚠️ Skipped {input_file}: No 'item' field found.")
        skipped_files.append(os.path.basename(input_file))
        return

    file_id = os.path.splitext(os.path.basename(input_file))[0]

    ingredients = []
    for ingredient in old_config['item'].get('recipe', []):
        ingredient = ingredient.strip()
        if ingredient == "":
            ingredients.append('          - ""')
        else:
            parts = ingredient.split()
            item_name, amount = (parts[0], parts[1]) if len(parts) == 2 else (parts[0], "1")
            ingredients.append(f'          - "minecraft:{item_name}/{amount}"')

    permission = old_config['item'].get('craftingPermission', f"craft.{file_id}")

    # Dynamically include permission in locked-lore
    ingredients_str = "\n".join(ingredients)

    yaml_template = dedent(f"""\
    recipes:
      - id: {file_id}
        shapeless: false
        workbench: default
        permission: "{permission}"
        result: "eco:ecoitems:{file_id}/1"
        symmetry: true
        ingredients:
{ingredients_str}
        vanilla-options:
          category: "equipment"
          group: "vanilla grouping stuff"
          choice-type: "item_type"
        display-options:
          locked-lore:
            - "&7You need {permission} &7to unlock this recipe."
        merge-options:
          2:
            enchants: true
            trim: true
    """)

    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "converted")
    os.makedirs(output_dir, exist_ok=True)

    output_file_path = os.path.join(output_dir, f"{file_id}.yml")
    with open(output_file_path, 'w') as file:
        file.write(yaml_template)

    print(f"✅ Converted: {os.path.basename(input_file)}")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    skipped_files = []
    for filename in os.listdir(current_dir):
        if filename.endswith((".yml", ".yaml")) and filename != os.path.basename(__file__):
            convert_file(os.path.join(current_dir, filename), skipped_files)

    if skipped_files:
        with open('skipped_files.txt', 'w') as f:
            f.write("\n".join(skipped_files))
        print("⚠️ Some files were skipped! Check 'skipped_files.txt'.")

    print("🎉 Conversion complete! Check the 'converted' folder.")

if __name__ == "__main__":
    main()
