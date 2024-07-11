#!/usr/bin/env bash
source ".env"

pnpm run build --base /slides/vortraege/ep2024-python-unplugged/
pnpm run export

# REMOTE="$ZOLA_USER@$ZOLA_DOMAIN:$ZOLA_REMOTE_FOLDER/slides/vortraege/ep2024-python-unplugged"
# scp -i "$ZOLA_KEY" -r dist/* "$REMOTE"

LOCAL="$HOME/project/lokidev-blog/static/slides/vortraege/ep2024-python-unplugged"
rm -rf "$LOCAL-bak" 2>/dev/null
mv "$LOCAL" "$LOCAL-bak"
cp -r dist "$LOCAL"

mv slides-export.pdf "$LOCAL/europython2024-python-unplugged-slides.pdf"
