#!/usr/bin/env python3
"""
Verification and Statistics Script for Alliance Forge NFT Collection
Analyzes the generated collection and provides detailed insights
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def verify_collection():
    """Verify the integrity and uniqueness of the NFT collection"""
    
    print("=" * 60)
    print("Alliance Forge NFT Collection Verification")
    print("=" * 60)
    
    # Check if collection was generated
    if not Path('metadata/collection.json').exists():
        print("❌ Collection not found. Run generate_nfts.py first.")
        return False
    
    # Load collection metadata
    with open('metadata/collection.json', 'r') as f:
        collection = json.load(f)
    
    total_supply = collection['total_supply']
    nfts = collection['nfts']
    
    print(f"\n📊 Collection: {collection['collection_name']}")
    print(f"📈 Total Supply: {total_supply}")
    print(f"✓ Metadata files: {len(nfts)}")
    
    # Verify uniqueness
    print("\n🔍 Checking uniqueness...")
    combinations = set()
    duplicate_count = 0
    
    for nft in nfts:
        combo = tuple(sorted([(attr['trait_type'], attr['value']) for attr in nft['attributes']]))
        if combo in combinations:
            duplicate_count += 1
            print(f"  ⚠️  Duplicate: {nft['name']}")
        combinations.add(combo)
    
    if duplicate_count == 0:
        print(f"  ✓ All {len(combinations)} NFTs are unique!")
    else:
        print(f"  ❌ Found {duplicate_count} duplicates")
    
    # Verify image files
    print("\n🖼️  Checking image files...")
    missing_images = []
    for i in range(1, total_supply + 1):
        if not Path(f'output/{i}.png').exists():
            missing_images.append(i)
    
    if len(missing_images) == 0:
        print(f"  ✓ All {total_supply} image files present")
    else:
        print(f"  ❌ Missing {len(missing_images)} images: {missing_images[:10]}...")
    
    # Verify metadata files
    print("\n📝 Checking metadata files...")
    missing_metadata = []
    for i in range(1, total_supply + 1):
        if not Path(f'metadata/{i}.json').exists():
            missing_metadata.append(i)
    
    if len(missing_metadata) == 0:
        print(f"  ✓ All {total_supply} metadata files present")
    else:
        print(f"  ❌ Missing {len(missing_metadata)} metadata files: {missing_metadata[:10]}...")
    
    return True

def analyze_rarity():
    """Analyze rarity distribution and trait statistics"""
    
    print("\n" + "=" * 60)
    print("Rarity Analysis")
    print("=" * 60)
    
    with open('metadata/collection.json', 'r') as f:
        collection = json.load(f)
    
    nfts = collection['nfts']
    
    # Collect trait statistics
    trait_counts = defaultdict(lambda: defaultdict(int))
    rarity_scores = []
    
    for nft in nfts:
        rarity_scores.append(nft['rarity_score'])
        for attr in nft['attributes']:
            trait_counts[attr['trait_type']][attr['value']] += 1
    
    # Rarity score statistics
    print(f"\n🎯 Rarity Score Statistics:")
    print(f"  Min: {min(rarity_scores):.2f}")
    print(f"  Max: {max(rarity_scores):.2f}")
    print(f"  Average: {sum(rarity_scores) / len(rarity_scores):.2f}")
    
    # Find rarest NFTs
    sorted_nfts = sorted(nfts, key=lambda x: x['rarity_score'], reverse=True)
    print(f"\n🏆 Top 10 Rarest NFTs:")
    for i, nft in enumerate(sorted_nfts[:10], 1):
        print(f"  {i}. {nft['name']} - Rarity Score: {nft['rarity_score']}")
        traits = ', '.join([f"{attr['value']}" for attr in nft['attributes']])
        print(f"     Traits: {traits}")
    
    # Trait distribution
    print(f"\n📊 Trait Distribution:")
    for trait_type in sorted(trait_counts.keys()):
        print(f"\n  {trait_type}:")
        total = sum(trait_counts[trait_type].values())
        for value, count in sorted(trait_counts[trait_type].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total) * 100
            rarity_bar = '█' * int(percentage / 2)
            print(f"    {value:25} {count:4} ({percentage:5.1f}%) {rarity_bar}")

def find_rare_combinations():
    """Find and display rare trait combinations"""
    
    print("\n" + "=" * 60)
    print("Special Trait Combinations")
    print("=" * 60)
    
    with open('metadata/collection.json', 'r') as f:
        collection = json.load(f)
    
    nfts = collection['nfts']
    
    # Find NFTs with all rare traits
    rare_nfts = [nft for nft in nfts if nft['rarity_score'] > 50]
    print(f"\n🌟 Ultra Rare NFTs (Rarity Score > 50): {len(rare_nfts)}")
    for nft in rare_nfts[:5]:
        print(f"  • {nft['name']} (Score: {nft['rarity_score']})")
        for attr in nft['attributes']:
            print(f"    - {attr['trait_type']}: {attr['value']}")
    
    # Find NFTs with maximum traits
    max_traits = max(len(nft['attributes']) for nft in nfts)
    max_trait_nfts = [nft for nft in nfts if len(nft['attributes']) == max_traits]
    print(f"\n✨ NFTs with Maximum Traits ({max_traits} traits): {len(max_trait_nfts)}")
    for nft in max_trait_nfts[:3]:
        print(f"  • {nft['name']}")
    
    # Find NFTs with minimum traits
    min_traits = min(len(nft['attributes']) for nft in nfts)
    min_trait_nfts = [nft for nft in nfts if len(nft['attributes']) == min_traits]
    print(f"\n🎨 NFTs with Minimum Traits ({min_traits} traits): {len(min_trait_nfts)}")

def export_rarity_table():
    """Export a rarity table to CSV"""
    
    print("\n" + "=" * 60)
    print("Exporting Rarity Table")
    print("=" * 60)
    
    with open('metadata/collection.json', 'r') as f:
        collection = json.load(f)
    
    nfts = collection['nfts']
    
    # Create CSV
    csv_path = 'rarity_table.csv'
    with open(csv_path, 'w') as f:
        # Header
        f.write("Token ID,Name,Rarity Score,Background,Base,Visor,Accent,Effects\n")
        
        # Data
        for nft in sorted(nfts, key=lambda x: x['rarity_score'], reverse=True):
            traits = {attr['trait_type']: attr['value'] for attr in nft['attributes']}
            f.write(f"{nft['token_id']},")
            f.write(f"\"{nft['name']}\",")
            f.write(f"{nft['rarity_score']},")
            f.write(f"{traits.get('Background', 'N/A')},")
            f.write(f"{traits.get('Base', 'N/A')},")
            f.write(f"{traits.get('Visor', 'N/A')},")
            f.write(f"{traits.get('Accent', 'None')},")
            f.write(f"{traits.get('Effects', 'None')}\n")
    
    print(f"✓ Rarity table exported to: {csv_path}")

def main():
    """Main entry point"""
    
    # Run verification
    if not verify_collection():
        return
    
    # Run analysis
    analyze_rarity()
    
    # Find rare combinations
    find_rare_combinations()
    
    # Export rarity table
    export_rarity_table()
    
    print("\n" + "=" * 60)
    print("Verification and Analysis Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
