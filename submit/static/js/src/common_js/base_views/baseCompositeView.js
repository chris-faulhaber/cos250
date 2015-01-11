var _ = require('lodash');
var Backbone = require('backbone');
var Rivets = require('rivets');

module.exports = Backbone.Marionette.CompositeView.extend({
    // override to call Rivet bindings before rendering children, to keep your grubby hands off their bindings
    render: function() {
        this._ensureViewIsIntact();
        this.isRendered = true;
        this.resetChildViewContainer();

        this.triggerMethod('before:render', this);

        this._renderTemplate();

        this.binding = Rivets.bind(this.el, _.result(this, 'bindingContext'));

        this._renderChildren();

        this.triggerMethod('render', this);
        return this;
    },

    onClose: function() {
        if (this.binding) {
            this.binding.unbind();
        }
    },

    bindingContext: function() {
        return {
            collection: this.collection,
            model: this.model,
            view: this,
            viewModel: this.viewModel
        };
    }
});