# TODO

## Code related

- [ ] Summary with all code at the end of each chapter
- [ ] (Try to) add code runner
- [ ] Add code output
- [ ] Add full code examples
- [ ] Annotations

## Design / Story
- [ ] Anständiger roter Faden - Geschichte erzählen
- [ ] Duplicate stuff von 02 -> 03 und rename 03 -> 04
- [ ] Design?
- [ ] Hide/Show text where appropriate
- [ ] Images for making it a little bit nicer

## Checks
- [ ] Check broken presentation
- [ ] Check animations
- [ ] Check variable names
- [ ] move chainmap example to the library code?
- [ ] Create PDF/Website/etc. -> Send PDF variant to bunny

# Tools to cover
- [ ] argparse
- [ ] collections.deque
- [ ] itertools.total_ordering


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


