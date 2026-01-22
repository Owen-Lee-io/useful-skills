---
name: flashcard-maker
description: Create Flash cards in a specific format for spaced repetition learning. Use when users request creating flashcards, memory cards, study cards from learning materials, or when they provide content (text, documents, notes, knowledge points) and ask to convert it into flashcard format. Also use when users explicitly say "make flashcards", "create memory cards", "generate study cards", or "convert to flashcard format". Supports color highlighting and cloze deletion features for enhanced memorization.
---

# Flash Card Maker

Generate Flash cards in a standardized format optimized for spaced repetition learning systems. This skill automatically converts learning materials into properly formatted flashcards with advanced features like color highlighting and cloze deletion.

## When to Use This Skill

This skill triggers when users:
- Provide learning materials (text, notes, documents) and want flashcards generated
- Explicitly request "make flashcards", "create memory cards", "generate study cards"
- Need to convert knowledge into structured Q&A format
- Want to edit or optimize existing flashcard content

## Core Card Structure

Each flashcard consists of three parts in this exact order:

```
[Card Front - Question]
---
[Card Back - Answer]
```

**Critical Rules:**
1. **Front (Question)**: Write the question or prompt directly without any prefix
2. **Separator**: Must be exactly `---` on its own line
3. **Back (Answer)**: Contains the answer with optional special markup

## Special Markup Syntax

### 1. Color Highlighting
**Format:** `[T#!!fbc0bc#(content)]`

Use to emphasize key information with color highlighting.

**Example:**
```
What is the chemical symbol for Oxygen?
---
Oxygen[T#!!fbc0bc#(O)] is a chemical element
```

### 2. Cloze Deletion (Fill-in-the-blank)
**Format:** `[F##content to hide]`

Create fill-in-the-blank memory points.

**Examples:**
```
What is the atomic number of Carbon?
---
Carbon has atomic number [F##6]

What is the capital of France?
---
The capital is [F##Paris]
```

## Organization Structure

### Chapter Grouping
Use `### Chapter Name` to group related cards:

```
### Chemical Elements Basics

What is the symbol for Hydrogen?
---
Hydrogen[T#!!fbc0bc#(H)] is the lightest element

What is the symbol for Helium?
---
Helium[T#!!fbc0bc#(He)] is a noble gas
```

### Card Spacing
- Separate cards with **one blank line**
- Blank lines help the system distinguish individual cards

## Complete Example

```
### Periodic Table Fundamentals

What is the third element in the periodic table?
---
Lithium[T#!!fbc0bc#(Li)] is a light metal with atomic number [F##3]

What are the noble gases?
---
The noble gases include Helium[T#!!fbc0bc#(He)], Neon[T#!!fbc0bc#(Ne)], Argon[T#!!fbc0bc#(Ar)], and others

### Chemistry Symbols

What does pH measure?
---
pH measures the [F##acidity or alkalinity] of a solution on a scale from [F##0 to 14]
```

## Best Practices

### Automatic Knowledge Point Identification
When generating cards from learning materials:

1. **Identify key concepts**: Look for definitions, facts, formulas, dates, names
2. **Apply highlighting strategically**: Use `[T#!!fbc0bc#()]` for:
   - Technical terms and their symbols
   - Important proper nouns
   - Key numerical values
3. **Create cloze deletions**: Use `[F##]` for:
   - Critical facts to memorize
   - Numerical values
   - Key terms in definitions

### Question Types to Generate

Support various question formats:
- **Factual Q&A**: "What is X?" → "X is..."
- **Fill-in-blank**: "What does pH measure?" → "pH measures [F##acidity]..."
- **Definition**: "Define photosynthesis" → "Photosynthesis[T#!!fbc0bc#(process)]..."
- **List items**: "Name the noble gases" → Lists with highlights

### Quality Guidelines

1. **Clear Questions**: Front should be unambiguous and self-contained
2. **Concise Answers**: Back should be focused and not overly verbose
3. **Strategic Markup**: Don't overuse highlighting - only for truly key information
4. **Logical Grouping**: Use chapters to organize related concepts
5. **One Concept Per Card**: Avoid cramming multiple unrelated facts into one card

## put Format

Always output the final flashcard content in a code block for easy copying:

````markdown
```
### Chapter Name

Question 1?
---
Answer with [T#!!fbc0bc#(highlighted)] and [F##cloze] elements

Question 2?
---
Answer content
```
````

## Error Prevention

**Common mistakes to avoid:**
- ❌ Adding prefixes like "Q:" or "A:" to questions/answers
- ❌ Using incorrect separator (must be exactly `---`)
- ❌ Forgetting blank lines between cards
- ❌ Malformed markup syntax (check brackets and symbols carefully)
- ❌ Multiple concepts in one card (keep atomic)
