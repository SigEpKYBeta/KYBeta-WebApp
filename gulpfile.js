'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var exec = require('child_process').exec;

gulp.task('sass', function() {
  gulp.src('./source/static/sass/styles.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./source/static/css'));
});

gulp.task('runserver', function() {
  var cmd = '. ./SigEpEnv/bin/activate';
  var proc = exec(cmd + ' && python source/manage.py runserver');
});

gulp.task('default', function() {
    gulp.watch('./source/static/sass/*.scss', ['sass']);
});
