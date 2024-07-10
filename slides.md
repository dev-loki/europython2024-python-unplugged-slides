---
theme: academic
# theme: academic
background: david-clode-oJlt2XBWuWs-unsplash.jpg
title: "Python unplugged: Mining for hidden batteries"
info: ""
class: text-center
highlighter: shiki
colorSchema: light
drawings:
  persist: false
mdc: true
layout: image-right
image: python-mining-for-batteries.webp
---

# Python unplugged

<br> <hr> <br>

#### Mining for hidden batteries

<!--
- Name of the talk
- What is the talk about
- Next: whoami
-->

---
layout: image-right
image: pingu.jpg
backgroundSize: contain
---

# \$ whoami

<br> <hr> <br>

**name:** Torsten

**occupation:** Polylang Software Architect/Backend Developer Mara Solutions

**dev since:** +12y

**first code:** ~25y if you count creating crappy Amiga Quickbasic textadventure

**other stuff:** Being a proud dad and husband. Reading, tabletennis, ...the usual stuff

<!--
- Whoami
- do not talk too much about amiga ;)
-->

---
layout: center
---

# What problem am I trying to solve here?

<br> <hr> <br>

<v-clicks depth="2">

- learn the possibilities of the built in standard library
- for simple cases external libraries are not always necessary¹
  - _¹for simple cases!_
- better portable one-off scripts!
- sometimes even easier!

</v-clicks>

<!--
- What can we do with the stuff the awesome maintainers already gave us?
- Better portable: Means -> do not expect people to have stuff like pandas/requests/etc. already installed
- obviously this is on a case by case basis, as python is multi purpose language
-->

---
layout: center
---

# What am I NOT trying to solve?

<br> <hr> <br>

<v-clicks>

- Performance issues
- If performance is really **crucial**: <br>
  Pandas/Polars/Numpy/etc. are perfect for you

</v-clicks>

<!--
- Typical python job for complex applications: glue code between libraries written in C, Rust or similar
    - e.g. pandas/polars/pydantic)
- Leet code
-->

---
layout: center
---

# Outline: 4 Chapters

<br> <hr> <br>

1. Fetching data
2. Cleaning data
3. Processing data
4. Miscellaneus / Additional stuff (Might be dropped because of time)
5. (Maybe some ASGI implementation)

---
layout: image-right
image: discworld.png
backgroundSize: contain
---

# What's the story?

<br><hr><br>

<v-clicks>

- Who is familiar with _Terry Pratchett_?
- We are working on a project in _Ankh Morpork_
- The "Unseen Library" and it's librarian finally want
  to implement some digitalisation magic
- The first step is, that we already have some API \**cough*\* magic funnel
  sending us the book data. One by one.
- It is our job to clean the data, work on the data and also save it in our excel (because why not)

</v-clicks>

<!--
I gave this a story to make it less like 30 bullet points containing different 
modules in the python ecoverse.

Ask people if they are familiar with the Discworld saga?

Mention that if we have time we might be able to look in a vanilla ASGI server representation at the end
-->

---
layout: center
---

<SlidevVideo autoplay autoreset>
    <source src="/book-streaming.mp4" type="video/mp4">
</SlidevVideo>

<small><i>
  \* I actually created a full (vanilla python) server and generator to
  generate those books - And we most likely won't even see nor use it -.-'
</i></small>

---

### Example book

<hr>

````md magic-move
```plain
Stupendous Folklore of the Agatean Empire
by Distinguished Discworld Diner Kerfuffle Michael

       title: Stupendous Folklore of the Agatean Empire
      author: Distinguished Discworld Diner Kerfuffle Michael
     lent_by: None
  lent_since: None
  lent_times: 2
        year: The 12th year after Seamstress's Secrets
  catalogued: year -037 in the 7th month
    location: Great Hall: middle shelve. 4m from the start
     excerpt: Amidst foolish surroundings, a blacksmith forged a 
              weapon in the enchanted forest. Time-worn treaties
              are broken.
```
```plain
Puzzling Eating of the Golems
by Senior Guildmaster Danielle Warren

       title: Puzzling Eating of the Golems
      author: Senior Guildmaster Danielle Warren
     lent_by: Jessica Silvermist
  lent_since: year 0065 in the 1st month
  lent_times: 42
        year: The 10th year after Silver Horde
  catalogued: year 0300 in the 7th month
    location: Restricted Section: middle shelve. 4m from the end
     excerpt: Amidst the ruins of a lost civilization trembled
              as a jester sang a melody. Hidden truths come to
              light.
```
````

---
src: ./chapter01_fetching_data.md
hide: false
---

---
src: ./chapter02_cleaning_data.md
hide: false
---

---
src: ./chapter03_summarization.md
hide: false
---

---
src: ./chapter04_misc.md
hide: false
---

---
layout: image-left
image: orang-utan-questionmark.png
---

<br>
<br>
<br>

# Questions?

<br>

<hr>

---
layout: image-right
image: orang-utan-dancing.png
---

<br>
<br>
<br>


# Konec a poděkování

<br>

<hr>

_(The end of the talk and thank you)_
