const fs = require('fs');
const path = require('path');

const USERS_FILE = path.join(__dirname, 'users.json');

function registerUser(emperorId, securityKey) {
    let users = JSON.parse(fs.readFileSync(USERS_FILE, 'utf8'));
    
    // Check if ID already exists
    if (users.find(u => u.id === emperorId)) {
        console.log(`[ALERT] ID ${emperorId} is already claimed in the Empire.`);
        return;
    }

    users.push({
        id: emperorId,
        key: securityKey,
        joined: new Date().toISOString(),
        status: 'Free_Trial'
    });

    fs.writeFileSync(USERS_FILE, JSON.stringify(users, null, 2));
    console.log(`[SUCCESS] New Recruit Authenticated: ${emperorId}`);
}

// Example usage (this will be called by your App's 'Authenticate' button later)
const args = process.argv.slice(2);
if (args.length === 2) registerUser(args[0], args[1]);
