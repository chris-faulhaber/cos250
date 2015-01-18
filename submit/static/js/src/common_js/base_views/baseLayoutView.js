var _ = require('lodash');
var Backbone = require('backbone');
var Rivets = require('rivets');

module.exports = Backbone.Marionette.LayoutView.extend({
    onRender: function() {
        this.binding = Rivets.bind(this.el, _.result(this, 'bindingContext'));
    },

    onClose: function() {
        if (this.binding) {
            this.binding.unbind();
        }
    },

    bindingContext: function() {
        return {
            model: this.model,
            view: this,
            viewModel: this.viewModel
        };
    }
});