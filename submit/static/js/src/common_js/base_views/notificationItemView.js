var Backbone = require('backbone');

var BaseItemView = require('./baseItemView');

var template = require('../base_templates/notification.html');

module.exports = BaseItemView.extend({
    tagName: "div",
    template: template,

    initialize: function(options){
        this.viewModel = new Backbone.Model();

        if (options.alertClass){
            this.viewModel.set('alertClass', options['alertClass'])
        }

        if (options.msg){
            this.viewModel.set('msg', options['msg'])
        }

        if (options.validationError){
            this.viewModel.set('notValid', true)
        }

        //Override default notification template
        if (options.template){
            this.template = options.template
        }
    }
});