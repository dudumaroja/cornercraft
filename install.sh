#!/bin/bash

APP_NAME="CornerCraft"
APP_ID="com.github.dudumaroja.cornercraft"

INSTALL_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"
ICON_DIR="$HOME/.local/share/icons/hicolor/512x512/apps"

mkdir -p "$INSTALL_DIR" "$DESKTOP_DIR" "$ICON_DIR"

# Copia o script principal
cp main.py "$INSTALL_DIR/cornercraft"
chmod +x "$INSTALL_DIR/cornercraft"

# Copia o ícone
cp icon.png "$ICON_DIR/$APP_ID.png"

# Cria o arquivo .desktop
cat > "$DESKTOP_DIR/$APP_ID.desktop" << EOF
[Desktop Entry]
Type=Application
Name=CornerCraft
Name[pt_BR]=CornerCraft
Name[pt]=CornerCraft
Name[en]=CornerCraft
Name[es]=CornerCraft
Comment=A tool to tweak window corner radius
Comment[pt_BR]=Ferramenta para ajustar o raio dos cantos das janelas
Comment[pt]=Ferramenta para ajustar o raio dos cantos das janelas
Comment[en]=Tool to adjust window corner radius
Comment[es]=Herramienta para ajustar el radio de las esquinas de las ventanas
Exec=$INSTALL_DIR/cornercraft
Icon=$APP_ID
Terminal=false
Categories=Utility;
EOF

# Atualiza caches
gtk-update-icon-cache -f "$HOME/.local/share/icons/hicolor" 2>/dev/null || true
update-desktop-database "$DESKTOP_DIR" 2>/dev/null || true

echo "CornerCraft installed."

