module.exports = {
    title: async (tp) => await tp.system.prompt("nome"),
    time: async (tp) => await tp.system.prompt("(YYYY-MM-DDTHH:mm)", tp.date.now("YYYY-MM-DDTHH:mm")),
    category: async (tp) => await tp.system.prompt("categoria"),
    notes: async (tp) => await tp.system.prompt("notas?")
}
