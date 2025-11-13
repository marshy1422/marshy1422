# Bjorn - Mental Health Viking Companion App

## 🎯 Project Overview

Build a cross-platform mobile app that gamifies mental wellness through a Tamagotchi-style Viking pet companion. Users improve their mental health while helping Bjorn the Viking grow from an egg to a legendary warrior.

---

## 📱 Core Concept

**Bjorn** is a mental health support app featuring:
- **Virtual Pet System**: Care for Bjorn as he evolves through 6 stages
- **Gamified Wellness**: Earn XP by completing mental health activities
- **AI Support**: Conversational therapy and insights powered by Claude AI
- **Evidence-Based Tools**: CBT exercises, mood tracking, and journaling
- **Immersive Environment**: Animated forest background with campfire and fireflies

---

## 🎮 Feature Specifications

### 1. Bjorn Pet System

**Evolution Stages** (6 total):
1. **Viking Egg** (Level 1-4) - Mystical egg with Nordic runes
2. **Baby Viking** (Level 5-14) - Cute Viking with oversized helmet
3. **Young Warrior** (Level 15-29) - Teen Viking with basic gear
4. **Skilled Fighter** (Level 30-49) - Adult Viking with upgraded armor
5. **Battle Viking** (Level 50-74) - Seasoned warrior with battle scars
6. **Legendary Viking** (Level 75+) - Epic form with glowing legendary armor

**Stats & Mechanics**:
- **Health** (0-100): Decreases 5 points per 12 hours without feeding
- **Happiness** (0-100): Decreases 3 points per 8 hours without interaction
- **Level & XP**: Visual progress bar, level-up triggers evolution
- **Interactions**: Feed (restore +20 health), Care (restore +15 happiness), Tap (small happiness boost)

**Animations**:
- Idle: Gentle 2-3 second bouncing loop
- Rotation: 360° rotation every 10 seconds
- Glow: Pulsing aura (intensifies with happiness)
- Evolution: Dramatic transformation with light effects
- Neglect: Slowed movement and dimmed colors when stats are low

---

### 2. Animated Forest Background

**Layered Environment** (parallax scrolling):

**Layer 1 - Background Trees**:
- Dark pine/spruce silhouettes
- Subtle swaying animation (2-4 second cycles)
- Time-based color transitions (dusk → night)

**Layer 2 - Campfire** (Main Feature):
- Position: Lower third, slightly off-center
- Flame animation: 8-12 frame flickering loop
- Light emission: Orange/yellow glow radius
- Particles: Rising embers that fade upward
- Smoke: Wisping gray smoke with random drift
- Dynamic intensity: Burns brighter when Bjorn's stats are high
- Optional sound: Gentle crackling (toggleable)

**Layer 3 - Fireflies** (Ambient):
- Quantity: 8-15 scattered across screen
- Movement: Slow bezier curve wandering paths (30-60s loops)
- Glow: Fade in/out cycles (0.5-1s), staggered timing
- Color: Soft yellow-green bioluminescence
- Interaction: Avoid Bjorn's proximity
- Trail: Subtle glow trail effect

**Layer 4 - Foreground**:
- Bjorn's platform/clearing
- Swaying grass blades
- Optional Nordic decorative elements (mushrooms, rocks)

**Technical Implementation**:
- `react-native-reanimated` for 60fps animations
- `react-native-parallax` for depth scrolling
- `react-native-skia` for particle systems
- Performance toggle option in settings
- Day/night cycle based on device time

---

### 3. AI Chat Feature (+10 XP per message)

**Interface**:
- User messages: Right-aligned, light blue bubbles
- AI responses: Left-aligned, purple/gray bubbles with Bjorn avatar
- Animated typing indicator
- Nordic-inspired bubble borders

**Claude AI Integration**:
- API: Anthropic Claude with conversation memory
- System Prompt: *"You are Bjorn, a supportive Viking companion. Provide empathetic mental health support with gentle wisdom. Use encouraging, non-judgmental language. Occasionally reference Viking metaphors (strength, journeys, battles). Keep responses warm and conversational, typically 2-4 sentences."*

