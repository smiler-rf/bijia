window.onload = function(){
	load();
	var shows = document.getElementsByClassName('show-list');
	var movies = document.getElementsByClassName( 'movie');
	var mCount = movies.length;
	document.querySelector('city-name');
	shows[0].className = "show-list active";
	movies[0].className = "movie active";
	/**********************轮播图*********************/
	var oLeft = document.getElementsByClassName('scroll-prev')[0]; //左按钮
	var oRight = document.getElementsByClassName('scroll-next')[0]; //右按钮
	var mList = document.getElementsByClassName('movie-list')[0]; //里面有所有的图片
    var iWidth = 175;
    var lenthLi = (mCount - 7) * (iWidth - 5);

	oLeft.onmouseover = oRight.onmouseover = function(){
		// this.className = 'hover';
		//点击左侧按钮
		oLeft.onclick = function(){
			var location = mList.offsetLeft + (iWidth - 10);
			rMove(mList, 'left', location); //右移
		};
		//点击右侧按钮
		oRight.onclick = function(){
			var location = mList.offsetLeft - iWidth;
			lMove(mList, 'left', location, lenthLi); //左移
		};
	};

	$('.city-list li a').hover(function () {
		$(this).css('color','white');
		$(this).css('background','red');
	},function () {
		$(this).css('color','black');
		$(this).css('background','white');
	});

};

function lMove(obj, attr, onEnd, lenthLi){
    if (onEnd < -lenthLi){
    	//克隆第一个子元素并添加，然后删除第一个子元素
		var parent = document.getElementsByClassName('movie-list')[0];
		parent.appendChild(parent.firstElementChild.cloneNode(true));
		parent.removeChild(parent.firstElementChild);
		//将show-list做同样操作
		var num = $('.show-list').length;
		$('.show-list').eq(num-1).after($('.show-list').eq(0).clone(true));
		$('.show-list').eq(0).remove();

		onEnd = -lenthLi;
    }
	obj.style[attr] = onEnd +'px';

    load();
}
function rMove(obj, attr, onEnd){
	if(onEnd > 0){
		//克隆最后一个子元素并添加作为第一个子元素，然后删除最后一个子元素
		var parent = document.getElementsByClassName('movie-list')[0];
		parent.insertBefore(parent.lastElementChild.cloneNode(true), parent.firstElementChild);
		parent.removeChild(parent.lastElementChild);

		var num = $('.show-list').length;
		$('.show-list').eq(0).before($('.show-list').eq(num-1).clone(true));
		$('.show-list').eq(num).remove();

		onEnd = 0
	}
	obj.style[attr] = onEnd +'px';

	load();
}

//点击电影后图片放大、显示电影详情、城市列表替换
function load() {
	$(".movie").click(function () {
		var shows = document.getElementsByClassName('show-list');
		var movies = document.getElementsByClassName('movie');
		var index = $(this).index();
		console.log("index:", index);
		for (var j = 0; j < movies.length; j++) {
			movies[j].className = 'movie';
			shows[j].className = 'show-list';
		}
		movies[index].className = 'movie active';
		shows[index].className = 'show-list active';
	})
}