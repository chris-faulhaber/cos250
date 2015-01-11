var Backbone = require('backbone');
var Marionette = require('backbone.marionette');
var Radio = require('backbone.radio');
var Q = require('q');

var AssignmentApp = new Marionette.Application();

//collections
var Assignments = require('../collections/assignments');

//regions
var AssignmentRegion = require('../regions/assignmentsRegion');

//Rivets
var create_custom_rivets_formatters = require('../../common_js/utils/create_custom_rivets_formatters');
var configure_rivets = require('../../common_js/utils/configure_rivets');

/** I need this in order to render the templates with rivets */
var create_backbone_rivets_adapter = require('../../common_js/utils/create_backbone_rivets_adapter');

AssignmentApp.addInitializer(function appInit() {
    var deferred = Q.defer();
    var assignments = new Assignments();
    assignments.fetch({
        success: function(){
            deferred.resolve();
        }
    }).then(function(){
        Radio.channel('assignmentsChannel').trigger('assignments_initialized', assignments)
    });

});

AssignmentApp.addInitializer(function historyInit() {
    if (Backbone.history) {
        Backbone.history.start();
    }
});

AssignmentApp.addRegions({
    AssignmentRegion: {
        el: '#assignments',
        regionClass: AssignmentRegion
    }
});

module.exports = AssignmentApp;