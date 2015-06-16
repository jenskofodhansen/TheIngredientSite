$(function() {
	$("#search_ingredient").autocomplete({
		source: "/api/get_ingredients",
		minLength: 3,
	});
});