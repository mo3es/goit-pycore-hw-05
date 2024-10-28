Functions, that expected from this programm in HW-5 was provided in HW-4, programm wasn`t rewrited


This programm is entry point to phone-book bot. It takes user`s input, parse it and provide some functions based on results of parsing:
allowed commands contains in module 'Constants.py';
in case of incorrect input, Usage message will be printed;
in case of one of series quit commands will be inputed - programm will be stopped;
in case of one of series add commands will be inputed - programm will be call add_contact function from contact_handler and contact will be added;
in case of one of series change commands will be inputed - programm will be call change_contact function from contact_handler and contact will be changed if exist;
in case of one of series show commands will be inputed - programm will be call show_contact function from contact_handler and contact will be shown if exist;
in case of one of series show commands will be inputed - programm will be call show_contact function from contact_handler and contact will be shown if exist;
in case of one of series show-all commands will be inputed - programm will be call show_all function from contact_handler and contact will be shown or printed message ' phone book is empry in case of empty or absent phone-book;
contact_handler module additionally contains functions to check cases of name or phone number in given arguments and, if they are absent - to get them from input.

Phone book can be readed from file and saved to file.