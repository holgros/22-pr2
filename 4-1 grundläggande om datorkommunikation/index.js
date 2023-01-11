let app = require('express')();
let port = 3000;

app.get("/", function(req, res) {
    console.log("En klient anslöt!");
    res.sendFile(__dirname + "/klient.html");
});

app.listen(port, () => {
    console.log(`Webbserver körs på port ${port}`)
});

/*
let http = require('http').Server(app);
let io = require('socket.io')(http);
app.use('/public', express.static(__dirname + '/public' ));

io.on("click", function() {
    console.log("Någon klickade!");
});
*/