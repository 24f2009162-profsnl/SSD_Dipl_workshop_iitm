echo "# Project: Custom Skin-Match Makeup Store" > project.md
echo "## Architecture: Dictionary-driven Python CLI App" >> project.md
echo "## State: Completed" >> project.md

mkdir -p docs/archive
echo "# Feature: Skin Matching Algorithm" > docs/archive/feature_matching.md
echo "Implemented a scalable dictionary mapping for skin types and undertones, avoiding nested conditionals." >> docs/archive/feature_matching.md

echo 'def get_recommendation(skin_type, undertone):
    """Returns makeup recommendations based on structured data mapping."""
    inventory = {
        "oily": {"warm": "Matte Peach Foundation & Setting Powder", "cool": "Matte Neutral Foundation & Setting Spray"},
        "dry": {"warm": "Dewy Golden Foundation & Hydrating Primer", "cool": "Dewy Fair Foundation & Cream Blush"}
    }
    
    # Clean fallback logic
    skin_profile = inventory.get(skin_type.lower())
    if skin_profile:
        return skin_profile.get(undertone.lower(), "Standard Foundation & Clear Gloss")
    return "Universal BB Cream & Lip Tint"

if __name__ == "__main__":
    print("💎 Welcome to the SDD Skin Store 💎")
    user_skin = input("Enter skin type (oily/dry): ")
    user_tone = input("Enter undertone (warm/cool): ")
    
    result = get_recommendation(user_skin, user_tone)
    print(f"\n🛍️  Your Custom Kit: {result}")' > makeup_store.py
