var gulp = require('gulp'),
    plugins = require('gulp-load-plugins')();

gulp.task('build-tests', function() {
    var source = [
        './syntropy/manage/static/fulfillment_house/tests/test.js'
    ];

    return gulp.src(source)
        .pipe(plugins.browserify({debug: true}))
        .pipe(gulp.dest('./syntropy/manage/static/fulfillment_house/tests/build'));
});
