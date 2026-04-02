const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();
const PORT = 3000;

// enable cross origin requests
app.use(cors());

// serve APK files
app.use("/apps", express.static(path.join(__dirname, "apps")));

// serve icons
app.use("/icons", express.static(path.join(__dirname, "icons")));

// serve repository file
app.get("/repo.json", (req, res) => {
    res.sendFile(path.join(__dirname, "repo.json"));
});

app.listen(PORT, () => {
    console.log("WhyzeD App Repository running at:");
    console.log("http://localhost:" + PORT + "/repo.json");
});
