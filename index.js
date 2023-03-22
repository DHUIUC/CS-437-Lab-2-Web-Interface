const { send } = require('process');

var server_port = 65432;
var server_addr = "192.168.1.3";   // the IP address of your Raspberry PI

function client(sendData){
    
    const net = require('net');

    //Data sanitization? will be making a server call

    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${sendData}\r\n`);
    });
    
    // get the data from the server
    client.on('data', (data) => {
        if (sendData === 'minus' || sendData === 'plus'){
            document.getElementById("litSpeed").innerHTML = data;
            document.getElementById("litCarSpeed").innerHTML = data;
        } else if (sendData === 'temp'){
            document.getElementById("litCarTemp").innerHTML = data;
        } else if (sendData === 'battery'){
            document.getElementById("litCarBat").innerHTML = data;
        }
        console.log(data.toString());
        client.end();
        client.destroy();
    });

    client.on('end', () => {
        console.log('disconnected from server');
    });
}

function move(direction){

    // get the element from html
    //var name = document.getElementById("myName").value;
    // update the content in html
    document.getElementById("litCarDir").innerHTML = direction;
    if (direction === 'left' || direction === 'right'){
        document.getElementById("litCarTurning").innerHTML = 'Yes';
    } else {
        document.getElementById("litCarTurning").innerHTML = 'No';
    }
    // send the data to the server 
    //to_server(name);
    client(direction);
    getStatus();
}

function speed(step){
    client(step);
    getStatus();
}

function getStatus(){
    client("temp");
    client("battery");
}

