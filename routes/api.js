const express = require ('express');
const router = express.Router();

// get list of data from db
router.get('/hikers', function(req, res) {
    res.send('GET');
});

// create and add new hiker to db
router.post('/hikers', function(req,res) {
    res.send('POST');
})

// update hiker in db
router.put('hikers/:id', function(req,res) {
    res.send('PUT');
})

// delete hiker from db
router.delete('hikers/:id', function(req,res) {
    res.send('DELETE');
})

module.exports = router;