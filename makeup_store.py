# Just vibing a makeup store logic
print("✨ Welcome to the Vibe Skin Store ✨")
skin = input("Is your skin oily or dry? ").lower()
tone = input("Is your undertone warm or cool? ").lower()

if skin == "oily":
    if tone == "warm":
        print("-> We recommend: Matte Peach Foundation & Setting Powder")
    else:
        print("-> We recommend: Matte Neutral Foundation & Setting Spray")
elif skin == "dry":
    if tone == "warm":
        print("-> We recommend: Dewy Golden Foundation & Hydrating Primer")
    else:
        print("-> We recommend: Dewy Fair Foundation & Cream Blush")
else:
    print("-> Just use whatever!")
