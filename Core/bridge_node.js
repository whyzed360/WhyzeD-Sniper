const { exec } = require('child_process');

// Function to call your Python Sniper logic
function executeTradeSignal(headline, price) {
    exec(`python3 ../Finance/injection.py "${headline}" ${price}`, (error, stdout) => {
        if (error) console.error(`Imperial Error: ${error}`);
        console.log(`Z-Signal Output: ${stdout}`);
    });
}
