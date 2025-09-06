---
date: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
week: <% tp.date.now("WW") %>
month: <% tp.date.now("MMMM") %>
year: <% tp.date.now("YYYY") %>
tags: [daily, journal]
---

# <% tp.date.now("dddd, MMMM Do YYYY") %>

```dataview
TABLE WITHOUT ID
  title AS "atividade",
  dateformat(time, "HH:mm") AS "horário",
  category AS "categoria",
  notes AS "notas?"
FROM "registers/activity"
WHERE dateformat(time, "yyyy-MM-dd") = dateformat(this.file.day, "yyyy-MM-dd")
SORT time ASC
```


## tarefas

```dataview
TASK 
FROM "tasks"
WHERE !completed AND due = date(<% tp.date.now("YYYY-MM-DD") %>)
SORT priority ASC
```

---
## diário


---
## trabalho do dia
### registros
#### notas criadas

```dataview
TABLE WITHOUT ID
  file.link AS "documento",
  file.folder AS "path",
  dateformat(file.ctime, "HH:mm") AS "criado às"
FROM ""
WHERE file.ctime >= date(today)
  AND file.ctime < (date(today) + dur(1 day))
SORT file.ctime ASC

```
---
---
---