**Features**:
- Quick prompt buttons: "I'm feeling anxious", "Need motivation", "Want to vent"
- Context awareness: References recent mood entries
- Crisis detection: Provides hotline resources if self-harm mentioned
- Rate limiting: Prevents spam
- Local storage: Saves last 50 messages with timestamps

**XP Reward**:
- +10 XP immediately after user sends message
- Floating "+10 XP" animation
- Bjorn plays happy animation on XP gain

---

### 4. Mood Tracking (+15 XP per entry)

**Mood Selection**:
Six emotion options with animated icons:
- 😊 **Happy** (yellow, bouncing)
- 😢 **Sad** (blue, teardrop)
- 😰 **Anxious** (orange, shaking)
- 😌 **Calm** (green, breathing)
- 😠 **Angry** (red, steam)
- 😐 **Neutral** (gray, static)

**Rating System**:
- Slider: 1-10 intensity scale
- Visual feedback: Emoji changes with rating
- Haptic feedback at each increment
- Color gradient: Cool (low) to warm (high)

**Optional Context**:
- Text field: "What's contributing to this mood?" (200 char max)
- Quick tags: Work, Relationships, Health, Sleep, Exercise

**Visualizations** (react-native-chart-kit):
- Line chart: Mood intensity over 7/30 days
- Bar chart: Emotion frequency distribution
- Heatmap calendar: Color-coded daily mood
- Time insights: "You feel best in the mornings"

**Statistics**:
- Average mood score (week/month)
- Most common emotion
- Improvement percentage vs last week
- Streak counter with bonus XP

**XP Rewards**:
- +15 XP per entry
- +5 bonus XP for adding notes
- +25 XP for 7-day streak, +50 XP for 30-day streak

---

### 5. Journaling (+20 XP per entry)

**Editor Interface**:
- Clean, distraction-free text area
- Word counter
- Auto-save every 30 seconds
- Randomized journaling prompts (20+ options):
  - "What am I grateful for today?"
  - "What challenge did I face and how did I handle it?"
  - "Describe a moment that made you smile"

**AI-Powered Insights** (Claude):
- Trigger: After completing 100+ word entry
- Analysis provides:
  - Emotional tone detection
  - Recurring theme identification
  - Cognitive distortion detection
  - Positive pattern recognition
  - Supportive feedback and reflection questions

**Example Insight**:
> "I notice you're being hard on yourself about today's presentation. Remember, mistakes are how warriors grow! You mentioned feeling relieved afterward, which shows courage. What's one thing you learned from this?"

**Journal Management**:
- Chronological entry list with previews
- Search by keyword
- Favorites/starring system
- Export to PDF or text
- Optional passcode lock

**XP Rewards**:
- +20 XP for entry (50+ words minimum)
- +10 bonus XP for AI insights
- +15 bonus XP for entries over 300 words

---

### 6. CBT Exercises (+25 XP per completion)

#### **Exercise 1: Thought Record**
*Challenge negative automatic thoughts with evidence*

**7-Step Flow**:
1. **Situation**: "Describe what happened"
2. **Automatic Thoughts**: "What went through your mind?"
3. **Emotions**: Select emotions, rate intensity (0-100)
4. **Evidence For**: "What supports this thought?"
5. **Evidence Against**: "What contradicts this thought?"
6. **Alternative Thought**: "What's a more balanced perspective?"
7. **Summary**: Review all responses + AI-generated reflection

#### **Exercise 2: Behavioral Activation**
*Plan mood-boosting activities*

**Flow**:
1. **Current Mood**: Rate mood (1-10) + select emotions
2. **Activity Selection**: Choose from categories:
   - Physical: Walk, stretch, dance
   - Social: Text friend, call family
   - Creative: Draw, write, play music
   - Restful: Meditate, bath, read
   - Productive: Organize, learn, create
   - Fun: Games, hobbies, entertainment
3. **Scheduling**: Set date/time + reminder notification
4. **Prediction**: "How much will this improve mood?" (1-10)
5. **Completion**: After activity, rate actual improvement
6. **Analysis**: Compare prediction vs reality, track effectiveness

#### **Exercise 3: Cognitive Restructuring**
*Identify and reframe cognitive distortions*

