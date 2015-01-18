var _ = require('lodash');
var Backbone = require('backbone');
var Rivets = require('rivets');
var Modal = require('backbone-modal');

module.exports = Backbone.Modal.extend({
    render: function() {
        Backbone.Modal.prototype.render.call(this);
        this.binding = Rivets.bind(this.el, _.result(this, 'bindingContext'));
    },

    remove: function() {
        Backbone.Modal.prototype.remove.call(this);
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