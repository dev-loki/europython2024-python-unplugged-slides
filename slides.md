---
theme: academic
background: david-clode-oJlt2XBWuWs-unsplash.jpg
title: "Python unplugged: Mining for hidden batteries"
info: ""
class: text-center
highlighter: shiki
colorSchema: light
drawings:
  persist: false
hideInToc: true
mdc: true
layout: image-right
image: images/python-mining-for-batteries.webp
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
image: images/pingu.jpg
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
hideInToc: true
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
hideInToc: true
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
hideInToc: true
layout: center
---

# Outline

<br> <hr> <br>

<Toc maxDepth="2" columns="2" />

---
layout: image-right
image: images/discworld.png
backgroundSize: contain
hideInToc: true
---

# What's the story?

<hr> <br>

<v-clicks>

- Who is familiar with _Terry Pratchett_?
- We are working on a project Ankh Morpork
- And the "Unseen Library" and it's librarian finalyl want
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
    <source src="images/book-streaming.mp4" type="video/mp4">
</SlidevVideo>

---
layout: center
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
image: images/orang-utan-questionmark.png
---

<br>
<br>
<br>

# Questions?

<br>

<hr>

---
layout: image-right
image: images/orang-utan-dancing.png
---

<br>
<br>
<br>


# Konec a poděkování

<br>

<hr>

_(The end of the talk and thank you)_
