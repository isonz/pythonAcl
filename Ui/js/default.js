var mainurl = 'http://py.ison.com';
var jsmodule =  'js/module/';
$(document).ready(function() {
	$.ajaxf.install('js/Ajax.swf'); 
	auth();
	$("#user_center_button").click(function(){
		if('undefined'==typeof($("#window_user_center").attr('id'))){
			$('#desktop').append(winBoxSimple('user_center', '用户中心', mainurl, 'user_center', 500, 300, 1));
			$.getJSON(mainurl+'/user?callback=?', function(data){
				if('0'==data.error){
					$("#window_user_center .window_content").html(data.html);
				}
			});
		}else{
			$("#window_user_center").show();
			$("#icon_dock_user_center").show();
		}
  	});
});

//此设置可以从外部应用中读取
var config = {
'modules':[
	['computer', '计算机', 'ci/admins/demo', 20, 20],	//URL为此模块的入口URL，该模块所有操作通过此URL带参数。
	['network', '网络', 'ci/admins/demo', 20,120]
]
};

function auth(){
	$.getJSON(mainurl+'/?callback=?', function(data){
		if('0'!= data.error){
			$('#desktop').append(winBoxSimple('login', '登入', mainurl, 'login', 500, 300, 0));
			//$('#desktop').append(msgWinBox('msg1', '消息', 400, 200));
			$('#desktop').css('bottom',0);
			$('#window_login .float_right').hide();
			$('#window_login .window_content').html(data.html);
			$('#loginform').submit(function(){
				$.ajaxf.post(mainurl+$(this).attr('action'), 'username='+$('#username').val()+'&password='+$('#password').val(), function(rs){
					console.log(rs);
					if('0'==rs.error){
						init(config);
						$("#window_login").hide();
					}else{
						$("#login_error_msg").html('<img src="images/icons/sys/error.png" />&nbsp;&nbsp;'+rs.msg);
					}
				},'json');
				return false;
			});
		}else{
			init(config);
		}
	});
}

function logout(){
	$.getJSON(mainurl+'/user?logout=1&callback=?', function(data){
		if('0'==data.error) location.reload();
	});
}

