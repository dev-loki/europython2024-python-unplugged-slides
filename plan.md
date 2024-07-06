# TODO

## Code related

- [x] Summary with all code at the end of each chapter
- [ ] Fix Book generation indentation
- [ ] Add book generation
- [ ] Add book generation as animation to slides
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


