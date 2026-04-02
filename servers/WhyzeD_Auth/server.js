const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// THE AGGREGATION ENGINE
// In production, these functions will fetch real data from YT/FB/X APIs
const getPlatformStats = () => {
  const ytViewers = Math.floor(Math.random() * 20); // YouTube Live
  const fbViewers = Math.floor(Math.random() * 15); // Facebook Live
  const xViewers = Math.floor(Math.random() * 10);  // X (Twitter) Live
  
  return ytViewers + fbViewers + xViewers;
};

// ENDPOINT: LIVE AUDIENCE MONITOR
app.get('/api/stats', (req, res) => {
  const totalGlobalViewers = getPlatformStats();
  res.json({ 
    live_count: totalGlobalViewers,
    status: "UPLINK_ACTIVE",
    origin: "BAYELSA_HQ"
  });
});

// ENDPOINT: OTP DELIVERY (Mock for now)
app.post('/send-otp', (req, res) => {
  const { email } = req.body;
  console.log(`[AUTH] Generating OTP for: ${email}`);
  res.json({ success: true, message: "OTP Dispatched via WhyzeD Registry" });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`-----------------------------------------`);
  console.log(` WHYZED AGGREGATOR ONLINE : PORT ${PORT} `);
  console.log(` LOCATION: BAYELSA STATE HQ NODE        `);
  console.log(`-----------------------------------------`);
});
