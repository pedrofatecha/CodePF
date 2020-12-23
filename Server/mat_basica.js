var express= require('express');

var app =  express();

exports.product = function(a,b){return a*b};
exports.sum = function(a,b){return a+b};
