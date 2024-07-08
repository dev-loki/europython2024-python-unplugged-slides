# TODO

## Bunny Anmerkungen

- [ ] Batching: Function name ist falsch -> nicht duplicate: mark a
- [ ] Bei "data again" vlt noch ein Spruch "I just love data"
- [ ] Book Response highlight line
- [ ] Flaten the list -> besseres Beispiel
- [ ] Let's continue: zauberspruch?
- [ ] Summary chain: Dinge größer machen
- [ ] Summary: "wonky"
- [ ] duplicate book nerd witz rausnehmen?
- [ ] lets continue hiding lost vooks: erst war smiley merkwürdig, dann gewöhnt man sich dran
- [ ] outline streichen
- [ ] remove booky we cannot get back: ganz am anfang: wirkte erst wie ein echter fehler; mehr obvious schauspielern?
- [ ] requirements änderung dingens: authors name, abstract 
- [ ] with suppress in "Misc"
- [x] 46 Besser machen
- [x] 39 Chainmap?
- [x] 40 "Besser machen" & Fixen
- [x] Folie 22: Destructuring Beispiel hinzufügen
- [x] Folie 22: Erklärung fehlt
- [x] Folie 25: Wird ein Objekt dargestellt, aber ein anderes
- [x] Folie 34 Rechtschreibfehler
- [x] filaly auf "waht's the story"

## Code related

- [x] Summary with all code at the end of each chapter
- [x] Fix Book generation indentation
- [x] Add book generation
- [x] Add book generation as animation to slides
- [ ] (Try to) add code runner
- [ ] Add code output
- [ ] Add full code examples in `/code`
- [ ] Annotations

## Design / Story
- [ ] Let's some more data: (Mehrere Datas hier einfügen)
- [ ] Emojis in überschriften
- [ ] Anständiger roter Faden - Geschichte erzählen
- [ ] Duplicate stuff von 02 -> 03 und rename 03 -> 04
- [ ] Design?
- [x] Hide/Show text where appropriate
- [x] Images for making it a little bit nicer
- [x] Questions/Finish slides

## Checks
- [x] Check broken presentation
- [x] Check animations
- [ ] Check variable names
- [ ] move chainmap example to the library code?
- [ ] Create PDF/Website/etc. -> Send PDF variant to bunny

# Tools to cover
- [x] argparse
- [ ] collections.deque
- [x] itertools.total_ordering


# Chapters

## Chapter 1: Collecting / Organizing Data
- urllib + batched
- Response als TypedDict
- Save locally in CSV / sqlite?

## Chapter 2: Organizing / Summarizing Data
- Clean data (itertools pairs)
- Summarize data (defaultdict + Counter)
    -> split + itertools.chain to flatten
    -> Counter
- Using NamedTuple as Summary object
- itertools.groupby location

## Chapter 3: Processing / Finding stuff
- Add new sources (prioritized)
- Use ChainMap to lookup data in new sources / else in archive
- islice to look into first 100 generated books:
    - accumulate: total lenders
    - kombiniere mit name counter (via reduce)

## Chapter 4: Saving tee -> async into csv/jsonl


