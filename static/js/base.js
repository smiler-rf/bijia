//显示/隐藏城市列表
$(document).ready(function () {
	$(".city-selected").hover(function(){
		$(".city-list").css('display', 'block');
		$(".city-container").addClass("active");
	},(function(){
		$(".city-list").css('display', 'none');
		$(".city-container").removeClass("active");
	}));

	$(".city-list").hover(function(){
		$(".city-list").css('display', 'block');
		$(".city-container").addClass("active");
	},(function(){
		$(".city-list").css('display', 'none');
		$(".city-container").removeClass("active");
	}))
});