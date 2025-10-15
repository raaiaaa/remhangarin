self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open('projectsite-cache-v1').then(function(cache) {
                return cache.addAll([
                    '/',
                    '/static/css/bootstrap.min.css',
                    '/static/css/sb-admin-2.min.css',
                    '/static/vendor/fontawesome-free/css/all.min.css',
                    '/static/vendor/jquery/jquery.min.js',
                    '/static/vendor/bootstrap/js/bootstrap.bundle.min.js',
                    '/static/vendor/jquery-easing/jquery.easing.min.js',
                    '/static/js/sb-admin-2.min.js',
                    '/static/img/clipboard-icon.png'
                ]);
            })
        );
    });

self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});