let app = require("express")();
let port = 3000;

app.get("/", function(req, res) {
    console.log("En klient anslöt!");
    res.sendFile(__dirname + "/klient.html");
});

let httpServer = app.listen(port, () => {
    console.log(`Webbserver körs på port ${port}`)
});

let io = require('socket.io')(httpServer);

io.on("connection", function(socket) {
    socket.on("click", function() {
        console.log("Någon klickade!");
    });
});