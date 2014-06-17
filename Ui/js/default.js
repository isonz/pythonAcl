var mainurl = 'http://py.ison.com';
$(document).ready(function() {
	$.ajaxf.install('js/Ajax.swf'); 
	auth();
});

//此设置可以从外部应用中读取
var config = {
'jspath': 'js/',
'modules':[
	['computer', '计算机', 'ci/admins/demo', 20, 20],	//URL为此模块的入口URL，该模块所有操作通过此URL带参数。
	['network', '网络', 'ci/admins/demo', 20,120]
]
};

function auth(){
	$.getJSON(mainurl+'/?callback=?', function(data){
		if('0'!= data.error){
			$('#desktop').append(winBoxSimple('login', '登入', 'mainurl', 'login', 500, 300, 0));
			//$('#desktop').append(msgWinBox('msg1', '消息', 400, 200));
			$('#desktop').css('bottom',0);
			$('#window_login .float_right').hide();
			$('#window_login .window_content').html(data.html);
			$('#loginbutton').click(function(){
				$.ajaxf.post(mainurl+$(this).attr('data'), 'username='+$('#username').val()+'&password='+$('#password').val(), function(rs){
					console.log(rs);									  
				},'json');
			});
		}else{
			init(config);
		}
	});
}