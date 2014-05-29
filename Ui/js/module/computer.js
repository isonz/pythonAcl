var computer = {
	box: '#window_computer',
	url: config.modules[0][2],
	currentUrl: '',
	
	init: function(){
		this.aside();
		this.main();
		this.bottom();
	},
	aside:function(){
		$("#demo_search_btn").click(function(){
			var val = $("#demo_keyword").val();
			var url = computer.url+"?op=search&keyword="+val;
			$.getJSON(url,function(data){
		       	$(computer.box+" .window_main").html(data.main);
		       	$(computer.box+" .window_bottom").html(data.bottom);
		       	computer.main();
		       	computer.bottom();
			});
			computer.currentUrl = url;
		});
			
	},
	main:function(){
		d = $(document);
		var url = computer.url+"?op=view";
		d.on(clicker, computer.box+" .window_main .data tr", function() {
			var id = $(this).children("td").children("input").val();
			var title = $(this).children("td").next().html();
			$.getJSON(url,function(data){
				var box = '#window_comouter_view'+id;
				url = url+id;
				var elem = $(box);
				if(elem.length<1){
					$('#desktop').append(initWinBox('comouter_view'+id, title, url, 'view')); //生成新的窗口
					elem = $('#window_comouter_view'+id);
				}
				elem.addClass("window_stack");
				elem.show();
				$("#icon_dock_comouter_view"+id).show();
				
				computer.view(data, box, url);
			});
		});
	},
	bottom:function(){
		var a = $(computer.box+" .window_bottom a");
		a.click(function(){
			var page = $(this).attr('href').replace("#p",'');
			var url = computer.currentUrl!='' ? computer.currentUrl+"&page="+page : computer.url+"?page="+page;
			$.getJSON(url,function(data){
		       	$(computer.box+" .window_main").html(data.main);
		       	computer.main();
			});
		});
	},
	view:function(data, box, url){
		//console.log(data,box,url);
		$(box+" .window_main").html(data.main);
	}
};

computer.init();
