var $ = require('jquery');
var Backbone = require('backbone');
Backbone.$ = $;

var fixCSRF = require('../common_js/utils/fix_csrf');

var AssignmentApp = require('./apps/assignmentApp');

$(function() {
    fixCSRF();
    AssignmentApp.start();
});