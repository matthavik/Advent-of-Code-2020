


var file = file_text_open_read( "input.txt");

show_debug_message("File open!");
var nums = ds_list_create();

while( !file_text_eof( file)){
	
	var num = file_text_read_real( file);
	ds_list_add( nums, num);
	show_debug_message( num);
	file_text_readln( file);	
	
}

file_text_close( file);

var entries = ds_list_size( nums);

for( var i = 0; i < entries; i++){
	
	var num1 = nums[| i];
	var num2 = -1;
	
	for( var ii = 0; ii < entries; ii++){
		
		if ii != i {
			
			num2 = nums[| ii];
			
			if num1 + num2 == 2020 {
				
				show_debug_message( num1 * num2);
				exit;	
				
			}
			
		}
		
	}	
	
}

