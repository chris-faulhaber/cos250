var BaseItemView = require('../../common_js/base_views/baseItemView');
var template = require('../templates/assignment_grade_item.html');

module.exports = BaseItemView.extend({
    template: template,
    tagName: 'tr',

    initialize: function(){
        var user = this.model.get('user');
        var fullName = user.first_name + " " + user.last_name;
        var assignment = this.model.get('assignment');
        this.model.set('fullName', fullName);
    }
});