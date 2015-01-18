var Backbone = require('backbone');
var AssignmentGrade = require('../models/assignmentGrade');

module.exports = Backbone.Collection.extend({
    url: 'api/assignment/grades/find',
    model: AssignmentGrade
});