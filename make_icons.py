from PIL import Image, ImageOps
from pathlib import Path

root = Path("android/app/src/main/res")
logo = Image.open("logo.png").convert("RGBA")

sizes = {
    "mdpi": 48,
    "hdpi": 72,
    "xhdpi": 96,
    "xxhdpi": 144,
    "xxxhdpi": 192,
}

for density, size in sizes.items():
    folder = root / f"mipmap-{density}"
    folder.mkdir(parents=True, exist_ok=True)

    icon = ImageOps.fit(
        logo, (size, size),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5)
    )

    icon.save(folder / "ic_launcher.png")
    icon.save(folder / "ic_launcher_round.png")

    foreground = ImageOps.contain(
        logo, (int(size * 0.68), int(size * 0.68)),
        method=Image.Resampling.LANCZOS
    )
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    canvas.alpha_composite(
        foreground,
        ((size - foreground.width) // 2,
         (size - foreground.height) // 2)
    )
    canvas.save(folder / "ic_launcher_foreground.png")

print("YouKi Shorts icons generated successfully!")
