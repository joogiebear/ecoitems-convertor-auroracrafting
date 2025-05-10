# EcoItem Config Converter

A simple tool to convert your EcoItem `.yml` files to the new required format — no coding knowledge needed!

---

## 🚀 How to Convert Your EcoItem Config Files

Follow the steps below to convert your EcoItem files using the included Python script.

---

### 📁 Step 1: Prepare Your Files

1. Create a new folder on your desktop, e.g., `EcoItem_Conversion`.
2. Copy all your EcoItem `.yml` files into this folder.
3. Download the `convert.py` script and place it in the same folder.

Your folder should look like this:

```
EcoItem_Conversion/
├── convert.py
├── enchanted_emerald.yml
├── another_item.yml
└── other_files.yml
```

---

### 🐍 Step 2: Install Python

> **Skip this step if Python is already installed.**

1. Download Python (recommended: version 3.12) from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Run the installer and **check "Add Python to PATH"**.
3. Click **Install Now** and follow the prompts.

---

### 📦 Step 3: Install Required Packages

1. Open **Command Prompt** (`cmd`) from the Start Menu.
2. Run the following command:

```
pip install pyyaml
```

Wait until you see: `Successfully installed`.

---

### 🔄 Step 4: Run the Conversion

1. Navigate to your folder by running:

```
cd %userprofile%\Desktop\EcoItem_Conversion
```

> If the folder is named differently or located elsewhere, drag the folder into the Command Prompt window after typing `cd `.

2. Start the conversion:

```
python convert.py
```

You’ll see a message for each converted file.

If any files fail, you'll see:

```
Some files were skipped! Check 'skipped_files.txt'.
```

---

### ✅ Step 5: Check the Results

- A new folder named `converted` will appear in `EcoItem_Conversion/`.
- Open it to view your converted files.
- If there were any problems, open `skipped_files.txt` to see which files were skipped and why.

---

## 🎉 You're Done!

You've successfully converted your EcoItem files. If you run into trouble, double-check each step above or open an issue for support.

Happy converting!
