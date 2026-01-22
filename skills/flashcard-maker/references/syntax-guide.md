# Markup Syntax Quick Reference

## Basic Card Structure

```
Question text here?
---
Answer text here
```

## Special Markup

### Color Highlighting
**Syntax:** `[T#!!fbc0bc#(content)]`

**Use for:**
- Chemical symbols: `Oxygen[T#!!fbc0bc#(O)]`
- Technical terms: `API[T#!!fbc0bc#(Application Programming Interface)]`
- Important proper nouns: `Paris[T#!!fbc0bc#(Capital of France)]`
- Key phrases: `photosynthesis[T#!!fbc0bc#(光合作用)]`

**Color:** `#fbc0bc` (light pink/peach color)

### Cloze Deletion (Fill-in-blank)
**Syntax:** `[F##content]`

**Use for:**
- Facts to memorize: `Carbon has atomic number [F##6]`
- Key terms: `pH measures [F##acidity]`
- Dates: `The war began in [F##1914]`
- Formulas: `E = [F##mc²]`

## Combining Both

You can use both types in one answer:

```
What is water's chemical formula?
---
Water[T#!!fbc0bc#(H₂O)] consists of [F##2] hydrogen atoms and [F##1] oxygen atom
```

## Chapter Organization

```
### Chapter Title

Card 1 question?
---
Card 1 answer

Card 2 question?
---
Card 2 answer
```

## Common Patterns

### Definition Card
```
What is photosynthesis?
---
Photosynthesis[T#!!fbc0bc#(process)] converts [F##light energy] into [F##chemical energy]
```

### Symbol/Term Card
```
What is the symbol for Gold?
---
Gold[T#!!fbc0bc#(Au)] from Latin 'Aurum'
```

### Date/Event Card
```
When did World War II end?
---
World War II ended in [F##1945]
```

### Formula Card
```
What is the area formula for a circle?
---
Area = [F##πr²] where r is the radius
```

### List Card
```
Name the primary colors?
---
The primary colors are [F##red], [F##blue], and [F##yellow]
```

## Validation Checklist

✅ Each card has exactly one `---` separator  
✅ Blank line between cards  
✅ No "Q:" or "A:" prefixes  
✅ Highlighting syntax: `[T#!!fbc0bc#(text)]` - check brackets  
✅ Cloze syntax: `[F##text]` - check brackets and ##  
✅ Chapter starts with `###`  
✅ One main concept per card
