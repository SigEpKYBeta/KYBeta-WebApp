'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var exec = require('child_process').exec;

gulp.task('sass', function() {
  gulp.src('./source/static/sass/styles.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./source/static/css'));
});

gulp.task('sass:watch', function() {
  gulp.watch('./source/static/sass/styles.scss', ['sass']);
});

gulp.task('runserver', function() {
  var cmd = '. ../Python_Virtual_Env/SigEp/bin/activate';
  var proc = exec(cmd + ' && python source/manage.py runserver');
});
