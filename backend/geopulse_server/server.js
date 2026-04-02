const express = require('express');
const { spawn } = require('child_process');
const app = express();
app.use(express.json());

app.post('/track', (req, res) => {
    const { userId, lat, lng, speed } = req.body;
    
    // Trigger AI Python Script
    const py = spawn('python3', ['../ai_engine/engine.py']);
    py.stdin.write(JSON.stringify({ lat, lng, speed }));
    py.stdin.end();

    py.stdout.on('data', (data) => {
        const result = JSON.parse(data);
        res.json({
            status: "success",
            message: "Location logged",
            prediction: result.prediction,
            anomaly: result.anomaly
        });
    });
});

app.listen(3000, () => console.log('GeoPulse Backend running on port 3000'));