**Flow**:
1. **Identify Thought**: "What negative thought are you having?"
2. **Distortion Detection**: Select from 10 common distortions:
   - All-or-Nothing Thinking
   - Overgeneralization
   - Mental Filter (focusing on negatives)
   - Discounting Positives
   - Jumping to Conclusions
   - Catastrophizing
   - Emotional Reasoning
   - Should Statements
   - Labeling
   - Personalization
3. **Challenge**: Answer questions for each selected distortion
4. **Reframe**: "Write a more balanced, realistic thought"
5. **Belief Rating**: "How much do you believe this?" (0-100%)
6. **AI Enhancement**: Claude provides additional reframing suggestions

#### **Exercise 4: Gratitude Practice**
*Shift focus to positive aspects*

**Flow**:
1. **List 3 Gratitudes**: Big or small things
2. **Depth Exploration**: "Why are you grateful for this?"
3. **Sensory Detail**: "Describe with your senses" (optional)
4. **Visualization**: "How does it make you feel?"
5. **History**: View gratitude journal, weekly patterns
6. **Correlation**: "Mood X% higher on gratitude days"

**Exercise Features**:
- Progress saving: Pause and resume anytime
- History view: All completed exercises by type
- Educational explainers about CBT principles
- Custom templates for common thoughts/activities
- Daily reminder notifications

**XP Rewards**:
- +25 XP per completed exercise
- +10 bonus XP for optional depth (reflections)
- Streak bonuses for consecutive days

---

## 🏆 Gamification System

### XP Distribution
| Activity | Base XP | Bonus Conditions |
|----------|---------|------------------|
| AI Chat | +10 XP per message | — |
| Mood Track | +15 XP per entry | +5 XP for notes, +25/50 XP for streaks |
| Journal | +20 XP per entry | +10 XP for AI insights, +15 XP for 300+ words |
| CBT Exercise | +25 XP per completion | +10 XP for optional depth |

### Level Progression
- **XP Formula**: XP needed = 100 × current_level (exponential)
- **Evolution Milestones**:
  - Level 1-4: Viking Egg (0-1,000 XP)
  - Level 5: Baby Viking (first evolution)
  - Level 15: Young Warrior
  - Level 30: Skilled Fighter
  - Level 50: Battle Viking
  - Level 75: Legendary Viking (max form)

### Evolution Animation
- Full-screen takeover
- Transformation sequence with light/particle effects
- Triumphant sound/music
- "Bjorn has evolved!" announcement
- New abilities showcase

### Achievement System
**Badges**:
- "First Steps" - Complete first activity
- "Consistent Warrior" - 7-day streak
- "Journaling Viking" - 10 journal entries
- "Mood Master" - 30 days of tracking
- "Thought Challenger" - 5 thought records
- "Legendary Companion" - Reach max level

### Stats Dashboard
- Total XP earned all-time
- Activities completed (by type)
- Current streak
- Achievements earned
- Time in app
- Bjorn's age (days since creation)

---

## 🛠️ Technical Stack

### Core Framework
- **React Native** 0.72+
- **TypeScript** for type safety
- **React Navigation** 6+ for routing
- **State Management**: Redux Toolkit or Zustand

### UI/Animation Libraries
- `react-native-reanimated` v3 - 60fps animations
- `react-native-gesture-handler` - Touch interactions
- `react-native-skia` - Canvas rendering for particles
- `react-native-svg` - Vector graphics
- `lottie-react-native` (optional) - Complex animations

### Data Visualization
- `react-native-chart-kit` - Mood charts
- `victory-native` (alternative) - More customizable

### Storage
- `@react-native-async-storage/async-storage` - Key-value storage
- `react-native-sqlite-storage` (alternative) - Relational database

### API Integration
- `axios` - HTTP requests to Claude API
- `react-native-config` - Environment variables for API keys

### Notifications
- `@react-native-firebase/messaging` - Push notifications
- `react-native-push-notification` - Local notifications

### Audio (Optional)
- `react-native-sound` - Campfire crackling, ambient sounds

### Performance Optimization
- `react-native-fast-image` - Optimized image loading
- `react-native-mmkv` (alternative) - Ultra-fast storage

