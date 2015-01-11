var Rivets = require('rivets');

module.exports = function() {
    Rivets.formatters['!'] = function(value) {
        return !value;
    };

    Rivets.formatters.renameRefactor = function(value){
        return value.replace(/_/g, ' ');
    }
};