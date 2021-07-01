$(function() {
	/*index*/
	$('.module3 .company').hover(function(){
			$(this).find('.score').stop(true,true).fadeToggle(200);
		});

	/*banner imgslide*/
    var unslider2 = $('.imgslide2').unslider({
		speed: 500,               //  The speed to animate each slide (in milliseconds)每张幻灯片动画的速度（以毫秒为单位）
		                 //  The delay between slide animations (in milliseconds)幻灯片动画之间的延迟（以毫秒为单位）
		complete: function() {},  //  A function that gets called after every slide animation每次滑动动画
		keys: true,               //  Enable keyboard (left, right) arrow shortcuts启用键盘（左、右）箭头快捷键
		dots: false,               //  Display dot navigation显示点导航
		fluid: false              //  Support responsive design. May break non-responsive designs持响应式设计。可能会破坏非响应式设计
	});
    $('.unslider-arrow2').click(function() {
        var fn = this.className.split(' ')[1]; //根据classname要么是prev要么是next
        unslider2.data('unslider')[fn]();
    });



    $('#jsDemandBtn').on('click', function(){
        perfect_demand_form_submit({
            jsPerfectSubmit: this,
            jsPerfectForm: '#jsDemandForm',
            jsPerfetTips:'#jsDemandTips',
            isIndex: 'index'
        });
    });

});