---

## 🎨 Design System

### Color Palette
```
Primary: Deep Viking Blue (#1E3A5F)
Secondary: Nordic Purple (#6B4E8B)
Accent: Gold (#D4AF37)
Background: Dark Forest Green (#1A2F23)
Campfire: Orange-Yellow gradient (#FF6B35 → #FFD23F)
Firefly Glow: Yellow-Green (#C2FF3D)
Success: Calm Green (#4CAF50)
Warning: Amber (#FFC107)
Danger: Battle Red (#D32F2F)
```

### Typography
- **Headers**: Bold Norse-inspired font (e.g., "Germania One")
- **Body**: Clean sans-serif (e.g., "Roboto", "SF Pro")
- **Accent**: Runic-style for decorative elements

### Layout Principles
- 8px base unit grid system
- Minimum 44×44px tap targets
- Card-based components with subtle shadows
- Viking-themed iconography (shields, swords, runes)

### Animation Guidelines
- Smooth ease-in-out transitions
- 60fps performance target
- Respect accessibility (reduce motion settings)

---

## 🗺️ User Flow

### Onboarding (First Launch)
1. Welcome screen with app introduction
2. "Meet Bjorn" - Egg appears with animation
3. Tutorial: "Help Bjorn grow by caring for yourself"
4. Feature walkthrough (swipeable cards)
5. Set daily reminder time (optional)
6. Grant notification permissions
7. Home screen with coaching tooltips

### Main Navigation
**Bottom Tab Navigator** (5 tabs):
- 🏠 **Home**: Forest background + Bjorn + stats
- 💬 **Chat**: AI conversation with Bjorn
- 📊 **Track**: Mood tracking
- 📝 **Journal**: Reflective writing
- 🛡️ **Exercises**: CBT activities

### Activity Completion Flow
1. User opens feature (Chat/Track/Journal/Exercise)
2. Completes activity
3. XP gain animation appears (floating "+X XP" text)
4. Returns to home screen
5. Bjorn plays celebration animation
6. **If level up**: Evolution sequence triggers
7. Stats update with smooth counter animations

### Notification Strategy
- **Daily Reminder**: "Check in with Bjorn!" (user-set time)
- **Low Health**: "Bjorn needs feeding" (when <30)
- **Low Happiness**: "Bjorn misses you" (when <30)
- **Streak Risk**: "Keep your streak alive!" (if about to break)
- **Achievements**: "You've unlocked [badge name]!"

---

## 🎯 Development Priorities

### Phase 1: MVP (Core Features)
1. Basic Bjorn pet system (3 evolution stages)
2. Simple forest background (no animations)
3. Mood tracking with basic charts
4. Journaling without AI insights
5. One CBT exercise (Thought Record)
6. XP/level system

### Phase 2: Enhancement
1. Full 6-stage evolution system
2. Animated forest (campfire + fireflies)
3. AI chat integration (Claude API)
4. AI journal insights
5. All 4 CBT exercises
6. Achievement system

### Phase 3: Polish
1. Advanced animations and effects
2. Sound effects and ambient audio
3. Daily challenges
4. Social features (optional friend sharing)
5. Export/backup functionality
6. Accessibility improvements

---

## 📊 Success Metrics

### User Engagement
- Daily active users (DAU)
- Average session duration
- Feature usage rates (which tools are most used)
- Retention rate (7-day, 30-day)

### Mental Health Impact
- Mood trend improvements over time
- Completion rates for CBT exercises
- Journaling consistency
- User self-reported wellbeing

### Gamification Effectiveness
- Average user level reached
- Streak lengths
- Achievement unlock rates
- XP earning patterns

---

## ⚠️ Important Considerations

### Mental Health Safety
- **Crisis Resources**: In-app links to crisis hotlines (988 Suicide & Crisis Lifeline, Crisis Text Line)
- **Disclaimer**: "This app is not a substitute for professional mental health care"
- **Professional Referral**: Suggest seeking therapy for persistent symptoms

### Data Privacy
- All data stored locally on device
- No cloud syncing without explicit user consent
- Option to delete all data
- Transparent privacy policy

