var Backbone = require('backbone');
var BaseCompositeView = require('../../common_js/base_views/baseCompositeView');
var AssignmentGradeView = require('./assignmentGradeItemView');
var Template = require('../templates/assignmentGradesTable.html');

module.exports = BaseCompositeView.extend({
    tagName: 'div',
    childView: AssignmentGradeView,
    childViewContainer: '.children',
    template: Template,

    initialize: function(){
        var self = this;
        if (this.collection.models.length > 0){
             self.assignmentName = self.collection.models[0].get('assignment').description
        }else{
            self.assignmentName = 'No grades for this assignment';
        }
        return this;
    }
});