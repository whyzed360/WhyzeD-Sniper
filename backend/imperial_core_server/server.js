const http = require('http');

// Imperial Server Configuration
const hostname = '127.0.0.1';
const port = 8080;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('WHYZED EMPIRE: SOVEREIGN NODE ONLINE\nStatus: Independent\n');
});

server.listen(port, hostname, () => {
  console.log(`[LOG] Sovereign Server running at http://${hostname}:${port}/`);
  console.log(`[LOG] Access this via ACode or Termux browser modules.`);
});
