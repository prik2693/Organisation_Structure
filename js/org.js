var app = angular.module('orgApp',['ngRoute','ngAnimate','ngMaterial']);
app.controller('userCtrl', ['$scope', '$http', '$location','$rootScope','$mdDialog','$window','$mdToast',function($scope, $http, $location, $rootScope,$mdDialog,$window,$mdToast) {
        $http.post('/py/getUserOrg',{}).
        success(function(data, status, headers, config) {
                if (data.status == "OK") {
                     $scope.user_org_struct = data.data;
                } else {
                    console.log("FAILED");
                }
        }).
        error(function(data, status, headers, config) {
            console.log("ERROR");
        });
    $scope.getOrgStructure = function(){
        $http.post('/py/getOrgDetails',{organisationId:$scope.orgId}).
        success(function(data, status, headers, config) {
                if (data.status == "OK") {
                     $scope.org_struct = data.data;
                } else {
                    console.log("FAILED");
                }
        }).
        error(function(data, status, headers, config) {
            console.log("ERROR");
        });
    }
}]);

