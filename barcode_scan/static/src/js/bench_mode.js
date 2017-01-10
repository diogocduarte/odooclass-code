odoo.define('barcode_scan.bench_mode', function (require) {
"use strict";

var core = require('web.core');
var Model = require('web.Model');
var Widget = require('web.Widget');
var Session = require('web.session');
var BarcodeHandlerMixin = require('barcodes.BarcodeHandlerMixin');

var QWeb = core.qweb;
var _t = core._t;


var BenchMode = Widget.extend(BarcodeHandlerMixin, {
    className: 'o_barcode_scan_bench',

    events: {
    },

    init: function (parent, action) {
        // Note: BarcodeHandlerMixin.init calls this._super.init, so there's no need to do it here.
        // Yet, "_super" must be present in a function for the class mechanism to replace it with the actual parent method.
        this._super;
        BarcodeHandlerMixin.init.apply(this, arguments);
    },

    start: function () {
        var self = this;
        self.session = Session;
        var res_company = new Model('res.company');
        res_company.query(['name'])
           .filter([['id', '=', self.session.company_id]])
           .all()
           .then(function (companies){
                self.company_name = companies[0].name;
                self.company_image_url = self.session.url('/web/image', {model: 'res.company', id: self.session.company_id, field: 'logo',})
                self.$el.html(QWeb.render("BarcodeScannerBench", {widget: self}));
            });
        return self._super.apply(this, arguments);
    },

    on_barcode_scanned: function(barcode) {
        var self = this;
        var product_obj = new Model('product.product');

        product_obj.call('product_scan', [barcode, ])
            .then(function (result) {
                if (result.warning) {
                    self.show_line(result.warning);
                }
            });
    },

    show_line: function(text) {
        this.$('.o_barcode_scan_bench_mode').append("<h2>" + text + "</h2>");
    },

    destroy: function () {
        clearInterval(this.clock_start);
        this._super.apply(this, arguments);
    },
});

core.action_registry.add('barcode_scan_bench_start', BenchMode);

return BenchMode;

});
