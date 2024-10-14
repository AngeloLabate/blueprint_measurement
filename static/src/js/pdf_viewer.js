odoo.define('blueprint_measurement.pdf_viewer', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var registry = require('web.field_registry');

    var PDFViewer = AbstractField.extend({
        template: 'PDFViewer',
        events: _.extend({}, AbstractField.prototype.events, {
            'click .pdf-page': '_onPageClick',
        }),

        init: function () {
            this._super.apply(this, arguments);
            this.pdfData = [];
        },

        _render: function () {
            var self = this;
            this._super.apply(this, arguments);
            this.pdfData = JSON.parse(this.value || '[]');
            this.$el.empty();
            _.each(this.pdfData, function (page, index) {
                self.$el.append($('<div>', {
                    class: 'pdf-page',
                    'data-page': index,
                    text: 'Page ' + (index + 1),
                    css: {
                        width: page.width + 'px',
                        height: page.height + 'px',
                    }
                }));
            });
        },

        _onPageClick: function (ev) {
            var pageIndex = $(ev.currentTarget).data('page');
            // TODO: Implement page zoom and measurement tools
            console.log('Clicked on page', pageIndex);
        },
    });

    registry.add('pdf_viewer', PDFViewer);

    return PDFViewer;
});