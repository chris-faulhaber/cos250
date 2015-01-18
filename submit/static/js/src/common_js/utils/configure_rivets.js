var Rivets = require('rivets');

module.exports = function() {
    // This passes the observed object as 'this', effectively making click callbacks sticky
    Rivets.configure({
        handler: function(context, ev, binding) {
            this.call(binding.model, context, ev, binding);
        }
    });
};