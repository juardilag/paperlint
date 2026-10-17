#!/usr/bin/env bash
# Sync the paper with its Overleaf project (git clone in ./overleaf).
#   ./sync_overleaf.sh pull            Overleaf -> local  (run before working)
#   ./sync_overleaf.sh push [message]  local -> Overleaf  (run when done)
#   ./sync_overleaf.sh auto            push only if something local changed (Stop hook)
set -euo pipefail
cd "$(dirname "$0")"
# Edit these three lines for your paper.
P=paper                      # folder with the main .tex and .bib
TEX="main.tex refs.bib"      # files synced both ways
FIGS=""                      # figure files pushed to overleaf/figures/, e.g. "figs/fig1.pdf figs/fig2.pdf"
O=overleaf; STAMP=$O/.git/last_sync
[ -d "$O/.git" ] || { echo "clone the Overleaf project into $O first"; exit 1; }
stamp() { (cd "$O" && sha1sum $TEX 2>/dev/null) > "$STAMP"; }
case "${1:-}" in
  pull)
    git -C "$O" pull --no-rebase
    # local edits since the last sync are never overwritten
    if [ -f "$STAMP" ] && ! (cd "$P" && sha1sum -c --quiet "$OLDPWD/$STAMP" >/dev/null 2>&1); then
      if (cd "$O" && sha1sum -c --quiet "$OLDPWD/$STAMP" >/dev/null 2>&1); then
        echo "Overleaf unchanged; local edits not pushed yet, nothing pulled"; exit 0
      fi
      echo "both local and Overleaf changed: merge $O/ into $P/ by hand"; exit 1
    fi
    for f in $TEX; do [ -f "$O/$f" ] && cp "$O/$f" "$P/"; done
    stamp
    echo "pulled; run /paperlint:learn if your co-authors edited the text" ;;
  push)
    git -C "$O" pull --no-rebase
    # hash check, not a 3-way merge: pull and merge by hand if it trips
    if [ -f "$STAMP" ] && ! (cd "$O" && sha1sum -c --quiet "$OLDPWD/$STAMP" >/dev/null 2>&1); then
      echo "Overleaf changed since your last pull: run './sync_overleaf.sh pull' first"; exit 1
    fi
    for f in $TEX; do cp "$P/$f" "$O/"; done
    if [ -n "$FIGS" ]; then mkdir -p "$O/figures"; cp $FIGS "$O/figures/"; fi
    git -C "$O" add -A
    git -C "$O" commit -qm "${2:-sync from local}" || { echo "nothing to push"; exit 0; }
    git -C "$O" push
    stamp ;;
  auto)
    changed=0
    for f in $TEX; do cmp -s "$P/$f" "$O/$f" || changed=1; done
    for f in $FIGS; do cmp -s "$f" "$O/figures/$(basename "$f")" || changed=1; done
    [ "$changed" = 1 ] || exit 0
    GIT_TERMINAL_PROMPT=0 exec bash "$0" push "auto-sync from local ($(date +%F\ %H:%M))" ;;
  *) echo "usage: $0 pull|push [message]|auto"; exit 1 ;;
esac
