var BaseItemView = require('../../common_js/base_views/baseItemView');
var template = require('../templates/assignment_item.html');

module.exports = BaseItemView.extend({
    template: template,

    getGrades: function(){
        console.log('test')
    }
});