# NFT Layers Guide

This directory contains the layer assets used to generate the NFT collection. Each subdirectory represents a different layer type that will be composited to create the final NFT images.

## Directory Structure

```
layers/
├── base/          # Base helmet designs (required)
├── visor/         # Visor styles (required)
├── accent/        # Accent details (optional)
├── background/    # Background colors/patterns (required)
└── effects/       # Special effects overlays (optional)
```

## Creating Custom Artwork

### Image Specifications

- **Format:** PNG with transparency (RGBA)
- **Dimensions:** 1000x1000 pixels (recommended)
- **Color Mode:** RGBA (8-bit per channel)
- **File naming:** Must match the trait names in `config.json` exactly

### Layer Guidelines

#### 1. Background Layer
- Should fill the entire canvas (1000x1000)
- No transparency required
- Examples: "Space Blue.png", "Cosmic Purple.png"

#### 2. Base Helmet Layer
- Main helmet design
- Should have transparent background
- Center the helmet in the canvas
- Recommended size: 500-700 pixels wide
- Examples: "Standard Helmet.png", "Elite Helmet.png"

#### 3. Visor Layer
- Overlay on the helmet
- Must have transparency
- Should align with helmet base
- Can have semi-transparent effects
- Examples: "Clear Visor.png", "Holographic.png"

#### 4. Accent Layer (Optional)
- Small details and decorations
- Must have transparency
- Examples: "Alliance Insignia.png", "Battle Scars.png"
- "None.png" should be a fully transparent image

#### 5. Effects Layer (Optional)
- Special effects and glows
- Should be semi-transparent
- Examples: "Particle Glow.png", "Energy Aura.png"
- "None.png" should be a fully transparent image

## Workflow

1. **Create your artwork** following the specifications above
2. **Save each variant** with the exact name from `config.json`
3. **Place files** in the appropriate layer directory
4. **Run the generator**: `python generate_nfts.py`

The generator will automatically use your custom artwork. If a trait image is missing, it will create a procedural placeholder.

## Tips for Best Results

### Color Palette
Use colors inspired by the Alliance Forge universe:
- Metallic grays and silvers for helmets
- Vibrant blues, purples, and reds for effects
- Dark space colors for backgrounds

### Consistency
- Keep lighting direction consistent across all helmet bases
- Maintain similar line weights and styles
- Use the same resolution for all layers

### Testing
- Generate a small batch first (modify `collection_size` in config.json)
- Check how layers composite together
- Adjust artwork as needed

### Layer Order
Layers are composited in this order (bottom to top):
1. Background
2. Base (helmet)
3. Visor
4. Accent
5. Effects

Design your layers knowing what will be underneath and what will be on top.

## Example Trait Names

From `config.json`:

**Base:**
- Standard Helmet.png
- Heavy Helmet.png
- Elite Helmet.png
- Legendary Helmet.png
- Mythic Helmet.png

**Visor:**
- Clear Visor.png
- Blue Tint.png
- Red Tint.png
- Gold Tint.png
- Holographic.png
- Void Visor.png

**Accent:**
- None.png (fully transparent)
- Battle Scars.png
- Alliance Insignia.png
- Energy Lines.png
- Command Stripes.png
- Forge Emblem.png

**Background:**
- Space Blue.png
- Cosmic Purple.png
- Nebula Red.png
- Solar Yellow.png
- Deep Black.png

**Effects:**
- None.png (fully transparent)
- Particle Glow.png
- Energy Aura.png
- Tactical HUD.png
- Plasma Field.png
- Quantum Distortion.png

## Current Status

The generator currently uses **procedural placeholders** when actual image files are not found. These placeholders demonstrate the layering system and provide a starting point for your custom artwork.

To see the full potential of the system, create custom artwork following the guidelines above!
