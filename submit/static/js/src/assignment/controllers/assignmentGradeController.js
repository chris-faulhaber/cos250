var AssignmentGrades = require('../collections/assignmentGrades');
var Q = require('q');

module.exports = function(){
    this.getAssignmentGrades = function(id){
        var deferred = Q.defer();
        var grades = new AssignmentGrades();
        grades.fetch({
            url: '/api/assignment/grades/find/' + id,
            success: function(){
                deferred.resolve(grades);
            }
        });

        return deferred.promise;
    }
};