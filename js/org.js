var app = angular.module('orgApp',['ngRoute','ngAnimate','ngMaterial']);
//app.controller('indexToolbarCtrl',['$scope','$http','$rootScope','$location','UserDetails','$mdDialog',function($scope,$http,$rootScope,$location,UserDetails,$mdDialog){
//    console.log("User Details ",UserDetails.getUserDetails());
//    UserDetails.isAuthenticated.then(
//        function(auth) {
//            console.log("Header Frame resolved user name = "+ auth.userName);
//            $scope.firstName= auth.firstName;
//            $scope.lastName= auth.lastName;
//            $rootScope.userId = auth.userId;
//            $rootScope.userLevel = auth.userLevel;
//        }
//    );
//    $scope.logout = function() {
//        $rootScope.login=false;
//        console.log("Try to logout");
//        $http.post('/py/logout',{}).
//        success(function(data, status, headers, config) {
//                var user = {};
//                user.userName = "";
//                user.userLevel = -2;
//                user.dept = "";
//                location.reload();
//                if (data.result == "OK") {
//                    console.log("SUCCESS");
//                    UserDetails.setDetail(user);
//                    $location.path("/login");
//                } else {
//                    console.log("LOGOUT FAILED");
//                }
//        }).
//        error(function(data, status, headers, config) {
//            console.log("LOGOUT ERROR");
//        });
//     };
//
//    console.log("User Details new",UserDetails);
//}]);
app.controller('userCtrl', ['$scope', '$http', '$location','$rootScope','$mdDialog','$window','$mdToast',function($scope, $http, $location, $rootScope,$mdDialog,$window,$mdToast) {
    //$rootScope.login = true;
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

