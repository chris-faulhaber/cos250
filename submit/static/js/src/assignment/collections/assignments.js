var Backbone = require('backbone');
var Assignment = require('../models/assignment');

module.exports = Backbone.Collection.extend({
    url: '/api/assignments',
    model: Assignment
});