$(document).ready(function() {
	auth();
});
var config = {
'jspath': 'js/',
'modules':[
	['computer', '计算机', 'ci/admins/demo', 20, 20],	//URL为此模块的入口URL，该模块所有操作通过此URL带参数。
	['network', '网络', 'ci/admins/demo', 20,120]
]
};
function auth(){
	$.getJSON('http://127.0.0.1:8080?callback=?', function(data){
		if('nologin' != data){
			$('#desktop').append(winBoxSimple('login', '登入', 'http://127.0.0.1:8080', 'login', 500, 300, 0));
			$('#desktop').css('bottom',0);
			$('#window_login .float_right').hide();
			$('#window_login .window_content').html(data);
			//$('#desktop').append(msgWinBox('msg1', '消息', 400, 200));
		}else{
			init(config);
		}
	});
}