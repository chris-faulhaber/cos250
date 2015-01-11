var Backbone = require('backbone');
var BaseCollectionView = require('../../common_js/base_views/baseCollectionView');
var AssignmentItemView = require('./assignmentItemView');

module.exports = BaseCollectionView.extend({
    childView: AssignmentItemView
});