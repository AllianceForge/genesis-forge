# Genesis Forge - Alliance Forge Commander Helmet NFT Collection

A foundational collection of 1,000+ unique, generative NFTs based on the iconic Alliance Forge Commander Helmet. Each NFT is created from generative art layers reflecting rarity, color, and visual attributes inspired by the tactical, futuristic Alliance Forge universe.

## 🎨 Collection Overview

This collection features procedurally generated Commander Helmets with the following attributes:

### Layers & Traits

1. **Background** (5 variants)
   - Space Blue (Common)
   - Cosmic Purple (Common)
   - Nebula Red (Uncommon)
   - Solar Yellow (Rare)
   - Deep Black (Epic)

2. **Base Helmet** (5 variants)
   - Standard Helmet (Common)
   - Heavy Helmet (Common)
   - Elite Helmet (Uncommon)
   - Legendary Helmet (Rare)
   - Mythic Helmet (Ultra Rare)

3. **Visor** (6 variants)
   - Clear Visor (Common)
   - Blue Tint (Common)
   - Red Tint (Uncommon)
   - Gold Tint (Rare)
   - Holographic (Epic)
   - Void Visor (Legendary)

4. **Accent** (6 variants, Optional)
   - None
   - Battle Scars
   - Alliance Insignia
   - Energy Lines
   - Command Stripes
   - Forge Emblem

5. **Effects** (6 variants, Optional)
   - None
   - Particle Glow
   - Energy Aura
   - Tactical HUD
   - Plasma Field
   - Quantum Distortion

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/AllianceForge/genesis-forge.git
cd genesis-forge
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Generate NFTs

Generate the complete collection of 1000 NFTs:

```bash
python generate_nfts.py
```

This will:
- Create 1000 unique NFT images in the `output/` directory
- Generate metadata for each NFT in the `metadata/` directory
- Create a collection metadata file at `metadata/collection.json`
- Display rarity statistics for all traits

### Custom Configuration

You can modify the `config.json` file to:
- Change collection size (default: 1000)
- Adjust image dimensions (default: 1000x1000)
- Modify trait rarity weights
- Add or remove layers and traits

Example: To generate 2000 NFTs instead of 1000, edit `config.json`:
```json
{
  "collection_size": 2000,
  ...
}
```

## 📁 Project Structure

```
genesis-forge/
├── generate_nfts.py      # Main NFT generation script
├── config.json           # Configuration and rarity settings
├── requirements.txt      # Python dependencies
├── layers/               # Layer asset directories
│   ├── base/            # Base helmet variants
│   ├── visor/           # Visor variants
│   ├── accent/          # Accent variants
│   ├── background/      # Background variants
│   └── effects/         # Effect variants
├── output/              # Generated NFT images (created on run)
└── metadata/            # Generated NFT metadata (created on run)
```

## 🎯 Using Custom Artwork

To use your own artwork instead of the generated placeholders:

1. Create PNG images with transparent backgrounds (1000x1000 pixels recommended)
2. Name them exactly as defined in `config.json` (e.g., "Standard Helmet.png")
3. Place them in the corresponding layer directories:
   - `layers/base/` for helmet bases
   - `layers/visor/` for visors
   - `layers/accent/` for accents
   - `layers/background/` for backgrounds
   - `layers/effects/` for effects

The generator will automatically use your custom artwork when available, falling back to generated placeholders if files are missing.

## 📊 Metadata Format

Each NFT includes metadata with:
- Name and description
- Token ID
- Image reference
- Trait attributes with rarity weights
- Calculated rarity score
- Collection information

Example metadata structure:
```json
{
  "name": "Alliance Forge Commander Helmet #1",
  "description": "A unique Alliance Forge Commander Helmet from the Genesis collection...",
  "token_id": 1,
  "image": "1.png",
  "attributes": [
    {
      "trait_type": "Background",
      "value": "Space Blue",
      "rarity_weight": 30
    },
    ...
  ],
  "rarity_score": 245.67,
  "collection": "Alliance Forge Commander Helmet"
}
```

## 🛠️ Development

The generator ensures:
- ✅ Each NFT is completely unique
- ✅ Trait distribution follows configured rarity weights
- ✅ All combinations are validated before generation
- ✅ Comprehensive metadata for each token
- ✅ Scalable to any collection size

## 📄 License

This project is part of the Alliance Forge universe.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the generator or add new features.
