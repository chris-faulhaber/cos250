'use strict';

var log = require(__dirname + '/logger');

module.exports = function handleError(err) {
    if(err) {
        log(err.message, true);
        throw err;
    }
};