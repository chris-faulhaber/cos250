'use strict';

var gulp = require('gulp')
    , plugins = require('gulp-load-plugins')();

require('require-dir')('./gulp');

gulp.task('help', function() {
    console.log('USAGE: gulp [task] --verbose\n\t--verbose (optional) logs additional info to STDOUT');
    return plugins.taskListing();
});

gulp.task('default', ['help']);