const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const NodeMediaServer = require('node-media-server');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

// --- WHYZED MEDIA CONFIG ---
// This handles the routing of RTMP streams from User -> Empire -> Social Media
const nmsConfig = {
  rtmp: {
    port: 1935,
    chunk_size: 60000,
    gop_cache: true,
    ping: 30,
    ping_timeout: 60
  },
  http: {
    port: 8000,
    allow_origin: '*'
  }
};

const nms = new NodeMediaServer(nmsConfig);
nms.run();

io.on('connection', (socket) => {
  console.log('[CORE] New User Connected to Uplink');

  socket.on('initiate_uplink', (data) => {
    // data.sourceUrl (e.g. user web stream)
    // data.streamKey (e.g. YouTube Key)
    console.log(`[CORE] Routing User Stream: ${data.sourceUrl} -> Target Key: ${data.streamKey}`);
    
    // Future Logic: Check 'WhyzeD Central Bank' for active subscription
    // If free_trial: Proceed. If expired: Block.
  });
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`[SYSTEM] WhyzeD Imperial Server running on Port ${PORT}`);
});
