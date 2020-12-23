var express = require(`express`);
var router = express.Router();

router.get('/',function(req,res){
    res.send(`Admin Ini`);
});


router.get('/users',function(req,res){
    res.send(`User in system`);
});

module.exports = router;

