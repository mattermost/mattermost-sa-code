const WebSocket = require('ws');

var ws = new WebSocket("ws://server/api/v4/websocket");

ws.on('open', function open(){
  var msg = {
  "seq": 1,
  "action": "authentication_challenge",
  "data": {
    "token": "token"
    }
  };
  ws.send(JSON.stringify(msg));
});

ws.onmessage = function (event) {
  var sortedKeys = Object.keys(event).sort();;
  var obj = JSON.parse(event.data);
  console.log(event.data);
  if(obj.event == "channel_created"){
    console.log("New channel created...")
    UserAction();
  }
  else if (obj.event == "channel_viewed") {
    console.log("Channel was viewed...")
  }
}

function UserAction() {
  var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function() {
    console.log("State: " + this.readyState);
    if (this.readyState === 4) {
      console.log("Complete.\nBody length: " + this.responseText.length);
      console.log("Body:\n" + this.responseText);
      }
    };

    xhr.open("POST", "https://httpbin.org/post");
    xhr.send();
    }
