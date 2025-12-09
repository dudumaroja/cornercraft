#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importa as bibliotecas necessárias.
# O gi (GObject Introspection) é usado para criar bindings para bibliotecas baseadas em GObject, como GTK e Adwaita.
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib
import os
import gettext

# Configura o gettext para tradução.
APPNAME = "cornercraft"
LOCALE_DIR = os.path.join(os.environ["HOME"], ".local/share/locale")
gettext.bindtextdomain(APPNAME, LOCALE_DIR)
gettext.textdomain(APPNAME)
_ = gettext.gettext

# Define a classe principal da aplicação, que herda de Adw.Application.
# O Adw.Application é uma classe especial que lida com o ciclo de vida da aplicação.
class CornerCraftApp(Adw.Application):
    def __init__(self, **kwargs):
        # O super().__init__() chama o construtor da classe pai (Adw.Application).
        super().__init__(**kwargs)
        # Conecta o sinal 'activate' a um método (on_activate).
        # O sinal 'activate' é emitido quando a aplicação é iniciada.
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        # Este método é chamado quando a aplicação é ativada.
        # Cria uma instância da nossa janela principal (MainWindow).
        self.win = MainWindow(application=app)
        # Apresenta a janela ao usuário.
        self.win.present()

# Define a classe da janela principal, que herda de Gtk.ApplicationWindow.
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define o ícone da janela
        self.set_icon_name("cornercraft")

        # Define o tamanho padrão e o título da janela.
        self.set_default_size(400, 500)
        self.set_title(_("CornerCraft"))

        # Cria uma caixa vertical (Gtk.Box) para organizar os widgets.
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        # Adiciona a caixa como o widget filho da janela.
        self.set_child(self.box)

        # Cria um Adw.HeaderBar, que é a barra de título da janela.
        self.header = Adw.HeaderBar()
        self.set_titlebar(self.header)

        # Cria uma Adw.PreferencesPage, que é uma página de preferências padrão do Adwaita.
        self.page = Adw.PreferencesPage()
        self.box.append(self.page)

        # Cria um grupo de preferências (Adw.PreferencesGroup) para os raios dos cantos.
        self.group = Adw.PreferencesGroup(title=_("Corner Radius"))
        self.page.add(self.group)

        # Lock switch
        self.lock_row = Adw.ActionRow(title=_("Lock all values"))
        self.group.add(self.lock_row)
        self.lock_switch = Gtk.Switch()
        self.lock_switch.set_active(False)
        self.lock_switch.connect("notify::active", self.on_lock_switch_toggled)
        self.lock_row.add_suffix(self.lock_switch)
        self.lock_row.set_activatable_widget(self.lock_switch)

        # Raio das janelas
        self.windows_row = Adw.ActionRow(title=_("Windows radius"))
        self.group.add(self.windows_row)
        self.windows_spin = Gtk.SpinButton.new_with_range(0, 100, 1)
        self.windows_spin.set_value(12)
        self.windows_spin.connect("value-changed", self.on_windows_spin_changed)
        self.windows_row.add_suffix(self.windows_spin)
        self.windows_row.set_activatable_widget(self.windows_spin)
        
        # Raio de Radio, Switch
        self.radio_switch_row = Adw.ActionRow(title=_("Radio, Switch radius"))
        self.group.add(self.radio_switch_row)
        self.radio_switch_spin = Gtk.SpinButton.new_with_range(0, 100, 1)
        self.radio_switch_spin.set_value(12)
        self.radio_switch_row.add_suffix(self.radio_switch_spin)
        self.radio_switch_row.set_activatable_widget(self.radio_switch_spin)

        # Raio dos Botões
        self.buttons_row = Adw.ActionRow(title=_("Buttons radius"))
        self.group.add(self.buttons_row)
        self.buttons_spin = Gtk.SpinButton.new_with_range(0, 100, 1)
        self.buttons_spin.set_value(12)
        self.buttons_row.add_suffix(self.buttons_spin)
        self.buttons_row.set_activatable_widget(self.buttons_spin)

        # Raio das Entradas de Texto
        self.text_inputs_row = Adw.ActionRow(title=_("Text Inputs radius"))
        self.group.add(self.text_inputs_row)
        self.text_inputs_spin = Gtk.SpinButton.new_with_range(0, 100, 1)
        self.text_inputs_spin.set_value(12)
        self.text_inputs_row.add_suffix(self.text_inputs_spin)
        self.text_inputs_row.set_activatable_widget(self.text_inputs_spin)

        # Raio de Menus e Popovers
        self.menus_popovers_row = Adw.ActionRow(title=_("Menus and Popovers radius"))
        self.group.add(self.menus_popovers_row)
        self.menus_popovers_spin = Gtk.SpinButton.new_with_range(0, 100, 1)
        self.menus_popovers_spin.set_value(12)
        self.menus_popovers_row.add_suffix(self.menus_popovers_spin)
        self.menus_popovers_row.set_activatable_widget(self.menus_popovers_spin)

        # Caixa de botões
        self.button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=12, margin_bottom=12, margin_start=12, margin_end=12)
        self.box.append(self.button_box)
        
        # Botão "Set" (Aplicar)
        self.set_button = Gtk.Button(label=_("Set"))
        self.set_button.connect("clicked", self.on_set_clicked)
        self.button_box.append(self.set_button)
        
        # Botão "Restore Defaults" (Restaurar Padrões)
        self.restore_button = Gtk.Button(label=_("Restore Defaults"))
        self.restore_button.connect("clicked", self.on_restore_clicked)
        self.button_box.append(self.restore_button)

        self.on_lock_switch_toggled(self.lock_switch)

    def on_lock_switch_toggled(self, switch, *args):
        is_active = switch.get_active()
        self.radio_switch_spin.set_sensitive(not is_active)
        self.buttons_spin.set_sensitive(not is_active)
        self.text_inputs_spin.set_sensitive(not is_active)
        self.menus_popovers_spin.set_sensitive(not is_active)
        
        if is_active:
            self.sync_values()

    def on_windows_spin_changed(self, spin_button):
        if self.lock_switch.get_active():
            self.sync_values()
            
    def sync_values(self):
        value = self.windows_spin.get_value()
        self.radio_switch_spin.set_value(value)
        self.buttons_spin.set_value(value)
        self.text_inputs_spin.set_value(value)
        self.menus_popovers_spin.set_value(value)

    # Método chamado quando o botão "Set" é clicado.
    def on_set_clicked(self, widget):
        self.apply_css()

    # Método chamado quando o botão "Restore Defaults" é clicado.
    def on_restore_clicked(self, widget):
        # Restaura os valores padrão dos SpinButtons.
        self.windows_spin.set_value(12)
        self.radio_switch_spin.set_value(12)
        self.buttons_spin.set_value(12)
        self.text_inputs_spin.set_value(12)
        self.menus_popovers_spin.set_value(12)
        self.lock_switch.set_active(False)
        # Aplica o CSS vazio para remover as personalizações.
        self.apply_css(restore=True)

    # Método que aplica o CSS.
    def apply_css(self, restore=False):
        # Obtém o diretório home do usuário.
        home = os.path.expanduser("~")
        # Define os caminhos para os arquivos gtk.css do GTK3 e GTK4.
        gtk3_css_path = os.path.join(home, ".config/gtk-3.0/gtk.css")
        gtk4_css_path = os.path.join(home, ".config/gtk-4.0/gtk.css")

        # Obtém os valores dos SpinButtons.
        windows_radius = self.windows_spin.get_value_as_int()
        radio_switch_radius = self.radio_switch_spin.get_value_as_int()
        buttons_radius = self.buttons_spin.get_value_as_int()
        text_inputs_radius = self.text_inputs_spin.get_value_as_int()
        menus_popovers_radius = self.menus_popovers_spin.get_value_as_int()

        # Cria o conteúdo do CSS.
        css = f"""
/* CornerCraft start*/
* {{
    border-radius: {windows_radius}px;
}}

radio, switch, slider {{
    border-radius: {radio_switch_radius}px;
}}

button {{
    border-radius: {buttons_radius}px;
}}

entry, textview {{
    border-radius: {text_inputs_radius}px;
}}

menu, popover {{
    border-radius: {menus_popovers_radius}px;
}}
/* CornerCraft end*/
"""
        # Se restore for True, o CSS é definido como uma string vazia.
        if restore:
            css = ""
            
        # Cria os diretórios de configuração se eles não existirem.
        os.makedirs(os.path.dirname(gtk3_css_path), exist_ok=True)
        os.makedirs(os.path.dirname(gtk4_css_path), exist_ok=True)
        
        # Escreve o CSS no arquivo gtk.css do GTK3.
        with open(gtk3_css_path, "w") as f:
            f.write(css)
            
        # Escreve o CSS no arquivo gtk.css do GTK4.
        with open(gtk4_css_path, "w") as f:
            f.write(css)


# Ponto de entrada da aplicação.
if __name__ == "__main__":
    # Cria uma instância da nossa aplicação.
    app = CornerCraftApp(application_id="com.github.dudumaroja.cornercraft")
    # Executa a aplicação.
    app.run([])
