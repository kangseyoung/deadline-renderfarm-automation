import os

def create_user_setup():
    user_setup_dir = os.path.expanduser("~/Documents/maya/2023/scripts")
    os.makedirs(user_setup_dir, exist_ok=True)
    user_setup_path = os.path.join(user_setup_dir, "userSetup.py")

    line = "import ui.menu\nui.menu.create_menu()"

    if os.path.exists(user_setup_path):
        with open(user_setup_path, "r") as f:
            content = f.read()
        if line in content:
            print("ReplaceA userSetup.py already contains menu setup.")
            return

    with open(user_setup_path, "a") as f:
        f.write(f"\n{line}\n")
        print(f"ReplaceA userSetup.py updated with: {line}")
