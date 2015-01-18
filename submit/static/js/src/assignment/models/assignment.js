var Backbone = require('backbone');
require('backbone-relational');
var _ = require('underscore');
var Part = require('./part');
var Parts = '../collections/parts';

module.exports = Backbone.Model.extend({
    url: 'api/assignment/'
});