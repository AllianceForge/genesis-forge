# Genesis Forgers — Alliance Forge Commander Helmet NFT Collection

A foundational collection of 1,000 unique, generative NFTs based on the iconic Alliance Forge Commander Helmet.  
Each NFT is constructed from layered generative art, reflecting rarity, color, and a distinct visual identity rooted in the tactical, futuristic Alliance Forge universe.

## Project Overview

Genesis Forgers aims to raise capital for continued game development, build the core Alliance Forge community, and establish the brand’s visual identity.

- **Blockchain:** Cronos (ERC-721 standard)
- **Total Supply:** 1,000 NFTs
- **Editions & Rarities:** 7 color/tiers, including exclusive 1-of-1 “Artisan Helmets”
- **Generative Layers:** Background, Helmet Plating, Visor Optics, AF Logo, Side Attachment, Condition, Aura
- **Utilities:** Exclusive Discord access, whitelist for future drops, in-game rewards, and more

## Rarity Structure

| Rarity Tier  | Color Name          | Hex Code  | Example Supply |
|--------------|---------------------|-----------|---------------|
| Common       | Silver              | #C0C0C0   | 400           |
| Uncommon     | Bright Green        | #7CFC00   | 200           |
| Rare         | Cyan                | #00FFFF   | 150           |
| Epic         | Radiant Purple      | #9370DB   | 100           |
| Legendary    | Vibrant Coral       | #FF7F50   | 70            |
| Mythic       | Fiery Red           | #FF4500   | 50            |
| Core         | Bright Gold         | #FFD700   | 27            |
| Artisan      | Unique 1-of-1s      | Varies    | 3             |

> **Note:** See `config/rarity_allocation.json` for precise distribution.

## Artwork & Traits

All NFTs are generated from seven distinct layers:
- **Background**
- **Helmet Plating** (color-coded by rarity)
- **Visor Optics** (static or animated for Epic+)
- **AF Logo** (static or animated for Epic+)
- **Side Attachment**
- **Condition**
- **Aura** (static or animated for Epic+)

## Special Features

- **Animated Traits:** NFTs of Epic rarity and higher feature animated Visor, Logo, and Aura layers.
- **Artisan Helmets:** 3-5 unique, hand-crafted 1-of-1 NFTs reserved for special holders.

## Holder Benefits

- Exclusive “Genesis Forger” Discord role and private channel access
- Guaranteed early access to all future Alpha/Beta tests
- Permanent whitelist status for future Alliance Forge NFT mints
- Unique in-game “Founder’s Insignia” at game launch
- Commander name reservation before game launch

## Repository Structure

```
/
├── DESCRIPTION.md
├── README.md
├── blueprint.md
├── layers/
│   ├── Background/
│   ├── HelmetPlating/
│   ├── VisorOptics/
│   ├── AFLogo/
│   ├── SideAttachment/
│   ├── Condition/
│   ├── Aura/
│   └── Artisan/
├── scripts/
│   └── generate_nfts.py
├── config/
│   └── rarity_allocation.json
├── output/
│   ├── images/
│   └── metadata/
└── ...
```

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/alliance-forge/genesis-forgers-nft.git
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure your collection**
   - Edit `config/rarity_allocation.json` to set the supply per tier.
   - Place your layer assets in the appropriate folders under `/layers/`.
4. **Generate the NFTs**
   ```bash
   python scripts/generate_nfts.py
   ```
   Generated images and metadata will be saved in `/output/`.

## Documentation

- See **DESCRIPTION.md** for a summary of the project.
- See **blueprint.md** for the full collection strategy and rarity plan.
- See **config/rarity_allocation.json** for the NFT distribution.

## License

All artwork and code are © Alliance Forge.  
For licensing or partnership inquiries, please contact the project team.

---

**Genesis Forgers — Building the future of Alliance Forge, one helmet at a time.**
