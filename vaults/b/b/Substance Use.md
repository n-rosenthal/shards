# `= this.file.name`
## âmbar
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

---

---

