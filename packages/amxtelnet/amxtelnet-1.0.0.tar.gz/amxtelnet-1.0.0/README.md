# amxtelnet
amx telnet functions

AMXTelnet():
Connect to the masters specified in set_systems(),
Send the command(s) specified in set_requests(), and
Set config(write_results)=True to save the responses to individual .txt files specified in config(path).
You can also set config(user_name,password). If you don't, the AMX default logins will be used.
When you're ready to scan systems, use AMXTelnet.run()


ParseAMXResponse():
Use this class to parse the information gathered from AMXTelnet().
This class is less universal in that it expects the .txt files to contain responses
to the following commands in the following order:
	'show device','get ip','program info','list'
You can append additional commands as needed.
The output of ParseAMXResponse().read_telnet_text() is a list of amx system dicts.
Current uses of this list:
	export to excel using amxtoexcel.py to archive campus system status
	code creation using code_creator_django.py or code_creator_usm.py


AMXTelnet.path and ParseAMXResponse.path will normally refer to the same location. If you use the
default locations in each class, they'll work together using systems/telnet responses/.

If there's already .txt files in 'path' you can bypass AMXTelnet() and go straight to ParseAMXResponse()
if using potentially outdated information is acceptable.
