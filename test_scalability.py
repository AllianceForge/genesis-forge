#!/usr/bin/env python3
"""
Test script to demonstrate the scalability of the NFT generator
Tests that the system can handle larger collections
"""

import json
import sys

def test_scalability():
    """Test if we can theoretically generate larger collections"""
    
    print("=" * 60)
    print("Scalability Test")
    print("=" * 60)
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Calculate theoretical capacity
    total_combinations = 1
    for layer in config['layers']:
        total_combinations *= len(layer['rarity_weights'])
    
    print(f"\nCurrent configuration:")
    print(f"  Collection size: {config['collection_size']}")
    print(f"  Maximum capacity: {total_combinations}")
    print(f"  Utilization: {(config['collection_size'] / total_combinations) * 100:.1f}%")
    
    # Test different collection sizes
    test_sizes = [1000, 2000, 3000, 4000, 5000, 5400]
    
    print(f"\nScalability Analysis:")
    print(f"{'Size':<10} {'Status':<15} {'Capacity %'}")
    print("-" * 40)
    
    for size in test_sizes:
        if size <= total_combinations:
            status = "✓ Possible"
            pct = f"{(size / total_combinations) * 100:.1f}%"
        else:
            status = "✗ Exceeds capacity"
            pct = f"{(size / total_combinations) * 100:.1f}%"
        
        print(f"{size:<10} {status:<15} {pct}")
    
    print("\n" + "=" * 60)
    print("Recommendations:")
    print("=" * 60)
    
    if config['collection_size'] < total_combinations * 0.5:
        print("✓ Current collection size is well within capacity")
        print("✓ System can easily scale to 2x current size")
    
    print(f"\nTo generate more than {total_combinations} NFTs:")
    print("  1. Add more trait variants to config.json")
    print("  2. Add additional layer types")
    print("  3. Each new variant multiplies total capacity")
    
    print(f"\nExample: Adding 1 new trait to each layer:")
    new_capacity = 1
    for layer in config['layers']:
        new_capacity *= (len(layer['rarity_weights']) + 1)
    print(f"  New capacity: {new_capacity} NFTs ({new_capacity - total_combinations} more)")
    
    return True

if __name__ == "__main__":
    test_scalability()
