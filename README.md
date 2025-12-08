# CornerCraft: Live Corner Radius Customization

[![License](https://img.shields.io/badge/License-GPL%20v2%2B-orange.svg)](https://www.gnu.org/licenses/gpl-2.0.html)
[![Kofi](https://img.shields.io/badge/Kofi-tips-green.svg)](https://ko-fi.com/dudumaroja)

## Description

Are you a fan of Adwaita, but wish you had a say in its curves? Do you yearn for an interface that's just a little bit more, or a little bit less, rounded? CornerCraft is here to give you that control! This simple yet powerful application empowers you to precisely adjust the corner radii (border-radius) of your GTK 3 and GTK 4 applications and UI elements. From sharper, more squared edges to a delightfully smooth, round aesthetic, CornerCraft puts the customization in your hands. It works its magic by injecting custom CSS directly into your `~/.config/gtk-3.0/gtk.css` and `~/.config/gtk-4.0/gtk.css` files, giving you a desktop that truly reflects your style.

## Features

*   **Granular Control:** Independently set radii for:
    *   **Windows & General Elements:** Applies to most application windows and UI components.
    *   **Radio Buttons, Switches & Sliders:** Specific control for these interactive elements.
    *   **Buttons:** Tailor the curvature of all your buttons.
    *   **Text Inputs:** Define the roundness of entry fields and text views.
    *   **Menus & Popovers:** Customize the corners of context menus and pop-up windows.
*   **Unified Control (Lock Option):** Effortlessly synchronize all corner radius values with a single toggle. Adjust one, and the rest follow suit, or unlock them for individual fine-tuning.
*   **Compatibility:** Works seamlessly with Adwaita and other GTK themes.
*   **Restore Defaults:** Instantly revert to Adwaita's default corner settings (12px) and clear any custom CSS.
*   **Internationalization:** Available in multiple languages to suit your preference.

## Installation

(Installation instructions will go here, referencing the `install.sh` script)

## Usage

After installation:

1.  **Corner Radius Section:**
    *   Use the individual sliders (0-100 pixels) to set the desired `border-radius` for each element type.
    *   Toggle the "Lock all values" switch to synchronize all sliders to the "Windows radius" value.
2.  **Actions Section:**
    *   **Set:** Click this button to apply your chosen corner radii to your system's `gtk.css` files.
    *   **Restore Defaults:** Click this button to revert all corner radii settings to Adwaita's default values (12px).
    *   **Adwaita Default Values:** Provides a quick reference for the default radii.

## Development

CornerCraft is open-source and contributions are welcome.

*   **Issues & Suggestions:** Feel free to open an issue on the [GitHub repository](https://github.com/dudumaroja/cornercraft/issues) for bugs, feature requests, or general feedback.
*   **Cloning & Modification:** The code is available for you to clone and modify at will.

## License

CornerCraft is released under the [GNU GPL v2.0 or later license](LICENSE).

## Credits

Developed by [@dudumaroja](https://github.com/dudumaroja).
