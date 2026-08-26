"""Patch gh-space-shooter's color theme to pink after pip install."""
import gh_space_shooter.game.render_context as rc
import inspect
import os

path = inspect.getfile(rc)

original = '''    @staticmethod
    def darkmode() -> "RenderContext":
        """Predefined dark mode rendering context."""
        return RenderContext(
            cell_size=12,
            cell_spacing=3,
            padding=40,
            background_color=(13, 17, 23),
            grid_color=(22, 27, 34),
            enemy_colors={1: (0, 109, 50), 2: (38, 166, 65), 3: (57, 211, 83), 4: (87, 242, 135)},
            ship_color=(68, 147, 248),
            bullet_color=(255, 223, 0),
        )
'''

patched = '''    @staticmethod
    def darkmode() -> "RenderContext":
        """Predefined pink theme rendering context."""
        return RenderContext(
            cell_size=12,
            cell_spacing=3,
            padding=40,
            background_color=(24, 12, 26),
            grid_color=(41, 20, 43),
            enemy_colors={1: (128, 22, 84), 2: (191, 46, 122), 3: (236, 72, 153), 4: (249, 168, 212)},
            ship_color=(232, 121, 249),
            bullet_color=(255, 240, 130),
        )
'''

with open(path, "r") as f:
    content = f.read()

if original not in content:
    raise SystemExit(
        "gh-space-shooter source has changed upstream; patch markers not found in "
        f"{path}. Update patch_pink.py to match the new render_context.py."
    )

content = content.replace(original, patched)

with open(path, "w") as f:
    f.write(content)

print(f"Patched {path} with pink theme.")