### Accessibility
- Screen reader support
- High contrast mode option
- Reduce motion setting
- Font size adjustability
- Color-blind friendly palette options

### API Cost Management
- Claude API rate limiting
- Cache common responses
- Batch API calls where possible
- User notification if API quota reached

---

## 🚀 Getting Started

### Prerequisites
```bash
node >= 18.0.0
npm >= 8.0.0
React Native CLI
Xcode (for iOS development)
Android Studio (for Android development)
```

### Installation
```bash
# Clone repository
git clone [repository-url]
cd bjorn-app

# Install dependencies
npm install

# iOS setup
cd ios && pod install && cd ..

# Set up environment variables
cp .env.example .env
# Add your Claude API key to .env

# Run on iOS
npm run ios

# Run on Android
npm run android
```

### Environment Variables
```
CLAUDE_API_KEY=your_api_key_here
API_BASE_URL=https://api.anthropic.com
```

---

## 📝 Next Steps for Implementation

1. **Set up project structure**: React Native with TypeScript
2. **Design Bjorn character sprites**: Create 6 evolution stage illustrations
3. **Implement animation system**: Start with basic idle/bounce animations
4. **Build forest background**: Layer by layer (trees → campfire → fireflies)
5. **Create navigation**: Bottom tab navigator with 5 screens
6. **Develop core features**: One at a time, starting with mood tracking
7. **Integrate Claude API**: Set up secure API calls with error handling
8. **Implement gamification**: XP system and level progression
9. **Add notifications**: Local and push notification system
10. **Testing**: Unit tests, integration tests, user testing
11. **Polish**: Animations, sound effects, accessibility
12. **Deploy**: App Store and Google Play submission

---

## 🎨 Asset Requirements

### Character Sprites Needed
For each of 6 evolution stages, create:
- Idle pose (base sprite)
- Animation frames (if needed for sprite-based animation)
- High resolution (3x size for retina displays)
- Transparent backgrounds (PNG format)
- Consistent style across all stages

**Recommended Size**: 512×512px base size

### Baby Viking Specifics (Level 5-14)
- Oversized Viking helmet (too big for head)
- Small, cute proportions (large head, small body)
- Friendly, innocent expression
- Simple wooden sword or toy weapon
- Soft, rounded shapes
- Bright, inviting colors
- No battle scars or intimidating features

**Style Reference**: Think "chibi" or "kawaii" Viking aesthetic - adorable and approachable, not fierce

### Environment Assets
- Pine/spruce tree silhouettes (various sizes)
- Campfire sprite sheet (8-12 frames)
- Firefly sprite (with glow)
- Smoke particles
- Ember particles
- Grass blades
- Optional: Rocks, mushrooms, logs

---

## 📄 License & Credits

**License**: MIT License (or your choice)

**Credits**:
- Mental health guidance: Consult with licensed therapists
- CBT exercises: Based on evidence-based cognitive behavioral therapy principles
- Character design: [Designer name]
- Sound effects: [Source/designer]
- Music: [Composer/source]

---

**Note**: This app should complement, not replace, professional mental health care. Always encourage users to seek professional help for serious mental health concerns.

---

## 🖼️ Image Generation Guide

### For Baby Viking Character

Since I cannot generate images directly, I recommend using one of these methods:

**Option 1: AI Image Generation Services**
Use this prompt with MidJourney, DALL-E, or Stable Diffusion:

```
"Cute baby Viking character, chibi style, large head with oversized horned helmet,
small body, friendly innocent expression, holding tiny wooden toy sword, soft rounded
shapes, bright cheerful colors (blues and purples), transparent background,
game asset, mobile game art style, high quality, 512x512px, front facing view"
```

**Option 2: Commission an Artist**
- Fiverr, Upwork, or ArtStation for professional character designers
- Provide this document as reference
- Request delivery in PNG format with transparent background
- Ask for multiple evolution stages in consistent style

**Option 3: Use Placeholder**
- Start development with simple geometric shapes or emoji
- Replace with final artwork later
- Allows you to build functionality without waiting for art

Would you like me to:
1. Create a more detailed character design brief?
2. Suggest specific AI image generation prompts for each evolution stage?
3. Help you set up the project structure to begin development?
