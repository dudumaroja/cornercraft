#!/bin/bash

APP_ID="com.github.dudumaroja.cornercraft"

INSTALL_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"
ICON_BASE="$HOME/.local/share/icons/hicolor"

rm -f "$INSTALL_DIR/cornercraft"
rm -f "$DESKTOP_DIR/$APP_ID.desktop"
rm -f "$ICON_BASE"/512x512/apps/"$APP_ID".png

gtk-update-icon-cache -f "$ICON_BASE" 2>/dev/null || true
update-desktop-database "$DESKTOP_DIR" 2>/dev/null || true

echo "CornerCraft removed."
