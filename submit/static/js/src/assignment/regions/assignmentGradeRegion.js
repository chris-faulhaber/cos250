var Marionette = require('backbone.marionette');
var Radio = require('backbone.radio');
var channel = Radio.channel('gradesChannel');

var GradeController = require('../controllers/assignmentGradeController');
var AssignmentGradesView = require('../views/assignmentGradesCollectionView');

module.exports = Marionette.Region.extend({
    initialize: function(){
        channel.on('show_grades', function(id){
            this.showGrades(id)
        }, this);
    },

    showGrades: function(id){
        var self = this;
        var controller = new GradeController();
        controller.getAssignmentGrades(id)
            .then(function(grades){
                self.show(new AssignmentGradesView({collection: grades}))
            });
    }
});