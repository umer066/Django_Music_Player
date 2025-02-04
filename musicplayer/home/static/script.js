var audio = {
    init: function () {
        var $that = this;
        document.addEventListener('DOMContentLoaded', function() {
            if ($that.components && typeof $that.components.media === 'function'){
                $that.components.media();
            }
        });
    },
    
    components: {

        media: function (target) {

            var media = $('audio.fc-media', target || 'body');

            if (media.length) {
                media.mediaelementplayer({
                    audioHeight: 50,
                    features: ['playpause', 'current', 'duration', 'progress', 'volume', 'tracks', 'fullscreen'],
                    alwaysShowControls: true,
                    timeAndDurationSeparator: '<span></span>',
                    iPadUseNativeControls: true,
                    iPhoneUseNativeControls: true,
                    AndroidUseNativeControls: true
                });
            }
        },

    },
};

audio.init();





