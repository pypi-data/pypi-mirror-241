/* global CKEDITOR */

$(document).ready(() => {
    'use strict';

    if ('undefined' !== typeof CKEDITOR) {
        $('form').on('reset', (e) => {
            if ($(CKEDITOR.instances).length) {
                for (let key in CKEDITOR.instances) {
                    if ({}.hasOwnProperty.call(CKEDITOR.instances, key)) {
                        const instance = CKEDITOR.instances[key];

                        if ($(instance.element.$).closest('form').attr('name') === $(e.target).attr('name')) {
                            instance.setData(instance.element.$.defaultValue);
                        }
                    }
                }
            }
        });
    }
});
