# Alliance Forge NFT Collection - Quick Start Guide

This guide will help you generate and work with the Alliance Forge Commander Helmet NFT collection.

## 🚀 Getting Started

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/AllianceForge/genesis-forge.git
cd genesis-forge

# Install dependencies
pip install -r requirements.txt
```

### 2. Generate NFTs

```bash
# Generate 1000 unique NFTs
python generate_nfts.py
```

This creates:
- `output/` - 1000 PNG images (1000x1000 pixels each)
- `metadata/` - 1000 JSON metadata files + collection.json

### 3. Verify Collection

```bash
# Run verification and analysis
python verify_collection.py
```

This provides:
- Uniqueness verification
- Rarity statistics
- Top rarest NFTs
- Trait distribution analysis
- Exports rarity_table.csv

### 4. View NFTs

Open `gallery.html` in a web browser to view the collection:

```bash
# Start a local server (optional)
python -m http.server 8000

# Then open: http://localhost:8000/gallery.html
```

## 📊 What Gets Generated

### File Structure
```
genesis-forge/
├── output/              # 1000 NFT images
│   ├── 1.png
│   ├── 2.png
│   └── ... 1000.png
├── metadata/            # 1000 metadata files
│   ├── 1.json
│   ├── 2.json
│   ├── ... 1000.json
│   └── collection.json  # Complete collection metadata
└── rarity_table.csv     # Sortable rarity rankings
```

### NFT Specifications

**Images:**
- Format: PNG with transparency (RGBA)
- Dimensions: 1000x1000 pixels
- Average file size: ~11-13 KB per image
- Total collection size: ~13 MB

**Metadata:**
- Format: JSON
- Standard NFT metadata format
- Includes rarity scores
- OpenSea compatible

## 🎨 Customization

### Modify Collection Size

Edit `config.json`:

```json
{
  "collection_size": 2000,  // Change from 1000 to 2000
  ...
}
```

### Adjust Rarity Weights

Edit `config.json` to change trait probabilities:

```json
{
  "layers": [
    {
      "name": "base",
      "rarity_weights": {
        "Standard Helmet": 40,    // Higher = more common
        "Heavy Helmet": 30,
        "Elite Helmet": 20,
        "Legendary Helmet": 8,
        "Mythic Helmet": 2        // Lower = more rare
      }
    }
  ]
}
```

### Add Custom Artwork

1. Create PNG files (1000x1000 pixels)
2. Name them exactly as in `config.json`
3. Place in appropriate layer directories:
   - `layers/base/` - Helmet designs
   - `layers/visor/` - Visor styles
   - `layers/accent/` - Accent details
   - `layers/background/` - Backgrounds
   - `layers/effects/` - Special effects

See `layers/README.md` for detailed artwork guidelines.

## 📈 Understanding Rarity

### Rarity Score Calculation

Each trait has a rarity weight in `config.json`. The rarity score is calculated as:

```
Rarity Score = Σ (100 / weight) for each trait
```

**Examples:**
- Common trait (weight: 40) = 2.5 points
- Rare trait (weight: 5) = 20 points
- Ultra rare (weight: 1) = 100 points

### Rarity Tiers

Based on the current collection:
- **Common**: Score 13-25 (~70% of collection)
- **Uncommon**: Score 25-35 (~20% of collection)
- **Rare**: Score 35-50 (~8% of collection)
- **Epic**: Score 50-100 (~1.8% of collection)
- **Legendary**: Score 100+ (~0.2% of collection)

## 🔧 Troubleshooting

### "No module named PIL"
```bash
pip install Pillow
```

### "Could not generate unique combination"
- Reduce collection size
- Add more trait variations
- Adjust rarity weights

### Missing images in gallery.html
- Ensure `output/` directory is in the same folder as `gallery.html`
- Check browser console for errors
- Try starting a local web server

## 📦 Export for Blockchain

### For IPFS Upload

```bash
# Images ready to upload
cd output
# Upload all PNG files to IPFS

# Metadata ready to upload
cd metadata
# Upload all JSON files to IPFS
```

### Update Metadata with IPFS URLs

After uploading to IPFS, update the `image` field in each JSON file:

```json
{
  "image": "ipfs://QmYourHashHere/1.png",
  ...
}
```

## 🎯 Best Practices

1. **Test First**: Generate a small batch (e.g., 100) before running the full 1000
2. **Backup**: Keep copies of generated collections
3. **Version Control**: Don't commit `output/` and `metadata/` to git (they're in `.gitignore`)
4. **Custom Art**: Create artwork in batches and test as you go
5. **Rarity Balance**: Aim for exponential rarity distribution

## 📊 Collection Statistics

From a typical 1000 NFT generation:

**Trait Distribution:**
- 5 layer types
- 28 unique traits (excluding "None")
- 1000 guaranteed unique combinations
- Average 4.36 traits per NFT
- Rarity scores: 13.19 to 148.33

**Rarest Traits:**
- Mythic Helmet: ~2.9%
- Quantum Distortion: ~1.3%
- Void Visor: ~5.8%
- Forge Emblem: ~6.8%

## 🤝 Support

For issues or questions:
1. Check this guide
2. Review `README.md`
3. Check `layers/README.md` for artwork questions
4. Open an issue on GitHub

## 📝 License

Part of the Alliance Forge universe.
