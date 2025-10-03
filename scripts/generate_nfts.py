import os
import json

# Example placeholder script – adapt for your actual generative process!
RARITY_ALLOCATION = {
    "Common": 400,
    "Uncommon": 200,
    "Rare": 150,
    "Epic": 100,
    "Legendary": 70,
    "Mythic": 50,
    "Core": 27,
    "Artisan": 3
}

def create_metadata(serial, tier, traits):
    metadata = {
        "name": f"Genesis Forger #{serial}",
        "description": f"Alliance Forge Commander Helmet NFT | {tier} Tier",
        "tier": tier,
        "serial": serial,
        "attributes": traits
    }
    return metadata

def main():
    serial = 1
    metadata_dir = "output/metadata"
    os.makedirs(metadata_dir, exist_ok=True)
    for tier, count in RARITY_ALLOCATION.items():
        for _ in range(count):
            traits = [
                {"trait_type": "Tier", "value": tier},
                {"trait_type": "Helmet Plating", "value": tier}
                # Add more trait generation as needed
            ]
            metadata = create_metadata(serial, tier, traits)
            with open(f"{metadata_dir}/{serial}.json", "w") as f:
                json.dump(metadata, f, indent=2)
            serial += 1

if __name__ == "__main__":
    main()
