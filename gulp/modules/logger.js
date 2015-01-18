'use strict';

var moment = require('moment')
    , fs = require('graceful-fs');

module.exports = function log(message, verbose) {
    var timestamp = moment.utc().format()
        , entry = '[' + timestamp + ']: ' + message;

    if(verbose) console.log(entry);

    fs.appendFile(__dirname + '/../logs/gulp.log', entry + '\n', function(err) {
        if(err) throw err;
    });
};