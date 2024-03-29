# Initialized `events.py` generated by ipm.
# Regists your text events and regist global variables here.# Documents at https://ipm.hydroroll.team/

from infini.register import Register

register = Register()

register.register_variable("logging_version", "0.1.0-beta.1")


register.register_textevent(
    "log.info",
    "NoctisLogger 版本 {{ logging_version }} [Infini {{ infini_version }} for DicerGirl {{ version }}]\n"
    "欢迎使用日志管理器, 当前会话共[{{ count }}]个日志序列, 其中共[{{ active_count }}]个活跃序列.",
)
register.register_textevent("log.new", "新增日志进程序列[{{ sequence }}]")
register.register_textevent("log.start", "日志进程序列[{{ sequence }}]启动记录")
register.register_textevent("log.stop", "日志进程序列[{{ sequence }}]中止记录")
register.register_textevent("log.clear", "日志进程序列已清空")
register.register_textevent(
    "log.export", "日志序列[{{ sequence }}]已导出至[{{ filename }}]"
)
register.register_textevent("log.error.not_found", "未找到日志进程序列[{{ sequence }}]")
register.register_textevent(
    "log.error.not_started", "日志进程序列[{{ sequence }}]未启动, 忽略中止请求."
)
register.register_textevent("role.kp", "[{{ card_name }}]已进入主持人席位")
register.register_textevent("role.kp.out", "[{{ card_name }}]已离开主持人席位")
register.register_textevent("role.ob", "[{{ card_name }}]已进入观战者席位")
register.register_textevent("role.ob.out", "[{{ card_name }}]已离开观战者席位")
register.register_textevent("role.pl", "[{{ card_name }}]已进入玩家席位")
register.register_textevent("role.pl.out", "[{{ card_name }}]已离开玩家席位")
