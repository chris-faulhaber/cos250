var Marionette = require('backbone.marionette');
var Radio = require('backbone.radio');
var channel = Radio.channel('assignmentsChannel');

var AssignmentsView = require('../views/assignmentCollectionView');

module.exports = Marionette.Region.extend({
    initialize: function(){
        channel.on('assignments_initialized', function(assignments){
            this.showAssignments(assignments)
        }, this);
    },

    showAssignments: function(assignments){
        this.show(new AssignmentsView({collection: assignments}))
    }
});