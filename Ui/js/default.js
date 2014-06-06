$(document).ready(function() {
	auth();
	init(config);
});
var config = {
'jspath': 'js/',
'modules':[
	['computer', '计算机', 'ci/admins/demo', 20, 20],	//URL为此模块的入口URL，该模块所有操作通过此URL带参数。
	['network', '网络', 'ci/admins/demo', 20,120]
]
};
function auth(){
	$.getJSON('http://127.0.0.1:8080?callback=?', function(json){
		console.log(json);
	});
}