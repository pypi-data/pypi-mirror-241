if __name__ == '__main__':
    from tkadw import *
    root = Adwite("win11", windark=False)
    root.set_default_theme("win11", "system")
    root.geometry("200x110")

    root.title("adw")

    version = AdwTLabel(root, text=f"tkadw`s version is {get_version()}")
    version.pack(anchor="center", padx=5, pady=5)

    button = AdwTButton(root, text="Quit", command=lambda: root.quit(), height=23)
    button.pack(anchor="center", padx=5, pady=5)

    light = AdwTButton(root, text="Light", command=lambda: root.dark(False), height=23)
    light.pack(anchor="center", padx=5, pady=5)

    dark = AdwTButton(root, text="Dark", command=lambda: root.dark(True), height=23)
    dark.pack(anchor="center", padx=5, pady=5)

    dark_icon = AdwTButton(root, text="Dark Icon", command=lambda: root.icon_dark(True), height=23)
    dark_icon.pack(anchor="center", padx=5, pady=5)

    root.run()