var config = {
    app: 'src',
    tpjsdist: "lpcoll/static/scripts/3p/",
    tpcssdist: "lpcoll/static/stylesheets/3p/",
    tpfontsdist: "web/css/fonts/",
    tpimagesdist: "web/images/3p/",
    web: "./web"
}


module.exports = function (grunt) {

    //grunt.loadNpmTasks('grunt-html');

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        config: config,
        
        clean: [
            config.tpjsdist, 
            config.tpcssdist, 
            config.tpfontsdist, 
            config.tpimagesdist
        ],

        htmllint: {
            all: ["web/**/*.html"]
        },
        
        copy: {
            dist: {
                files: [
                    // ************************ jquery
                    {  // js
                        expand: true,
                        cwd: 'bower_components/jquery/dist/',
                        src: '*.min.js',
                        dest: '<%= config.tpjsdist %>'
                    },
                    // ************************ angularjs
                    {  // js
                        expand: true,
                        cwd: 'bower_components/angularjs/',
                        src: '*.min.js',
                        dest: '<%= config.tpjsdist %>'
                    }
              ]
            }
        }
    });


    // Load the plugin that provides the "uglify" task.
    //grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.loadNpmTasks('grunt-contrib-copy');

    // clean
    grunt.loadNpmTasks('grunt-contrib-clean');
    
    // Default task(s).
    grunt.registerTask('default', ['copy']);

};