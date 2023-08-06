# amxtelnet
amx telnet functions

Separating the polling/.txt creation from the parsing to make it easier to
decide if you want to rescan masters before reading the information

minimum requirements when instantiating:
AMXTelnet(user_name, password)
ParseAMXResponse()

AMXTelnet.output_path and ParseAMXResponse.input_path will normally refer to the same location.
AMXTelnet creates the files, and ParseAMXResponse reads them. If you use the default locations
in each class, they'll work together using /telnet responses/