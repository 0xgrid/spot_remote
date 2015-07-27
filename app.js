var exec = require('child_process').exec;
var spawn = require('child_process').spawn

var express = require('express');
var app = express();
var commands = 
{
play_pause:"python ./media_keys.py play_pause", 
vol_down:"python ./media_keys.py vol_down",
vol_up:"python ./media_keys.py vol_up",
next:"python ./media_keys.py next"
};

app.get('/', function (req, res) {
	res.send('Hello World!');
});

app.get('/play_pause', function (req, res) {
	exec(commands.play_pause)
	res.sendStatus(200);
});

app.get('/next', function (req, res) {
	exec(commands.next)
	res.sendStatus(200);
});

app.get('/vol_up', function (req, res) {
	exec(commands.vol_up)
	res.sendStatus(200);
});

app.get('/vol_down', function (req, res) {
	exec(commands.vol_down)
	res.sendStatus(200);
});

app.get('/test', function (req, res) {
	exec('python ./test.py play_pause');
	res.sendStatus(200);
});



var server = app.listen(3000, function(){
	var host = server.address().address;
	var port = server.address().port;
	console.log ('Example app listening at http://%s:%s', host, port);
})