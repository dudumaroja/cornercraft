import Adw from 'gi://Adw';
import Gtk from 'gi://Gtk';
import {ExtensionPreferences, gettext as _} from 'resource:///org/gnome/Shell/Extensions/js/extensions/prefs.js';
import Gio from 'gi://Gio';
import GLib from 'gi://GLib';

const RADIUS_WINDOWS_KEY = 'windows-radius';
const RADIUS_SWITCH_KEY = 'switch-radius';  

export default class SquaredwaitaPreferences extends ExtensionPreferences {
  fillPreferencesWindow(window) {
    const preferences = this;
    preferences.settings = preferences.getSettings();

    const page = new Adw.PreferencesPage();
    const group = new Adw.PreferencesGroup({
      title: _('Corner Radius'),
    });
    page.add(group);

    // Windows radius (applies to *)
    const windowsRow = new Adw.ActionRow({
      title: _('Windows radius'),
    });
    group.add(windowsRow);
    const windowsEntry = new Gtk.SpinButton({
      adjustment: new Gtk.Adjustment({
        lower: 0,
        upper: 100,
        step_increment: 1,
      }),
      valign: Gtk.Align.CENTER,
    });
    windowsRow.add_suffix(windowsEntry);
    windowsRow.activatable_widget = windowsEntry;

    // Combined Radio/Switch/Slider radius (overrides *)
    const combinedRow = new Adw.ActionRow({
      title: _('Radio, Switch radius'),
    });
    group.add(combinedRow);
    const combinedEntry = new Gtk.SpinButton({
      adjustment: new Gtk.Adjustment({
        lower: 0,
        upper: 100,
        step_increment: 1,
      }),
      valign: Gtk.Align.CENTER,
    });
    combinedRow.add_suffix(combinedEntry);
    combinedRow.activatable_widget = combinedEntry;

    // Bind settings (using existing schema keys)
    preferences.settings.bind(RADIUS_WINDOWS_KEY, windowsEntry, 'value', Gio.SettingsBindFlags.DEFAULT);
    preferences.settings.bind(RADIUS_SWITCH_KEY, combinedEntry, 'value', Gio.SettingsBindFlags.DEFAULT);

    const actionsGroup = new Adw.PreferencesGroup({
      title: _('Actions'),
    });
    page.add(actionsGroup);

    const setButton = new Gtk.Button({
      label: _('Set'),
      valign: Gtk.Align.CENTER,
    });
    setButton.connect('clicked', () => {
      preferences.updateCss(false);
    });
    actionsGroup.add(setButton);

    const restoreButton = new Gtk.Button({
      label: _('Restore Defaults'),
      valign: Gtk.Align.CENTER,
    });
    restoreButton.connect('clicked', () => {
      preferences.restoreDefaults();
    });
    actionsGroup.add(restoreButton);

    const defaultsNoteRow = new Adw.ActionRow({
      title: _('Adwaita Default Values'),
      subtitle: _('Windows: 12px, Radio/Switch/Slider: 12px'),
    });
    actionsGroup.add(defaultsNoteRow);

    window.add(page);
  }

  restoreDefaults() {
    this.settings.reset(RADIUS_WINDOWS_KEY);
    this.settings.reset(RADIUS_SWITCH_KEY);
    this.updateCss(true);
  }

  updateCss(restore) {
    let css = '';
    if (!restore) {
      css = `
/* windows corners set by squaredwaita START*/
* {
  border-radius: ${this.settings.get_int(RADIUS_WINDOWS_KEY)}px;
}

radio, .radio, switch, switch slider {
  border-radius: ${this.settings.get_int(RADIUS_SWITCH_KEY)}px;
}
/* windows corners set by squaredwaita END */
`;
    }

    const home = GLib.get_home_dir();
    const gtk3Path = `${home}/.config/gtk-3.0/gtk.css`;
    const gtk4Path = `${home}/.config/gtk-4.0/gtk.css`;

    const updateFile = (path) => {
      let content = '';
      if (GLib.file_test(path, GLib.FileTest.EXISTS)) {
        content = GLib.file_get_contents(path)[1].toString();
        // Remove old CSS
        content = content.replace(/\/\* windows corners set by squaredwaita START\*\/[\s\S]*?\/\* windows corners set by squaredwaita END \*\//, '');
      }
      // Add new CSS
      GLib.file_set_contents(path, content + css);
    };

    try {
      updateFile(gtk3Path);
      updateFile(gtk4Path);
    } catch (e) {
      // silent error
    }
  }
}

