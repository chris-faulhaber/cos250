'use strict';

var gulp = require('gulp')
    , runSequence = require('run-sequence');

gulp.task('build-all', function(callback) {
  runSequence('build',
              ['minify-js'], callback);
});
