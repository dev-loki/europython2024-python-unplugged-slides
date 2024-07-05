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

#### Mining for hidden batteries

---
layout: image-right
image: images/pingu.jpg
backgroundSize: contain
---

# \$ whoami

**name:** Torsten

**occupation:** Software Architect/Backend Developer Mara Solutions

**age:** 37

**dev since:** +12y


**first code:** ~25y if you count creating crappy Amiga Quickbasic textadventure

---
hideInToc: true
layout: center
---

# What problem am I trying to solve here?

<v-clicks depth="2">

- learn the possibilities of the built in standard library
- for simple cases external libraries are not always necessary¹
  - _¹for simple cases!_
- better portable one-off scripts!
- sometimes even easier!

</v-clicks>

---
hideInToc: true
layout: center
---

# What am I NOT trying to solve?

<v-clicks>

- Performance issues
- If performance is really **crucial**: <br>
  Pandas/Polars/Numpy/etc. are perfect for you

</v-clicks>

---
hideInToc: true
layout: center
---

# Outline

<Toc maxDepth="2" columns="2" />

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
