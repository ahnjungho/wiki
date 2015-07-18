module.exports = function(grunt) {
  grunt.initConfig({

    sass: {
      options: {
        sourceMap: true
      },
      dist: {
        files: {
          'static/stylesheets/main.css': 'static/stylesheets/main.scss'
        }
      }
    },
    watch: {
      css: {
        files: '**/*.scss',
        tasks: ['sass']
      }
    }

  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['watch']);

};

