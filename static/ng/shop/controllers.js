angular.module('shop.controllers', [
  'common.resources',
  'shop.directive'
])
.controller('StoreSelect', function($scope, FruitexAPI) {
  FruitexAPI.stores.get().$promise
  .then(function(res) {
    $scope.stores = res.results;
  });
})
.controller('StoreHome', function($scope, $stateParams, FruitexAPI, $log){
  var slug = $stateParams.slug;
  $scope.store = {
    slug: slug
  };
});
