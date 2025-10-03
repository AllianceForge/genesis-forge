import os
from PIL import Image
import json

WIDTH, HEIGHT = 1000, 1000
OUTPUT_DIR = "./output"
IMG_DIR = os.path.join(OUTPUT_DIR, "images")
META_DIR = os.path.join(OUTPUT_DIR, "metadata")
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)

COLORS = [
    ("silver", "Silver"),
    ("green", "Bright Green"),
    ("cyan", "Cyan"),
    ("purple", "Radiant Purple"),
    ("coral", "Vibrant Coral"),
    ("red", "Fiery Red"),
    ("gold", "Bright Gold")
]

for idx, (color, color_name) in enumerate(COLORS, 1):
    base = Image.new("RGBA", (WIDTH, HEIGHT), (0,0,0,0))
    attributes = []

    # 1. Background
    bg = Image.open(f"./layers/Background/bg_{color}.png").convert("RGBA")
    base.alpha_composite(bg)
    attributes.append({"trait_type": "Background", "value": color_name})

    # 2. Helmet base (siempre igual)
    helmet = Image.open(f"./layers/Helmet/helmet_base.png").convert("RGBA")
    base.alpha_composite(helmet)
    attributes.append({"trait_type": "Helmet", "value": "Base"})

    # 3. Visor (cambia de color)
    visor = Image.open(f"./layers/Visor/visor_{color}.png").convert("RGBA")
    base.alpha_composite(visor)
    attributes.append({"trait_type": "Visor", "value": color_name})

    # 4. Logo (cambia de color)
    logo = Image.open(f"./layers/Logo/logo_{color}.png").convert("RGBA")
    base.alpha_composite(logo)
    attributes.append({"trait_type": "Logo AF", "value": color_name})

    # 5. (Opcional: puedes agregar Attachment, Condition, Aura si quieres)

    # Guarda imagen y metadata
    out_path = os.path.join(IMG_DIR, f"{idx}.png")
    base.save(out_path)
    metadata = {
        "name": f"Genesis Forger #{idx}",
        "description": f"Alliance Forge Commander Helmet NFT | {color_name} Tier",
        "image": f"ipfs://<your_hash>/{idx}.png",
        "attributes": attributes
    }
    with open(os.path.join(META_DIR, f"{idx}.json"), "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"Generated NFT #{idx} - {color_name}")

print(f"\n✅ Listo: ¡7 NFTs generados en {IMG_DIR}!")
                json.dump(metadata, f, indent=2)
            serial += 1

if __name__ == "__main__":
    main()
