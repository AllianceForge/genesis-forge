#!/usr/bin/env python3
"""
Alliance Forge Commander Helmet NFT Generator
Generates unique NFT images and metadata based on layered assets
"""

import json
import os
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageColor
import hashlib

class NFTGenerator:
    def __init__(self, config_path='config.json'):
        """Initialize the NFT generator with configuration"""
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.collection_name = self.config['collection_name']
        self.collection_size = self.config['collection_size']
        self.image_width = self.config['image_width']
        self.image_height = self.config['image_height']
        self.layers = self.config['layers']
        
        # Track generated combinations to ensure uniqueness
        self.generated_hashes = set()
        self.metadata_list = []
        
    def get_weighted_random_choice(self, layer_config):
        """Select a random trait based on rarity weights"""
        traits = list(layer_config['rarity_weights'].keys())
        weights = list(layer_config['rarity_weights'].values())
        return random.choices(traits, weights=weights, k=1)[0]
    
    def generate_combination(self):
        """Generate a unique combination of traits"""
        max_attempts = 1000
        attempts = 0
        
        while attempts < max_attempts:
            combination = {}
            for layer in self.layers:
                trait = self.get_weighted_random_choice(layer)
                combination[layer['name']] = trait
            
            # Create hash of combination to check uniqueness
            combo_str = json.dumps(combination, sort_keys=True)
            combo_hash = hashlib.md5(combo_str.encode()).hexdigest()
            
            if combo_hash not in self.generated_hashes:
                self.generated_hashes.add(combo_hash)
                return combination
            
            attempts += 1
        
        raise Exception("Could not generate unique combination after maximum attempts")
    
    def create_placeholder_layer(self, trait_name, layer_name):
        """Create a placeholder image for a trait"""
        img = Image.new('RGBA', (self.image_width, self.image_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Define colors based on layer and trait
        color_map = {
            'background': {
                'Space Blue': (10, 25, 80, 255),
                'Cosmic Purple': (60, 20, 80, 255),
                'Nebula Red': (80, 20, 30, 255),
                'Solar Yellow': (80, 70, 20, 255),
                'Deep Black': (5, 5, 10, 255)
            },
            'base': {
                'Standard Helmet': (120, 120, 140, 255),
                'Heavy Helmet': (90, 90, 100, 255),
                'Elite Helmet': (140, 140, 160, 255),
                'Legendary Helmet': (180, 160, 100, 255),
                'Mythic Helmet': (200, 150, 255, 255)
            },
            'visor': {
                'Clear Visor': (200, 220, 255, 200),
                'Blue Tint': (100, 150, 255, 180),
                'Red Tint': (255, 100, 100, 180),
                'Gold Tint': (255, 215, 0, 180),
                'Holographic': (150, 255, 200, 150),
                'Void Visor': (20, 10, 40, 220)
            },
            'accent': {
                'Battle Scars': (60, 60, 60, 200),
                'Alliance Insignia': (255, 200, 50, 255),
                'Energy Lines': (100, 200, 255, 200),
                'Command Stripes': (255, 100, 50, 255),
                'Forge Emblem': (200, 50, 50, 255)
            },
            'effects': {
                'Particle Glow': (255, 255, 200, 100),
                'Energy Aura': (100, 200, 255, 120),
                'Tactical HUD': (50, 255, 100, 100),
                'Plasma Field': (255, 100, 255, 80),
                'Quantum Distortion': (200, 100, 255, 90)
            }
        }
        
        if trait_name == 'None':
            return img
        
        # Draw background
        if layer_name == 'background':
            color = color_map.get(layer_name, {}).get(trait_name, (128, 128, 128, 255))
            draw.rectangle([0, 0, self.image_width, self.image_height], fill=color)
        
        # Draw helmet base
        elif layer_name == 'base':
            color = color_map.get(layer_name, {}).get(trait_name, (128, 128, 128, 255))
            # Main helmet body
            draw.ellipse([250, 200, 750, 700], fill=color, outline=(80, 80, 80, 255), width=5)
            # Top crest
            draw.polygon([(350, 200), (500, 150), (650, 200)], fill=color, outline=(80, 80, 80, 255))
            # Side vents
            draw.rectangle([220, 400, 280, 500], fill=(60, 60, 60, 255))
            draw.rectangle([720, 400, 780, 500], fill=(60, 60, 60, 255))
        
        # Draw visor
        elif layer_name == 'visor':
            color = color_map.get(layer_name, {}).get(trait_name, (200, 200, 200, 200))
            draw.ellipse([320, 350, 680, 550], fill=color, outline=(40, 40, 40, 255), width=3)
        
        # Draw accents
        elif layer_name == 'accent':
            color = color_map.get(layer_name, {}).get(trait_name, (255, 255, 255, 200))
            if trait_name == 'Battle Scars':
                # Draw scratches
                for i in range(5):
                    x = random.randint(300, 700)
                    y = random.randint(250, 650)
                    draw.line([(x, y), (x + random.randint(20, 60), y + random.randint(-20, 20))], 
                             fill=color, width=2)
            elif trait_name == 'Alliance Insignia':
                # Draw star insignia
                center = (500, 280)
                draw.regular_polygon((center, 30), 5, fill=color)
            elif trait_name == 'Energy Lines':
                # Draw energy lines
                for i in range(3):
                    y = 300 + i * 80
                    draw.line([(280, y), (720, y)], fill=color, width=3)
            elif trait_name == 'Command Stripes':
                # Draw stripes
                for i in range(3):
                    y = 250 + i * 30
                    draw.rectangle([450, y, 550, y + 15], fill=color)
            elif trait_name == 'Forge Emblem':
                # Draw emblem
                draw.ellipse([470, 260, 530, 320], fill=color, outline=(100, 100, 100, 255), width=2)
        
        # Draw effects
        elif layer_name == 'effects':
            color = color_map.get(layer_name, {}).get(trait_name, (255, 255, 255, 100))
            if trait_name == 'Particle Glow':
                # Draw glow particles
                for i in range(20):
                    x = random.randint(200, 800)
                    y = random.randint(150, 750)
                    size = random.randint(3, 10)
                    draw.ellipse([x, y, x + size, y + size], fill=color)
            elif trait_name == 'Energy Aura':
                # Draw aura
                draw.ellipse([200, 150, 800, 750], outline=color, width=15)
            elif trait_name == 'Tactical HUD':
                # Draw HUD elements
                draw.rectangle([100, 100, 200, 120], outline=color, width=2)
                draw.rectangle([800, 100, 900, 120], outline=color, width=2)
                draw.line([(150, 500), (150, 600)], fill=color, width=2)
            elif trait_name == 'Plasma Field':
                # Draw plasma field
                for i in range(10):
                    x = random.randint(200, 800)
                    y = random.randint(150, 750)
                    size = random.randint(20, 50)
                    draw.ellipse([x, y, x + size, y + size], fill=color)
            elif trait_name == 'Quantum Distortion':
                # Draw distortion lines
                for i in range(15):
                    x = random.randint(200, 800)
                    y = random.randint(150, 750)
                    draw.line([(x, y), (x + random.randint(-30, 30), y + random.randint(-30, 30))], 
                             fill=color, width=2)
        
        return img
    
    def create_image(self, combination, token_id):
        """Create the final NFT image by compositing layers"""
        # Create base image
        final_image = Image.new('RGBA', (self.image_width, self.image_height), (255, 255, 255, 0))
        
        # Composite each layer
        for layer in self.layers:
            trait = combination[layer['name']]
            
            # Try to load actual layer file first
            layer_path = Path(layer['directory']) / f"{trait}.png"
            
            if layer_path.exists():
                layer_img = Image.open(layer_path).convert('RGBA')
                # Resize if necessary
                if layer_img.size != (self.image_width, self.image_height):
                    layer_img = layer_img.resize((self.image_width, self.image_height), Image.LANCZOS)
                final_image = Image.alpha_composite(final_image, layer_img)
            else:
                # Create placeholder
                layer_img = self.create_placeholder_layer(trait, layer['name'])
                final_image = Image.alpha_composite(final_image, layer_img)
        
        return final_image
    
    def calculate_rarity_score(self, combination):
        """Calculate rarity score based on trait weights"""
        total_score = 0
        for layer in self.layers:
            trait = combination[layer['name']]
            weight = layer['rarity_weights'].get(trait, 1)
            # Lower weight = more rare = higher score
            rarity = 100 / weight if weight > 0 else 100
            total_score += rarity
        return round(total_score, 2)
    
    def create_metadata(self, combination, token_id):
        """Create metadata JSON for the NFT"""
        attributes = []
        for layer in self.layers:
            trait = combination[layer['name']]
            if trait != 'None':
                weight = layer['rarity_weights'].get(trait, 1)
                attributes.append({
                    "trait_type": layer['name'].capitalize(),
                    "value": trait,
                    "rarity_weight": weight
                })
        
        metadata = {
            "name": f"{self.collection_name} #{token_id}",
            "description": f"A unique Alliance Forge Commander Helmet from the Genesis collection. Part of a limited set of {self.collection_size} tactical helmets.",
            "token_id": token_id,
            "image": f"{token_id}.png",
            "attributes": attributes,
            "rarity_score": self.calculate_rarity_score(combination),
            "collection": self.collection_name
        }
        
        return metadata
    
    def generate_collection(self):
        """Generate the entire NFT collection"""
        print(f"Generating {self.collection_size} unique NFTs...")
        print(f"Collection: {self.collection_name}")
        print("-" * 50)
        
        # Create output directories
        Path('output').mkdir(exist_ok=True)
        Path('metadata').mkdir(exist_ok=True)
        
        for i in range(1, self.collection_size + 1):
            if i % 100 == 0:
                print(f"Generated {i}/{self.collection_size} NFTs...")
            
            # Generate unique combination
            combination = self.generate_combination()
            
            # Create image
            image = self.create_image(combination, i)
            image_path = Path('output') / f"{i}.png"
            image.save(image_path, 'PNG')
            
            # Create metadata
            metadata = self.create_metadata(combination, i)
            metadata_path = Path('metadata') / f"{i}.json"
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            self.metadata_list.append(metadata)
        
        # Save collection metadata
        collection_metadata = {
            "collection_name": self.collection_name,
            "total_supply": self.collection_size,
            "nfts": self.metadata_list
        }
        
        with open('metadata/collection.json', 'w') as f:
            json.dump(collection_metadata, f, indent=2)
        
        print("-" * 50)
        print(f"✓ Successfully generated {self.collection_size} unique NFTs!")
        print(f"✓ Images saved to: output/")
        print(f"✓ Metadata saved to: metadata/")
        
        # Print rarity statistics
        self.print_rarity_stats()
    
    def print_rarity_stats(self):
        """Print statistics about trait distribution"""
        print("\n" + "=" * 50)
        print("RARITY STATISTICS")
        print("=" * 50)
        
        for layer in self.layers:
            print(f"\n{layer['name'].upper()}:")
            trait_counts = {}
            for metadata in self.metadata_list:
                # Find trait value from attributes
                trait_value = None
                for attr in metadata['attributes']:
                    if attr['trait_type'].lower() == layer['name']:
                        trait_value = attr['value']
                        break
                
                # If no attribute found, it might be "None"
                if trait_value is None:
                    # Check in generated combinations (we need to store this)
                    trait_value = "None"
                
                trait_counts[trait_value] = trait_counts.get(trait_value, 0) + 1
            
            # Sort by count
            for trait, count in sorted(trait_counts.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / self.collection_size) * 100
                print(f"  {trait}: {count} ({percentage:.1f}%)")

def main():
    """Main entry point"""
    print("=" * 50)
    print("Alliance Forge Commander Helmet NFT Generator")
    print("=" * 50)
    print()
    
    generator = NFTGenerator()
    generator.generate_collection()
    
    print("\n" + "=" * 50)
    print("Generation Complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()
