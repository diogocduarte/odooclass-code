odoo.define('pos_member.member', function (require) {
"use strict";

var gui = require('point_of_sale.gui');
var models = require('point_of_sale.models');
var _super_posmodel = models.PosModel.prototype;

models.PosModel = models.PosModel.extend({
    initialize: function (session, attributes) {
        // New code
        var partner_model = _.find(this.models, function(model){
            return model.model === 'res.partner';
        });
        partner_model.fields.push('membership_code');

        var users_model = _.find(this.models, function(model){
            return model.model === 'res.users' && model.ids == null;
        });
        users_model.fields.push('login');

        // Inheritance
        return _super_posmodel.initialize.call(this, session, attributes);
    },
});

gui.Gui.prototype.screen_classes.filter(function(el) { return el.name == 'clientlist'})[0].widget.include({
    render_list: function (partners) {
        var self = this;
        this._super.apply(this, arguments);
        //console.debug('--------------- RENDER LIST');
    },
    display_client_details: function (visibility, partner, clickpos) {
        var self = this;
        this._super.apply(this, arguments);
        //console.debug('--------------- TEST --- ');
    }
});

});
