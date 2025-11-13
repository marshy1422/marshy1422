# Bjorn Character Design Specifications

## 🎯 Overview

This document provides detailed specifications for creating the 6 evolution stages of Bjorn, the Viking companion character for the mental health app.

---

## 🎨 General Design Principles

### Style Guidelines
- **Aesthetic**: Friendly, approachable, professional mental health app character
- **NOT**: Overly childish, scary, or intimidating
- **Target**: Appeals to adults (18-45) seeking mental wellness support
- **Mood**: Encouraging, warm, trustworthy

### Technical Requirements
- **Format**: PNG with transparent background
- **Resolution**: 512×512px base (will be scaled for different devices)
- **Color Mode**: RGB
- **Bit Depth**: 32-bit (8-bit color + 8-bit alpha)
- **Optimization**: Compressed for mobile (keep under 200KB per sprite)

### Animation Considerations
- Character should have clear center point for rotation animations
- Design should look good when:
  - Bouncing vertically (±20px)
  - Rotating 360°
  - Scaled 80%-120%
  - With glow/particle effects around it

---

## 🥚 Stage 1: Viking Egg (Level 1-4)

### Description
A mystical egg waiting to hatch, adorned with Nordic runes and subtle magical effects.

### Visual Details
- **Shape**: Rounded egg shape, slightly wider at bottom
- **Size Ratio**: 60% of the 512px canvas (leaves room for glow effects)
- **Color Palette**:
  - Base: Stone gray (#8B9196)
  - Runes: Glowing blue (#4A90E2)
  - Accent: Gold trim (#D4AF37)
  - Cracks (higher levels): Glowing orange (#FF6B35)

### Key Features
- 3-5 carved Nordic runes around the surface
- Subtle texture (stone-like, not smooth)
- Faint glow emanating from runes
- Optional: Small cracks appearing at Level 3-4 (pre-hatch)
- Base shadow underneath

### Mood
Mysterious, anticipatory, magical potential

---

## 👶 Stage 2: Baby Viking (Level 5-14) ⭐ PRIMARY FOCUS

### Description
An adorable baby Viking who just hatched - small, cute, and ready to start their journey.

### Visual Details

**Proportions**:
- **Head**: 50% of total character height (large, chibi-style)
- **Body**: 30% of total character height (small, pudgy)
- **Legs**: 20% of total character height (short, stubby)
- **Overall stance**: Standing upright, centered

**Head & Face**:
- Large, round head with soft features
- Big, expressive eyes (bright and curious)
  - Color: Bright blue or green
  - Style: Slightly oversized for cuteness
- Small button nose
- Gentle smile or neutral expression
- Baby blonde hair peeking out from helmet (wispy, messy)
- Rosy cheeks (subtle)

**Outfit & Gear**:
- **Helmet** (KEY FEATURE):
  - Classic Viking horned helmet
  - Oversized - too big for the baby's head
  - Sits slightly tilted or loose
  - Color: Steel gray/silver (#7C8791)
  - Small dents/imperfections (inherited from ancestors)
  - Horns: Small, rounded (not sharp/dangerous)
- **Body Armor**:
  - Simple cloth tunic
  - Color: Nordic blue (#1E3A5F) or earth brown (#8B6F47)
  - Slightly oversized/baggy
  - Nordic pattern trim (simple geometric)
- **Weapon** (OPTIONAL):
  - Tiny wooden practice sword or stick
  - Held in one hand, dragging on ground
  - OR: Small wooden shield with Viking symbol

**Accessories**:
- Small cape or fur collar (optional)
- Tiny leather belt (oversized)
- Simple boots or bare feet

**Posture & Expression**:
- Standing pose, slightly wobbly/innocent stance
- One arm raised (waving or holding weapon)
- Friendly, non-threatening
- Conveys: "I'm new but excited!"

**Color Palette**:
```
Primary: Nordic Blue (#1E3A5F)
Secondary: Steel Gray (#7C8791)
Accent: Gold (#D4AF37)
Skin Tone: Peachy pink (#FFD1A1)
Hair: Blonde (#F5E6B3)
Eyes: Bright Blue (#4A90E2)
Cheeks: Rosy Pink (#FF9AA2)
```

### Mood
Innocent, curious, adorable, beginner energy, "I'm learning!"

### Animation Notes
- Should look cute when bouncing
- Helmet might wobble slightly during animations (future enhancement)
- Glow color during happiness: Warm yellow

---

## ⚔️ Stage 3: Young Warrior (Level 15-29)

### Description
A teenage Viking who's gained confidence and basic skills.

### Visual Details
- **Proportions**: More balanced (head 35%, body 40%, legs 25%)
- **Physique**: Lean, growing muscle definition
- **Face**: Still youthful but more defined features
- **Hair**: Longer, possibly braided or tied back
- **Expression**: Determined, focused

**Gear Upgrades**:
- Helmet now fits properly, slightly more decorative
- Leather armor with metal studs
- Real (but simple) sword and round shield
- Color scheme: Browns and blues, less gold
- Cape or cloak

### Mood
Confident, eager, "I'm getting the hang of this!"

---

## 🛡️ Stage 4: Skilled Fighter (Level 30-49)

### Description
A capable adult Viking warrior with proven battle experience.

### Visual Details
- **Proportions**: Adult realistic proportions
- **Physique**: Muscular, strong build
- **Face**: Mature features, possible stubble beard
- **Hair**: Full beard and braided hair
- **Expression**: Serious, capable

**Gear Upgrades**:
- Chain mail armor under leather
- Decorated helmet with etched patterns
- Quality forged sword with Nordic engravings
- Larger wooden shield with painted symbol
- Fur-trimmed cape
- Battle-worn appearance (scuffs, but maintained)

### Mood
Competent, reliable, "I know what I'm doing"

---

## ⚡ Stage 5: Battle Viking (Level 50-74)

### Description
A seasoned veteran with visible battle history and intimidating presence.

### Visual Details
- **Proportions**: Bulky, powerful build
- **Physique**: Very muscular, imposing
- **Face**: Battle-hardened, scars, full thick beard
- **Hair**: Long braided hair and beard, possibly graying
- **Expression**: Fierce but controlled

**Gear Upgrades**:
- Heavy plate and mail armor
- Ornate helmet with fur crest
- Large battle axe OR longsword
- Tower shield with clan insignia
- War paint or tattoos visible
- Multiple weapons (axe on belt, bow on back)
- Tattered cape showing battle damage
- Trophies or charms

### Mood
Intimidating, experienced, "I've seen battles you wouldn't believe"

---

## 🏆 Stage 6: Legendary Viking (Level 75+)

### Description
A mythical warrior of legend with supernatural elements.

### Visual Details
- **Proportions**: Heroic proportions, slightly larger than life
- **Physique**: Peak warrior form
- **Face**: Wise, weathered, respected elder warrior
- **Hair**: Long flowing hair and beard (possibly white/silver)
- **Expression**: Calm confidence, inner peace

**Legendary Features**:
- Glowing armor with runic enchantments
- Ethereal glow around entire character (blue/gold)
- Legendary weapon (glowing blade or axe)
- Ornate helmet with supernatural elements
- Particle effects (floating runes, light wisps)
- Flowing cape with magical energy
- Halo or crown-like light effect
- Eyes glow with power

**Color Shifts**:
- More golds and silvers
- Ethereal blues and purples
- Shimmering effects

### Mood
Legendary, awe-inspiring, achieved enlightenment, "I am the master of my journey"

---

## 🎨 AI Image Generation Prompts

### For Baby Viking (Most Important)

**MidJourney / DALL-E Prompt**:
```
Cute baby Viking character, chibi proportions with large head and small body,
oversized silver Viking horned helmet (too big, slightly tilted), big bright
blue eyes, friendly smile, small button nose, wispy blonde hair, wearing
oversized Nordic blue tunic with gold trim, holding tiny wooden toy sword,
pudgy arms and legs, adorable kawaii style, game character asset, mobile game
art, professional digital illustration, transparent background, front-facing
view, soft lighting, high quality, 512x512px, mental health app mascot,
approachable and friendly, not childish
```

**Alternative Prompt (More Detailed)**:
```
Character design: Baby Viking, newborn hero, extremely cute chibi style,
head is 50% of body size, large expressive eyes (bright blue, sparkling),
gentle smile, rosy cheeks, oversized steel Viking helmet with small rounded
horns sliding down over eyes, wispy blonde baby hair, small pudgy body,
wearing baggy Nordic blue cloth tunic with geometric patterns, tiny leather
belt, simple brown boots, holding small wooden practice sword (dragging on
ground), standing wobbly pose, one arm raised waving, innocent expression,
soft peachy skin tone, gold accent details, professional game asset art,
clean transparent background, mobile game quality, front view, centered,
no shadows, flat colors with subtle shading, 512x512 pixels, suitable for
mental health wellness app, trustworthy and warm aesthetic
```

**Stable Diffusion Prompt**:
```
baby viking character, chibi, kawaii, oversized horned helmet, big eyes,
blonde hair, blue tunic, wooden sword, cute, adorable, game asset,
transparent background, high quality, digital art, front view, centered,
(professional:1.3), (mental health app:1.2), (friendly:1.4)

Negative prompt: scary, realistic, dark, violent, angry, weapon blood,
childish, cartoon, anime, low quality, blurry
```

### Tips for Best Results
1. **Iterate**: Generate 5-10 variations, pick the best
2. **Refine**: Use "this but with [change]" for adjustments
3. **Consistency**: Save the prompt that works for future stages
4. **Style Reference**: Upload your chosen Baby Viking when generating later stages for consistency
5. **Background Removal**: If needed, use remove.bg or Photoshop

---

## 🛠️ DIY Creation Guide

### If You're Creating Manually (Illustration/Design)

**Software Options**:
- **Vector**: Adobe Illustrator, Figma, Inkscape (free)
- **Raster**: Procreate (iPad), Adobe Photoshop, Krita (free)

**Process**:
1. **Sketch**: Rough sketch on paper or digital
2. **Proportions**: Use circles to map head/body ratio
3. **Line Art**: Clean line work with consistent stroke weight
4. **Color Flats**: Fill in base colors
5. **Shading**: Add depth with 1-2 shadow layers
6. **Highlights**: Add light spots for dimension
7. **Details**: Add textures, patterns, finishing touches
8. **Export**: PNG, transparent background, 512×512px

**Reference Images** (Search for inspiration):
- "Chibi Viking character"
- "Cute warrior game character"
- "Tamagotchi evolution stages"
- "Mobile game mascot design"
- "How to Train Your Dragon (young characters)"

---

## 📏 Character Consistency Guide

To maintain visual consistency across all 6 stages:

### Common Elements (All Stages)
- **Eye color**: Keep consistent (blue or green)
- **Color scheme**: Blues, grays, golds throughout
- **Helmet style**: Horned Viking helmet (evolves but remains recognizable)
- **Symbol/motif**: Consider a personal emblem that appears on all stages
- **Silhouette**: Should be recognizable even in shadow

### Progression Visual Cues
- **Size**: Grows larger within frame
- **Detail**: More intricate designs as level increases
- **Color saturation**: Deeper, richer colors at higher levels
- **Effects**: More glow/particles at higher stages
- **Posture**: More confident stance as evolution progresses

---

## 📦 Delivery Format

### Required Files for Development
```
bjorn_stage1_egg.png          (512×512px, <200KB)
bjorn_stage2_baby.png          (512×512px, <200KB)
bjorn_stage3_young_warrior.png (512×512px, <200KB)
bjorn_stage4_skilled_fighter.png (512×512px, <200KB)
bjorn_stage5_battle_viking.png (512×512px, <200KB)
bjorn_stage6_legendary.png     (512×512px, <200KB)
```

### Optional (Recommended)
```
bjorn_stage2_baby_happy.png     (Happy animation frame)
bjorn_stage2_baby_sad.png       (Neglected state)
bjorn_stage2_baby_eating.png    (Feeding animation)
```

### Folder Structure
```
assets/
  characters/
    bjorn/
      evolution/
        stage_1_egg.png
        stage_2_baby.png
        stage_3_young_warrior.png
        stage_4_skilled_fighter.png
        stage_5_battle_viking.png
        stage_6_legendary.png
      animations/
        baby/
          idle.png
          happy.png
          sad.png
          eating.png
```

---

## 🎯 Quick Start for Developers

### Using Placeholder Until Art is Ready

```javascript
// Temporary emoji-based placeholders
const BJORN_STAGES = {
  1: '🥚', // Egg
  2: '👶', // Baby Viking - REPLACE WITH REAL ART
  3: '🧒', // Young Warrior
  4: '🧔', // Skilled Fighter
  5: '💪', // Battle Viking
  6: '👑', // Legendary Viking
};

// Replace with actual image imports later
import BabyViking from './assets/bjorn/stage_2_baby.png';
```

This allows development to proceed while waiting for final artwork.

---

## 📞 Next Steps

1. **Choose Creation Method**:
   - AI Generation (fastest): Use prompts above with MidJourney/DALL-E
   - Commission Artist (best quality): Hire on Fiverr/Upwork
   - DIY (most control): Illustrate yourself if you have skills

2. **Start with Baby Viking**: This is the most important stage since users will see it most

3. **Test in App**: Import into React Native and test:
   - Does it look good at different sizes?
   - Does it work with the forest background?
   - Does it animate well (bounce, rotate)?

4. **Iterate**: Adjust based on testing feedback

5. **Create Remaining Stages**: Once Baby Viking is approved, create others matching the style

---

## 📋 Quality Checklist

Before finalizing each character:
- [ ] Transparent background with no artifacts
- [ ] 512×512px exactly
- [ ] File size under 200KB
- [ ] Looks good when scaled to 50% and 150%
- [ ] Works with dark forest background
- [ ] Readable when rotated 360°
- [ ] Consistent style with other stages
- [ ] Appropriate for mental health app (friendly, professional)
- [ ] No sharp/dangerous looking elements (especially baby stage)
- [ ] Colors match app palette

---

**Remember**: Bjorn is a mental health companion, not a battle game character. The design should feel supportive, encouraging, and warm - like a friend on your wellness journey. The Viking theme adds personality and gamification, but shouldn't feel aggressive or intimidating.

Good luck bringing Bjorn to life! 🎨⚔️
