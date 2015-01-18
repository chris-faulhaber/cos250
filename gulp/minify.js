'use strict';

var gulp = require('gulp'),
    plugins = require('gulp-load-plugins')(),
    uglify = require('gulp-uglify'),
    log = require(__dirname + '/modules/logger'),
    handleError = require(__dirname + '/modules/handler'),
    argv = require('yargs').argv,
    jsConfig = require(__dirname + '/config/jsSettings.json');


gulp.task('minify-js', function () {
    var source = jsConfig.buildDirectory;

    return gulp.src(source)
        .pipe(uglify().on('error', handleError))
        .pipe(plugins.tap(function (file) {
            log('gulp minify-js ' + file.path, argv.verbose);
        }))
        .pipe(gulp.dest(jsConfig.minDirectory))
        .on('error', handleError);
});
