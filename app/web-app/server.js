const express = require('express');
const app = express();
const port = 3000;

// Allow serving static files from 'public' directory
app.use(express.static('public'));


app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
