var Backbone = require('backbone');
require('backbone-relational');

module.exports = Backbone.Model.extend({
    url: '/api/part'
});