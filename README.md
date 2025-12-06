# CornerCraft GNOME Shell Extension: Live Corner Radius Customization

[![GNOME Version](https://img.shields.io/badge/GNOME-45%2B-blue.svg)](https://extensions.gnome.org/extension/8748/cornercraft/)
[![License](https://img.shields.io/badge/License-GPL%20v2%2B-orange.svg)](https://www.gnu.org/licenses/gpl-2.0.html)
[![GNOME Extensions](https://img.shields.io/badge/GNOME-Extensions-red.svg)](https://extensions.gnome.org/extension/8748/cornercraft/)
[![Kofi](https://img.shields.io/badge/Kofi-tips-green.svg)](https://ko-fi.com/dudumaroja)

## Description

CornerCraft is a simple yet powerful GNOME Shell extension that allows you to live-adjust the corner radii (border-radius) of your GTK 3 and GTK 4 applications and UI elements. Whether you prefer sharper, more squared corners or a softer, rounder aesthetic, CornerCraft provides granular control to customize the look and feel of your desktop. This extension directly modifies your theme's appearance by injecting CSS into your `~/.config/gtk-3.0/gtk.css` and `~/.config/gtk-4.0/gtk.css` files.

## Features

*   **Live Customization:** Adjust corner radii instantly without restarting GNOME Shell.
*   **Granular Control:** Independently set radii for:
    *   **Windows & General Elements:** Applies to most application windows and UI components.
    *   **Radio Buttons, Switches & Sliders:** Specific control for these interactive elements.
*   **Compatibility:** Works with Adwaita and other GTK themes by directly modifying CSS.
*   **Restore Defaults:** Easily revert to Adwaita's default corner settings (12px).

## Installation

### Via extensions.gnome.org (Recommended)

The easiest way to install CornerCraft is directly from the official GNOME Extensions website:

1.  Visit the [CornerCraft extension page](https://extensions.gnome.org/extension/8748/cornercraft/).
2.  Toggle the switch to "ON" to install and enable the extension.
3.  Open the GNOME Extensions application (or `gnome-extensions-app`) to access its preferences.

### Manual Installation

If you prefer to install manually or for development purposes:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dudumaroja/cornercraft.git ~/.local/share/gnome-shell/extensions/cornercraft@dudumaroja
    ```
    This command directly clones the repository into your GNOME Shell extensions directory.

2.  **Compile GSettings schemas:**
    ```bash
    glib-compile-schemas ~/.local/share/gnome-shell/extensions/cornercraft@dudumaroja/schemas/
    ```
    This step is crucial for the extension's settings to be recognized by GNOME.

3.  **Restart GNOME Shell:**
    *   **X11:** Press `Alt` + `F2`, type `r` (or `restart`), and press `Enter`.
    *   **Wayland:** You will need to log out and log back in.

4.  **Enable the extension:**
    ```bash
    gnome-extensions enable cornercraft@dudumaroja
    ```

## Usage

After installation, open the CornerCraft preferences through the GNOME Extensions application:

1.  **Corner Radius Section:**
    *   **Windows radius:** Use the slider to set the desired `border-radius` in pixels (0-100) for general windows and most UI elements.
    *   **Radio, Switch radius:** Use the slider to set the `border-radius` in pixels (0-100) specifically for radio buttons, switches, and sliders.

2.  **Actions Section:**
    *   **Set:** Click this button to apply your chosen corner radii. The extension will inject the necessary CSS into `~/.config/gtk-3.0/gtk.css` and `~/.config/gtk-4.0/gtk.css`.
    *   **Restore Defaults:** Click this button to revert all corner radii settings to Adwaita's default values (12px for both). This will also remove the injected CSS from your GTK configuration files.
    *   **Adwaita Default Values:** Provides a quick reference for the default radii.

## Development

CornerCraft is open-source and contributions are welcome.

*   **Issues & Suggestions:** Feel free to open an issue on the [GitHub repository](https://github.com/dudumaroja/cornercraft/issues) for bugs, feature requests, or general feedback.
*   **Cloning & Modification:** The code is available for you to clone and modify at will.

## License

CornerCraft is released under the [GNU GPL v2.0 or later license](LICENSE).

## Credits

Developed by [@dudumaroja](https://github.com/dudumaroja).