var gulp = require('gulp'),
    plugins = require('gulp-load-plugins')();

gulp.task('build', function() {
    var source = [
        './submit/static/js/src/assignment/assignment.js'
    ];

    return gulp.src(source)
        .pipe(plugins.browserify({debug: true}))
        .pipe(gulp.dest('./submit/static/js/build'));
});

