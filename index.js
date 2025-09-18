const express = require('express');
// set up express app

const app = express();

// initialize routes
app.use('/api', require('./routes/api'));
// handle requests
//app.get('/', function(req, res) {
   // console.log('GET requests');
   // res.send({name: 'Nylah'});
//});
// listen on port 4000 for requests
app.listen(process.env.PORT || 4000, function() {
    console.log('Server is now listening for requests...');
});