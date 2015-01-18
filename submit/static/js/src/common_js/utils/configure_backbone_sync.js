var Backbone = require ('backbone');

var oldBackboneSync = Backbone.sync;
Backbone.sync = function( method, model, options ) {
    // delete request WITH data
    if ( method === 'delete' && options.data ) {
        options.data = JSON.stringify(options.data);
        options.contentType = 'application/json';
    } // else, business as usual.
    return oldBackboneSync.apply(this, [method, model, options]);
};