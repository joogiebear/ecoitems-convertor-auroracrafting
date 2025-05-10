import os
import yaml

def convert_files(input_files, output_file):
    all_recipes = []
    skipped_files = []
    
    for input_file in input_files:
        print(f"🔍 Processing {input_file}...")
        with open(input_file, 'r') as file:
            try:
                old_config = yaml.safe_load(file)
                print(f"✅ Loaded YAML: {old_config}")
            except yaml.YAMLError as e:
                print(f"❌ Error parsing {input_file}: {e}")
                skipped_files.append(os.path.basename(input_file))
                continue

        if not isinstance(old_config, dict) or 'item' not in old_config:
            print(f"⚠️ Skipped {input_file}: No 'item' field found.")
            skipped_files.append(os.path.basename(input_file))
            continue

        file_id = os.path.splitext(os.path.basename(input_file))[0]

        ingredients = []
        for ingredient in old_config['item'].get('recipe', []):
            ingredient = ingredient.strip()
            if ingredient == "":
                ingredients.append('        - ""')
            else:
                parts = ingredient.split()
                item_name, amount = (parts[0], parts[1]) if len(parts) == 2 else (parts[0], "1")
                
                # Check if the ingredient belongs to ecoitems or minecraft
                if item_name.startswith("ecoitems:"):
                    formatted_item = f'        - "eco:{item_name}/{amount}"'
                else:
                    formatted_item = f'        - "minecraft:{item_name}/{amount}"'
                
                ingredients.append(formatted_item)

        permission = old_config['item'].get('craftingPermission', f"craft.{file_id}")

        # Build recipe structure
        recipe_yaml = (
            f"  - id: {file_id}\n"
            f"    shapeless: false\n"
            f"    workbench: default\n"
            f"    permission: \"{permission}\"\n"
            f"    result: \"eco:ecoitems:{file_id}/1\"\n"
            f"    symmetry: true\n"
            f"    ingredients:\n"
            + "\n".join(ingredients) + "\n"
            f"    display-options:\n"
            f"      locked-lore:\n"
            f"        - \"&7You need {permission} &7to unlock this recipe.\"\n"
            f"    merge-options:\n"
            f"      2:\n"
            f"        enchants: true\n"
            f"        trim: true\n"
        )
        
        all_recipes.append(recipe_yaml)
    
    if not all_recipes:
        print("⚠️ No valid recipes found. Check input files.")
        return

    # Combine all recipes into a single YAML structure
    combined_yaml = "recipes:\n" + "\n".join(all_recipes)
    
    with open(output_file, 'w') as file:
        file.write(combined_yaml)
    
    print(f"✅ All recipes combined into: {output_file}")
    
    if skipped_files:
        with open('skipped_files.txt', 'w') as f:
            f.write("\n".join(skipped_files))
        print("⚠️ Some files were skipped! Check 'skipped_files.txt'.")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_files = [os.path.join(current_dir, f) for f in os.listdir(current_dir) if f.endswith(('.yml', '.yaml')) and f != os.path.basename(__file__)]
    output_file = os.path.join(current_dir, "combined_recipes.yml")
    
    if not input_files:
        print("⚠️ No YAML files found to process.")
        return
    
    convert_files(input_files, output_file)
    print("🎉 Conversion complete! Check 'combined_recipes.yml'.")

if __name__ == "__main__":
    main()
