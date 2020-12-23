var express = require(`express`);
var app = express();
var admin = require(`./admin.js`);
var express = require(`morgan`);

app.use('/admin', admin); 