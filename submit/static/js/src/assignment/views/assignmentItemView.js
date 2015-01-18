var BaseItemView = require('../../common_js/base_views/baseItemView');
var template = require('../templates/assignment_item.html');
var Radio = require('backbone.radio');

module.exports = BaseItemView.extend({
    template: template,
    events: {
        "click #assignment": "getGrades"
    },

    getGrades: function(){
        var assignmentID = this.model.get('id');
        Radio.channel('gradesChannel').trigger('show_grades', assignmentID);
    }
});